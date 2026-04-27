#aprobados y reprobados por promedio

estudiantes = []

aprobados = []
reprobados = []

for i in range(5):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} del estudiante {nombre}: "))
        notas.append(nota)
        
    estudiante = {
        "nombre": nombre,
        "notas": notas
    }

    estudiantes.append(estudiante)

for estudiante in estudiantes:
    prom = sum(estudiante['notas'])/len(estudiante['notas'])
    
    if prom >=61:
        aprobados.append(estudiante['nombre'])

    else:
        reprobados.append(estudiante['nombre'])

print(f"Los estudiantes aprobados son: {aprobados}")
print(f"Los estudiantes reprobados son: {reprobados}")