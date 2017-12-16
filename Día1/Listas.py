lista = ["Karina", 'Ricardo', "Alan", 'Roger','Alberto']

print lista[0]
print lista[1:3]
print lista[-4]

lista[1] = 'Fantasma que azota el edificio'
print lista
lista.append('Arturo')
print lista
indice = lista.index('Alan')
print indice
#eliminar
del lista[indice]
print lista
del lista[0]
print lista