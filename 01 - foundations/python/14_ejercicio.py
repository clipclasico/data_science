#Sistema de biblioteca
libros = []

salida = 1

while salida != 0:
    print("Bienvenido/a al sistema de biblioteca\n.")
    print("1. Agregar libro")
    print("2. Ver libro")
    print("3. Buscar libro por nombre")
    print("4. Contar libros")
    print("5. Salir")

    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            titulo = input("Ingrese el título del libro: ")
            autor = input(f"Ingrese el autor de {titulo}: ")

            libro = {
                "titulo": titulo,
                "autor": autor
            }

            libros.append(libro)
            print(f"{titulo} agregado correctamente.")

        case 2:
            print("Ver libros disponibles\n")

            if len(libros) == 0:
                print("No hay libros agregados. Pruebe agregando.")
            else:
                for libro in libros:
                    print(f"Título: {libro['titulo']}. Autor: {libro['autor']}")


        case 3:
            print("Buscar libro por nombre.")

            encontrado = False

            nombre = input("Ingrese el libro que desea buscar: ")

            for libro in libros:
                if nombre == libro['titulo']:
                    print("Libro encontrado")
                    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}")
                    encontrado = True
                    break

            if not encontrado:
                    print(f"Libro {nombre} no encontrado. Pruebe agregándolo.")

        case 4:
            contar = len(libros)
            
            print(f"Libros en total: {contar}")

        case 5:
            salida = 0
            print("Gracias por usar el programa. Hasta pronto")

        case _:
            print("Entrada no válida.")