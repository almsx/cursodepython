#!/usr/bin/python
# -*- coding: utf-8-*-

agenda=[{'idContacto':'1',
		'Nombre':'Ricardo',
		'Apellidos':'Cruz',
		'Edad':25,
		'Telefono':'5549423627',
		'Email':'cruz.r230@gmail.com',
		'Direccion':'Real del oro 9'
		},
		{'idContacto':'2',
		'Nombre':'Arturo',
		'Apellidos':'Castro',
		'Edad':27,
		'Telefono':'5577542365',
		'Email':'castroa@gmail.com',
		'Direccion':'Bugambilias 5'
		},
		{'idContacto':'3',
		'Nombre':'Adolfo',
		'Apellidos':'Cruz',
		'Edad':30,
		'Telefono':'5540721018',
		'Email':'adolfoc97@gmail.com',
		'Direccion':'Real del oro 9'
		},
		{'idContacto':'4',
		'Nombre':'Daniel',
		'Apellidos':'Macias',
		'Edad':45,
		'Telefono':'5564785234',
		'Email':'danyfantom@gmail.com',
		'Direccion':'culiacan 78'
		},
		{'idContacto':'5',
		'Nombre':'Fernanda',
		'Apellidos':'Alonso',
		'Edad':24,
		'Telefono':'5597654512',
		'Email':'alonsomrf@gmail.com',
		'Direccion':'zaragosa 49'
		}]

for item in agenda:
	print(item['Nombre'])
	print(item['Email'])
	print(item['Telefono'])