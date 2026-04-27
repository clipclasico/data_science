#Sistema de supermercado

salida = 1
productos = []

while salida != 0:
    print("Bienvenido/a al menú del supermercado !")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Calcular total")
    print("4. Producto más caro")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            nombre_producto = input("Ingrese el nombre del producto por agregar: ")
            valor_producto = float(input(f"Ingrese el valor de {nombre_producto}: "))

            producto = {
                "nombre": nombre_producto,
                "precio": valor_producto
            }

            productos.append(producto)
            print("Producto agregado con éxito.")
        
        case 2:
            print("Productos agregados:")
            for producto in productos:
                print(f"Nombre: {producto['nombre']}. Precio: {producto['precio']}")

        case 3:
            print("Calcular total:")
            suma = 0
            for producto in productos:
                suma += producto['precio']

            print(f"El total es de: {suma}")

        case 4:
            producto_caro = ""
            precio_caro = 0

            for producto in productos:
                if producto['precio'] > precio_caro:
                    precio_caro = producto['precio']
                    producto_caro = producto['nombre']

            print(f"Producto más caro: {producto_caro}")
            print(f"Precio del producto más caro: {precio_caro}")

        case 5:
            salida = 0
            print("Gracias por usar el programa.")
        
        case _:
            print("Opción no válida.")