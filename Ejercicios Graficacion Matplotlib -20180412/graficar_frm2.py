# -*- coding: utf-8 -*- 

###########################################################################
# Uso de Matplotlib y Numpy invocado desde wxpython
## Matplotlib es una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays 
## en el lenguaje de programación Python y su extensión matemática NumPy. 
###########################################################################

import wx
import wx.xrc
import matplotlib  #Importamos la librería de graficación matplotlib
from math import *
import numpy as np
from numpy import sin,cos,tan,log,sqrt,exp,linspace #Importamos la librería de numpy, pues de aquí podemos extraer funciones como seno, coseno, logaritmo, etc.
import matplotlib.pyplot as plt 
matplotlib.rcParams['toolbar'] = 'None' #deshabilitar  toolbar por defecto de la grafica, si se quiere mostrar se comenta esta linea
from numpy import sin,cos,tan,log,sqrt,exp,linspace
from scipy.optimize import fsolve
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu Graficar con Matplotlib", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.SetSizer( bSizer4 )
		self.Layout()
		self.menubar1 = wx.MenuBar( 0 ) #barra de menu
		self.menu1 = wx.Menu() #menu
		self.smenu1 = wx.Menu() #submenu
		
		self.item1 = wx.MenuItem( self.smenu1, wx.ID_ANY, u"Grafica 1", wx.EmptyString, wx.ITEM_NORMAL ) #items de menu
		self.smenu1.AppendItem( self.item1 )		
		self.item2 = wx.MenuItem( self.smenu1, wx.ID_ANY, u"Cap. Funcion", wx.EmptyString, wx.ITEM_NORMAL )  #items de menu
		self.smenu1.AppendItem( self.item2 )
		self.item3 = wx.MenuItem( self.smenu1, wx.ID_ANY, u"Usar Scipy", wx.EmptyString, wx.ITEM_NORMAL )  #items de menu
		self.smenu1.AppendItem( self.item3 )
		self.item4 = wx.MenuItem( self.smenu1, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )  #items de menu
		self.smenu1.AppendItem( self.item4 )
		self.menu1.AppendSubMenu( self.smenu1, u"Graficar" ) #agregar submenu a menu
				
		self.menubar1.Append( self.menu1, u"Opciones" )  #agregar menu a barra		
		self.SetMenuBar( self.menubar1 )		
		self.Centre( wx.BOTH )
		
		# Eventos asociados a item de menu

		self.Bind( wx.EVT_MENU, self.item1_Accion, id = self.item1.GetId() )
		self.Bind( wx.EVT_MENU, self.item2_Accion, id = self.item2.GetId() )
		self.Bind( wx.EVT_MENU, self.item3_Accion, id = self.item3.GetId() )
		self.Bind( wx.EVT_MENU, self.Salir, id = self.item4.GetId() )
	
	def __del__( self ):
		pass
	

	def item1_Accion( self, event ):	#Evento que genera una grafica dados los valores fijos
		fig = plt.figure() # figure Crea una ventana 
		title1="Seno de X"
		subtitle1='WxPython & Matplotlib'
		fig.canvas.set_window_title(title1) 
		plt.title(subtitle1)
		plt.ylabel('eje Y')
		plt.xlabel('eje X')
		plt.suptitle(title1, fontsize=16) # Configurar título de la gráfica
		x=np.arange(0,10,0.1)	
		y=np.sin(x)
		plt.plot(x,y)
		plt.show()
	
	def item2_Accion( self, event ): #Evento que invoca una clase de dialogo para capturar una funcion que posteriiormente se grafica
		dialogo=MyDialog1(None)		
		dialogo.ShowModal()

	def item3_Accion( self, event ):	#Evento que genera dos graficas con puntos de interpolacion dados los valores 		
		x = np.linspace(0, 50, 10000) #  rango de datos
		# funciones a intersectar
		onda = lambda x: np.cos(x / 5) * np.sin(x / 2)
		linea = lambda x: 0.01 * x - 0.5

		# rango estimado
		x0 = [15, 20, 30, 35, 40, 45, 50]

		# obtener interseccion 
		resultado = self.encuentra_interseccion(onda, linea, x0)
		# plot graficar
		fig = plt.figure() # figure Crea una ventana 
		title1="Interseccion de 2 Funciones"
		fig.canvas.set_window_title(title1) 
		plt.title('Puntos de Interseccion')
		plt.ylabel(' Y ')
		plt.xlabel(' X ')
		plt.plot(x, onda(x), label='Func. de Onda')
		plt.plot(x, linea(x), label='Func. Lineal')
		plt.grid(True) # Coloca cuadricula
		plt.plot(resultado, linea(resultado), '*')
		plt.xlim(0, 50)
		plt.ylim(-1, 1)
		plt.legend()
		plt.show()

	def encuentra_interseccion(self, func1, func2, x0): # funcion  para encontrar la interseccion con scipy
		return fsolve(lambda x: func1(x) - func2(x), x0)	
		

	def Salir( self, event ):
		#event.Skip()
		self.Close()
###########################################################################
## Class MyDialog1 que muestra un modal para capturar una funcion, a graficar posteriormente
###########################################################################


class MyDialog1( wx.Dialog ): 
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ingresar una funcion", pos = wx.DefaultPosition, size =(350,100), style = wx.ID_OK)
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"f(x)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		self.txt2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (250,40), 0 )
		bSizer3.Add( self.txt1, 0, wx.ALL, 5 )
		bSizer3.Add( self.txt2, 0, wx.ALL, 5 )
		self.btn1 = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btn1, 0, wx.ALL, 5 )		
		self.SetSizer( bSizer3 )
		self.Layout()
		bSizer3.Fit( self )	
		self.Centre( wx.BOTH )
	
		# Evento que sirve para capturar la funcion y si es valida lo grafica 
		self.btn1.Bind( wx.EVT_BUTTON, self.Graficar)
		
	
	def __del__( self ):
		pass
	def Cerrar( self ):
		self.Close()	
	
	# Virtual event handlers, overide them in your derived class
	def Graficar( self, event):
		f=self.txt2.GetValue()
		f=f.lower()
		
		title1="f(x)="+f
		subtitle1='WxPython & Matplotlib'
		
		x=np.arange(0,10,0.1)  #Creamos el conjunto de puntos que queremos evaluar en la función de numpy np.arange(a,b,paso) crea el intervalo desde el número a hasta b, con un paso de 0.1.
		
		try:
			y = eval(f) #eval sirve para evaluar si el valor que recibe es realmente una funcion valida para python
			fig = plt.figure() #crear ventana de dibujo con figure 
			fig.canvas.set_window_title(title1) #iniciar canvas con titulo 
			plt.title(subtitle1)  #titulo de grafica
			plt.ylabel('eje Y')  #titulo de eje y
			plt.xlabel('eje X')  #titulo de eje x
			plt.suptitle(title1, fontsize=16) # Configurar título de la gráfica
			plt.grid(True) # Coloca cuadricula
			plt.plot(x,y) #graficar 
			plt.show() #mostrar
		except: #  continua mostrando el mensaje mientras no se ingrese una funcion valida
			wx.MessageBox(u'Inserte una función f(x)','msg')
			return 
						
		self.Cerrar()	
		
if __name__ == '__main__':
  
    app = wx.App()
    frame=MyFrame1(None)
    frame.Show()
    app.MainLoop()	
