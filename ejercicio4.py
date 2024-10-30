### **Ejercicio 4: Verificación de Edad**
#Crea un programa que pida la edad del usuario y verifique si es mayor de edad (18 años o más). Usa operadores lógicos para determinar si la persona puede votar o no.
edad = float(input("Ingrese su edad"))

menorEdad = edad < 18
mayorEdad = edad >= 18

print(f'¿La persona de edad {edad} años, es mayor de edad?\n{mayorEdad}')
print(f'¿La persona de edad {edad} años, es menor de edad?\n{menorEdad}')