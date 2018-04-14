#! /usr/bin/python
#-*-encoding: utf-8 -*-
#Author: Alberto Luebbert M.

def calcularImpuesto(precio,impuesto):
	precioNuevo = float(precio / 100 * (100+impuesto))
	#print "El precio de tu producto es de $",precio
	#print "El impuestro es de", impuesto,"%"
	#print "El costo Final es $", precioNuevo
	return float(precioNuevo)
