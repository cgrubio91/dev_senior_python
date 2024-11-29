class Animal:

    def __init__(self, tipo, name, age):
        self.tipo = tipo
        self.name = name
        self.age = age


    def saludar(self):
        return f"Mi animalito es un {self.tipo} se llama {self.name} y tiene {self.age} años"
    
animal1 = Animal("perro", "rocko", 8)

print(animal1.saludar)
print(animal1.tipo)
print(animal1.name)
print(animal1.age)
