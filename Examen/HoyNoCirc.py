#!/usr/bin/python
# -*- coding: utf-8-*-

placa = raw_input("Digita tu numero de placa ( formato XXX000 ): ")
anio = input("Ingresa el anio de tu automovil (formato 0000): ")
marca = raw_input("Que marca es tu vehiculo?: ")


if  placa[-1:] == "1" or placa[-1:] == "2" :
	calcomania = "Tu Vehiculo calcomania VERDE. "
	circula = " los dias Jueves"
	sabado = ", descansara el cuarto sabado de abril y el ultimo sabado de mayo y junio"
elif placa[-1:] == "3" or placa[-1:] == "4" :
	calcomania = "Tu Vehiculo calcomania ROJO. "
	circula = " los dias Miercoles"
	sabado = ", descansara el 3er sabado de cada mes"
elif placa[-1:] == "5" or placa[-1:] == "6" :
	calcomania = "Tu Vehiculo calcomania AMARILLO. "
	circula = " los dias Lunes"
	sabado = ", descansas en mayo y junio el 1er sabado"
elif placa[-1:] == "7" or placa[-1:] == "8" :
	calcomania = "Tu Vehiculo calcomania ROSA. "
	circula = " los dias Martes"
	sabado = ", descansaras el 2o sabado de cada mes"
elif placa[-1:] == "9" or placa[-1:] == "0" :
	calcomania = "Tu Vehiculo calcomania AZUL. "
	circula = " los dias Viernes"
	sabado = ", descansa un sabado en abril"

if anio == 2007 or anio == 2008 or anio == 2009:
	circula = "Debe actualizar su estatus o dejara de circular" + circula + sabado
elif anio < 2007:
	circula = "Ya no circulas" + circula + sabado
elif anio > 2009:
	circula = "Circula todos los dias"

print( calcomania + circula + " y es un vehiculo marca " + marca.upper())