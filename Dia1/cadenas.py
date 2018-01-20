#!/usr/bin/python
# -*- coding: utf-8-*-

#Metodos aplicables a Cadenas

#lower(): convertir en minúsculas
minusculas = "CURSO DE PYTHON"
print minusculas
print minusculas.lower()

#upper(): convertir en minúsculas
mayusculas = "curso de python"
print mayusculas
print mayusculas.upper()

#isdigit(): ¿es numérico?
#Valida que un valor sea numerico ... 0 al 9
soy_numero = '5'
if soy_numero.isdigit():
    print "Cierto, soy digito"
else: 
    print "Falso, no soy digito"

#isalpha(): ¿es alfanumérico?
#Valida que un valor tenga letras
soy_letras = 'Alberto'
if soy_letras.isalpha():
    print "Cierto, Soy letras"
else:
    print "Falso, no soy letras"

#islower(): ¿está en minúsculas?
#valida que el objeto este en minusculas
soy_minusculas = "estoyminusculas"
if soy_minusculas.islower():
    print("Si esta en minusculas")
else: 
    print("no esta en minusculas")

#isupper(): ¿está en mayúsculas?
#Valida que la cadena este en Mayusculas
soy_mayusculas = "ESCRITOENMAYUSCULAS"
if soy_mayusculas.isupper():
    print("Si esta en mayusculas")
else: 
    print("no esta en mayusculas")

