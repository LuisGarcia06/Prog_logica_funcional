###
#02 Types
#Python tiene varios tipos de datos
###

from os import system
if system("clear") != 0: system("cls");

'''
El comando type() devuelve el tipo de dato de un objeto en python
'''

print("int:"); #Entero sin la parte decimal
print(type(10)); #Numero entero positivo
print(type(0)); #El numero 0 tambien es un entero
print(type(-5)); #El numero entero negativo
print(type(6564594484488285858858)); #Python permite enteros de gran tamaño


print("float:") #Numeros decimales (de punto flotante)
print(type(3.14)) #Numero con punto decimal
print(type(1.0)) #Tambien se considera una float
print(type(1e3)) #Notacion cientifica

print("Complejo:") #Numeros complejos (con reales e imaginarios)
print(type(1+2j)) #Numero complejo en python

print("str:") #Cadenas de texto
print(type("Hola")) #Un string con texto
print(type("")) #Un string vacio
print(type("123")) #Numero pero sigue siendo string
print(type("""
    Multilinea
""")) #Un string que abarca varias lineas


print("bool:") #Booleanos
print(type(True)) #Valor booleano verdadero
print(type(False)) #Valor booleano falso
print(type(1<2)) #Comparacion que devuelve un booleano

print("NoneType") #Nulos
print(type(None)) #'Nulo' es un tipo de datos especio que representa "Sin valor"

