#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import wx.xrc
import mysqlclass3 #Clase para mysql
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		self.title="Listar Productos, Busqueda por Descripcion"
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = self.title, pos = wx.DefaultPosition, size = wx.Size( 610,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 3, 1, 0, 0 )
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
		
		fgSizer3 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.listctrl = wx.ListCtrl( self, wx.ID_ANY,  wx.Point( 10,10 ), wx.Size( 600,200 ), wx.LC_REPORT|wx.SUNKEN_BORDER )
		fgSizer3.Add( self.listctrl, 0, wx.ALL, 5 )
		fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		#Agregar un sizer de 1 fila 4 col
		fgSizer4 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		#Botones para mantenimiento
		self.btn_Insertar = wx.Button( self, wx.ID_ANY, u"Insertar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btn_Insertar, 0, wx.ALL, 5 )  
		self.btn_Ver = wx.Button( self, wx.ID_ANY, u"Ver", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btn_Ver, 0, wx.ALL, 5 )  
		self.btn_Editar = wx.Button( self, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btn_Editar, 0, wx.ALL, 5 )          
		self.btn_Eliminar = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btn_Eliminar, 0, wx.ALL, 5 )          
		fgSizer1.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_Buscar.Bind( wx.EVT_BUTTON, self.Buscar )
		self.txt_Busqueda.Bind( wx.EVT_TEXT, self.Busqueda )
		self.listctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.Seleccionar)
		self.btn_Insertar.Bind( wx.EVT_BUTTON, self.Insertar )
		self.btn_Ver.Bind( wx.EVT_BUTTON, self.Ver )
		self.btn_Editar.Bind( wx.EVT_BUTTON, self.Editar )
		self.btn_Eliminar.Bind( wx.EVT_BUTTON, self.Eliminar )
		#Conexion Bd
		self.db = mysqlclass3.Database("ventas") #Instanciar la conexion a la Bd.
		#definir valor de item2
		self.item ='' 
		self.item2 ='' 
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
	def Busqueda( self, event ):
		self.Cargar()   
	def Seleccionar(self, event):  # wxGlade: MyFrame2.<event_handler>
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
	def Insertar( self, event ):
		form_hijo=MyDialog1(self)
		form_hijo.Show()
		form_hijo.Mostrar("INSERTAR")
	def Ver( self, event ):
		form_hijo=MyDialog1(self)
		form_hijo.Show()
		form_hijo.Mostrar("VER")
	def Editar( self, event ):
		form_hijo=MyDialog1(self)
		form_hijo.Show()
		form_hijo.Mostrar("EDITAR")
		#form_hijo.txt1.SetValue(self.item2)
	def Eliminar( self, event ):
		form_hijo=MyDialog1(self)
		form_hijo.Show()
		form_hijo.Mostrar("ELIMINAR")
 
