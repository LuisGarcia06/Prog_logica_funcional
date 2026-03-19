#Importamos el modulo OS
from os import system;

#system() nos permite ejecutar un comando en la terminal
if system ("clear") != 0: system("cls")

#
print( "¡Hola crayola!");

#Comillas simples
print('Esto tambien es una comilla');

#Imprimir multiples elementos separados por un espacio
print('Python', 'es', 'genial');

#Parametro 'SEP' permite definir como separar los elementos
print('Python', 'es', 'brutal', sep="-");

#El parametro 'end'
