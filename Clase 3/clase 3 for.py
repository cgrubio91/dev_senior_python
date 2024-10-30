# Este bucle se repite hasta que se cumple la condición,
# for i in range(0,10,2):
#     print(i)

numero = int(input('ingrese un número: '))
for numero in range(1, 6):
    if numero == 3:
        print('Número 3 encontrado, saliendo del bucle')
        break
    print(numero)