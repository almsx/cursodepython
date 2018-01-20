#!/usr/bin/python
palabra = raw_input("Ingresa una palabra ")
while not all(x.isalpha() for x in palabra):
	palabra = raw_input("Ingresa una palabra ")
print "Las vocales son:"
for caracter in palabra:
        if caracter in "aeiouAEIOU":
           print caracter + caracter.upper()

print "Las consonantes son:"
for caracter in palabra:
        if caracter not in "aeiouAEIOU":
           print caracter + caracter.upper()