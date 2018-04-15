#! /usr/bin/python
#-*-encoding: utf-8 -*-
#Author: Alberto Luebbert M.

class Perro(object):

	def __init__(self, nombre, raza, edad):
		self.nombre = nombre
		self.raza = raza
		self.edad = edad

	def ladra(self):
		print self.nombre, "dice ¡Woof! y tiene", self.edad

mascota = Perro("Coco", "Collis", 18)
mascota.ladra()