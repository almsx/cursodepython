#/usr/bin/python 

#edad=45
#if edad >=18:
#	print "entregar IFE"
#else:
#	print "menor de edad"

compra= input ("cuanto gasto? ")
if compra<100:
	print "paga con efectivo"
elif compra ==110 or compra==220 or compra==330:
	print "paga con vale de descuento"
elif compra >=100 and compra <=300:
# el elif es una condicion en una condicion.
	print "pago con tarjeta de debito"
else:
	print "pago con tarjeta de credito"

