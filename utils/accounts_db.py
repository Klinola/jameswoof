import sqlite3
from datetime import datetime

def init_db(db_path="accounts.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            folder_name TEXT UNIQUE,
            token TEXT,
            invite_code TEXT,
            account_id TEXT,
            last_interaction_time TEXT,
            in_group INTEGER DEFAULT 0,
            is_leader INTEGER DEFAULT 0,
            leader TEXT,
            status TEXT DEFAULT 'incomplete'
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_accounts(account_tokens, db_path="accounts.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    for folder_name, account_data in account_tokens.items():
        token = account_data["token"]
        invite_code = account_data["invite_code"]
        cursor.execute('''
            INSERT OR IGNORE INTO accounts (folder_name, token, invite_code)
            VALUES (?, ?, ?)
        ''', (folder_name, token, invite_code))
    
    conn.commit()
    conn.close()

def load_accounts_into_db(cache_path, init_accounts_func, db_path="accounts.db"):
    account_tokens, total_accounts, accounts_with_token = init_accounts_func(cache_path)
    insert_accounts(account_tokens, db_path)
    print(f"Total accounts: {total_accounts}, Accounts with token: {accounts_with_token}")

def get_all_accounts(db_path="accounts.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM accounts WHERE token IS NOT NULL')
    accounts = cursor.fetchall()
    
    conn.close()
    return accounts

def update_last_interaction_time(folder_name, db_path="accounts.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    formatted_time = datetime.now().strftime("%m-%d %H:%M")
    cursor.execute('''
        UPDATE accounts
        SET last_interaction_time = ?
        WHERE folder_name = ?
    ''', (formatted_time, folder_name))
    
    conn.commit()
    conn.close()

def set_leader(folder_name, db_path="accounts.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE accounts
        SET is_leader = 1
        SET in_group = 1
        WHERE folder_name = ?
    ''', (folder_name,))
    
    conn.commit()
    conn.close()

def clear_leader(folder_name, db_path="accounts.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE accounts
        SET is_leader = 0
        WHERE folder_name = ?
    ''', (folder_name,))
    
    conn.commit()
    conn.close()

def set_member(folder_name, db_path="accounts.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE accounts
        SET is_leader = 0
        SET in_group = 1
        WHERE folder_name = ?
    ''', (folder_name,))
    
    conn.commit()
    conn.close()

def update_invite_code(folder_name, invite_code, db_path="accounts.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE accounts
        SET invite_code = ?
        WHERE folder_name = ?
    ''', (invite_code, folder_name))
    
    conn.commit()
    conn.close()

def update_status(folder_name, status, db_path="accounts.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE accounts
        SET status = ?
        WHERE folder_name = ?
    ''', (status, folder_name))
    
    conn.commit()
    conn.close()
