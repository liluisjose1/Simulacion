# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar  1 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import ctypes 

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Metodo Cuadrados Medios IM15005 - TS2018", pos = wx.DefaultPosition, size = wx.Size( 450,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		fgSizer2 = wx.FlexGridSizer( 6, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer2.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Pseudo Aleatorios a Generar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.txt1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.txt1, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Valor Semilla", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer2.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.txt2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.txt2, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Procesar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.list_ctrl = wx.ListCtrl( self, wx.ID_ANY,pos=(255, 100),  size=(300, 200), style=wx.LC_REPORT)
		self.list_ctrl.InsertColumn(0, 'n',width=50)
		self.list_ctrl.InsertColumn(1, 'Medios',width=120)
		self.list_ctrl.InsertColumn(2, 'Pseudoaleatorios',width=130)
		fgSizer2.Add( self.list_ctrl, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.eventClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.eventC )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def eventClick( self, event ):
		
		n=int(self.txt1.GetValue())
		seed=float(self.txt2.GetValue())
		lista=[]
		for i in range(n):
			s2=str(seed**2)
			x=2*len(str(seed))
			ls=len(s2)
			if (ls<x):
				dif=x-ls
				for j in range(dif):
					s2="0"+ s2		
			s22=len(s2)/2
			izq=s22-2
			der=s22+2
			s3=s2[izq:der]
			s4=int(s3)/10000.0
	#print s3,s4
			seed=int(s3)
			lista.append(str(seed))
			if (lista.count(str(seed))==2):
				print "Comienza a repetir en iteracion ", i
				break
			else:
				index = i
				self.list_ctrl.InsertStringItem(index, str(i))
				self.list_ctrl.SetStringItem(index, 1, str(s3))
				self.list_ctrl.SetStringItem(index, 2, str(s4))
				#fgSizer2.Add(self.list_ctrl, 0, wx.ALL|wx.EXPAND, 5)
				#self.SetSizer( fgSizer2 )
				#self.index += 1
				
				##fgSizer2.Add( self.list_ctrl, 0, wx.ALL, 5 )
				##print "n=",i,s3,s4
				
	
	def eventC( self, event ):
		self.Close();
	

if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame1(None)
	frame.Show()
	app.MainLoop()
	
