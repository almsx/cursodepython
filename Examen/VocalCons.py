#!/usr/bin/python 
# -*- coding: utf-8-*- 


cadena = raw_input("Ingresa alguna palabra: ")
a = b = espacios = con = voc = num = ""
count = cuenta = 0

for x in cadena.upper():
	if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
		a = a + x
		voc = " - Las vocales son: " + a
	elif x == " ":
		count = count + 1
		espacios = " - Ingresaste: " + str(count) + " espacio(s)"
	elif x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9" or x == "0":
		cuenta = cuenta + 1
		num = " - Hubo: " + str(cuenta) + u" número(s)"
	else:
		b = b + x
		con = " - Las consonantes son: " + b

print  voc + con + espacios + num

