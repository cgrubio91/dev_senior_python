# clase sobre los log
import logging 
from dataclasses import dataclass, field
"""
logging.basicConfig(
    level=logging.DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.DEBUG('Este es un mensaje de debug')
logging.INFO('Este es un mensaje de info')
logging.WARNING('Este es un mensaje de warning')
logging.ERROR('Este es un mensaje de error')
logging.CRITICAL('Este es un mensaje de critical')

"""

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='registro.log',
    filemode='a'
)
@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int

    def comprar(self, cantidad: int):
        if cantidad > self.cantidad:
            logging.error('No hay suficientes productos')
            raise ValueError('No hay suficientes productos')
        else:
            self.cantidad -= cantidad
            logging.info('Compra exitosa')
            return self.precio * cantidad

@dataclass
class Tienda:
    productos: list[Producto] = field(default_factory=list)

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        logging.info('Producto agregado')

    def comprar_producto(self, nombre: str, cantidad: int):
        producto = next((p for p in self.productos if p.nombre == nombre), None)
        if producto:
            try:
                total = producto.comprar(cantidad)
                logging.info(f'Compra exitosa. Total: {total}')
            except ValueError as e:
                logging.error(f'Error: {e}')

if __name__ == '__main__':
    tienda = Tienda()

    inventario_portatil = Producto('Portatil', 1000, 5)
    inventario_mouse = Producto('Mouse', 20, 10)
    tienda.agregar_producto(inventario_portatil)
    tienda.agregar_producto(inventario_mouse)
    tienda.comprar_producto('Portatil', 3)
    tienda.comprar_producto('Mouse', 15)

    with open('registro.log', 'r') as file:
        print(file.read())