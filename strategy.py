import wx
import os
from datetime import datetime
from utils.leveldb import init_accounts
from utils.api_client import APIClient
from utils.utils import get_timestamp
from utils.accounts_db import (
    init_db, insert_accounts, load_accounts_into_db,
    get_all_accounts, update_last_interaction_time, 
    set_leader, update_invite_code, clear_leader, set_member, update_status
)
from utils.wx_gui import frameMain

# 单个账户的每日操作
def daily_interaction(account, db_path):
    folder_name, token, invite_code, account_id, last_interaction_time, in_group, is_leader, leader, status = account[1:]
    if status != 'incomplete':
        return

    client = APIClient(token)
    wakeup_response = client.wakeup()
    reward_response = client.getDailyReward()
    
    if wakeup_response.status_code == 200 and reward_response.status_code == 200:
        update_status(folder_name, 'complete', db_path)

    update_last_interaction_time(folder_name, db_path)

# 组队操作
def group_interaction(accounts, db_path):
    leader = accounts[0]
    leader_folder_name, leader_token, leader_invite_code, leader_account_id, leader_last_interaction_time, leader_in_group, leader_is_leader, leader_leader, status = leader[1:]
    client_leader = APIClient(leader_token)
    create_response = client_leader.create()
    if create_response.status_code == 200:
        set_leader(leader_folder_name, db_path)

    for member in accounts[1:]:
        member_folder_name, member_token, member_invite_code, member_account_id, member_last_interaction_time, member_in_group, member_is_leader, member_leader, status = member[1:]
        if member_in_group == 0:
            client_member = APIClient(member_token)
            custom_data = {
                "code": leader_invite_code,
                "uuid": get_timestamp()
            }
            join_response = client_member.joinGroup(data=custom_data)
            if join_response.status_code == 200:
                set_member(member_folder_name, leader_folder_name, db_path)

class MainApp(wx.App):
    def OnInit(self):
        self.frame = frameMain(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)

        # Attach event handlers
        self.frame.buttonStart.Bind(wx.EVT_BUTTON, self.on_start_stop)
        self.frame.buttonGroup.Bind(wx.EVT_BUTTON, self.on_group)
        self.frame.buttonInit.Bind(wx.EVT_BUTTON, self.on_init)

        return True

    def on_start_stop(self, event):
        db_path = self.frame.dirPickerDbPath.GetPath()
        if not db_path:
            wx.MessageBox("Please select a DB path.", "Error", wx.OK | wx.ICON_ERROR)
            return
            
        selected_accounts = self.get_selected_accounts()

        # 每日交互
        for account in selected_accounts:
            daily_interaction(account, db_path)

        self.update_account_list()

    def on_group(self, event):
        db_path = self.frame.dirPickerDbPath.GetPath()
        if not db_path:
            wx.MessageBox("Please select a DB path.", "Error", wx.OK | wx.ICON_ERROR)
            return
        selected_accounts = self.get_selected_accounts()
        
        # 组队交互
        for i in range(0, len(selected_accounts), 6):
            group = selected_accounts[i:i+6]
            if len(group) <= 6:
                group_interaction(group, db_path)

        self.update_account_list()

    def on_init(self, event):
        cache_path = self.frame.dirPickerCachePath.GetPath()
        db_path = self.frame.dirPickerDbPath.GetPath()
        if not cache_path or not db_path:
            wx.MessageBox("Please select both Cache and DB paths.", "Error", wx.OK | wx.ICON_ERROR)
            return
        init_db(db_path)
        load_accounts_into_db(cache_path, init_accounts, db_path)

        self.update_account_list()

    def update_account_list(self):
        db_path = self.frame.dirPickerDbPath.GetPath()
        if not db_path:
            wx.MessageBox("Please select a DB path.", "Error", wx.OK | wx.ICON_ERROR)
            return
        accounts = get_all_accounts(db_path)
        
        self.frame.m_listCtrl1.DeleteAllItems()
        for account in accounts:
            index = self.frame.m_listCtrl1.InsertItem(self.frame.m_listCtrl1.GetItemCount(), "")
            self.frame.m_listCtrl1.SetItem(index, 1, account[1])
            self.frame.m_listCtrl1.SetItem(index, 2, account[2] or "")
            self.frame.m_listCtrl1.SetItem(index, 3, account[3] or "")
            self.frame.m_listCtrl1.SetItem(index, 4, account[5] or "")
            self.frame.m_listCtrl1.SetItem(index, 5, str(account[6]))
            self.frame.m_listCtrl1.SetItem(index, 6, str(account[7]))
            self.frame.m_listCtrl1.SetItem(index, 7, account[8] or "")
            self.frame.m_listCtrl1.SetItem(index, 8, account[9] or "")

    def get_selected_accounts(self):
        db_path = self.frame.dirPickerDbPath.GetPath()
        if not db_path:
            wx.MessageBox("Please select a DB path.", "Error", wx.OK | wx.ICON_ERROR)
            return
        accounts = get_all_accounts(db_path)
        selected_accounts = []
        item_count = self.frame.m_listCtrl1.GetItemCount()
        for index in range(item_count):
            if self.frame.m_listCtrl1.IsItemChecked(index):
                selected_accounts.append(accounts[index])
        return selected_accounts

if __name__ == "__main__":
    app = MainApp(False)
    app.MainLoop()
