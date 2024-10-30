# El bucle while se usa cuando no se sabe cuantas veces se va a repetir una acción y depende de una condición que puede cambiar durante la ejecución
contador = 1

while contador <= 5:
    print(f'Este es el número {contador}')
    contador +=1


userHasDNI = True
while userHasDNI <= 3:

    age = int(input('Enter your age: '))
    country = input('Entre yout country: ')

    #bloque 1
    if age >= 21 and country == 'USA':
        print('You can buy alcohol')
    elif age >= 18 and country == 'COL':
        print('You can buy alcohol')
    else:
        userHasDNI = False
        print('You can´t buy alcohol')