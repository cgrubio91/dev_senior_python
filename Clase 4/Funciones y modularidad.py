#Programa de gestión de drogueria
ventasTotales = 0.0
#solicitar el número de productos
numProductos = int(input('Ingrese el npumero de productos a gestionar: '))

#Listas para almacenar la información del inventario

nombres = []
precios = []
cantidades = []

print('Ingreso inicial de productos de la tienda: ')
for i in range(numProductos):
    print(f'Producto {i+1}: ')
    nombre = input('Ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    precio = float(input('Ingrese el precio del producto: '))
    precios.append(precio)
    cantidad = int(input('Ingrese la cantidad del producto: '))
    cantidades.append(cantidad)

#ciclo menú principal
while True:
    print('\n ---MENÚ DE GESTIÓN DROGUERÍA---' )
    print('1. Vender Producto')
    print('2. Mostrar Inventario')
    print('3. Mostrar Ventas Totales')
    print('4. Salir')

    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        print('\n Vender Producto')
        nombreVenta = input('Ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('Ingrese la cantidad a vender: '))
        productoEncontrado = False

        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    print(f'Venta realizada, por un valor de ${totalVenta:.2f}')
                    print(f'Quedan {cantidades[i]} unidades de {nombres[i]} en el inventario')
                else:
                    print(f'Cantidad insuficiente para la venta, sólo hay disponible {cantidades[i]}')
                break
        if not productoEncontrado:
            print('Producto no encontrado en el inventario.')
    elif opcion == 2:
        print('\n Inventario de productos')
        for i in range(len(nombres)):
            print(f'Producto {i+1}: \n{nombres[i].capitalize()}, Cantidades: {cantidades[i]}, Precio: {precios[i]:.2f}')
    elif opcion == 3:
        print(f'\n Ventas totales acumuladas: ${ventasTotales:.2f}')
    elif opcion == 3:
        print('Gracias por usar el sistema de gestión de droguería.')
        break
    else:
        print('Elija una opción válida entre 1 y 4')

            
