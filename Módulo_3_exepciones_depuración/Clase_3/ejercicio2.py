class Reserva:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha
    
reservas = [
    Reserva("Ana", None), 
    Reserva("Luis", "2021-10-11")
    ]

for reserva in reservas:
    if not reserva.fecha:
        print(f"*** La reserva de {reserva.cliente} no tiene fecha")
        