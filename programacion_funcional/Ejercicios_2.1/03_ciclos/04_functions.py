###
#04-Funciones
#Bloques de codigo reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system ("clear") != 0: system ("cls");

#"""" Definicion de una funcion 

#def nombre_de_la_funcion(parametro1, paramentro2, ...)
#   # docstring
#   # cuerpo de la funcion
#   # return valor_de_retorno opcional

#""""

# #Ejemplo de una funcion para imprimir algo en consola
# def saludar();
#   print("Hola mundo")
# saludar();

# #Ejemplo de una funcion con un parametro
# def saludar_a(nombre);
#   print(f"Hola {nombre}")
# saludar_a();

# saludar_a("Estudiante")
# saludar_a("Jefa")
# saludar_a("Profesor")
# saludar_a("prefecto")

# Funciones con mas parametros
# def sumar(a,b):
#   suma  = a + b 
#  return suma

# result = sumar(3,2)
#  print(sumar)

##Ejemplo de una funcion con parámetro
# def restar(a,b)
# """Resta dos números y devuelve el resultado"""
#return a-b

#parametro por defecto
# def multiplicar(a, b = 2)
#   return a * b

#print(multplicar(2))
#print(multplicar(2,3))



#Argumentos por posicion
def describir_persona(nombre: str, edad: int, sexo: str):
    print(f"Soy{nombre}, tengo{edad}, y soy {sexo}")

describir_persona(1,25,"gato")
describir_persona("carlos", 25, "ingeniero")

#Argumentos por clave
#parametros nombrados
describir_persona(sexo="perro", nombre="Reyes", edad=12)
describir_persona(sexo="mujer", nombre="Alejandra", edad=23)


#Argumentos por longitud de variable(*args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1,2,3,4,5))
print(sumar_numeros(1,2))
print(sumar_numeros(1,2,3,4,5,6,7,8,9))

#Argumentos clave-valor varaiable (**kwargs)
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}, {valor}")

mostrar_informacion_de(nombre="carlos", edad=25, sexo="ave")
        