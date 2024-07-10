import wx
import sqlite3
from datetime import datetime
from utils.leveldb import init_accounts
from utils.api_client import APIClient
from utils.utils import get_timestamp
from utils.accounts_db import (
    init_db, insert_accounts, load_accounts_into_db,
    get_all_accounts, update_last_interaction_time, 
    set_leader, update_invite_code
)
from utils.wx_gui import frameMain

# 单个账户的每日操作
def daily_interaction(account, db_path="accounts.db"):
    folder_name, token, invite_code, account_id, last_interaction_time, in_group, is_leader, leader = account[1:]
    client = APIClient(token)
    client.wakeup()
    client.getDailyReward()
    
    update_last_interaction_time(folder_name, db_path)

# 组队操作
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

class MainApp(wx.App):
    def OnInit(self):
        self.frame = frameMain(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)

        # Attach event handlers
        self.frame.on_start_stop = self.on_start_stop
        self.frame.on_group = self.on_group
        self.frame.on_init = self.on_init

        return True

    def on_start_stop(self, event):
        db_path = "accounts.db"
        accounts = get_all_accounts(db_path)
        
        # 每日交互
        for account in accounts:
            daily_interaction(account, db_path)

    def on_group(self, event):
        db_path = "accounts.db"
        accounts = get_all_accounts(db_path)
        
        # 组队交互
        for i in range(0, len(accounts), 6):
            group = accounts[i:i+6]
            if len(group) == 6:
                group_interaction(group, db_path)

    def on_init(self, event):
        cache_path = "C:\Users\Klinola\AppData\Local\Google\Chrome"
        db_path = "accounts.db"
        init_db(db_path)
        load_accounts_into_db(cache_path, init_accounts, db_path)

        self.update_account_list()

    def update_account_list(self):
        db_path = "accounts.db"
        accounts = get_all_accounts(db_path)
        
        self.frame.m_dataViewListCtrl4.DeleteAllItems()
        for account in accounts:
            self.frame.m_dataViewListCtrl4.AppendItem([
                account[1],  # folder_name
                account[2],  # token
                account[3],  # invite_code
                account[5],  # last_interaction_time
                str(account[6]),  # in_group
                str(account[7]),  # is_leader
                account[8]   # leader
            ])

if __name__ == "__main__":
    app = MainApp(False)
    app.MainLoop()
