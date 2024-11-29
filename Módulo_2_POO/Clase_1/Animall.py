class Animall:

    cantidadAnimales = 0

    def __init__(self, name):
        self.name = name
        Animall.cantidadAnimales += 1

    @classmethod
    def totalAnimales(cls):
        return f"Tengo{cls.cantidadAnimales} animalitos"

animalito1 = Animall("Tomy")
animalito2 = Animall("Rocko")

print(Animall.cantidadAnimales)
print(animalito1.name)