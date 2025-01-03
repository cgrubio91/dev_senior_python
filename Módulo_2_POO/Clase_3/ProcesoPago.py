from abc import ABC, abstractmethod

class ProcesoPago(ABC):

    @abstractmethod

    def procesoPago(self, cantidad: float) -> None:
        pass

    @abstractmethod

    def reembolsoPago(self, transaccionId: str) -> None:
        pass

class Paypal(ProcesoPago):

    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago de ${cantidad} por Paypal")
    
    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando Id transacción númeero {transaccionId}")

class Stripe(ProcesoPago):
    
    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago de ${cantidad} por Stripe")
    
    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando Id transacción número {transaccionId} por Stripe")

if __name__ == "__main__":
    ProcesoPaypal = Paypal()
    proceosStripe = Stripe()
    
    ProcesoPaypal.procesoPago(500.0)
    ProcesoPaypal.reembolsoPago("FDCX65CFGE")

    proceosStripe.procesoPago(1000.0)
    proceosStripe.reembolsoPago("FDCX65CFGG")
