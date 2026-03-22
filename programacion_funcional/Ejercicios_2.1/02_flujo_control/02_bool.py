###
#02-Booleanos
#valores logicos: True (verdadero) y False (falso)
#Fundamentales para el control de flujo y la logica en programación
###

from os import system
if system("clear")!=0: system("cls");

print("\nValores booleanos básicos")
#Los booleanos representan valores de verdad: True o False.
print(True)
print(False)

print("\nOperadores de comparación: devuelven un valor booleano")
#Operadores de comparación: devuelven un valor booleano.
print("5 > 3:", 5 > 3) #True
print("5 < 3:", 5 < 3) # False
print("5 == 5:", 5== 5)      #True (igualdad)
print("5 != 3:", 5 != 3) #True (desigualdad)
print("5 >= 5:", 5 >= 5) #True (mayor o igual que)
print("5 <= 3:", 5 <= 3) # False (menor o igual que)

print("\nComparacion de cadenas")
print(" 'manzana' < 'pera':", "manzana" < "pera") #True
print(" 'Hola' == 'hola'", "Hola" == "hola") #False

# Operadores lógicos: and, or, not 
print("\nOperadores lógicos:")
print("True and True:", True and True) #True
print("True and False:", True and False) # False
print("True or False:", True or False) # True
print("False or False:", False or False) # False
print("not True:", not True) # False 
print("not False:", not False) #True 

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")
print("\nand:")
print("A      B      A and B")
print("True   True  ", True and True)
print("True   False", True and False)
print("False  True  ", False and True)
print("False  False", False and False)

print("\nor:")
print("A      B      A or B")
print("True   True  ", True or True)
print("True   False", True or False)
print("False  True  ", False or True)
print("False  False", False or False)

print("\nnot:")
print("A      not A")
print("True  ", not True)
print("False", not False)