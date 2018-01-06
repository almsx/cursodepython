#!/usr/bin/python
# -*- coding: utf-8-*-

#Operaciones:
#1 Acceder por índice: lista[posición]
#2 Recortar: lista[inicio:final] 
#3 Comprobar pertenencia de un elemento: in

a = ['pan', 'huevos', 100, 1234]
print a[0]
#'pan'
print a[3]
#1234
print a[-2]
#100
print a[1:-1]
#['huevos', 100]
print 'huevos' in a
#True

