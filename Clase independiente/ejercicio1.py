from datetime import datetime
import statistics

class evento:
    def __init__(self, nombreEvento, fecha, lugarEvento, participantes):
        self.nombreEvento = nombreEvento
        self.fecha = fecha
        self.lugarEvento = lugarEvento
        self.participantes = participantes
    
    def agregarEvento