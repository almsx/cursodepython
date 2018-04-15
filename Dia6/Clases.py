#! /usr/bin/python
#-*-encoding: utf-8 -*-
#Author: Alberto Luebbert M.

class PrimeraClase:
	"Esta es mi primera clase"
	a = 10
	def func(self):
		print('Hola Mundo!')

# create a new MyClass
ob = PrimeraClase()

# Mandamos a llamar a una función dentro de mi clase
# Salida: Hola Mundo!
ob.func()
print ob.a