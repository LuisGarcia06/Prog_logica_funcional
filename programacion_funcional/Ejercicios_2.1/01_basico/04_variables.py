##
#04 - Variables
#Python es de tipado dinamico y fuerte
##


from os import system
if system("clear") != 0: system("cls");

#Para asignar una variable solo hace falta poner el nombre de la variable y asignarle
my_name = "Luis Bernardo";
print(my_name) #Imprime el valor de la variable

age = 21
print(age);

#Reasignar la variable 
age = 26;
print(age) #Ahora tiene 26

#Tipado dinamico: el tipo de dato se determina en tiempo de ejecucion
#No es necesario declarar el tipo de dato a la variable
name = 'Luis Bernardo'
print(type(name)) #Tipo de dato str

name = 32;
print(type(name)); #Tipo de dato int

#Tipado fuerte: Python no realiza conversion de tipo automaticas
#Esto generara un error porque no puede sumar un numero con cadena
#print(10 + "2") xxx

#f-string(literal de cadena de formato)
print(f"Hola{my_name}, tengo{age+5} años")

#No recomendada forma de asignar variables
name, age, city = "Esteban", 22, "FCP"

#Convenciones de nombre de variables
mi_nombre_de_variable = "ok" #snake_case
nombre = "ok"

miNombreDeVariable = "No-recomendado" #camelcase
MiNombreDeVariable = "No-recomendado" #pascalcase
minombredevariable = "No-recomendado" #todojunto 

# #Anotaciones de tipo
# is_user_logged_in: bool = True #Indica que la variable es una cadena de texto
# print(is_user_logged_ins)

name_luis: str = 'Luis'
print(name_luis)

