#!/usr/bin/python
# -*- coding: utf-8 -*-
palabra = raw_input("Ingresa una palabra ")
while not all(x.isalpha() or x.isspace() or x in "ÁÉÍÓÚéáíóú" for x in palabra):
	palabra = raw_input("Ingresa una palabra ")
palabra = palabra.decode('utf-8').upper()
print "Las vocales de "+palabra+" son:"
for caracter in palabra:
        if caracter in u"aeiouAEIOUÁÉÍÓÚ":
           print caracter.upper()

print "Las consonantes son:"
for caracter in palabra:
        if caracter not in u"aeiouAEIOUÁÉÍÓÚ" and caracter != " ":
           print caracter.upper()