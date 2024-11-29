import random

numeroSecreto = random.randint(1, 10)

vidas = 3

while vidas > 0:
    intento = int(input('Adivina el número'))
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
