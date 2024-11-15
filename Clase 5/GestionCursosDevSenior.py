#Crear las listas necesarias
estudiantes = []
cursos = ['Java', 'Python']
docentes = []
horarios = []

# función para matricular estudiantes
def matricularEstudiante():
    nombre = input('Ingrese el nombre del estudiante: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}:{curso}')

    cursoSeleccionado = int(input('Ingrese el número del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(curso):
        curso = cursos[cursoSeleccionado-1]
        estudiante = {'nombre':nombre, 'curso': curso}
        estudiantes.append(estudiante)
        print(f'Estudiante: {nombre}, matriculado en el curso {curso}')
    else:
        print(f'Selección invalida, recuerde que solo hay {len(cursos)} cursos')

# función para asignar un docente al curso
def asignarDocente():
    print('Seleccionar el curso al que desea asignar un docente: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}:{curso}')

    cursoSeleccionado = int(input('Ingrese el número del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(curso):
        curso = cursos[cursoSeleccionado-1]
        nombreDocente = input('Ingrese el nombre del docente: ')
        docente = {'nombre': nombreDocente, 'curso':curso}
        docentes.append(docente)
        print(f'Docente{nombreDocente}, matriculado en el curso {curso}')
    else:
        print(f'Selección invalida, recuerde que solo hay {len(cursos)} cursos')

# función para asignar horario a un curso
def asignarHorario():
    print('Sellecionar el curso al que desea asignar el horario: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}:{curso}')

    cursoSeleccionado = int(input('Ingrese el número del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(curso):
        curso = cursos[cursoSeleccionado-1]
        dias = input('Ingrese los días de clase: ')
        hora = input('Ingrese la hora de la clase: ')
        horario = {'curso': curso, 'dias': dias, 'hora': hora}
        horarios.append(horario)
        print(f'Horario asignado al curso: {curso}: {dias} a las {hora}')
    else:
        print(f'Selección invalida, recuerde que solo hay {len(cursos)} cursos')

# función para mostrar la lista de estudiantes
def mostrarEstudiantes():
    if estudiantes:
        print('Lista de estudiantes matriculados: ')
        for estudiante in estudiantes:
            print(f'Estudiante: {estudiante['nombre'],}, Curso: {estudiante['curso']}')
        else:
            print('No hay estudiantes asignados')

# función para mostrar la lista de estudiantes
def mostrarDocentes():
    if docentes:
        print('Lista de docentes es: ')
        for docente in docentes:
            print(f'Estudiante: {docente['nombre'],}, Curso: {docente['curso']}')
        else:
            print('No hay estudiantes asignados')


# función para mostrar los horarios
def mostrarHorarios():
    if horarios:
        print('\nHorarios de los cursos')
        for horario in horarios:
            print(f'Curso: {horario['curso'],}, Días: {horario['dias']}, Hora: {horario['hora']}' )
        else:
            print('No hay horarios asignados')

#Creación del menú
while True:
    print('\n Sistema de matricula de DevSenior')
    print('1. Matricular estudiante')
    print('2. Asignar docente al curso')
    print('3. Aisgnar horario a un curso')
    print('4. Mostrar lista de estudiantes matriculados')
    print('5. Mostrar lista de docentes asignados')
    print('6. Mostrar la lista de los horarios')
    print('7. Salir')

    opcion = int(input('digite una opción: '))

    if opcion == 1:
        matricularEstudiante()
    elif opcion == 2:
        asignarDocente()
    elif opcion == 3:
        asignarHorario()
    elif opcion == 4:
        mostrarEstudiantes()
    elif opcion == 5:
        mostrarDocentes
    elif opcion == 6:
        mostrarHorarios
    elif opcion == 7:
        print('Gracias por usar nuestro sistema')
        break
    else:
        print('Selecciones una opción válida')
    
