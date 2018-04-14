#! /usr/bin/python
#-*-encoding: utf-8 -*-

import math

number = input('Ingrese el numero a utilizar para el calculo: ')
sen = math.sin(number)
cos = math.cos(number)
tan = math.tan(number)
raiz = math.sqrt(number)
fab = math.fabs(number)

redondeo1 = math.ceil(number)
redondeo2 = math.floor(number)
#factor = math.factorial(number)
potencia = math.pow(number,2)


print "El Seno es = ",sen
print "El Coseno es = ",cos
print "La tangente es = ",tan
print "La raiz es = ",raiz
print "El valor absoluto es = ",fab
print "El numero superior es = ",redondeo1
print "El numero inferior es = ",redondeo2
#print "El factorial es = ",factor
print "La pontencia es = ",potencia
