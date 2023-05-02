romano = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 1000, 'm': 10000}

def convert_romano_to_dec(numero_romano):
    if len(numero_romano) == 1:
        return romano[numero_romano]
    else:
        if romano[numero_romano[0]] >= romano[numero_romano[1]]:
            return romano[numero_romano[0]] + convert_romano_to_dec(numero_romano[1:])
        else:
            return - romano[numero_romano[0]] + convert_romano_to_dec(numero_romano[1:])
        
