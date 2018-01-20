#!/usr/bin/python
# -*- coding: utf-8-*-
# Ambitos de Variables
# local: dentro de la función
# global: fuera de la función

cont = 0
def prueba():
    global cont
    incremento = 1
    cont = cont + incremento
    print cont

print cont
prueba()