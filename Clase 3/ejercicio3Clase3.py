# ## 3. **Ejercicio: Cálculo de Potencias** 💥

# Escribe un programa que solicite al usuario dos números: la base y el exponente. El programa debe calcular la potencia utilizando la fórmula:

# \[ 	a^{n} = a*a*a*a \ (n\ veces)\]

# ### **Instrucciones**:
# 1. Solicita la base y el exponente al usuario.
# 2. Calcula la potencia utilizando el operador `**` en Python.
# 3. Muestra el resultado en pantalla.

# * Hazlo ahora sin usar el operador `**`
# ### **Ejemplo de salida**:
# ```
# Ingresa la base: 3
# Ingresa el exponente: 4
# El resultado de 3^4 es: 81

base = int(input('Ingresa la base: '))
exponente = int(input('Ingresa el exponente: '))

potencia = 1
for i in range(exponente):
    potencia *= base 

print(f'El resultado de {base} elevado a la {exponente} es: {potencia}')