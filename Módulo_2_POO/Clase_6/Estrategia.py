from abc import ABC, abstractmethod

class EstrategiaDescuentos(ABC):

    @abstractmethod
    def calcular(self, monto):
        pass

class SinDescuento(EstrategiaDescuentos):
    def calcular(self, monto):
        return monto
    
class DescuentoPorcentaje(EstrategiaDescuentos):  # Hereda de EstrategiaDescuentos
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def calcular(self, monto):
        return monto - (monto * self.porcentaje / 100)  # Uso correcto de paréntesis
    
class DescuentoFijo(EstrategiaDescuentos):
    def __init__(self, montoDescuento):
        self.montoDescuento = montoDescuento
    
    def calcular(self, monto):
        return monto - self.montoDescuento

class Pedidos:
    def __init__(self, monto, estrategiaDescuento: EstrategiaDescuentos):
        if not isinstance(estrategiaDescuento, EstrategiaDescuentos):
            raise TypeError("La estrategia debe ser una instancia de EstrategiaDescuentos")
        self.monto = monto
        self.estrategiaDescuento = estrategiaDescuento

    def calcularTotal(self):
        return self.estrategiaDescuento.calcular(self.monto)
    
# Crear instancias de estrategias
pedido1 = Pedidos(1000, SinDescuento())  # Instancia de SinDescuento
print(f"Total sin descuento: {pedido1.calcularTotal()}")

pedido2 = Pedidos(1000, DescuentoPorcentaje(50))  # Instancia de DescuentoPorcentaje
print(f"Total con 50% de descuento: {pedido2.calcularTotal()}")

pedido3 = Pedidos(1000, DescuentoFijo(100))  # Instancia de DescuentoFijo
print(f"Total con descuento fijo de $100: {pedido3.calcularTotal()}")
