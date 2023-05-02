def usar_la_fuerza(mochila, elemento):
    if not mochila:
        return None
    elif mochila[0] == elemento:
        return 1
    else:
        objetos_sacados = usar_la_fuerza(mochila[1:], elemento)
        if not objetos_sacados:
            return None
        else:
            return objetos_sacados + 1


mochila = ["sable de luz", "comida", "capa", "brujula", "llaves", "sable de luz"]
elemento = input('Ingrese el elemento a buscar: ')


objetos_sacados = usar_la_fuerza(mochila, elemento)

if objetos_sacados == None:
    print(f"No se ha encontrado {elemento} en la mochila")
else:
    print(f"Se ha encontrado {elemento} después de sacar {objetos_sacados} objetos")