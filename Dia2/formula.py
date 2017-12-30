#!/usr/bin/python
import math

a = input("Ingresa el valor de a ")
b = input("Ingresa el valor de b ")
c = input("Ingresa el valor de b ")

x1 = (-b+math.sqrt((pow(b,2)) -(4*a*c)))/(2*a)
x2 = (-b-math.sqrt((pow(b,2)) -(4*a*c)))/(2*a)

print "Si a = " , a , ", b = " , b , " y c = " , c , ", el valor de X1 seria: " , x1
print "Si a = " , a , ", b = " , b , " y c = " , c , ", el valor de X2 seria: " , x2