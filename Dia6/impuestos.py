#! /usr/bin/python
#-*-encoding: utf-8 -*-
#Author: Alberto Luebbert M.

import Calculo

costo = 321.01
impuesto = 16

print "El costo de tu articulo es de $",costo, ". Si aplicamos un impuesto del ",impuesto,"%  tendra un costo final de $",Calculo.calcularImpuesto(costo,impuesto)