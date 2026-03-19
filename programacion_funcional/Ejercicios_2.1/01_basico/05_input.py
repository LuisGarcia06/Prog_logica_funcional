##
#05 - Input
#Python es de tipado dinamico y fuerte
##


from os import system
if system("clear") != 0: system("cls");

#Para obtener datos de usuario se usa el input()
#La funcion input() recibe un mensaje que se muestra al usuario
#y devuelve el valor introducido por el usuario
nombre = input("Hola, ¿Como te llamas?\n")
print(f"Hola {nombre}, encatado de conocerte")

#Ten en cuenta que la funcion input() siempre devuelve un string
#Asi que hay que convertir
age = input("¿Cuantos años tienes?\n")
print(f"Tienes {age} años")

#Puede devolver varios valores 
#Para hacerlo, usuario debe separar los valores con una coma
print("Imprimir varios valores a la vez")
country, city = input("¿En que pais y ciudad vives\n").split();

print(f"Vives en {country}, {city}")


