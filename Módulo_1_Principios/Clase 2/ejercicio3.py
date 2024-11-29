### **Ejercicio 3: Comparador de Números**
#Escribe un programa que solicite dos números al usuario y determine si el primer número es mayor, menor o igual al segundo. Muestra el resultado en pantalla usando operadores relacionales.

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

igualQue = num1 == num2
mayorQue = num1 > num2
menorQue = num1 < num2
diferenteDe = num1 != num2

print(f"¿Los números {num1} y {num2} son iguales?\n{igualQue}")
print(f"Los números {num1} es mayor que {num2}\n{mayorQue}")
print(f"Los números {num1} es menor que {num2}\n{menorQue}")
print(f"Los números {num1} es diferente que {num2}\n{diferenteDe}")
