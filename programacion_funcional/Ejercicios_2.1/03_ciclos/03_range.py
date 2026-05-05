###
#03-range()
#Permite crear una secuencia de numeros, util para for, pero no solo para eso.
###

from os import system
if system ("clear") != 0: system ("cls");

print("\nRange():")
#Generando una secuencia de numeros del 0 a 9
for num in range(10): #Una secuencia de numeros
    print(num);

#range(inicio, fin)
for num in range(5, 10): 
    print(num);

#range(inicio, fin, paso)
for num in range(0,1000, 5):
    print(num);

for num in range(-5, 0):
    print(num);

for num in range(0, 10, -1):
    print(num);

for num in range(0, 444):
    print(num);

nums = range(10);
list_of_nums = list(nums);
print(list_of_nums);

# seria para hacerlo cinco veces 
for _ in range(5):
    print("Hacerlo 5 veces algo");

###
# EJERCICIOS (range)
##

#