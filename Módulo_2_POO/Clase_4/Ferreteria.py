import threading
from abc import ABC, abstractmethod

# Patrón Singleton para crear un solo objeto
class SistemaFacturacion:

    _instancia = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):



        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
                cls._instancia._inicializacionHistorico()
            return cls._instancia
        
