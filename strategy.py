from datetime import datetime
from utils.leveldb import init_accounts
from utils.api_client import APIClient
from utils.utils import get_timestamp
from utils.accounts_db import (
    init_db, insert_accounts, load_accounts_into_db,
    get_all_accounts, update_last_interaction_time, 
    set_leader, update_invite_code
)

# daily
def daily_interaction(account, db_path="accounts.db"):
    folder_name, token, invite_code, account_id, last_interaction_time, in_group, is_leader, leader = account[1:]
    client = APIClient(token)
    client.wakeup()
    client.getDailyReward()
    
    update_last_interaction_time(folder_name, db_path)

# team up
def group_interaction(accounts, db_path="accounts.db"):
    leader = accounts[0]
    leader_folder_name, leader_token, leader_invite_code, leader_account_id, leader_last_interaction_time, leader_in_group, leader_is_leader, leader_leader = leader[1:]
    client_leader = APIClient(leader_token)
    client_leader.create()
    set_leader(leader_folder_name, db_path)

    for member in accounts[1:]:
        member_folder_name, member_token, member_invite_code, member_account_id, member_last_interaction_time, member_in_group, member_is_leader, member_leader = member[1:]
        client_member = APIClient(member_token)
        custom_data = {
            "code": leader_invite_code,
            "uuid": get_timestamp()
        }
        client_member.joinGroup(data=custom_data)

# example
if __name__ == "__main__":
    cache_path = "/path/to/chrome/cache"
    db_path = "accounts.db"
    init_db(db_path)
    load_accounts_into_db(cache_path, init_accounts, db_path)
    
    accounts = get_all_accounts(db_path)
    
    # daily
    for account in accounts:
        daily_interaction(account, db_path)
    
    ## teamup
    #for i in range(0, len(accounts), 6):
    #    group = accounts[i:i+6]
    #    if len(group) == 6:
    #        group_interaction(group, db_path)
