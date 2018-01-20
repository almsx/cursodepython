#!/usr/bin/python
# -*- coding: utf-8-*-

p_ap = raw_input("Ingresa el Apellido Paterno ")
p_am = raw_input("Ingresa el Apellido Materno ")
p_no = raw_input("Ingresa el Nombre ")
p_ye = raw_input("Ingrese el Año de Nacimiento ")
p_mo = raw_input("Ingrese el Mes ")
p_da = raw_input("Ingrese el Día ")

p_f_ye = p_f_mo = p_f_da = m_ap =  m_am = m_no = a_ap = ""
#Apellido Paterno - 1a Forma
#if all(x.isalpha() or x.isspace() for x in p_ap):
#    m_ap = p_ap[:2]
     #Agregar validacion de las vocales
#else:
#    print("El Apellido Paterno debe incluir unicamente letras")
#    m_ap = "XX"

#Apellido Paterno - 2a Forma
while not all(x.isalpha() or x.isspace() for x in p_ap):
    print("El Apellido Paterno debe incluir unicamente letras")
    p_ap = raw_input("Ingresa el Apellido Paterno ")   

#Incluir validación de las vocales
x_ap = p_ap[1:]
for x in x_ap.upper():
	if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
		a_ap = x
		break

m_ap = p_ap[:1] + a_ap

#Apellido Paterno
if all(x.isalpha() or x.isspace() for x in p_am):
    m_am = p_am[:1]
else:
    print("El Apellido Materno debe incluir unicamente letras")
    m_am = "X"

#Nombre
if all(x.isalpha() or x.isspace() for x in p_no):    
    m_no = p_no[:1]
else:
    print("El Nombre debe incluir unicamente letras")
    m_no = "X"

#Año
if p_ye.isdigit():
    #calculo la longitud
    m_ye = str(p_ye)
    if len(m_ye) == 2:
        #print("Son 2")
        p_f_ye = m_ye
    elif len(m_ye) == 4:
        #print("son 4")
        p_f_ye = m_ye[2:]
else:
    print(u"El año debe ser solo digitos")
    p_f_ye = "00"

#Mes
if p_mo.isdigit():
    #calculo la longitud
    m_mo = str(p_mo)
    if len(m_mo) == 2:
        #print("Son 2")
        p_f_mo = m_mo
    elif len(m_mo) == 1:
        #print("son 1")
        p_f_mo = "0" + m_mo[:1]
else:
    print(u"El mes debe ser solo dígitos")
    p_f_mo = "00"

#Dia
if p_da.isdigit():
    #calculo la longitud
    m_da = str(p_da)
    if len(m_da) == 2:
        #print("Son 2")
        p_f_da = m_da
    elif len(m_da) == 1:
        #print("son 1") 
        p_f_da = "0" + m_da[:1]
else:
    print(u"El día debe ser solo digitos")
    p_f_da = "00"


#Calculamos el RFC
rfc = m_ap + m_am + m_no + "-" + p_f_ye + p_f_mo + p_f_da + "-XXX"
print rfc.upper()