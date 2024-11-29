from datetime import datetime
import statistics

class evento:
    def __init__(self, nombreEvento, fecha, lugarEvento, participantes):
        self.nombreEvento = nombreEvento
        self.fecha = fecha
        self.lugarEvento = lugarEvento
        self.participantes = participantes
    
    def agregarEvento(eventos):
        nombreEvento = input("ingrese el nombre del evento: ")
        fecha_str = input("ingrese la fecha del evento en dd/mm/aaaa: ")
        try:
            fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
        except ValueError:
            print("Fecha inválida")
            return
