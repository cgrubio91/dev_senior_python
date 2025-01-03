import json

class SistemaGuardado:
    # ... (código del Singleton)

    def guardad_juego(self, datos_a_guardar):
        with open(self.archivo_guardado, "w") as f:
            json.dump(datos_a_guardar, f)

    def cargar_juego(self):
        with open(self.archivo_guardado, "r") as f:
            return json.load(f)

class Jugador:
    def __init__(self, nombre="", nivel=1):
        self.nombre = nombre
        self.nivel = nivel

    def serializar(self):
        return {
            "nombre": self.nombre,
            "nivel": self.nivel
        }

    def guardar_progreso(self):
        guardado = SistemaGuardado.get_instance()
        datos_a_guardar = self.serializar()
        guardado.guardad_juego(datos_a_guardar)

def cargar_partida():
    guardado = SistemaGuardado.get_instance()
    datos_cargados = guardado.cargar_juego()
    jugador = Jugador(datos_cargados["nombre"], datos_cargados["nivel"])
    return jugador

# Ejemplo de uso:
jugador1 = Jugador("Cristian", 33)
jugador1.guardar_progreso()

# Cargar partida:
jugador_cargado = cargar_partida()
print(jugador_cargado.nombre)  # Imprime "Cristian"
print(jugador_cargado.nivel)   # Imprime 33