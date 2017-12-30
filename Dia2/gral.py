#!/usr/bin/python
import math

a = input("Ingresa el valor de a ")
b = input("Ingresa el valor de b ")
c = input("Ingresa el valor de b ")


x1 = (-b + math.sqrt((b*b) - 4*a*c)) / 2*a
x2 = (-b - math.sqrt((b*b) - 4*a*c)) / 2*a

print x1
print x2