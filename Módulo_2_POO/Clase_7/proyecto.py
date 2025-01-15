from abc import ABC, abstractmethod
from datetime import datetime

class Persona(ABC):
    def __init__(self, nombre, contacto, direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion
    
    @abstractmethod
    def mostrar_informacion(self):
        pass

class Mascota(ABC):
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_citas = []
    
    @abstractmethod
    def agregar_al_historial(self, detalles_servicio):
        pass

class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario
    
    @abstractmethod
    def actualizar(self, **kwargs):
        pass

    # Definición de subclases
class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion)
        self.mascota = []

    def agregar_mascota(self, mascota):
        self.mascota.append(mascota)
    
    def mostrar_informacion(self):
        return f'Nombre: {self.nombre}\nContacto: {self.contacto}\nDirección: {self.direccion}'

class RegistroMascota(Mascota):
    def agregar_al_historial(self, detalles_servicio):
        self.historial_citas.append(detalles_servicio)
    
    def agregar_al_historial(self):
        return self.historial_citas

class CitaMascota(Cita):
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)
    
class SistemaVeterinaria:
    def __init__(self):
        self.clientes = []
    
    def registrar_cliente(self):
        try:
            nombre = input('Ingrese el nombre del cliente: ').strip()
            contacto = input('Ingrese el contacto del cliente: ').strip()
            direccion = input('Ingrese la dirección del cliente: ').strip()
            
            if not nombre or not contacto or not direccion:
                raise ValueError('Todos los campos son obligatorios')
            
            cliente = Cliente(nombre, contacto, direccion)
            self.clientes.append(cliente)
            print('Cliente registrado con éxito')
        except ValueError as e:
            print(f"Error: {e}")

    def registrar_mascota(self):
        try:
            nombre_cliente = input('Ingrese el nombre de la mascota: ').strip()
            cliente = next((cliente for cliente in self.clientes if cliente.nombre == nombre_cliente), None)

            if not cliente:
                raise ValueError('Cliente no encontrado')
            
            nombre_mascota = input('Ingrese el nombre de la mascota: ').strip()
            especie = input('Ingrese la especie de la mascota: ').strip()
            raza = input('Ingrese la raza de la mascota: ').strip()
            edad = int(input('Ingrese la edad de la mascota: ').strip())

            if not nombre_mascota or not especie or not raza or not edad <= 0:
                raise ValueError('Todos los campos son obligatorios')
            
            mascota = RegistroMascota(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print('Mascota registrada con éxito')
        except ValueError as e:
            print(f"Error: {e}")
        
    def programar_cita(self):
        try:
            nombre_cliente = input('Ingrese el nombre del cliente: ').strip()
            cliente = next((cliente for cliente in self.clientes if cliente.nombre == nombre_cliente), None)

            if not cliente:
                raise ValueError('Cliente no encontrado')
            
            nombre_mascota = input('Ingrese el nombre de la mascota: ').strip()
            mascota = next((mascota for mascota in cliente.mascota if mascota.nombre == nombre_mascota), None)

            if not mascota:
                raise ValueError('Mascota no encontrada')
            
            fecha = input('Ingrese la fecha de la cita (dd/mm/yyyy): ').strip()
            hora = input('Ingrese la hora de la cita (hh:mm): ').strip()
            servicio = input('Ingrese el servicio de la cita: ').strip()
            veterinario = input('Ingrese el nombre del veterinario: ').strip()

            if not fecha or not hora or not servicio or not veterinario:
                raise ValueError('Todos los campos son obligatorios')
            
            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.agregar_al_historial(cita)
            print('Cita programada con éxito')
        except ValueError as e:
            print(f"Error: {e}")