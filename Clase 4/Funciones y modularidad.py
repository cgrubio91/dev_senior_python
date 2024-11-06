#Programa de gestión de drogueria
ventasTotales = 0.0
#solicitar el número de productos
numProductos = int(input('Ingrese el npumero de productos a gestionar: '))

#Listas para almacenar la información del inventario

nombre = []
precios = []
cantidades = []

print('Ingreso inicial de productos de la tienda: ')
for i in range(numProductos):
    print(f'Producto {i+1}: ')
    
