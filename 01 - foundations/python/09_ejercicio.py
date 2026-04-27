#Varios estudiantes
estudiantes = []

for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))

    estudiante = {
        "nombre": nombre,
        "edad": edad
    }

    estudiantes.append(estudiante)

for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")
    if estudiante['edad'] >=18:
        print(f"{estudiante['nombre']} es mayor de edad.")
    else:
        print(f"{estudiante['nombre']} es menor de edad.")