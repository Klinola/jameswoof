import wx
import os
import wx.xrc
import gettext
_ = gettext.gettext

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Jameswoof Autointeraction Tools v1.0"), pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizerMainFrame = wx.BoxSizer( wx.VERTICAL )

        bSizerFrameMain = wx.BoxSizer( wx.VERTICAL )

        self.panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanel = wx.BoxSizer( wx.VERTICAL )

        bSizerPaths = wx.BoxSizer( wx.HORIZONTAL )

        self.staticTextDbPath = wx.StaticText( self.panelMain, wx.ID_ANY, _(u"DB Path:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextDbPath.Wrap( -1 )
        bSizerPaths.Add( self.staticTextDbPath, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        current_dir = os.path.join(os.getcwd(), "account.db") # Get currrent working directory
        self.dirPickerDbPath = wx.DirPickerCtrl( self.panelMain, wx.ID_ANY, current_dir, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_USE_TEXTCTRL )
        bSizerPaths.Add( self.dirPickerDbPath, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.staticTextCachePath = wx.StaticText( self.panelMain, wx.ID_ANY, _(u"Cache Path:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticTextCachePath.Wrap( -1 )
        bSizerPaths.Add( self.staticTextCachePath, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.dirPickerCachePath = wx.DirPickerCtrl( self.panelMain, wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_USE_TEXTCTRL )
        bSizerPaths.Add( self.dirPickerCachePath, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizerMainPanel.Add( bSizerPaths, 0, wx.EXPAND, 5 )

        bSizerList = wx.BoxSizer( wx.HORIZONTAL )

        self.m_listCtrl1 = wx.ListCtrl( self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES|wx.LC_SINGLE_SEL )
        bSizerList.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

        # Adding columns
        self.m_listCtrl1.InsertColumn(0, "Select", width=50, format=wx.LIST_FORMAT_CENTER)
        self.m_listCtrl1.InsertColumn(1, "Account", width=150)
        self.m_listCtrl1.InsertColumn(2, "Token", width=300)
        self.m_listCtrl1.InsertColumn(3, "Code", width=100)
        self.m_listCtrl1.InsertColumn(4, "Last Interaction Time", width=150)
        self.m_listCtrl1.InsertColumn(5, "in Group", width=80)
        self.m_listCtrl1.InsertColumn(6, "is Leader", width=80)
        self.m_listCtrl1.InsertColumn(7, "Leader", width=100)

        bSizerMainPanel.Add( bSizerList, 1, wx.EXPAND, 5 )

        bSizerFunctions = wx.BoxSizer( wx.HORIZONTAL )

        self.checkBoxSelectAll = wx.CheckBox(self.panelMain, wx.ID_ANY, _(u"Select All"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerFunctions.Add(self.checkBoxSelectAll, 0, wx.ALL, 5)
        self.checkBoxSelectAll.Bind(wx.EVT_CHECKBOX, self.on_select_all)

        self.buttonStart = wx.Button( self.panelMain, wx.ID_ANY, _(u"Start/Stop"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerFunctions.Add( self.buttonStart, 0, wx.ALL, 5 )

        self.buttonGroup = wx.Button( self.panelMain, wx.ID_ANY, _(u"Group"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerFunctions.Add( self.buttonGroup, 0, wx.ALL, 5 )

        self.buttonInit = wx.Button( self.panelMain, wx.ID_ANY, _(u"Init"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerFunctions.Add( self.buttonInit, 0, wx.ALL, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self.panelMain, wx.ID_ANY, _(u"Log: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer8.Add( self.m_staticText1, 0, wx.ALL, 5 )


        bSizerFunctions.Add( bSizer8, 1, wx.EXPAND, 5 )


        bSizerMainPanel.Add( bSizerFunctions, 0, 0, 5 )


        self.panelMain.SetSizer( bSizerMainPanel )
        self.panelMain.Layout()
        bSizerMainPanel.Fit( self.panelMain )
        bSizerFrameMain.Add( self.panelMain, 1, wx.EXPAND |wx.ALL, 0 )


        bSizerMainFrame.Add( bSizerFrameMain, 1, wx.EXPAND, 0 )


        self.SetSizer( bSizerMainFrame )
        self.Layout()
        self.menubarMain = wx.MenuBar( 0 )
        self.menuFile = wx.Menu()
        self.menuItemFileNew = wx.MenuItem( self.menuFile, wx.ID_ANY, _(u"New")+ u"\t" + u"Ctrl+N", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuFile.Append( self.menuItemFileNew )

        self.menuItemFileOpen = wx.MenuItem( self.menuFile, wx.ID_ANY, _(u"Open")+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuFile.Append( self.menuItemFileOpen )

        self.menubarMain.Append( self.menuFile, _(u"File") )

        self.menuEdit = wx.Menu()
        self.menubarMain.Append( self.menuEdit, _(u"Edit") )

        self.menuHelp = wx.Menu()
        self.menubarMain.Append( self.menuHelp, _(u"Help") )

        self.SetMenuBar( self.menubarMain )


        self.Centre( wx.BOTH )

        # Connect Events
        self.buttonStart.Bind( wx.EVT_BUTTON, self.buttonStartOnButtonClick )
        self.buttonGroup.Bind( wx.EVT_BUTTON, self.buttonGroupOnButtonClick )
        self.buttonInit.Bind( wx.EVT_BUTTON, self.buttonInitOnButtonClick )
        self.Bind( wx.EVT_MENU, self.menuItemFileNewOnMenuSelection, id = self.menuItemFileNew.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItemFileOpenOnMenuSelection, id = self.menuItemFileOpen.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def buttonStartOnButtonClick( self, event ):
        event.Skip()

    def buttonGroupOnButtonClick( self, event ):
        event.Skip()

    def buttonInitOnButtonClick( self, event ):
        event.Skip()

    def menuItemFileNewOnMenuSelection( self, event ):
        event.Skip()

    def menuItemFileOpenOnMenuSelection( self, event ):
        event.Skip()

    def on_select_all(self, event):
        check = self.checkBoxSelectAll.GetValue()
        item_count = self.m_listCtrl1.GetItemCount()
        for index in range(item_count):
            self.m_listCtrl1.CheckItem(index, check)
