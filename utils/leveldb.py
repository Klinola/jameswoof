import os
import plyvel
import json
import re
import shutil


def get_account_folders(cache_path):
    account_folders = []

    for folder_name in os.listdir(cache_path):
        folder_path = os.path.join(cache_path, folder_name)
        if os.path.isdir(folder_path):
            account_folders.append(folder_name)
    
    return account_folders

def clean_json_string(json_str):
    # clear invalid chars
    json_str = re.sub(r'[^\x20-\x7E]+', '', json_str)
    return json_str

def ignore_lock_files(src, names):
    return ['LOCK'] if 'LOCK' in names else []

def search_tokens_in_leveldb(leveldb_path):
    search_str = "https://app.jameswoof.com"
    token = None
    invite_code = None

    # copy database
    temp_db_path = leveldb_path + "_copy"
    try:
        
        if os.path.exists(temp_db_path):
            shutil.rmtree(temp_db_path)
        shutil.copytree(leveldb_path, temp_db_path, ignore=ignore_lock_files) 
        plyvel.repair_db(temp_db_path)
        db = plyvel.DB(temp_db_path, compression=None)
               
        for key, value in db:
            key_str = key.decode('utf-8', errors='ignore')
            value_str = value.decode('utf-8', errors='ignore')
            if search_str in key_str:
                print(key_str)
                print(value_str)
                if "\"token\"" in value_str:
                    value_str = clean_json_string(value_str)
                    try:
                        value_json = json.loads(value_str)
                        token = value_json.get('token')
                    except json.JSONDecodeError as e:
                        print("JSON decode failed:", e)
                        print("Value string that caused the error:", value_str)
                if "userInfo" in value_str:
                    value_str = clean_json_string(value_str)
                    try:
                        value_json = json.loads(value_str)
                        user_info = value_json.get('userInfo', {})
                        invite_code = user_info.get('number', '').replace('W', '')
                    except json.JSONDecodeError as e:
                        print("JSON decode failed:", e)
                        print("Value string that caused the error:", value_str)
                        
        db.close()
        # delete copy
        shutil.rmtree(temp_db_path)
    except Exception as e:
        print(f"Error accessing LevelDB at {leveldb_path}: {e}")
    
    return {"token": token, "invite_code": invite_code}


def init_accounts(cache_path):
    account_folders = get_account_folders(cache_path)

    account_tokens = {}
    total_accounts = len(account_folders)
    accounts_with_token = 0

    for folder in account_folders:
        leveldb_path = os.path.join(cache_path, folder, "Default", "Local Storage", "leveldb")
        
        if os.path.exists(leveldb_path):
            account_data = search_tokens_in_leveldb(leveldb_path)
            if account_data["token"] is not None:
                account_tokens[folder] = account_data
                accounts_with_token += 1
            else:
                account_tokens[folder] = {"token": None, "invite_code": None}
        else:
            print(f"\nLevelDB path does not exist: {leveldb_path}")
            account_tokens[folder] = {"token": None, "invite_code": None}
    print(account_tokens)
    return account_tokens, total_accounts, accounts_with_token
