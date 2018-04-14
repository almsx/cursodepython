#! /usr/bin/python
#-*-encoding: utf-8 -*-

# Farenheit a Centigrados

#0 to 120 Centigrados

inicio = input("Ingrese el rango inicial de grados centigrados a convertir: ") 
limit = input("Ingrese el rango final de grados centigrados a convertir: ")
#print Farenheit

while inicio <= limit:
	Farenheit = (inicio * 1.8) + 32
 	print str(inicio) + " grados Celcius equivalen a " + str(Farenheit) + " Farenheit"
 	inicio += 1  