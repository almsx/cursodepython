#!/usr/bin/python
lista = ["almendras", 'brocoli', "zanahoria", "cereal","ensalada"]
opcion = raw_input("Que comiste hoy? ")
blnOk=False

for elemento in lista:
	if opcion==elemento:
		print opcion
		blnOk=True

if blnOk==True:
	print "Felicidades, comes bien"
else:
	print "Comes mal, te recomendamos comer algo de esto:"
	for elemento in lista:
		print elemento
