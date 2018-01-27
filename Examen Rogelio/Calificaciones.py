#!/usr/bin/python
# -*- coding: utf-8-*-

c1 = input("Ingresa la 1er calificacion: ")
c2 = input("Ingresa la 2a calificacion: ")
c3 = input("Ingresa la 3er calificacion: ")
c4 = input("Ingresa la 4a calificacion: ")
c5 = input("Ingresa la 5a calificacion: ")

miTupla = (c1,c2,c3,c4,c5)
while not (z.isnumeric() for z in miTupla):
    print("Debes ingresar unicamente numeros")
    miTupla = raw_input("Ingresa la 1er calificacion: ")  

mayor = -10000000000
menor = 10000000000
for x in miTupla:
	if (x) > mayor:
		mayor = x

for y in miTupla:
	if (y) < menor:
		menor = y

print "El numero mayor capturado es: " + str(mayor) + ", y el numero menor es: " + str(menor)