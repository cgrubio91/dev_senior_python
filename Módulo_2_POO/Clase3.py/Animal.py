class Animal:

    def __init__(self):
        pass

    def hablar(self):
        pass

class Perro(Animal):

    def __init__(self):
        pass

    def hablar(self):
        return f"El perro hace guau guau"

class Gato(Animal):
    def __init__(self):
        pass

    def hablar(self):
        return f"El perro hace miau miau"

animales = [Perro(),
            Gato()
]

for animal in animales:
    print(animal.hablar())