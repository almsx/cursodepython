#! /usr/bin/python
#-*-encoding: utf-8 -*-
# -*- encoding: utf-8 -*-

#Author: jcastelo on 030318

mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]

print 'Mi lista original es: ' + str(mi_lista)

print 'El primer elemento es: ' + str(mi_lista[0])
print 'El segundo elemento es: ' + str(mi_lista[1])
print 'El tercer elemento es: ' + str(mi_lista[2])
print 'El penultimo elemento es: ' + str(mi_lista[-2])
print 'El ultimo elemento es: ' + str(mi_lista[4]) 

# Aqui estamos cambiando un elemento de la lista

nuevo_elemento = input("Ingrese el nuevo elemento: ")
print 'El nuevo elemento es: ', nuevo_elemento
mi_lista[2] = nuevo_elemento

print 'Mi nueva lista es: ' + str(mi_lista)

#Con append le agregamos el nuevo dato al final

mi_lista.append('Nuevo Dato')

print 'Mi nueva lista agregada es: ' + str(mi_lista)

print 'cadena de texto esta en la posicion:  ' + str(mi_lista.index("cadena de texto"))

# Buscando posicion

ubicacion = mi_lista.index(nuevo_elemento)

del mi_lista[ubicacion]

print 'La nueva lista menos el nuevo elemento es: ' + str(mi_lista)





