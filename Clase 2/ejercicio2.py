### **Ejercicio 2: Conversión de Unidades**
#Crea un programa que convierta una medida en metros a centímetros y milímetros. El programa debe pedir al usuario que ingrese una longitud en metros y luego mostrar el resultado en las dos unidades.

medidaInicial = float(input("Ingresa una longitud en metros: "))

centimetros = medidaInicial * 100
milimetros = medidaInicial * 1000

print("Ejercicio 2: Conversión de unidades")
print(f"\n{medidaInicial} mts es igual a {centimetros} cm")
print(f"{medidaInicial} mts es igual a {milimetros} ml")