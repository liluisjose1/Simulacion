#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx
import wx.xrc
import mysqlclass2 #Clase para mysql
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        self.title="Listar Productos, Busqueda por Descripcion"
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = self.title, pos = wx.DefaultPosition, size = wx.Size( 610,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txt_Busqueda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,  wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
        fgSizer2.Add(self.txt_Busqueda , 0, wx.ALL, 5 )
        
        self.btn_Buscar = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.btn_Buscar, 0, wx.ALL, 5 )
        
        
        
        fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
        
        fgSizer3 = wx.FlexGridSizer( 2,2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        #fgSizer3.AddSpacer( ( 30, 0), 1, wx.EXPAND, 5 )
        self.listctrl = wx.ListCtrl( self, wx.ID_ANY,  wx.Point( 10,10 ), wx.Size( 600,200 ), wx.LC_REPORT|wx.SUNKEN_BORDER )
        fgSizer3.Add( self.listctrl, 0, wx.ALL, 5 )
        
        fgSizer3.Add( ( 20, 20), 1, wx.EXPAND, 5 )
        self.btn_Editar = wx.Button( self, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.btn_Editar, 0, wx.ALL, 5 )
        
        fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
        

        
        self.SetSizer( fgSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn_Buscar.Bind( wx.EVT_BUTTON, self.Buscar )
        self.btn_Editar.Bind( wx.EVT_BUTTON, self.Editar )
        self.txt_Busqueda.Bind( wx.EVT_TEXT, self.Busqueda )
        self.listctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.Seleccionar)
        #Conexion Bd
        self.db = mysqlclass2.Database("ventas") #Instanciar la conexion a la Bd.
        #Evento cargar datos de encabezado a la lista y se definen las columnas que lleva el control
        self.listctrl.InsertColumn(0, 'Id', width=100)
        self.listctrl.InsertColumn(1, 'Barcode', width=150)
        self.listctrl.InsertColumn(2, 'Descripcion', width=350)
        self.Cargar()
        
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def Buscar( self, event ):
        self.Cargar()  
    def Editar( self, event ):
        self.frm_child = MyFrame2(self) #para llamar al segundo form
        self.frm_child.Show()
        if (self.item2 !='' ):
            self.frm_child.txt1.SetValue(self.item2)
            #self.frm_child.cargarDatos(self.item2)
            #self.frm_child.valor=(self.item2)
  
    def Busqueda( self, event ):
        self.Cargar()   
    def Seleccionar(self, event):  # wxGlade: MyFrame2.<event_handler>
        self.item ='' 
        self.item2 ='' 
        self.item = self.listctrl.GetFocusedItem() #traer la posicion del indice
        self.item2 = self.listctrl.GetItemText(self.item)#traer el texto del primera columna segun la posicion del indice
        print self.item,self.item2  
    def Cargar(self):
        #evento para cargar datos de la bd a la lista de 2 maneras todos si el ctrl texto esta vacio 
        #o dependiendo de la busqueda con like asi muestra los resultados
        self.listctrl.DeleteAllItems() # quita los renglones de la lista
        cadena_buscar=self.txt_Busqueda.GetValue()  
        if cadena_buscar!="":
            self.prod="%"+str(cadena_buscar)+"%"
            #c.execute("SELECT * FROM data WHERE params LIKE %s LIMIT 1", ("%" + param + "%",))
            sql="select * from producto where descripcion  LIKE  %s"
            print sql
            data_param=self.prod
            
            typesql='SL'
            self.rows=self.db.query(sql,data_param,typesql)
        else:   
            sql="""select * from producto"""
            data_param=''
            typesql='S'
            self.rows=self.db.query(sql,data_param,typesql) 
        self.row_count = 0
        #al tener el cursor se van insertando las columnas
        for row in self.rows:
            #Para insertar el indice de la fila pero del control va en la posicion columna 0
            self.listctrl.InsertStringItem(self.row_count, str(row[0])) 
     
            self.listctrl.SetStringItem(self.row_count,1, str(row[1])) 
            #en la fila insertada columna 2, se inserta el valor siguiente 
            desc=row[3].encode('utf-8')
            self.listctrl.SetStringItem(self.row_count,2, str(desc)) 
            
            if self.row_count % 2:
                self.listctrl.SetItemBackgroundColour(self.row_count, "cyan")
            else:
                self.listctrl.SetItemBackgroundColour(self.row_count, "yellow")
            self.row_count += 1     
 
class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Guardar / Editar", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.db = mysqlclass2.Database("ventas") #Instanciar la conexion a la Bd.
        self.form1=parent
        #self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        fgSizer1 = wx.FlexGridSizer( 6, 3, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        
        fgSizer1.Add( ( 20, 20), 1, wx.EXPAND, 5 )
        
        
        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer1.Add( ( 0, 20), 1, wx.EXPAND, 5 )
        
        self.texto = wx.StaticText( self, wx.ID_ANY, u"Barcode", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.texto.Wrap( -1 )
        fgSizer1.Add( self.texto, 0, wx.ALL, 5 )
        
        self.txt1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.txt1, 0, wx.ALL, 5 )
        
        
        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Descripcion", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txt2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
        fgSizer1.Add( self.txt2, 0, wx.ALL, 5 )
        
        
        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Costo", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txt3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.txt3, 0, wx.ALL, 5 )
        
        
        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Precio", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txt4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.txt4, 0, wx.ALL, 5 )
        
        
        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.btn1 = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.btn2, 0, wx.ALL, 5 )
        
        
        self.SetSizer( fgSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn1.Bind( wx.EVT_BUTTON, self.Aceptar )
        self.btn2.Bind( wx.EVT_BUTTON, self.Salir )
        
        #Cargar Datos
        self.cargarDatos()
    
    def __del__( self ):
        pass
    
    def cargarDatos(self):
        """ Function doc """
        id_producto=self.form1.item2
        #print id_producto
        sql="select * from producto where id_producto='"+id_producto+"'"
        typesql='S'
        self.rows=self.db.query(sql,"",typesql)
        
        self.row_count = 0
        #al tener el cursor se van insertando las columnas
        for row in self.rows:
            #print row[]
            self.txt1.SetValue(str(row[2]))
            self.txt2.SetValue(str(row[3]))
            self.txt3.SetValue(str(row[5]))
            self.txt4.SetValue(str(row[6]))
    # Virtual event handlers, overide them in your derived class
    def Aceptar( self, event ):
        event.Skip()
    
    def Salir( self, event ):
        self.Close()
    

 
            
if __name__ == '__main__':
  
    app = wx.App()
    frame=MyFrame1(None)
    frame.Show()
    app.MainLoop()  
