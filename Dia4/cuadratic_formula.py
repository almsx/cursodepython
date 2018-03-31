#!/usr/bin/python
# -*- encoding: utf-8 -*-

# Formula cuadratica

import math

a = -3
b = 8
c = 4

cuadratica1 = (-b + math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
cuadratica2 = (-b - math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)

print 'El primer resultado es = ',cuadratica1
print 'El segundo resultado es = ',cuadratica2


# Factor by Factor

# first_factor = math.pow(b,2) - 4*a*c
# second_factor = math.sqrt(first_factor)
# thrid_factor = -b + second_factor
# final_factor_positivo = thrid_factor/(2*a)
# #cuadratica2 = ((-b) - math.sqrt((math.pow(b,2) - 4*a*c))/2*a

# #print "El primer resultado es = ",first_factor
# #print "El segundo resultado es = ",second_factor
# #print "El tercer resultado es = ", thrid_factor
# print "El primer factor es = ", forth_factor

