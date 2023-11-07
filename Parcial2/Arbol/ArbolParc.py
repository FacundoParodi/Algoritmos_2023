from Arboles import BinaryTree

Pokemon_name_tree = BinaryTree()
Pokemon_num_tree = BinaryTree()
Pokemon_type_tree = BinaryTree()



#La lista la genere con chatgpt

lista_pokemon = [
    {'pokemon': 'Tifón', 'numero': 666, 'tipo': 'agua'},
    {'pokemon': 'Ceto', 'numero': 123, 'tipo': 'fuego'},
    {'pokemon': 'Equidna', 'numero': 555, 'tipo': 'agua'},
    {'pokemon': 'Dino', 'numero': 444, 'tipo': 'planta'},
    {'pokemon': 'Jolteon', 'numero': 356, 'tipo': 'acero'},
    {'pokemon': 'Pefredo', 'numero': 333, 'tipo': 'planta'},
    {'pokemon': 'Enio', 'numero': 666, 'tipo': 'fuego'},
    {'pokemon': 'Ladón', 'numero': 999, 'tipo': 'electrico'},
    {'pokemon': 'Caribdis', 'numero': 234, 'tipo': 'electrico'},
    {'pokemon': 'Medusa', 'numero': 789, 'tipo': 'electrico'},
    {'pokemon': 'Euríale', 'numero': 765, 'tipo': 'electrico'},
    {'pokemon': 'Esteno', 'numero': 98, 'tipo': 'agua'},
    {'pokemon': 'Lycanroc', 'numero': 1, 'tipo': 'electrico'},
    {'pokemon': 'Hidra de Lerna', 'numero': 234, 'tipo': 'fuego'},
    {'pokemon': 'León de Nemea', 'numero': 654, 'tipo': 'acero'},
    {'pokemon': 'Esfinge', 'numero': 333, 'tipo': 'fuego'},
    {'pokemon': 'Dragón de la Cólquida', 'numero': 456, 'tipo': 'agua'},
    {'pokemon': 'Cerbero', 'numero': 555, 'tipo': 'agua'},
    {'pokemon': 'Tyrantrum', 'numero': 987, 'tipo': 'acero'},
]


for pokemon in lista_pokemon:
    Pokemon_name_tree.insert_node(pokemon['pokemon'], pokemon)
    Pokemon_num_tree.insert_node(pokemon['numero'], pokemon)
    Pokemon_type_tree.insert_node(pokemon['tipo'], pokemon)



#A

print('Por nombre:')
Pokemon_name_tree.inorden()
print()
print('Por numero:')
Pokemon_num_tree.inorden()
print()
print('Por tipo:')
Pokemon_type_tree.inorden()
print()


#B

Pokemon_num_tree.inorden()
num = input('ingrese num a buscar:')
n = int(num)
pos = Pokemon_num_tree.search(n)
if pos is not None:
    print (f'La informacion del numero {n} es: {pos.other_values}')
con = input('Ingrese el nombre, (o al menos una parte) del pokemon que desea buscar:')
print (f'Resultados de ({con})')
Pokemon_name_tree.search_by_coincidence_pokemon(con)
print()


#C

tipo = input("Ingrese la clase del pokemon: ")
Pokemon_type_tree.inorden_pokemon(tipo)
print()

#D

print('ordenado en forma ascendente por numero:')
Pokemon_num_tree.inorden_pokemon2()
print()

print('ordenado en forma ascendente por nombre:')
Pokemon_name_tree.inorden_pokemon2()
print()

print('ordenado en forma ascendente por nivel: ')
Pokemon_name_tree.by_level()
print()

#E

jolteon = Pokemon_name_tree.search('Jolteon')
lycanroc = Pokemon_name_tree.search('Lycanroc')
tyrantrum = Pokemon_name_tree.search('Tyrantrum')

if jolteon is not None:
    print (f'Los datos de Jolteon son:{jolteon.other_values}')

if lycanroc is not None:
    print (f'Los datos de Lycanroc son:{lycanroc.other_values}')

if tyrantrum is not None:
    print (f'Los datos de Tyrantrum son:{tyrantrum.other_values}')


#F

num1 = Pokemon_type_tree.contar('electrico')
num2 = Pokemon_type_tree.contar('acero')
print (f'Hay un total de {num1} pokemones electricos y {num2} pokemones de tipo acero')