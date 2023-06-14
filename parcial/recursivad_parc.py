palabras = ["gato", "perro", "gato", "ratón", "gato"]

def contador(vec, palabra):
    if len(vec) == 0:
        return 0
    elif vec[0] == palabra:
        return 1 + contador(vec[1:], palabra)
    else:
        return contador(vec[1:], palabra)

num = contador(palabras, "gato")
print(f"se encontro a la palabra {num} veces")

