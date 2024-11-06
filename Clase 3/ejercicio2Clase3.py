# ## 2. **Ejercicio: Cálculo del Factorial** 🎯

# El factorial de un número \( n \) (representado como \( n! \)) es el producto de todos los enteros positivos hasta \( n \). La fórmula es:

# \[ n! = n*(n-1)*(n-2)* \ldots* 1 \]

# ### **Instrucciones**:
# 1. Crea un programa que pida un número al usuario y calcule su factorial usando un bucle.
# 2. Muestra el resultado en pantalla.

# ### **Ejemplo de salida**:
# ```
# Ingresa un número para calcular su factorial: 5
# El factorial de 5 es: 120

factorial = int(input('Ingresa un número para calcular su factorial: '))
n = 1

for i in range(1,factorial + 1):
    n *= i

print(f'El factorial de {factorial} es: {n}')