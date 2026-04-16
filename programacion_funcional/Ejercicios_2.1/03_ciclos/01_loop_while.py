###
#01 - Bucles (while)
#
###

from os import system
if system ("clear") != 0: system ("cls");

print("\n Bucle while");

#Bucle con una simple condicion 
contador = 0;
while contador <= 5:
    print(contador);
    contador += 1; #es super importante para evitar un bucle infinito


#utilzando la palabra break, para romper el bucle
print("\n Bucle while con break");
contador = 0;

while True:
    print(contador);
    contador += 1;
    if contador == 5:
        break; #rompe el bucle cuando contador es igual a 5

#continue, que lo que hace es saltar a la siguiente iteración del bucle
# y continuar con el bucle 
print("\n Bucle while con continue");
contador = 0;
while contador < 10:
    contador += 1

    if contador % 2 == 0: 
        continue #si es par, no continua e imprime los impares
print(contador);

#else, esta codición cuando se ejecuta?
print("\n Bucle while con else");
contador = 0;
while contador < 5:
    print(contador);
    contador +=1;
else: 
    print("El bucle ha terminado");

#pedirle al usuario un numero que tiene que ser positivo si no, no lo dejamos en paz
numero = -1;
while numero < 0:
    numuero = int(input("Introduce un numero poitivo: "));
    if numero < 0:
        print("El numero aun no es positivo, intentalo de nuevo");

print(f"El numero introducido es: {numero}");

numero = -1;
while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo"))
        if numero < 0:
            print("El numero aun no es positivo, intentalo de nuevo");
    except:
        print("Lo que debes de introducir es un numero");

print(f"El numero introducido es: {numero}");





