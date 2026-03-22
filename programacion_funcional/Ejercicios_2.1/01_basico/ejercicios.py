##
#06 - Ejercios
#
##


from os import system
if system("clear") != 0: system("cls");

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en lineas separadas. ")
print("Mi nombre es: Luis Bernardo \nMi ciudad es: FCP")

##

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables")
print("Usa el comando type() para determinar el tipo de dato de cada variable")
a = 15
b = 3.1416
c = 'Hola mundo'
d = True
e = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

###

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena de \"12345\" a un entero y luego en un float.")
print("Convierte el float 3.99 a un entero. Que ocurre?")
print(type(float(int("12345"))))
print(int(3.99))

###

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación")
nombre = "Luis Bernardo"
edad = 21
altura = 1.60
print(f"Hola me llamo {nombre} y tengo {edad} años, mido {altura} metros.")

# ###

print("\nEjercicios 5: Números")
print("1. Crea una variable con el numero PI (Sin asignar una variable)")
print("2. Redondea el numero con round()")
print("4. El resultado deberia de ser 1")
print(round(3.14))