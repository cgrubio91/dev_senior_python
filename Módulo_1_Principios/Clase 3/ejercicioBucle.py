import random

numeroSecreto = random.randint(1, 10)

vidas = 3

while vidas > 0:
    intento = int(input('Adivina el número: '))
    if intento == numeroSecreto:
        print("Adivinó el número")
        break
    elif intento < numeroSecreto:
        print('el numero es mayor')
        vidas -= 1
    else:
        print('el número es menor')
        vidas -= 1
    if vidas == 0:
        print('Yaper')


numero = 1  # Empezamos en 1
while numero <= 5:  # Mientras el número sea menor o igual a 5
    print(numero)  # Mostramos el número
    numero += 1  # Sumamos 1 al número
