# Ejercicio 3: Inflar globos
# Objetivo: Crea un programa que simule la inflada de globos 🎈 para una fiesta, de acuerdo al número de invitados que asistirán.
def inflarglobo():
    return "🎈"

inflar_globo_lambda = lambda : "🎈";

invitados = int(input('Ingrese los invitados porfavor: '));

globo = [inflar_globo_lambda for i in range(invitados)]

def preparar_globos(numero_invitados):
    lista = [inflar_globo_lambda() for _ in range(numero_invitados)]
    return lista

numero = int(input("¿Cuántos invitados van a la fiesta? "))
globos_fiesta = preparar_globos(numero)

print(globos_fiesta)

