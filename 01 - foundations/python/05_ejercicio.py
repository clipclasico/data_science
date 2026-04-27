#Sistema de estudiante con notas

estudiantes = []

for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    
    notas = []
    
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} del estudiante {nombre}: "))
        notas.append(nota)

    estudiante = {
        "nombre": nombre,
        "notas": notas
    }

    estudiantes.append(estudiante)

for i in estudiantes:
    print(i)

for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    notas = estudiante["notas"]
    
    suma = 0
    for nota in notas:
        suma += nota
    
    promedio = suma / len(notas)
    
    print(f"{nombre} promedio: {round(promedio, 2)}")