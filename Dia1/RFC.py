#/usr/bin/python 
#-*-encoding: utf-8 -*-

while True:
	Fname =raw_input("primer nombre: " )
	if len(Fname) > 0 and Fname.isalpha() :
		break 
	else:
		print ("\033[32merror datos inv\033[m")


while True:
	Sname =raw_input("segundo nombre: " )
	if len(Sname) > 0 and Sname.isalpha() :
		break 
	else:
		print ("\033[32merror datos inv\033[m")



while True:
	apellido=raw_input("apellido paterno: " )
	if len(apellido) > 0 and apellido.isalpha() :
		break 
	else:
		print ("\033[32merror datos inv\033[m")



while True:
	apellidom=raw_input("apellido materno: " )
	if len(apellidom) > 0 and apellidom.isalpha() :
		break 
	else:
		print ("\033[32merror datos inv\033[m")


while True:
	dia=raw_input("dia de nacimiento: ")
	if len(dia) > 0 and dia.isdigit() :
		break 
	else:
		print ("\033[32merror datos inv\033[m")



while True:
	mes=raw_input("mes de nacimiento: ")
	if len(mes) > 0 and mes.isdigit() :
		break 
	else:
		print ("\033[32merror datos inv\033[m")



while True:
	year=raw_input("anhio de nacimiento: ")
	if len(year) > 0 and year.isdigit() :
		break 
	else:
		print ("\033[32merror datos inv\033[m")



MFname= Fname.upper()

#SI ES JOSE, TOMA EL SEGUNDO NOMBRE, SI NO HAY SEGUNDO, TOMA EL PRIMERO.
if len(Sname)==0:
	name2= MFname[:1]
elif MFname=="JOSE" or "MARIA":
	name2=Sname[:1] 
else: 
	name2= Sname[:1]

#AGREGA UN DIGITO AL DIA, SI LO NESECITA y 
if  len(dia)==1:
	dia2= "0" + str(dia)
else: 
	dia2= "0" + str(dia)

#AGREGA UN DIGITO AL MES, SI LO NESECITA.
if len(mes)==1 :
		mes2= "0" + str(mes)
else:
	mes2=mes

#SOLO USA LOS DOS ULTIMOS DIGITOS DEL ANHIO

if len(year)==4:
	year2= year[2:]
else: 
	year2=year

x=apellido[:2].upper()
y=apellidom[:1].upper()
z=name2.upper()
anio=year2
RFCx= x + y + z

#REVISA EL RFC, QUE NO TENGO PALABRAS PROHIBIDAS.

lista=['PUTO','CULO', 'PIPI','COLA','pedo', 'MOGY']

check= RFCx in lista

if check == True:
	x1=x[:1] + "X"
else:
	x1=x

RFCx1= x1 + y + z

RFC= RFCx1 + dia2 + mes2 + anio + "xxx"


print ("\033[32m" + RFC + "\033[0m")
 











