#! /usr/bin/env python
# -*- coding: utf-8 -*-
#conector mysql
import MySQLdb as pymysql
class Db:   
    def __init__(self):
        self.db = "ventas"
        self.host ="localhost"
        self.user = "root"
        self.passwd = "123456"
        self.port=3306
    def conectar(self):
        self.conexion = pymysql.connect(host="localhost", port=self.port, user=self.user,passwd=self.passwd, db=self.db,charset = 'utf8')
        self.cursor = self.conexion.cursor()  
class Datos:
    def cargar_datos(self):
        self.barcode=str(raw_input("Barcode:"))  
        self.descripcion=str(raw_input("Descripcion:"))  
        self.costo=float(raw_input("Costo:"))
        self.precio=float(raw_input("Precio:"))
        self.cat=1
        self.exento=0        
    def insertar(self):
        db=Db()
        db.conectar()       
        sql="""INSERT INTO producto(barcode, id_categoria,descripcion, exento, costo, precio) 
                    VALUES(%s, %s, %s, %s, %s, %s)"""
        valores=(self.barcode,self.cat,self.descripcion,self.exento,self.costo,self.precio)
        db.cursor.execute(sql,valores)
        db.conexion.commit()
        db.conexion.close()
if __name__ == '__main__':
  
    app = Datos()
    app.cargar_datos()
    app.insertar()
            
        


