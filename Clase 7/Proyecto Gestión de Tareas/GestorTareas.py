from datetime import datetime
import statistics

from datetime import datetime

class Tarea:
    def __init__(self, nombre, fechaLimite, categorias, horasDedicadas):  # método constructor
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categorias = categorias
        self.horasDedicadas = horasDedicadas

# Función para agregar una tarea, requerimiento 1 Gestión de Tareas
def agregarTarea(listaTareas):
    nombre = input('Ingrese el nombre de la tarea: ')
    fechaLimite_str = input('Ingrese la fecha límite de la tarea (DD/MM/AAAA): ')
    try:
        fechaLimite = datetime.strptime(fechaLimite_str, '%d/%m/%Y')
    except ValueError:
        print('Fecha no válida')
        return
    
    categorias = input('Ingrese la categoría de la tarea:\nEstudio\nPersonal\nTrabajo\nOtras\n')
    
    horasDedicadas_str = input('Ingrese el número de horas dedicadas (separe con comas si son varias): ')
    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(',')))
    except ValueError:
        print('Formato de horas no válido')
        return

    # Crear un objeto Tarea y agregarlo a la lista de tareas
    tarea = Tarea(nombre, fechaLimite, categorias, horasDedicadas)
    listaTareas.append(tarea)
    print('Tarea agregada con éxito.')

# Función para visualizar las tareas
def visualizarTareas(listaTareas):
    if not listaTareas:
        print('No hay tareas registradas')
        return
    for i, tarea in enumerate(listaTareas, start=1):
        print(f'\nTarea {i}')
        print(f'Nombre: {tarea.nombre}')
        print(f'Fecha límite: {tarea.fechaLimite.strftime("%d/%m/%Y")}')
        print(f'Categoría: {tarea.categorias}')
        print(f'Horas dedicadas: {tarea.horasDedicadas}')

# Calcular estadisticas básicas
def analizarHoras(listaTareas):
    if not listaTareas:
        print('No hay tareas registradas')
        return
    for tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)
        maximo = max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f'\nAnalisis de {tarea.nombre}')
        print(f'Promedio de horas {promedio}')
        print(f'Maximo de horas {maximo}')
        print(f'Minimo de horas {minimo}')

def generarInforme(listaTareas):
    if not listaTareas:
        print('No hay tareas registradas')
        return
# Abrir un archivo txt para escribir el informe
    with open("Informe_tareas.txt", "w") as archivo:
        # Escribir los detaller del archivo txt
        for tarea in listaTareas:
            archivo.write(f'Nombre: {tarea.nombre}\n')
            archivo.write(f'Fecha límite: {tarea.fechaLimite.strftime("%d/%m/%Y")}')
            archivo.write(f'Categoría: {tarea.categorias}')
            archivo.write(f'Horas dedicadas: {tarea.horasDedicadas}')
            archivo.write("\n")
    print("Informe generado como 'informe de tareas'")

def menu():
    listaTareas = []
    while True:
        print("\nMenú de opciones")
        print("1. Agregar tarea: ")
        print("2. Visualizar tarea: ")
        print("3. Analizar horas dedicadas: ")
        print("4. Generar informe: ")
        print("5. Salir")

        opcion = int(input('\nSeleccione el numero de su selección\n '))
        if opcion == 1:
            agregarTarea(listaTareas)
        elif opcion == 2:
            visualizarTareas(listaTareas)
        elif opcion == 3:
            analizarHoras(listaTareas)
        elif opcion == 4:
            generarInforme(listaTareas)
        elif opcion == 5:
            print('Saliendo del programa...')
            break
        else:
            print("Opción invalida")

if __name__== "__main__":
    menu()