class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def arrancar(self):
        return f"El motor {self.tipo} está arrancando..."

class Llantas:
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def inflar(self):
        return f"Las {self.cantidad} llantas están infladas."

class Auto:
    def __init__(self, marca, motor, llantas):
        self.marca = marca
        self.motor = motor
        self.llantas = llantas

    def encender(self):
        motor_status = self.motor.arrancar()
        llantas_status = self.llantas.inflar()
        return f"El auto {self.marca} está listo. {motor_status} {llantas_status}"

# Uso
motor_v6 = Motor("V6")
llantas_auto = Llantas(4)
mi_auto = Auto("Toyota", motor_v6, llantas_auto)

print(mi_auto.encender())
