# ## 4. **Ejercicio: Suma de Números Naturales** ➕

# La suma de los primeros \( n \) números naturales se calcula con la fórmula:

# \[{\displaystyle \sum _{k=1}^{n}k={\frac {n(n+1)}{2}}}\]

# ### **Instrucciones**:
# 1. Pide al usuario un número entero positivo.
# 2. Usa la fórmula para calcular la suma de los primeros \( n \) números naturales.
# 3. Muestra el resultado en pantalla.

# ### **Ejemplo de salida**:
# ```
# Ingresa un número: 10
# La suma de los primeros 10 números naturales es: 55

numero = int(input('ingrese un número natural positivo: '))
suma = 0

for i in range(1,numero + 1):
    suma += i

print(f'la suma de los primeros {numero} numeros naturales es: {suma}')