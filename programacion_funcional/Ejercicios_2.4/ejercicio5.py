from functools import reduce

# Lista de precios de la cafetería
orden = [15.50, 30.00, 22.00, 45.00, 18.75, 35.50]

# Paso 1-3: map() — aplicar 10% de descuento a cada precio
precios_con_descuento = list(map(lambda precio: precio * 0.90, orden))
print(precios_con_descuento)
# [13.95, 27.0, 19.8, 40.5, 16.875, 31.95]

# Paso 4-6: filter() — quedarse solo con precios mayores a $25
bebidas_caras = list(filter(lambda precio: precio > 25, precios_con_descuento))
print(bebidas_caras)
# [27.0, 40.5, 31.95]

# Paso 7-9: reduce() — sumar todos para obtener el total
total = reduce(lambda acumulado, precio: acumulado + precio, bebidas_caras)
print(f"Total a pagar: ${total:.2f}")
# Total a pagar: $99.45