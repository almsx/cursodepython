#!/usr/bin/python
palabra = raw_input("Ingresa una palabra ")
while not all(x.isalpha() or x.isspace() for x in palabra):
	palabra = raw_input("Ingresa una palabra ")
print "Las vocales son:"
for caracter in palabra:
        if caracter in "aeiouAEIOU":
           print caracter + caracter.upper()

print "Las consonantes son:"
for caracter in palabra:
        if caracter not in "aeiouAEIOU" and caracter != " ":
           print caracter + caracter.upper()