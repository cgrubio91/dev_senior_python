import pdb
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Empleado(ABC):
    nombre: str
    salario_base: float

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

@dataclass
class Manager(Empleado):
    def calcular_salario(self) -> float:
        return self.salario_base + 5000

class Developer(Empleado):
    def calcular_salario(self) -> float:
        return self.salario_base + 2000
    
def calcular_total_salario(empleado:Empleado) -> float:
    """_summary_
    
    n = Avance de linea en linea
    s = Saltos de linea
    c =  Para saltar hacia la siguiente pausa
    r =  Para continuar la ejecución hasta la siguiente pausa
    l =  Para mostrar el código fuente
    w =  Para mostrar la lista de funciones
    a =  Para mostrar los argumentos de la función
    q =  Para salir del depurador
    """
    
    return empleado.calcular_salario()

if __name__ == '__main__':
    manager = Manager('Juan', 1000)
    developer = Developer('Pedro', 2000)
    print(calcular_total_salario(manager))
    print(calcular_total_salario(developer))