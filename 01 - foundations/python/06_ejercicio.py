#Diccionarios

nom = input("Ingrese su nombre: ")
ed = int(input("Ingrese su edad: "))
car = input("Ingrese su carrera: ")

estudiante = {
    "nombre": nom,
    "edad": ed,
    "Carrera": car
}


print(f"Nombre: {estudiante['nombre']}")
print(f"Edad: {estudiante['edad']}")
print(f"Carrera: {estudiante['Carrera']}")

estudiante["edad"] = 30

print(f"Nueva edad: {estudiante['edad']}")