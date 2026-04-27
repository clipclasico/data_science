#Diccionarios2

nom = input("Ingrese su nombre: ")
ed = int(input("Ingrese su edad: "))
car = input("Ingrese su carrera: ")

estudiante = {
    "nombre": nom,
    "edad": ed,
    "Carrera": car
}

for clave,valor in estudiante.items():
    print(clave, ":", valor)