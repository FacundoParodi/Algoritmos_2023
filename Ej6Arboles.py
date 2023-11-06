# 6. Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-
# miento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
# siguientes consignas:

# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;

# b. realizar un barrido inorden del árbol por nombre y ranking;

# c. realizar un barrido por nivel de los árboles por ranking y especie;

# d. mostrar toda la información de Yoda y Luke Skywalker;

# e. mostrar todos los Jedi con ranking “Jedi Master”;

# f. listar todos los Jedi que utilizaron sabe de luz color verde;

# g. listar todos los Jedi cuyos maestros están en el archivo;

# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;

# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.



from Arboles import BinaryTree, get_value_from_file

file_jedi = open('TP5\jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()

print("A")
arbol_nombre = BinaryTree()
arbol_ranking = BinaryTree()
arbol_especie = BinaryTree()
print()


print("B")
arbol_nombre.inorden()
arbol_ranking.inorden()
print()


print("C")
arbol_ranking.by_level()
arbol_especie.by_level()


print("D")
pos = arbol_nombre.search('yoda')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no esta en la lista')

pos = arbol_nombre.search('luke skywalker')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no esta en la lista')
print()


print("E")
print('Jedis con rango Jedi Master: ')
arbol_ranking.inorden_rank('jedis.txt', 'jedi master')
print()


print('F')
print('Jedis con sable de luz verde:')
arbol_nombre.inorden_file_lightsaber('jedis.txt', 'green')
print()

print('G')
print('Jedis con maestro:')
arbol_nombre.inorden_master('jedis.txt')
print()


print("H")
print('Jedis de la especie Togruta')
arbol_especie.inorden_especie('jedis.txt','togruta')
print()
print('Jedis de la especie Cerean')
arbol_especie.inorden_especie('jedis.txt','cerean')
print()


print("I")
print('Jedis que comienzan con A:')
arbol_nombre.inorden_start_with_jedi('A')
print()

print('Jedis que tienen "-" en el nombre')
arbol_nombre.inorden_carcter('jedis.txt','-')
print()






