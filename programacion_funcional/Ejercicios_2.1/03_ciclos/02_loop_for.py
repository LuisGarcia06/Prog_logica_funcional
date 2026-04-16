###
#02- Bucles (for)
#
###

from os import system
if system ("clear") != 0: system ("cls");

#Iterar una lista 
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta);

#Iterar sobre cualquier cosa que sea iterable
cadena = "estudiante";
for character in cadena:
    print(character)

#enumerate():
frutas = ["manzana", "pera", "mandarina"];
for idx, value in enumerate(frutas):
    print(f"El indice es: {idx} y la fruta es: {value}");

#Bucles anidados
letras = ["a", "b", "c"];
numeros = [1, 2, 3];

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

#break 
print("\nBreak")
animales = ["perro", "gato", "conejo", "tortuga", "pez", "raton"];
for idx, animal in enumerate(animales):
    print(animal);
    if animal == "tortuga":
        print(f"Encontramos la tortuga en el indice: {idx}");
        break;

#continue
print("\nContinue")
animales = ["perro", "gato", "conejo", "tortuga", "pez", "raton"];
for idx, animal in enumerate(animales):
    if animal == "tortuga":
        continue;
    print(animal);

#compresion de listas 
animales = ["perro", "gato", "conejo", "tortuga", "pez", "raton"];
animales_mayus = [animal.upper() for animal in animales];
print(animales_mayus);

#Muestra los numeros pares de la lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]; #el primer num es el que se va a mostrar, el segundo num es el que se va a iterar y el if es la condicion para mostrar el numero
print(pares);
