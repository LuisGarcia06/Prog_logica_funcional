#Evaluacion

#EJERCICIO 1 PRESENTACION PERSONAL

print("EJERCICIO 1: PRESENTACIÓN PERSONAL")

nombre = "Luis Bernardo Garcia Caamal";
edad = 21
ciudad = "Tulum";
es_estudiante = True;

print(f"Mi nombre es: {nombre}");
print(f"Mi edad es: {edad}");
print(f"Vivo en: {ciudad}");
print(f"¿Soy ISC? {es_estudiante}");
print(f"Hola, me llamo {nombre}, tengo {edad} años, vivo en {ciudad}, y soy ISC")

#EJERCICIO 2: CASA DE CAMBIO

# print("EJERCICIO 2: CASA DE CAMBIO");

# usd = input("¿Cuántos USD tienes?: ");
# tasa = float(usd)*19.00;
# print( f"{usd} = {tasa} MXN");

#EJERCICIO 3: ¿QUIEN ES MAYOR DE EDAD?

# print("EJERCICIO 3: ¿QUIEN ES MAYOR DE EDAD?")

# nombreprimera = input("El nombre de la primera persona")
# edadprimera = input("La edad de la primera persona");
# nombresegunda = input("El nombre de la segunda persona");
# edadsegunda = input("La edad de la segunda persona ")

# if(int(edadprimera) > int(edadsegunda)):
#     print(f"{nombreprimera} es mayor por {nombresegunda} por {int(edadprimera) - int(edadsegunda)}")
# else:
#     print(f"{nombresegunda} es mayor por {nombreprimera} por {int(edadsegunda) - int(edadprimera)}")

#EJERCICIO 4: BOLETA DE CALIFICACIONES

print("EJERCICIO 4: BOLETA DE CALIFICACIONES")
participacion = input("Partcipacion (0-100): " );
trabajos = input("trabajos (0-100): " );
examen = input("Examen final (0-100): ");

participacionFinal = float(participacion) * 0.20;
trabajosFinal = float(trabajos) * 0.30;
examenFinal = float(examen) * 0.50;

print("La calificacion final es de: ", participacionFinal+trabajosFinal+examenFinal);
