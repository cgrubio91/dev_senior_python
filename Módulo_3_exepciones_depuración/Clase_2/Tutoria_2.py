#Manejo de exepciones
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")
#Exepción por try y except
try:
    edad = int(input("Ingrese su edad: "))
    print(f"Edad: {edad}")
except ValueError:
    print("El valor ingresado no es un número entero")
#Se ejecuta solo si no se cumple ninguna exepción en el try
else:
    print("El valor ingresado es un número entero")
#Se ejecuta siempre
finally:
    print("¡Gracias por usar el sistema!")