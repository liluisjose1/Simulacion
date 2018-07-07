#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb

db = MySQLdb.connect(host="localhost",    # tu host, para este ejemplo localhost
                     user="root",         # tu usuario
                     passwd="123456",  # tu password
                     db="ventas")        # el nombre de la base de datos

# Debes crear un objeto Cursor. Te permitirá
# ejecutar todos los queries que necesitas
cur = db.cursor()

# Usa todas las sentencias SQL que quieras
cur.execute("SELECT * FROM producto")

# Imprimir la primera columna de todos los registros
for row in cur.fetchall():
    print row[0], row[1],row[3]

# disconnect from server
db.close()
