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
		self.lista_numeros=[41, 68, 89, 94, 74, 91, 55, 62, 36, 27,
		19, 72, 75, 9, 54, 2, 1, 36, 16, 28,
		18, 1, 95, 69, 18, 47, 23, 32, 82, 53,
		31, 42, 73, 4, 83, 45, 13, 57,63, 29]
		self.n = self.lista_numeros.__len__()
		self.unos_y_ceros = list({})
		self.numero_de_corridas = -1
		self.varianza = 0
		self.miu = 0
		#self.hipotesis=="Los numeros aletorios no son aceptados"
		self.z=0
		#self.start()
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pruebas Arriba y Abajo", pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer2.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Lista de Numeros a probar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grid1.CreateGrid( 5, 6 )
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
		   
		fgSizer3 = wx.FlexGridSizer( 6, 3, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer3.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.Add( ( 0, 20), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Corridas=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.lbl_corridas = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_corridas.Wrap( -1 )
		fgSizer3.Add( self.lbl_corridas, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"Valor Esperado=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )
		fgSizer3.Add( self.m_staticText111, 0, wx.ALL, 5 )
		
		self.lbl_esperado = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_esperado.Wrap( -1 )
		fgSizer3.Add( self.lbl_esperado, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1111 = wx.StaticText( self, wx.ID_ANY, u"Varianza=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1111.Wrap( -1 )
		fgSizer3.Add( self.m_staticText1111, 0, wx.ALL, 5 )
		
		self.lbl_varianza = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_varianza.Wrap( -1 )
		fgSizer3.Add( self.lbl_varianza, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText11111 = wx.StaticText( self, wx.ID_ANY, u"Z=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11111.Wrap( -1 )
		fgSizer3.Add( self.m_staticText11111, 0, wx.ALL, 5 )
		
		self.lbl_z = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_z.Wrap( -1 )
		fgSizer3.Add( self.lbl_z, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText111111 = wx.StaticText( self, wx.ID_ANY, u"Hipotesis=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111111.Wrap( -1 )
		fgSizer3.Add( self.m_staticText111111, 0, wx.ALL, 5 )
		
		self.lbl_h = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_h.Wrap( -1 )
		fgSizer3.Add( self.lbl_h, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		
		self.Centre( wx.BOTH )
		
		self.cargarGrid()
		self.start()
		#self.cargarList()
	
	def __del__( self ):
		pass
	
	def cargarGrid(self):
		
		#self.grid1.SetCellValue(0,0,"Lista de Numeros Aleatorios")
		i=0
		for row in range(0,5):
			for col in range(0,6):
				self.grid1.SetCellValue(row,col," %s" % (self.lista_numeros[i]))
				i+=1
	def start(self):
		corridas=0
		for i in range(1,self.n): # del 1 al n-1( ya que comienza en cero
			# Si el numero es menor o igual que el anterior se pone cero
			if self.lista_numeros[i] <= self.lista_numeros[i-1]:
				self.unos_y_ceros.append(0)
			else: # Si no se pone 1
				self.unos_y_ceros.append(1)
			
			if i == 1: # Si ES el primer caso
				self.numero_de_corridas = 1
				corridas=1
			else: 
				if self.unos_y_ceros[i-1] != self.unos_y_ceros[i-2]:
					self.numero_de_corridas += 1
					corridas += 1
					
		
		ceros = self.unos_y_ceros.count(0)
		unos = self.unos_y_ceros.count(1)
		u1 = 2*(ceros*unos)/(self.n) + 0.5
		numerador=2*(ceros*unos)*((2*ceros*unos)-self.n)
		denominador=(self.n)**2*(self.n-1)
		o=numerador/denominador
		
		
		
		self.varianza = o
		self.mui = u1
		z=(self.numero_de_corridas-u1)/o
		self.z=z
		
		
		#salidas
		self.lbl_corridas.SetLabel(str(self.numero_de_corridas))
		self.lbl_esperado.SetLabel(str(u1))
		self.lbl_varianza.SetLabel(str(o))
		self.lbl_z.SetLabel(str(z))
		hipotesis=''
		if z>1.96:
			hipotesis="Numeros Psuedoaleatorios Rechazados"
			self.lbl_h.SetLabel(hipotesis)
			self.lbl_h.SetForegroundColour(wx.Colour(255,0,0))
		else:
			hipotesis="Numeros Pseudoaleatorios Aceptados"
			self.lbl_h.SetLabel(hipotesis)
			self.lbl_h.SetForegroundColour(wx.Colour(14,25,182))
if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame1(None)
	frame.Show()
	app.MainLoop()
