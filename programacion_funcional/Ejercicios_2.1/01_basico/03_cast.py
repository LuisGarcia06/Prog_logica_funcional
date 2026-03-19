###
#03-casting de types
#Transformar valores
##

from os import system
if system("clear") != 0: system("cls");

print("Conversion de tipos")

#Convertir una cadena a entero
print(2 + int("100")) #Convierte un "100" a entero y suma 2

#Convertir un entero a cadena
print("100" +str(2)) #Convierte el 2 a cadena y lo concatena. 

#Convertir una cadena a float
print(type(float("3.1416"))) #Convierte "3.1416" a float y muestra su tipo

#Convertir un numero decimal a entero
print(int(3.1416)) #Convierte 3.1416 a 3 eliminando los decimales

#Evaluar valores numericos como booleanos
print(bool(3)) #Cualquier numero distinto de 0 es true
print(bool(0)) #Cualquier numero 0 es false
print(bool(-1))

#Evaluar cadenas como booleanos
print(bool("")) #Una cadena vacia es false
print(bool(" ")) #Una cadena con espacio es true
print(bool("False")) #Una cadena con texti es true

#Redondear un numero decimal
print(round(2.51))

