# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar  1 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,430 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer1.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Tolerancia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.txt1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt1, 0, wx.ALL, 2 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Lista", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.txt2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt2, 0, wx.ALL, 2 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Procesar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		self.list_ctrl = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, size=(390, 200), style=wx.LC_REPORT )
		self.list_ctrl.InsertColumn(0, 'n',width=50)
		self.list_ctrl.InsertColumn(1, 'Medios',width=120)
		self.list_ctrl.InsertColumn(2, 'Pseudoaleatorios',width=130)
		bSizer1.Add( self.list_ctrl, 0, wx.ALL, 5 )
		
		self.lResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lResult.Wrap( -1 )
		bSizer1.Add( self.lResult, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.EventProcesar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def EventProcesar( self, event ):
		lista=int(self.txt1.GetValue())
		#event.Skip()
	

if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame1(None)
	frame.Show()
	app.MainLoop()
