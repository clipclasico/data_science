#Perfil de estudiante

nom = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
carr = input("Ingrese su carrera: ")
prom = int(input("Ingrese su promedio: "))

estudiante = {
    "nombre": nom,
    "edad": edad,
    "carrera": carr,
    "promedio": prom
}

aprobado = estudiante["promedio"]
if aprobado >= 61:
    print("Estado: Aprobado")
else:
    print("Estado: No aprobado")

for clave,valor in estudiante.items():
    if clave == "nombre":
        print(f"Estudiante: {estudiante['nombre']}")
    elif clave == "carrera":
        print(f"Carrera elegida: {estudiante['carrera']}")

    else:
        print(clave, ":", valor)