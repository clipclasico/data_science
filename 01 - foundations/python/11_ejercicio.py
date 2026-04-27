#Mejor estudiante

estudiantes = []

for i in range(3):
    nombre = input(f"ingrese el nombre del estudiante {i + 1}: ")

    notas = []
    for j in range(5):
        nota = int(input(f"ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)

    estudiante={
        "nombre": nombre,
        "notas": notas
    }
    estudiantes.append(estudiante)

mejor_promedio = 0
mejor_estudiante = ""

for estudiante in estudiantes:
    prom = sum(estudiante['notas'])/len(estudiante['notas'])

    if prom > mejor_promedio:
        mejor_promedio = prom
        mejor_estudiante = estudiante['nombre']