# Ejercicio 4: Mostrar el menú de la cafetería
# Objetivo: Usar comprensión de listas para formatear y mostrar el menú de una cafetería con los precios de cada bebida.
def ver_menu(menu):
    lista = [f"{nombre.capitalize()}: ${precio:.2f}" for nombre, precio in menu.items()]
    return lista

menu = {
   "americano": 25.50,
    "cafe de olla": 22.00,
    "capuchino": 35.75,
    "coca": 40.00,
    "agua": 18.50
}

menu_formateado = ver_menu(menu)

for item in menu_formateado:
    print(item)
