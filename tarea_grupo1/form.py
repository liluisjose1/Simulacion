# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Apr 12 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import os
import matplotlib 
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
#from numpy import sin,cos,tan,log,sqrt,exp,linspace

import numpy as np
import matplotlib.pyplot as plt
#matplotlib.rcParams['toolbar'] = 'None' #deshabilitar  toolbar por defecto de la grafica, si se quiere mostrar se comenta esta linea

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Distribuciones TS155-2018 ", pos = wx.DefaultPosition, size = wx.Size( 789,585 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        self.menubar1 = wx.MenuBar( 0 )
        self.menu1 = wx.Menu()
        self.menuItem1 = wx.MenuItem( self.menu1, wx.ID_ANY, u"Acerca de programadores..", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu1.AppendItem( self.menuItem1 )
        
        self.menu1.AppendSeparator()
        
        self.menuItem2 = wx.MenuItem( self.menu1, wx.ID_ANY, u"Salir", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu1.AppendItem( self.menuItem2 )
        
        self.menubar1.Append( self.menu1, u"Opciones" ) 
        
        self.menu2 = wx.Menu()
        self.sizerCanvas = wx.Menu()
        self.menuItem3 = wx.MenuItem( self.sizerCanvas, wx.ID_ANY, u"Boltzmann", wx.EmptyString, wx.ITEM_NORMAL )
        self.sizerCanvas.AppendItem( self.menuItem3 )
        
        self.menu2.AppendSubMenu( self.sizerCanvas, u"Discretas" )
        
        self.sub_menu11 = wx.Menu()
        self.menuItem4 = wx.MenuItem( self.sub_menu11, wx.ID_ANY, u"Normal o Gauss", wx.EmptyString, wx.ITEM_NORMAL )
        self.sub_menu11.AppendItem( self.menuItem4 )
        
        self.menu2.AppendSubMenu( self.sub_menu11, u"Continuas" )
        
        self.menubar1.Append( self.menu2, u"Distribuciones" ) 
        
        self.SetMenuBar( self.menubar1 )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.panelGrafico = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizerCanvas = wx.BoxSizer( wx.VERTICAL )
        
        
        self.panelGrafico.SetSizer( sizerCanvas )
        self.panelGrafico.Layout()
        sizerCanvas.Fit( self.panelGrafico )
        bSizer4.Add( self.panelGrafico, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer4 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_MENU, self.info, id = self.menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.salir, id = self.menuItem2.GetId() )
        self.Bind( wx.EVT_MENU, self.boltzmannDistribution, id = self.menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.gaussDistribution, id = self.menuItem4.GetId() )
    
            # Constants
        self.BOLTZMANN_K = 1.3806488e-23 # J/K
        self.H_MASS = 1.673534e-27 # Masa del Hidrogeno (Kg)

        # Variables
        self.TEMP = 600# °Kelvin
        self.ATOMS_MASS = 1*self.H_MASS # Kg
        self.NUM_ATOMS = 20000 
        self.MAX_SPEED = 10000 # Vector de velocidad en  (m/s). 
        self.ATOMS_PER_BIN = 100
    
    def distVelocidadMaxwell(self,s, m, T):
        # See wikipedia: https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution
        s2 = s*s
        twokT = 2 * self.BOLTZMANN_K * T
        coeff = 4 * np.pi * (m / (np.pi * twokT)) ** (3./2.)
        return coeff * s2 * np.exp(-m * s2 / (twokT))
        
    def distTeoriaVelocidad(self):
        tsd = list()
        spds = list()
        for s in xrange(0, self.MAX_SPEED, 1):
            tsd.append(self.distVelocidadMaxwell(s, self.ATOMS_MASS, self.TEMP))
            spds.append(s)
        
        pctCovered = sum(tsd)
        print "Prueba de Teoria: ", pctCovered, pctCovered >= 0.99 
        return spds, tsd
        
    def MCSpeedDist(self,maxProb):
        count = 0
        mcsd = list()
        while (len(mcsd) < self.NUM_ATOMS):
            s = np.random.random() * self.MAX_SPEED
            prob = self.distVelocidadMaxwell(s, self.ATOMS_MASS, self.TEMP)
            
            if np.random.random() * maxProb <= prob:
                mcsd.append(s)
            count += 1
        
        print "MC Blucles: %d, Blucles/Particula: %f" % (count, float(count)/self.NUM_ATOMS)
        return mcsd
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def info( self, event ):
        dialogo= DialogProgrammers(None)        
        dialogo.ShowModal()
    
    def salir( self, event ):
        self.Close()
    
    def boltzmannDistribution( self, event ):
        spds, tsd = self.distTeoriaVelocidad()
        mcsd = self.MCSpeedDist(max(tsd))
        
        fig, ax1 = plt.subplots() # figure Crea una ventana 
        ax2 = ax1.twinx() #mismos parametros de la funcion principal
        title1="Distribucion de Boltzmann para elemento de Hidrogeno"
        subtitle1='...'
        fig.canvas.set_window_title(title1) 
        
        plt.title(subtitle1)
        plt.ylabel('N')
        plt.xlabel('Velocidad m/s ')
        plt.suptitle(title1, fontsize=16) # Configurar título de la gráfica
        
        ax1.hist(mcsd, bins = self.NUM_ATOMS/self.ATOMS_PER_BIN)
        ax2.plot(spds, self.ATOMS_PER_BIN*np.array(tsd), 'r-')
        plt.show() 
        """
        dialogo=Dialog_boltz(None)      
        dialogo.ShowModal()"""
        #event.Skip()
    
    def gaussDistribution( self, event ):
        dialogo=Campana(None)      
        dialogo.ShowModal()
        #event.Skip()
###########################################################################
## Class Dialog_boltz
###########################################################################

class Dialog_boltz ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ingrese Datos", pos = wx.DefaultPosition, size = wx.Size( 569,212 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        #self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        fgSizer4 = wx.FlexGridSizer( 5, 5, 0, 0 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        
        fgSizer4.Add( ( 0, 10), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 10), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 10), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 10), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 10), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 10, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Temperatura °K", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )
        fgSizer4.Add( self.m_staticText22, 0, wx.ALL, 5 )
        
        self.txt1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.txt1, 0, wx.ALL, 5 )
        
        self.m_staticText221 = wx.StaticText( self, wx.ID_ANY, u"N° Atomos", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText221.Wrap( -1 )
        fgSizer4.Add( self.m_staticText221, 0, wx.ALL, 5 )
        
        self.txt2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.txt2, 0, wx.ALL, 5 )
        
        
        fgSizer4.Add( ( 10, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText222 = wx.StaticText( self, wx.ID_ANY, u"Masa del Atomo (Kg)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText222.Wrap( -1 )
        fgSizer4.Add( self.m_staticText222, 0, wx.ALL, 5 )
        
        self.txt3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.txt3, 0, wx.ALL, 5 )
        
        self.m_staticText2221 = wx.StaticText( self, wx.ID_ANY, u"Atomos por Contenedor", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2221.Wrap( -1 )
        fgSizer4.Add( self.m_staticText2221, 0, wx.ALL, 5 )
        
        self.txt4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.txt4, 0, wx.ALL, 5 )
        
        
        fgSizer4.Add( ( 10, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText22211 = wx.StaticText( self, wx.ID_ANY, u"Velocidad Maxima (m/s)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22211.Wrap( -1 )
        fgSizer4.Add( self.m_staticText22211, 0, wx.ALL, 5 )
        
        self.txt5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.txt5, 0, wx.ALL, 5 )
        
        
        fgSizer4.Add( ( 10, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 10, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 10, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 10, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 10, 0), 1, wx.EXPAND, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.m_button2, 0, wx.ALL, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Procesar", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.m_button3, 0, wx.ALL, 5 )
        
        
        fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( fgSizer3 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button2.Bind( wx.EVT_BUTTON, self.salirBoltz )
        self.m_button3.Bind( wx.EVT_BUTTON, self.procesarBoltz )
        
        """ # Constants
        
        self.BOLTZMANN_K = 1.3806488e-23 # J/K
        self.H_MASS = 1.673534e-27 # Masa del Hidrogeno (Kg)

        # Variables
        self.TEMP = 600# °Kelvin
        self.ATOMS_MASS = 1*self.H_MASS # Kg
        self.NUM_ATOMS = 20000 
        self.MAX_SPEED = 10000 # Vector de velocidad en  (m/s). 
        self.ATOMS_PER_BIN = 100"""
        # Constants
        
        self.BOLTZMANN_K = 1.3806488e-23 # J/K
        self.H_MASS  # Masa del Hidrogeno (Kg)

        # Variables
        self.TEMP # °Kelvin
        self.ATOMS_MASS = 1*self.H_MASS # Kg
        self.NUM_ATOMS   
        self.MAX_SPEED # Vector de velocidad en  (m/s). 
        self.ATOMS_PER_BIN 
    
    def distVelocidadMaxwell(self,s, m, T):
        # See wikipedia: https://en.wikipedia.org/wiki/Maxwell1.673534e-27 %E2%80%93Boltzmann_distribution
        s2 = s*s
        twokT = 2 * self.BOLTZMANN_K * T
        coeff = 4 * np.pi * (m / (np.pi * twokT)) ** (3./2.)
        return coeff * s2 * np.exp(-m * s2 / (twokT))
        
    def distTeoriaVelocidad(self):
        tsd = list()
        spds = list()
        for s in xrange(0, self.MAX_SPEED, 1):
            tsd.append(self.distVelocidadMaxwell(s, self.ATOMS_MASS, self.TEMP))
            spds.append(s)
        
        pctCovered = sum(tsd)
        print "Sanity check: ", pctCovered, pctCovered >= 0.99 
        return spds, tsd
        
    def MCSpeedDist(self,maxProb):
        count = 0
        mcsd = list()
        while (len(mcsd) < self.NUM_ATOMS):
            s = np.random.random() * self.MAX_SPEED
            prob = self.distVelocidadMaxwell(s, self.ATOMS_MASS, self.TEMP)
            
            if np.random.random() * maxProb <= prob:
                mcsd.append(s)
            count += 1
        
        print "MC Loops: %d, Loops/Particle: %f" % (count, float(count)/self.NUM_ATOMS)
        return mcsd
        
    """def main():
        spds, tsd = self.distTeoriaVelocidad()
        mcsd = self.MCSpeedDist(max(tsd))
        
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.hist(mcsd, bins = self.NUM_ATOMS/self.ATOMS_PER_BIN)
        ax2.plot(spds, self.ATOMS_PER_BIN*np.array(tsd), 'r-')
        plt.show()"""
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def salirBoltz( self, event ):
        self.Close()
    
    def procesarBoltz( self, event ):
        
        self.TEMP= self.txt1.GetValue()
        self.NUM_ATOMS = self.txt2.GetValue()
        self.H_MASS = self.txt3.GetValue()
        self.ATOMS_PER_BIN = self.txt4.GetValue()
        self.MAX_SPEED  = self.txt5.GetValue()
        
        spds, tsd = self.distTeoriaVelocidad()
        mcsd = self.MCSpeedDist(max(tsd))
        
        fig, ax1 = plt.subplots() # figure Crea una ventana 
        ax2 = ax1.twinx() #mismos parametros de la funcion principal
        title1="Distribucion de Boltzmann para elemento de Hidrogeno"
        subtitle1='...'
        fig.canvas.set_window_title(title1) 
        
        plt.title(subtitle1)
        plt.ylabel('N')
        plt.xlabel('v ')
        plt.suptitle(title1, fontsize=16) # Configurar título de la gráfica
        
        ax1.hist(mcsd, bins = self.NUM_ATOMS/self.ATOMS_PER_BIN)
        ax2.plot(spds, self.ATOMS_PER_BIN*np.array(tsd), 'r-')
        plt.show()
        
        self.Close()

###########################################################################
## Class DialogProgrammers
###########################################################################

class DialogProgrammers ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Acerca de ..", pos = wx.DefaultPosition, size = wx.Size( 320,200 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        #self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer15 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Tecnicas de Simulacion UES-FMO 2018", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText33.Wrap( -1 )
        bSizer15.Add( self.m_staticText33, 0, wx.ALL, 5 )
        
        
        bSizer15.Add( ( 2, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText331 = wx.StaticText( self, wx.ID_ANY, u"Luis Jose Iraheta Medrano IM15005\nYenifer Zuleyma Garcia Melendez GM15002\nClaudia Patricia Salamanca Martinez SM13038 \nAna Ruth Sanchez Henriquez   SH13012", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText331.Wrap( -1 )
        bSizer15.Add( self.m_staticText331, 0, wx.ALL, 5 )
        
        
        bSizer15.Add( ( 2, 0), 1, wx.EXPAND, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_button4, 0, wx.ALL, 5 )
        
        
        self.SetSizer( bSizer15 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button4.Bind( wx.EVT_BUTTON, self.salir )
    
    def __del__( self ):
        self.Skip()
    
    
    # Virtual event handlers, overide them in your derived class
    def salir( self, event ):
        self.Close()
class Campana ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 392,86 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        #self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"μ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txt1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.txt1, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"σ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txt2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.txt2, 0, wx.ALL, 5 )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Procesar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.processGauss )
    
    def __del__( self ):
        pass
    
    def soloNum(self, valor):
        try:
            valor = float(valor)
            return valor
        except:
            wx.MessageBox(u'Ingrese solo numeros','Error')
            return # vuelve a mostrar el mensaje
    
    # Virtual event handlers, overide them in your derived class
    def processGauss( self, event ):
        mu, sigma = self.soloNum(self.txt1.GetValue()),self.soloNum(self.txt2.GetValue()) # media y desvio estandar
        datos = np.random.normal(mu, sigma, 1000) #creando muestra de datos

        # histograma de distribución normal.
        cuenta, cajas, ignorar = plt.hist(datos, 20)
        plt.ylabel('frequencia')
        plt.xlabel('valores')
        plt.title('Histograma de Distribucion Normal o Gauss')
        plt.show()
        
        self.Close()      
        #event.Skip()
        
if __name__ == '__main__':
    app = wx.App()
    frame=MyFrame1(None)
    frame.Show()
    app.MainLoop()
    

