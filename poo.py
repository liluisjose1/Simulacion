#! /usr/bin/env python
# -*- coding: utf-8 -*-
#clase base

class Persona(object):
	""" Class doc """
	
	def __init__ (self,dui,nombre,apellido):
		self.dui=dui
		self.nombre=nombre
		self.apellido=apellido
	def mostrar (self):
		return "%s: %s, %s " % (str(self.dui,self.nombre,self.apellido))
		""" Function doc """
class Alumno(Persona):
	""" Class doc """
	
	def __init__ (self,dui,nombre,apellido,due):
		persona.__init__(self,dui,nombre,apellido)
		self.due = due
	def mostrar (self):
		""" Function doc """
		return "DUE:%s ALUMNO:%s DUI:%S"

