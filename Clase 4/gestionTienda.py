from datetime import datetime

inventario = []
ventas = []
ventasTotalesAcumuladas = []

while True:
    print('---MENU DE GESTION DE MASCOTAS---')
    print('1. Agregar un producto al inventario')
    print('2. Vender un producto')
    print('3. Mostrar el inventario detallado')
    print('4. Historico de ventas')
    print('5. Mostrar ventas totales')
    print('6. Salir')

    opcion = input('Selecciones una opción')

    if opcion == '1':
        nombre = input('ingrese el nombre del producto')
        categoria = input('ingrese la categoria del producto')
        precio = float(input('Íngrese el valor del producto'))
        cantidad = int(input('Ingrese la cantidad de productos'))
        fechaIngreso = datetime.now().strftime('%Y-%m-%d')
        producto = [nombre, categoria, precio, cantidad, fechaIngreso]
    elif opcion == "2":
        print("VENTAS DE PRODUCTO")
        nombre = input("Ingrese el nombre del producto:").lower()
        
        producto_encontrado = False
        for producto in inventario:
            if producto[0] == nombre:
                producto_encontrado = True
                cantidad_vender = int(input("Ingrese la cantidad a vender: "))
                if producto[3] >= cantidad_vender:
                    total = producto[2] * cantidad_vender
                    producto[3] -= cantidad_vender
                    ventas.append([nombre, cantidad_vender, total])
                    ventas_totales_acumuladas += total
                    print("Se ha vendido el producto.")
                else:
                    print("No hay suficientes productos en inventario.")
                break
        if not producto_encontrado:
            print("El producto no se encuentra en inventario.")
    elif opcion == '3':
        pass
    elif opcion == '4':
        pass
    elif opcion == '5':
        pass
    elif opcion == '6' or opcion == 'Salir':
        print('Gracias por usar este sistema')
        break
    else:
        print('Opción invalida')
