import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Vendedor:
    nombre: str
    ventas_totales: float

    def calculo_comision(self)-> float:
        if self.ventas_totales > 10000:
            comision = self.ventas_totales * 0.10
            logging.debug(f'{self.nombre} ha ganado una comisión de {comision}')
        else:
            comision = self.ventas_totales * 0.05
            logging.debug(f'{self.nombre} ha ganado una comisión de {comision}')
        return comision
    
if __name__ == '__main__':
    vendedor1 = Vendedor('Juan', 15000)
    vendedor1.calculo_comision()
    vendedor2 = Vendedor('Pedro', 5000)
    vendedor2.calculo_comision()