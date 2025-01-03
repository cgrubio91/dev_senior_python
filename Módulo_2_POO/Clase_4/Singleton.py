class ReyDelReino:
    # Atributo de clase para almacenar la única instancia
    _instancia = None

    def __new__(cls, *args, **kwargs):
        # Si ya existe una instancia, la reutiliza
        if not cls._instancia:
            cls._instancia = super().__new__(cls, *args, **kwargs)
            cls._instancia.nombre = None  # Inicializamos con un atributo
        return cls._instancia

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return f"El rey del reino es: {self.nombre} 👑"


# Intentemos crear dos reyes
rey1 = ReyDelReino()
rey1.establecer_nombre("Rey Arturo")

rey2 = ReyDelReino()
rey2.establecer_nombre("Rey Enrique")

# Verificamos si ambos apuntan a la misma instancia
print(rey1.obtener_nombre())  # "El rey del reino es: Rey Enrique 👑"
print(rey2.obtener_nombre())  # "El rey del reino es: Rey Enrique 👑"

# Comprobamos que ambos son el mismo objeto
print(rey1 is rey2)  # True
