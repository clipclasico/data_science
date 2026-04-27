# Sistema de calificaciones inteligente

import random

estudiantes = []


def calcular_promedio(notas):
    promedio = sum(notas)/len(notas)
    return promedio

def es_aprobado(promedio):
    if promedio >= 61:
        return True
    else:
        return False
    
def generar_estudiante():
    nombre = f"Estudiante {random.randint(1,10)}"
    notas = []

    for i in range(3):
        nota = random.randint(1,100)
        notas.append(nota)

    promedio = calcular_promedio(notas)
    estado = es_aprobado(promedio)

    estudiante = {
        "nombre": nombre,
        "notas": notas, 
        "promedio": promedio, 
        "aprobado": estado
    }

    estudiantes.append(estudiante)

menu = True
while menu:
    print("Bienvenido/a al menú de calificaciones inteligentes.")
    print("1. Agregar estudiante manual.")
    print("2. Agregar estudiante automático.")
    print("3. Ver estudiantes.")
    print("4. Ver mejor estudiante.")
    print("5. Ver aprobados/reprobados")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del estudiante: ")
            num = int(input(f"Ingrese la cantidad de notas que desea agregar de {nombre}: "))
            notas = []
            for i in range(num):
                nota = int(input(f"Ingrese la nota #{i+1} de {nombre}: "))
                notas.append(nota)

            promedio = calcular_promedio(notas)
            estado = es_aprobado(promedio)

            estudiante = {
                "nombre": nombre,
                "notas": notas,
                "promedio": promedio,
                "aprobado": estado
            }

            estudiantes.append(estudiante)
        
        case 2:
            generar_estudiante()
            print("Estudiante generado con éxito.")

        case 3:
            print("Estudiantes enlistados: ")
            for estudiante in estudiantes:
                print(f"Nombre: {estudiante['nombre']}, Notas: {estudiante['notas']}, Promedio: {estudiante['promedio']}, Aprobado: {estudiante['aprobado']}")

        case 4:
            mejor_promedio = 0
            mejor_estudiante = ""

            for estudiante in estudiantes:
                if estudiante['promedio'] > mejor_promedio:
                    mejor_promedio = estudiante['promedio']
                    mejor_estudiante = estudiante['nombre']

            print(f"El mejor estudiante es: {mejor_estudiante} con un promedio de: {mejor_promedio}")

        case 5:
            aprobados = []
            reprobados = []

            for estudiante in estudiantes:
                if estudiante['aprobado']:
                    aprobados.append(estudiante['nombre'])

                else:
                    reprobados.append(estudiante['nombre'])

            print(f"Estudiantes aprobados: {aprobados}")
            print(f"Estudiantes reprobrados: {reprobados}")

        case 6:
            menu = False
            print("Gracias por usar el programa. Hasta pronto")

        case _:
            print("Opción no válida. Intente nuevamente.")
            
