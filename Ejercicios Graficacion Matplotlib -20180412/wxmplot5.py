#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import wx
import wx.xrc

import os
import matplotlib 
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from numpy import sin,cos,tan,log,sqrt,exp,linspace




###########################################################################
## Class FrmGraficar
###########################################################################

class FrmGraficar ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Numpy, & Mathplotlib  dentro de WxPython", pos = wx.DefaultPosition, size = wx.Size( 700,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), wx.TAB_TRAVERSAL )
        bSizerGeneral = wx.BoxSizer( wx.VERTICAL )
        
        bSizerFuncion = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.panel1, wx.ID_ANY, u"f(x)", wx.Point( -1,-1 ), wx.Size( 25,-1 ), 0 )
        self.m_staticText1.Wrap( -1 )
        bSizerFuncion.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtFuncion = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
        bSizerFuncion.Add( self.txtFuncion, 0, wx.ALL, 5 )
        
        self.btnGraficar = wx.Button( self.panel1, wx.ID_ANY, u"Graficar", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
        bSizerFuncion.Add( self.btnGraficar, 0, wx.ALL, 5 )
        
        
        bSizerGeneral.Add( bSizerFuncion, 1, wx.EXPAND, 5 )
        
        bSizerTxt = wx.BoxSizer( wx.VERTICAL )
        
     
        
        bSizerGeneral.Add( bSizerTxt, 1, wx.EXPAND, 5 )
        
        fgSizerIntervalos = wx.FlexGridSizer( 1, 7, 0, 0 )
        fgSizerIntervalos.SetFlexibleDirection( wx.BOTH )
        fgSizerIntervalos.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText3 = wx.StaticText( self.panel1, wx.ID_ANY, u"Intervalo 1", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText3.Wrap( -1 )
        fgSizerIntervalos.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txtIntervalo1 = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        fgSizerIntervalos.Add( self.txtIntervalo1, 0, wx.ALL, 5 )
        
        self.m_staticText5 = wx.StaticText( self.panel1, wx.ID_ANY, u"Intervalo 2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        fgSizerIntervalos.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.txtIntervalo2 = wx.TextCtrl( self.panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizerIntervalos.Add( self.txtIntervalo2, 0, wx.ALL, 5 )
        
        
        
       
        
        self.btnAjustar = wx.Button( self.panel1, wx.ID_ANY, u"Ajustar", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        fgSizerIntervalos.Add( self.btnAjustar, 0, wx.ALL, 5 )
        
        
        bSizerGeneral.Add( fgSizerIntervalos, 1, wx.EXPAND, 5 )
        
        
        self.panel1.SetSizer( bSizerGeneral )
        self.panel1.Layout()
        bSizerGeneral.Fit( self.panel1 )
        bSizer1.Add( self.panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.panelGrafico = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,450 ), wx.TAB_TRAVERSAL )
        self.sizerCanvas = wx.BoxSizer( wx.VERTICAL )
        
        
        self.panelGrafico.SetSizer( self.sizerCanvas )
        self.panelGrafico.Layout()
        self.sizerCanvas.Fit( self.panelGrafico )
        bSizer1.Add( self.panelGrafico, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnGraficar.Bind( wx.EVT_BUTTON, self.Graficar )
        self.btnAjustar.Bind( wx.EVT_BUTTON, self.Ajustar )
        #Para los graficos
        self.intervalo = [0.0,15.0]
        self.txtIntervalo1.SetValue('0.0')
        self.txtIntervalo2.SetValue('15.0')
        
        
        self.xlabel = "x"
        self.ylabel = "y"
        self.Fit()
        self.Centre(True)
        self.iniciarCanvas()
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class

    
    def Ajustar( self, event ):
        self.int1 = str(self.txtIntervalo1.GetValue())
        self.int2 = str(self.txtIntervalo2.GetValue())
       
        self.interv=self.int1+","+self.int2
        self.intervalo=self.interv.split(",")
        print( self.intervalo)
    def iniciarCanvas(self):
        # Creamos Figure
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111) # subplot parametros de tamanio de dibujo 111, ancho completo ej 121
        
        # FigureCanvas
        self.canvas = FigureCanvas(self.panelGrafico , -1, self.figure)   #agregado a un panel    
        self.sizerCanvas.Add(self.canvas, 1, wx.EXPAND) #agregarlo a un sizer wx
    
    def Graficar( self, event ):
        self.Ajustar(event)
        f=self.txtFuncion.GetValue()
        f=f.lower()        
        x = linspace(float(self.intervalo[0]), float(self.intervalo[1]))
        try:
            y = eval(f)
        except:
            wx.MessageBox(u'Inserte una función f(x) valida','Aviso')
            return # vuelve a mostrar el mensaje
        self.axes.cla() # Limpiar axes 
        
        hLine = self.axes.plot(x, y) # Gráfica 
        self.axes.set_title('f(x) = ' + f) # Configurar título de la gráfica
        self.axes.set_xlabel('x') #titulo eje x
        self.axes.set_ylabel('y') #titulo eje y
        self.axes.grid(True) # Coloca cuadricula
        self.canvas.draw() # Redibuja el elementos "canvas"
    


    
if __name__ == '__main__':
  
    app = wx.App()
    frame=FrmGraficar(None)
    frame.Show()
    app.MainLoop()
