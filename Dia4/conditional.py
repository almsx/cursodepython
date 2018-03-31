#!/usr/bin/python
# -*- encoding: utf-8 -*-


# edad = input("Ingrese la edada a considerar: ")
monto_compra = input("Ingrese el monto de la compra: ")

# if edad >= 18:
# 	print "Entregar IFE/INE"
# else:
# 	print "Es menor de edad"

if monto_compra <= 100:
	print "Pago en efectivo"
elif monto_compra == 110 or monto_compra == 220 or monto_compra == 330:
	print "Pago con vale despensa CDMX"	
elif monto_compra > 100 and monto_compra <= 300:
	print "Pago con tarjeta de debito"
else:
	print "Pago con tarjeta de credito"

