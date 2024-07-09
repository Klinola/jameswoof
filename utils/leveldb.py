import os
import plyvel
import json
import re

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

def search_tokens_in_leveldb(leveldb_path):
    search_str = "https://app.jameswoof.com"
    try:
        # open leveldb database
        db = plyvel.DB(leveldb_path, compression=None)
        
        for key, value in db:
            key_str = key.decode('utf-8', errors='ignore')
            value_str = value.decode('utf-8', errors='ignore')
            if search_str in key_str and "\"token\"" in value_str:
                value_str = clean_json_string(value_str)
                try:
                    value_json = json.loads(value_str)
                    token = value_json.get('token')
                    db.close()
                    return token
                except json.JSONDecodeError as e:
                    print("JSON decode failed:", e)
                    print("Value string that caused the error:", value_str)
        
        db.close()
    except Exception as e:
        print(f"Error accessing LevelDB at {leveldb_path}: {e}")
    
    return None

def init_accounts(cache_path):
    account_folders = get_account_folders(cache_path)

    account_tokens = {}
    total_accounts = len(account_folders)
    accounts_with_token = 0

    for folder in account_folders:
        leveldb_path = os.path.join(cache_path, folder, "Default", "Local Storage", "leveldb")
        
        if os.path.exists(leveldb_path):
            token_value = search_tokens_in_leveldb(leveldb_path)
            if token_value is not None:
                account_tokens[folder] = token_value
                accounts_with_token += 1
            else:
                account_tokens[folder] = None
        else:
            print(f"\nLevelDB path does not exist: {leveldb_path}")
            account_tokens[folder] = None
    print(account_tokens)
    return account_tokens, total_accounts, accounts_with_token
