#Colores.py
#Imprimir un mensaje bajo colores

#Imprime mensaje normal
print ("Hola Mundo")

#Imprime mensaje en color verde
print ("\033[32mHola Mundo")

#Imprime mensaje con negritas
print("\033[1mHola Mundo \033[0m ")

#Imprimira la palabra Hola Mundo con fondo de color rojo y letra color azul.
print ("\033[41;34mHola Mundo \033[0m")

#Imprimira la palabra con subrayado
print ("\033[4mHola Mundo\033[0m")

#Imprimir una variable
mensaje = "Hola Mundo desde variable"

#Imprimir en color y subrayado el contenido de una variable
print ("\033[4;34m"+mensaje)