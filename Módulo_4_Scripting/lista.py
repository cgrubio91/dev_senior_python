def agregar_pedido(pedidos:list[str], nuevo_pedido:str)->list[str]:
    pedidos.append(nuevo_pedido)
    pedidos.append(nuevo_pedido)
    return pedidos

def eliminar_pedido(pedidos:list[str], pedido_eliminar:str)->list[str]:
    if pedido_eliminar in pedidos:
        pedidos.remove(pedido_eliminar)
    else:
        print("El pedido no existe")
    return pedidos

def buscar_pedido(pedidos:list[str], pedido_buscar:str)->bool:
    if pedido_buscar in pedidos:
        return pedidos.index(pedido_buscar)
    else:
        print("El pedido no existe")
        return -1
    
def main():
    pedidos = ["carne", "papa", "tomate"]
    print(agregar_pedido(pedidos, "arroz"))
    print(eliminar_pedido(pedidos, "papa"))
    print(buscar_pedido(pedidos, "tomate"))
    print(buscar_pedido(pedidos, "papa"))

if __name__ == "__main__":
    main()