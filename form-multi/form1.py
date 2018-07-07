# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar  1 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import os
import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Prueba", pos = wx.DefaultPosition, size = wx.Size( 250,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 6, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer1.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Valor1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.txt1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt1, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Valor2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		fgSizer1.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.txt2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt2, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText311 = wx.StaticText( self, wx.ID_ANY, u"Valor3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )
		fgSizer1.Add( self.m_staticText311, 0, wx.ALL, 5 )
		
		self.txt3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt3, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText3111 = wx.StaticText( self, wx.ID_ANY, u"Resultado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3111.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3111, 0, wx.ALL, 5 )
		
		self.txtr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtr, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Procesar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.evenProcesar )
		self.m_button3.Bind( wx.EVT_BUTTON, self.evetSalir )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def evenProcesar( self, event ):
		v1=float(self.txt1.GetValue())
		v2=float(self.txt2.GetValue())
		v3=float(self.txt3.GetValue())
		res = v1*v2*v3
		self.txtr.SetValue(str(res))
		#event.Skip()
	
	def evetSalir( self, event ):
		self.Close()
		#event.Skip()
	
if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame1(None)
	frame.Show()
	app.MainLoop()
	
