# ## 1. **Ejercicio: Serie de Fibonacci** 🌀

# La serie de Fibonacci es una secuencia de números en la que cada número es la suma de los dos anteriores, comenzando con 0 y 1. La fórmula de Fibonacci es:

# \[ F(n) = F(n-1) + F(n-2) \]

# ### **Instrucciones**:
# 1. Escribe un programa que solicite al usuario cuántos términos de la serie de Fibonacci desea calcular.
# 2. Usa un bucle `for` o `while` para calcular y mostrar los términos de la serie.

# ### **Ejemplo de salida**:
# ```
# ¿Cuántos términos de la serie de Fibonacci deseas? 7
# 0, 1, 1, 2, 3, 5, 8
# ```

# #### **Solución**
# ```python
    
# Solicitar al usuario el número de términos
terminos = int(input("¿Cuántos términos de la serie de Fibonacci deseas? "))

# En esta linea declaramos dos variables al tiempo, es lo mismo que usar: 
# a = 0
# b = 1
a, b = 0, 1
for i in range(terminos):
    print(a)
    tempA = a
    a = b
    b = tempA + b
# ```


# ```

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
# ```

# ## 5. **Ejercicio: Calcular la Hipotenusa de un Triángulo Rectángulo** 📐

# Usa el **Teorema de Pitágoras** para calcular la hipotenusa de un triángulo rectángulo. La fórmula es:

# \[ c = \sqrt{a^2 + b^2} \]

# donde \( a \) y \( b \) son los catetos del triángulo, y \( c \) es la hipotenusa.

# ### **Instrucciones**:
# 1. Solicita al usuario los valores de los catetos.
# 2. Calcula la hipotenusa usando la fórmula.
# 3. Muestra el resultado en pantalla.

# * Usa la funcion `sqrt` de la libreria math de python como en el ejemplo para importar librerias.

# ### **Ejemplo de salida**:
# ```
# Ingresa el valor del primer cateto: 3
# Ingresa el valor del segundo cateto: 4
# La hipotenusa del triángulo es: 5.0
# ```