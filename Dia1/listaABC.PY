#/usr/bin/python 
#-*-encoding: utf-8 -*-
#agregar acentos
lista=['a','b', 'c','d','e','f', 'g','h']

print lista[0:9]
print "el primer caracter fue " + str(lista[0])
print "la letra F se encuentra en la posicion " + str(lista.index("h"))
print "se agregra la letra H " 
lista.append('h')
print lista 
print "agregar mayusculas"
lista[0:9]=['A','B', 'C','D', 'd','E','F', 'G','H']
print lista
print "elimina ese error " 
del lista[4]
print lista
print "México"
