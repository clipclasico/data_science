#Sistema de estudiantes pro

salida = True
estudiantes = []

while salida:
    print("Bienvenido al sistema de estudiantes PRO\n")
    print("1. Agregar estudiante (con notas)")
    print("2. Ver estudiantes")
    print("3. Ver promedios")
    print("4. Mejor estudiante")
    print("5. Aprobados/reprobados")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            print("Agregar estudiante.")
            nombre = input("Nombre del estudiante:")
            notas = []
            cantidad_notas = int(input(f"Ingrese cuantas notas desea ingresar de {nombre}: "))

            for i in range(cantidad_notas):
                nota = int(input(f"Ingrese la nota {i+1} de {nombre}"))

                notas.append(nota)
            
            estudiante = {
                "nombre": nombre,
                "notas": notas
            }

            estudiantes.append(estudiante)

        case 2:
            print("Ver estudiantes.")
            if len(estudiantes) == 0:
                print("No hay estudiantes registrados. Agregue uno y pruebe nuevamente")
            else:
                for estudiante in estudiantes:
                    print(f"Nombre: {estudiante['nombre']}, notas: {estudiante['notas']}")

        case 3:
            print("Ver promedios.")
            if len(estudiantes) == 0:
                print("No hay estudiantes registrados. Agregue uno y pruebe nuevamente")
            else:  
                for estudiante in estudiantes:
                    promedio = sum(estudiante['notas'])/len(estudiante['notas'])
                    print(f"Promedio de {estudiante['nombre']}: {promedio}")

        case 4:
            print("Mejor estudiante.")

            mejor_promedio = 0
            mejor_estudiante = ""

            if len(estudiantes) == 0:
                print("No hay estudiantes registrados. Agregue uno y pruebe nuevamente")
            else:
                
                for estudiante in estudiantes:
                    promedio = sum(estudiante['notas'])/len(estudiante['notas'])
                    if promedio > mejor_promedio:
                        mejor_estudiante = estudiante['nombre']
                        mejor_promedio = promedio

                print(f"Mejor estudiante: {mejor_estudiante}, con un promedio de: {mejor_promedio}")

        case 5:
            aprobados = []
            reprobados = []

            if len(estudiantes) == 0:
                print("No hay estudiantes registrados. Agregue uno y pruebe nuevamente")
            else:

                for estudiante in estudiantes:
                    promedio = sum(estudiante['notas'])/len(estudiante['notas'])

                    if promedio >= 61:
                        aprobados.append(estudiante['nombre'])

                    else:
                        reprobados.append(estudiante['nombre'])

                print(f"Aprobados: {aprobados}")
                print(f"Reprobados: {reprobados}")

        case 6:
            salida = False

        case _:
            print("Opción no válida, intente nuevamente.")