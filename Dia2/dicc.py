#!/usr/bin/python
Agenda = [{'id':1, 'nombre': 'Juana', 'tel': '5556581111', 'mail':'prueba@mail.com', 'edad':35, 'edoCivil': 'Soltero'},
{'id':2, 'nombre':'Petra', 'tel':'6589524554', 'mail':'petra@mail.com', 'edad':21, 'edoCivil':'Divorciada'},
{'id':3, 'nombre':'Jacinto', 'tel':'2224578554', 'mail':'jaci21@mail.com', 'edad':63, 'edoCivil':'Casada'},
{'id':4, 'nombre':'Rumualdo', 'tel':'8153968554', 'mail':'rumu25@mail.com', 'edad':57, 'edoCivil':'Casado'},
{'id':5, 'nombre':'Anastacia', 'tel':'3356895241', 'mail':'ani25ss@mail.com', 'edad':18, 'edoCivil':'Soltera'}]



for item in Agenda:
	print (item['nombre'])
	print (item['tel'])
	print (item['mail'])