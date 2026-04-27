#Estudiante con notas

estudiantes = []

for i in range(2):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    notas = []

    for j in range(3):
        
        nota = float(input(f"Ingresar la nota {j+1} de {nombre}: "))
        notas.append(nota)

    estudiante={
        "nombre": nombre,
        "notas": notas
    }

    estudiantes.append(estudiante)

for estudiante in estudiantes:
    print(f"Estudiante: {estudiante['nombre']}, Notas: {estudiante['notas']}")
    
    print(f"Promedio de {estudiante['nombre']}:  {sum(estudiante['notas'])/len(estudiante['notas'])}")  
