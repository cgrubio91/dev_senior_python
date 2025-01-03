# Clases para los animales
class Perro:
    def sonido(self):
        return "¡Guau guau! 🐶"

class Gato:
    def sonido(self):
        return "¡Miau miau! 🐱"

class Pajaro:
    def sonido(self):
        return "¡Pío pío! 🐦"

# La Fábrica de Animales
class FabricaDeAnimales:
    @staticmethod
    def crear_animal(tipo):
        if tipo == "perro":
            return Perro()
        elif tipo == "gato":
            return Gato()
        elif tipo == "pajaro":
            return Pajaro()
        else:
            return None

# El niño pide un animal
fabrica = FabricaDeAnimales()

# Pide un perro
animal1 = fabrica.crear_animal("perro")
if animal1:
    print(animal1.sonido())  # "¡Guau guau! 🐶"

# Pide un gato
animal2 = fabrica.crear_animal("gato")
if animal2:
    print(animal2.sonido())  # "¡Miau miau! 🐱"

# Pide un pájaro
animal3 = fabrica.crear_animal("pajaro")
if animal3:
    print(animal3.sonido())  # "¡Pío pío! 🐦"

# Pide algo que no existe
animal4 = fabrica.crear_animal("dinosaurio")
if not animal4:
    print("Ese animal no está en la fábrica 🦕")
