# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar  1 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Test Poker", pos = wx.DefaultPosition, size = wx.Size( 587,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer2.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Lista de Pseudoaleatorios", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grid1.CreateGrid( 7, 7 )
		self.grid1.EnableEditing( True )
		self.grid1.EnableGridLines( True )
		self.grid1.EnableDragGridSize( False )
		self.grid1.SetMargins( 0, 0 )
		
		# Columns
		self.grid1.EnableDragColMove( False )
		self.grid1.EnableDragColSize( True )
		self.grid1.SetColLabelSize( 30 )
		self.grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grid1.EnableDragRowSize( True )
		self.grid1.SetRowLabelSize( 80 )
		self.grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer2.Add( self.grid1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer3.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Resultados", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.listCtrl = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		self.listCtrl.InsertColumn(0, 'Combinacion',width=200)
		self.listCtrl.InsertColumn(1, 'FO',width=50)
		self.listCtrl.InsertColumn(2, 'FE',width=100)
		self.listCtrl.InsertColumn(3, 'X^2 Calculada',width=200)
		fgSizer3.Add( self.listCtrl, 0, wx.ALL, 5 )
		
		bSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.aleatorios=['0.73133','0.49413','0.46597','0.00287','0.25196','0.29722',
					'0.30940','0.95766','0.50045','0.91111',
					'0.47221','0.84079','0.45868','0.27362','0.89875',
					'0.23318','0.72385','0.11985','0.05139','0.20524',
					'0.05450','0.17048','0.65126','0.87417','0.30761',
					'0.35595','0.81577','0.08958','0.24829','0.37092']

		self.cargarGrid()
		#self.cargarList()
	
	def __del__( self ):
		pass
	
	def cargarGrid(self):
		
		self.grid1.SetCellValue(0,0,"Lista de Numeros Aleatorios")
		i=0
		for row in range(1,5):
			for col in range(0,6):
				self.grid1.SetCellValue(row,col," %s" % (self.aleatorios[i]))
				i+=1
		self.cargarList()
	def mano(self,valor):
		result=[]
		pares=0
		tercias=0
		tienejuego="td"
		for i in range(10):
			result.append(valor.count(str(i)))
			#print result
		for j in range(10):
			if result[j]==2:
				pares+=1
			if result[j]==3:
				tercias+=1
			if result[j]==4:
				tienejuego="Poker"
			if result[j]==5:
				tienejuego= "Pocarin"

		if pares==1:
			tienejuego="1par"
		elif pares==2:
			tienejuego="2pares"
		if pares==0 and tercias==1:
			tienejuego="Tercia"
		if pares==1  and tercias==1:
			tienejuego="Full"
		return tienejuego

	def cargarList(self):
		probabilidad=[0.3024,0.5040,0.1080,0.0720,0.0090,0.0045,0.0001]
		combinacion = ["Todos Diferentes","Un Par","Dos Pares","Tercia","Full","Poker","Quintilla"]
		n = len(self.aleatorios)
		fo=[]
		td=0
		par1=0
		par2=0
		tercia=0
		full=0
		poker=0
		pocarin=0
		p=0
		fe=[]
		for i in range (n):
			entero,decimal=self.aleatorios[i].split('.')
			juego = self.mano(decimal)
			if juego == "td":
				td+=1
			if juego == "1par":
				par1+=1
			if juego == "2pares":
				par2+=1
			if juego == "Tercia":
				tercia+=1
			if juego == "Full":
				full+=1
			if juego == "Poker":
				poker+=1
			if juego == "Pocarin":
				pocarin+=1
		fo.append(td)
		fo.append(par1)
		fo.append(par2)
		fo.append(tercia)
		fo.append(full)
		fo.append(poker)
		fo.append(pocarin)
		total=0
		for k in range(7):
			index = k
			p=((n*probabilidad[k]-fo[k])**2)/(n*probabilidad[k])
			fe.append(p)
			total+= fe[k]	
			self.listCtrl.InsertStringItem(index, combinacion[k])
			self.listCtrl.SetStringItem(index, 1, str(fo[k]))
			self.listCtrl.SetStringItem(index, 2, str(n*probabilidad[k]))
			self.listCtrl.SetStringItem(index, 3, str(fe[k]))
		
		print total

		"""listachi6=[22.4575,20.2491,18.5475,16.8119,14.4494,12.5916,10.6446,9.4461,8.5581,7.8408,7.2311,6.6948,6.2108,5.7652,5.3481]
		tol= int(raw_input("Ingresa Tolerancia"))"""
		if total<10.6446:
			print "Pseudoaleatorios aceptados"
		else:
			print "Pseudoaleatorios No aceptados"
		pass
			
		
		""" Function doc """
		

if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame1(None)
	frame.Show()
	app.MainLoop()