###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"CRUD Productos", pos = wx.DefaultPosition, size = wx.Size( -1,390 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		#Clase Padre formulario superior
		self.frm_padre=parent
		
		sizer1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 8, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"ACCION", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		self.lbl1 = wx.StaticText( self, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )
		fgSizer1.Add( self.lbl1, 0, wx.ALL, 5 )
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Id. Producto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.txt1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt1, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Descripcion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.txt2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer1.Add( self.txt2, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Barcode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.txt3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt3, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Costo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.txt4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt4, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Precio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.txt5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txt5, 0, wx.ALL, 5 )
	   
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Categoria", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		OpcionCat = ['Seleccionar']
		self.cbCat = wx.ComboBox( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, OpcionCat, 0 )
		fgSizer1.Add( self.cbCat, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Inactivo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.checkInactivo = wx.CheckBox( self, wx.ID_ANY, u"Checkear Inactivo", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.checkInactivo, 0, wx.ALL, 5 )
		
		
		sizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer2.Add( ( 50, 0), 1, wx.EXPAND, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn1, 0, wx.ALL, 5 )
		
		self.btn4 = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn4, 0, wx.ALL, 5 )
		
		
		sizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer(sizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.btnAceptar )
		self.btn4.Bind( wx.EVT_BUTTON, self.btnSalir )
		self.cbCat.Bind( wx.EVT_COMBOBOX, self.CatSeleccion )
		self.checkInactivo.Bind( wx.EVT_CHECKBOX, self.chkInactivar )
		#base de datos
		self.db = mysqlclass3.Database("ventas") #Instanciar la conexion a la Bd.
		#Evento mostrar datos
		
		#MODAL PARA mensajes
		self.dial = wx.MessageDialog(None, 'DATOS GUARDADOS', 'Info', wx.OK|wx.CENTRE)

	def __del__( self ):
		pass
	
	def Mostrar(self,accion):
		self.lbl1.SetLabel(accion)
		self.id_producto=str(self.frm_padre.item2)
		self.id_cat=0
		id_cat=0
		inactivo=0
		self.ChkInactivo=False
		if ( self.lbl1.GetLabel()=='INSERTAR'):
			self.txt2.SetValue('')
			self.txt3.SetValue('')
			self.txt4.SetValue('')
			self.txt5.SetValue('')
		   
		else:
			if (self.id_producto!=''):
				self.txt1.SetValue(self.frm_padre.item2)
				sql="""SELECT * FROM producto WHERE id_producto = '%s'"""% (self.id_producto) 

				typesql='S1'
				self.rows=self.db.query(sql,"",typesql)
		
				self.txt2.SetValue(self.rows[3])
				self.txt3.SetValue(self.rows[1])
				self.txt4.SetValue(str(self.rows[5]))
				self.txt5.SetValue(str(self.rows[6]))
				id_cat=int(self.rows[2])
				inactivo=int(self.rows[8]) 
		print id_cat
		sql2='''SELECT  * FROM categoria '''
		typesql2='S'
		self.rows2=self.db.query(sql2,'',typesql2)
		self.cbCat.Clear() # Limpiar el combo antes de rellenar
		#Para rellenar el combo con los datos traidos de la bd.     
		for row2 in self.rows2:     
			self.cbCat.Append(str(row2[0])+"-"+row2[1])
		#Asignar la categoria por defecto en el combo
		self.cbCat.SetSelection(id_cat)
		#ver si el producto esta como inactivo
		if (inactivo==1):
			self.checkInactivo.SetValue(True)
			self.checkInactivo.SetLabel("El producto esta inactivo!!!")
		else:
			self.checkInactivo.SetValue(False)
			self.checkInactivo.SetLabel("El producto esta activo!!!")    
	# Virtual event handlers, overide them in your derived class
	def btnAceptar( self, event ):
		if ( self.lbl1.GetLabel()=='EDITAR'):
			self.descripcion=str(self.txt2.GetValue())  
			self.barcode=str(self.txt3.GetValue())  
			self.costo=str(self.txt4.GetValue())  
			self.precio=str(self.txt5.GetValue())  
			self.exento=0  
			if (self.ChkInactivo==True):
				self.inactivo=1
			else:
				self.inactivo=0
			#self.id_cat = self.cbCat.GetSelection()
			sql="""UPDATE producto SET barcode=%s,id_categoria=%s,descripcion=%s,exento=%s, costo=%s,precio=%s,inactivo=%s
				WHERE id_producto=%s"""
			valores=(self.barcode,self.id_cat,self.descripcion,self.exento,self.costo,self.precio,self.inactivo,self.id_producto)
			typesql='U'
			query=self.db.query(sql,valores,typesql)
			self.dial.ShowModal()
			self.frm_padre.Cargar()
		elif ( self.lbl1.GetLabel()=='ELIMINAR'):
			
			self.id_producto=str(self.txt1.GetValue())  
			
			sql="""DELETE FROM producto WHERE id_producto="""+self.id_producto
			valores=(self.id_producto)
			typesql='D'
			query=self.db.query(sql,'',typesql)
			self.dial.ShowModal()
			self.frm_padre.Cargar()
		elif ( self.lbl1.GetLabel()=='INSERTAR'):
			
			#self.id_producto=str(self.txt1.GetValue())  
			self.descripcion=str(self.txt2.GetValue())  
			self.barcode=str(self.txt3.GetValue())  
			self.costo=str(self.txt4.GetValue())  
			self.precio=str(self.txt5.GetValue())  
			self.cat=0
			self.exento=0
			sql="""INSERT INTO producto (barcode,id_categoria,descripcion,exento,costo,precio,inactivo) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
			valores=(self.barcode,self.id_cat,self.descripcion,self.exento,self.costo,self.precio,self.inactivo)
			typesql='I'
			query=self.db.query(sql,valores,typesql)
			self.dial.ShowModal()
			self.frm_padre.Cargar() 

	
	def btnSalir( self, event ):
		self.Close()
	def CatSeleccion( self, event ):
		self.id_cat= self.cbCat.GetSelection() #seleccionar el id categoria
		print self.cbCat.GetString(self.id_cat)  #mostrar la descripcion de categoria
	def chkInactivar( self, event ):
		self.Chk=event.GetEventObject() 
		self.ChkInactivo=self.Chk.GetValue()
		print self.Chk.GetLabel(),' esta checkeado ',self.ChkInactivo
	 

			
if __name__ == '__main__':
  
	app = wx.App()
	frame=MyFrame1(None)
	frame.Show()
	app.MainLoop()  
