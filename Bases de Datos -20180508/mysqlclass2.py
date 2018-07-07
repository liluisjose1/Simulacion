#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Class for mysql with module pymsql db management 
# Author: Luis J. Aguilar
#instalar: aptitude install python-pymysql
#o con pip: pip install PyMySQL
#import pymysql
#con el modulo python-mysqldb
import MySQLdb as pymysql
class Database:   
    def __init__(self,db):
		#recibe como parametro el nombre de la bd
		self.db = db
		self.host ="localhost"
		self.user = "root"
		self.passwd = "123456"
		self.port=3306
		self.connection = pymysql.connect(host="localhost", port=self.port, user=self.user,passwd=self.passwd, db=self.db,charset = 'utf8')
		self.cursor = self.connection.cursor()
		self.cursor.execute('SET NAMES utf8;')
		self.cursor.execute('SET CHARACTER SET utf8;')
		self.cursor.execute('SET character_set_connection=utf8;')
		

    def query(self,q,data_param,typequery):
		self.typequery=typequery
		cursor = self.cursor
		self.data_param=data_param
		if self.typequery=='S':
			#S: Select SQL 
			#print q, self.typequery,self.data_param
			if self.data_param=='':
				cursor.execute(q)
			else:
			    cursor.execute(q,data_param)
			    print self.cursor
			rows=cursor.fetchall()
			return rows
		elif self.typequery=='SL':	
			#SL: SQL Select for like 
			dato = (data_param,)
			print q,dato
			cursor.execute(q,dato)
			rows=cursor.fetchall()
			return rows
		elif self.typequery=='U':
			#U: update operation SQL
			if self.data_param=='':
				cursor.execute(q)
			else:
			    cursor.execute(q,data_param)
			self.connection.commit()			
		elif self.typequery=='I':
			#I: insert operation SQL
			if self.data_param=='':
				cursor.execute(q)
			else:
			    cursor.execute(q,data_param)
			self.connection.commit()			
			
		elif self.typequery=='D':
			#D: Delete operation SQL
			if self.data_param=='':
				cursor.execute(q)
			else:
			    cursor.execute(q,data_param)
			self.connection.commit()	
		elif self.typequery=='II':
			#I: insert image operation SQL
			idd=data_param[0]
			img=data_param[1]
			binario = pymysql.Binary(img)
			data_paramx=(idd,binario)
			#print data_paramx
			cursor.execute(q,data_paramx)
			self.connection.commit()			
						
    def __del__(self):
        self.connection.close()
