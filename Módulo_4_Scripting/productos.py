#Lista, se pueden modificar o inmutar
productos_lista = ["carne", "papa", "tomate"]
productos_lista.append("arroz")
print(productos_lista)

#Tupla, son inmodificables e inmutables
productos_Tupla = ("carne", "papa", "tomate")
print(productos_Tupla)
#productos_Tupla[1] = "arroz"
#print(productos_Tupla)

#Set (conjuntos) en python
categoria = {"Terror", "Drama", "ScFc"}
categoria.add("Comedia")
print(categoria)

#Diccionarios (dict) en python
clientes = {
    "id": 1010,
    "nombre": "Juan",
    "apellido": "Perez",
}
clientes["email"] = "cgrubio91@gmail.com"
print(clientes)