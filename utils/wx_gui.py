# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Jameswoof Autointeraction Tools v1.0"), pos = wx.DefaultPosition, size = wx.Size( 638,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizerMainFrame = wx.BoxSizer( wx.VERTICAL )

        bSizerFrameMain = wx.BoxSizer( wx.VERTICAL )

        self.panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanel = wx.BoxSizer( wx.VERTICAL )

        bSizerList = wx.BoxSizer( wx.HORIZONTAL )

        self.m_dataViewListCtrl4 = wx.dataview.DataViewListCtrl( self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
        self.m_dataViewListColumn1 = self.m_dataViewListCtrl4.AppendTextColumn( _(u"Account"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn2 = self.m_dataViewListCtrl4.AppendTextColumn( _(u"Token"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn3 = self.m_dataViewListCtrl4.AppendTextColumn( _(u"Code"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn4 = self.m_dataViewListCtrl4.AppendTextColumn( _(u"Last Interaction Time"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn5 = self.m_dataViewListCtrl4.AppendTextColumn( _(u"in Group"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn6 = self.m_dataViewListCtrl4.AppendTextColumn( _(u"is Leader"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn7 = self.m_dataViewListCtrl4.AppendTextColumn( _(u"Leader"), wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        bSizerList.Add( self.m_dataViewListCtrl4, 1, wx.ALL|wx.EXPAND, 5 )


        bSizerMainPanel.Add( bSizerList, 1, wx.EXPAND, 5 )

        bSizerFunctions = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button1 = wx.Button( self.panelMain, wx.ID_ANY, _(u"Start/Stop"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerFunctions.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self.panelMain, wx.ID_ANY, _(u"Group"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerFunctions.Add( self.m_button2, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self.panelMain, wx.ID_ANY, _(u"Init"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerFunctions.Add( self.m_button3, 0, wx.ALL, 5 )

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
        self.m_dataViewListCtrl4.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.m_dataViewListCtrl4OnDataViewListCtrlItemActivated, id = wx.ID_ANY )
        self.Bind( wx.EVT_MENU, self.menuItemFileNewOnMenuSelection, id = self.menuItemFileNew.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItemFileOpenOnMenuSelection, id = self.menuItemFileOpen.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def m_dataViewListCtrl4OnDataViewListCtrlItemActivated( self, event ):
        event.Skip()

    def menuItemFileNewOnMenuSelection( self, event ):
        event.Skip()

    def menuItemFileOpenOnMenuSelection( self, event ):
        event.Skip()


