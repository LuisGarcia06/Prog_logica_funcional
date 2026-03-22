##
#01- Sentencias condicionales (if, elif, else)
#Permiten ejecutar bloques de codigo si cumplen una condición
##

from os import system
if system("clear")!=0: system("cls");

print("\nSentencia simple condicional")
#Solo podemos usar la palabra clave if para ejecutar un bloque de codigo
#Solo si cumple una codición 
edad = 18
if edad >=18:
    print("Felicidades eres mayor de edad")

#Si no se cumple la condición no se ejecuta 
edad = 15
if edad >=18:
    print("Felicidades eres mayor de edad")


print("\nSetencia condicional con else")
#Podemos usar el comando else para ejecutar un bloque de codigo 
#si no se cumple la codición anterior de if
edad = 15;
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

print("\nSetencia condicional con elif")
#Ademas de usar "if" y "else" podemos usar "elif" para determinar 
#Multiple condiciones, ten en cuenta que solo se ejecutara el primer bloque de codigo
#que cumpla la condición (o la de else, si esta presente)
nota = 4;
if nota >= 9:
    print("¡Sobresaliente!")
elif nota >= 7:
    print("¡Aprobado!")
elif nota >= 5:
    print("¡Aprobado!")
else:
    print("No esta calificado")

print("\nCondiciones Multiples")
edad = 15
tiene_carnet = True
#Los operadores logicos en python son
#and: True si ambos son verdaderos
#or: True si almenos uno de los operandos es verdadero
#En javascript
#&& seria and
#|| seria or
if edad >=18 and tiene_carnet:
    print("Puedes condicir")
else:
    print("¡¡¡¡Policia!!!!!!")

#En uno pueblo de Isla Holbox son mas relajados y 
#te dejan conducir si eres mayor de edad o tienes carnet
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la isla holbox")
else:
    print("Paga al policia y te dejara conducir!!!")

#Tambien tenemos el operador logico not
#que nos permite negar una condición 
es_fin_de_semana = False
#javascript => !
if not es_fin_de_semana:
    print("!ISC, anda que hay que ir al Tec!")

print("\nAnidar condicionales")
#Podemos anidar condicionales, uno dentro del otro
#Para determinar multiples condiciones aunque 
#siempre intentaremos evitar esto para simplificar
edad = 20
tiene_dinero = False
if edad >= 20:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la discoteca")

# Más fácil sería:
#if edad < 18:
# print("No puedes entrar a la disco")
# elif tiene_dinero:
# print("Puedes ir a la discoteca")
# else:
# print("Quédate en casa")

#Ten en cuenta que hay valores que al usarlos como condiciones
# en python son evaluados como verdaderos o falson
# por ejemplo, el numero 5, es true
numeros = 5
if numeros: #True
    print("El numero no es cero")

#Pero el numero 0 se evalua como falso
numero2 = 0
if numero2: #False
    print("Aqui no entrará nunca")

#Tambien el valor vacio "" se evalua como False
nombre2 = ""
if nombre2:
    print("El nombre no es vacio")

# !Ten cuidad con no confundir la asignación = con la comparación ==!
numero3 = 3
es_el_tres = numero3 == 3

if es_el_tres:
    print("El numero es 3")


print("\nLa condición ternaria:")
#Aveces podemos crear condicionales en una sola linea usando
#las ternarias, es una forma concisa de un if-else en una linea de codigo
# [codigo si cumple la codicion] if [condición] else [codigo si no cumple]
edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
#EJERCICIOS
###

#Ejercicio 1: Determinar el mayor de dos numeros
#Pide al usuario que introduzca dos numeros 
#Y muestre un mensaje de cual es mayor o si son iguales
print("\nEjercicio 1: Determinar el mayor de dos numeros")
number1 = input("Introduzca el primer numero:")
number2 = input("Introduzca el segundo numero:")

if number1 == number2:
    print("Los numeros son iguales")
elif number1 > number2:
    print("El primer numero es mayor")
else:
    print("El segundo numero es mayor")

#Ejercicio 2: Calculadora simple
#Pide al usuario que introduzca dos numeros y una operación (+,-,*,/) 
#Realiza la operación y muestra el resultado(maneja la división entre 0)

operacion = input("Ingresa la operación:" )
if operacion == "+":
    print("La suma de los numeros es de: ", int(number1) + int(number2))
elif operacion == "-":
    print("La resta de los numeros es de: ", int(number1) - int(number2))
elif operacion == "*":
    print("La multiplicación de los numeros es de: ", int(number1) * int(number2))
elif operacion == "/":
    if int(number1) == 0 or int(number2) == 0:
        print("No se puede dividir entre cero")
    else:
        print("La división de los numeros es de: ", int(number1) / int(number2))

#Ejercicio 3: Año bisiesto
#Pida al usuario que introduzca un año y determina si es bisiesto
#Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 y no por 400

print("\nEjercicio 3: Año bisiesto")
bisiesto = int(input("Ingresa el año por favor: "))
if bisiesto % 4 == 0:
    if bisiesto % 100 == 0:
        if bisiesto % 400 == 0:
            print(f"El año de {bisiesto} es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año no es bisiesto")
else:
    print("El año no es bisiesto")

 
#Ejercicio 4: Categorizar edades
#Pide al usuario que introduzca una edad y las clasifique en
#-Bebe (0-2 años)
#-Niño (3-12 años)
#-Adolescente (13-17 años)
#-Adulto(18-64 años)
#-Adulto mayor (65 años o mas)

print("\nEjercicio 4: Categorizar edades")
edad_usuario = int(input("Ingresa su edad porfavor: "))
if edad_usuario <=2:
    print("Bebe")
elif edad_usuario >= 3 and edad_usuario <=12:
    print("Niño")
elif edad_usuario >= 13 and edad_usuario <=17:
    print("Adolescente")
elif edad_usuario >= 18 and edad_usuario <= 64:
    print("Adulto")
else:
    print("Adulto Mayor")
