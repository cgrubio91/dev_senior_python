class Persona:
    def __init__(self, nombre, contacto, direccion):
        self._nombre = nombre
        self._contacto = contacto
        self._direccion = direccion

    def get_info(self):
        return f"Nombre: {self._nombre}, Contacto: {self._contacto}, Dirección: {self._direccion}"


class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion)
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def listar_mascotas(self):
        return [mascota.get_info() for mascota in self.mascotas]


class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self._nombre = nombre
        self._especie = especie
        self._raza = raza
        self._edad = edad
        self.historial = []

    def agregar_cita(self, cita):
        self.historial.append(cita)

    def get_info(self):
        return f"Nombre: {self._nombre}, Especie: {self._especie}, Raza: {self._raza}, Edad: {self._edad}"

    def mostrar_historial(self):
        return [cita.get_info() for cita in self.historial]


class Cita:
    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario

    def get_info(self):
        return f"Fecha: {self.fecha}, Hora: {self.hora}, Servicio: {self.servicio}, Veterinario: {self.veterinario}"


class SistemaVeterinaria:
    def __init__(self):
        self.clientes = []

    def registrar_cliente(self, nombre, contacto, direccion):
        cliente = Cliente(nombre, contacto, direccion)
        self.clientes.append(cliente)
        return cliente

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente._nombre == nombre:
                return cliente
        return None

    def mostrar_menu(self):
        while True:
            print("\nMenú de Gestión Veterinaria")
            print("1. Registrar Cliente")
            print("2. Registrar Mascota")
            print("3. Programar Cita")
            print("4. Consultar Historial")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.opcion_registrar_cliente()
            elif opcion == "2":
                self.opcion_registrar_mascota()
            elif opcion == "3":
                self.opcion_programar_cita()
            elif opcion == "4":
                self.opcion_consultar_historial()
            elif opcion == "5":
                print("¡Gracias por usar el sistema!")
                break
            else:
                print("Opción no válida, intente de nuevo.")

    def opcion_registrar_cliente(self):
        nombre = input("Nombre del cliente: ")
        contacto = input("Contacto: ")
        direccion = input("Dirección: ")
        cliente = self.registrar_cliente(nombre, contacto, direccion)
        print(f"Cliente registrado: {cliente.get_info()}")

    def opcion_registrar_mascota(self):
        nombre_cliente = input("Nombre del cliente: ")
        cliente = self.buscar_cliente(nombre_cliente)
        if cliente:
            nombre = input("Nombre de la mascota: ")
            especie = input("Especie: ")
            raza = input("Raza: ")
            edad = input("Edad: ")
            mascota = Mascota(nombre, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print("Mascota registrada exitosamente.")
        else:
            print("Cliente no encontrado.")

    def opcion_programar_cita(self):
        nombre_cliente = input("Nombre del cliente: ")
        cliente = self.buscar_cliente(nombre_cliente)
        if cliente:
            nombre_mascota = input("Nombre de la mascota: ")
            mascota = next((m for m in cliente.mascotas if m._nombre == nombre_mascota), None)
            if mascota:
                fecha = input("Fecha (YYYY-MM-DD): ")
                hora = input("Hora (HH:MM): ")
                servicio = input("Servicio: ")
                veterinario = input("Veterinario asignado: ")
                cita = Cita(fecha, hora, servicio, veterinario)
                mascota.agregar_cita(cita)
                print("Cita programada exitosamente.")
            else:
                print("Mascota no encontrada.")
        else:
            print("Cliente no encontrado.")

    def opcion_consultar_historial(self):
        nombre_cliente = input("Nombre del cliente: ")
        cliente = self.buscar_cliente(nombre_cliente)
        if cliente:
            nombre_mascota = input("Nombre de la mascota: ")
            mascota = next((m for m in cliente.mascotas if m._nombre == nombre_mascota), None)
            if mascota:
                historial = mascota.mostrar_historial()
                if historial:
                    print("\nHistorial de servicios:")
                    for cita in historial:
                        print(cita)
                else:
                    print("No hay servicios registrados.")
            else:
                print("Mascota no encontrada.")
        else:
            print("Cliente no encontrado.")


# Ejemplo de ejecución
sistema = SistemaVeterinaria()
sistema.mostrar_menu()
