#! /usr/bin/python
# -*- encoding: utf-8 -*-

def saludar():
	str = "Hola mundo"
	return str
	
print "Mensaje desde función Saludar -> ", saludar()

def calculadora(a, operacion, b):
	valor1 = a
	valor2 = b

	if operacion == "+":
		resultado = valor1 + valor2
	elif operacion == "-":
		resultado = valor1 - valor2

	return str(resultado)

print ("Suma " + calculadora(1,"+", 1))
print ("Resta " + calculadora(7,"-", 5))
