
from listaa import lista
from random import randint


class Entrenador():

    def _init_(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def _str_(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbg{self.cb_ganadas}-cbp{self.cb_perdidas}'

class Pokemon():

    def _init_(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def _str_(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Juan', ct_ganados=randint(1, 10),cb_perdidas=randint(1,20),cb_ganadas=randint(0,20))
e2 = Entrenador('Maria', ct_ganados=randint(1, 10),cb_perdidas=randint(1,20),cb_ganadas=randint(0,20))
e3 = Entrenador('Ana', ct_ganados=randint(1, 10),cb_perdidas=randint(1,20),cb_ganadas=randint(0,20))

entrenadores = [e1, e2, e3]

lista_entrenadores = lista()

p1 = Pokemon('pikachu', 'electrico', randint(1, 20))
p2 = Pokemon('jolteon', 'electrico', randint(1, 20))
p3 = Pokemon('vaporeon', 'agua', randint(1, 20))
p4 = Pokemon('flareon', 'fuego', randint(1, 20))
p5 = Pokemon('leafeon', 'planta', randint(1, 20))
p6 = Pokemon('A1', 'fuego',randint(1, 20),'planta')
p7 = Pokemon('A2', 'agua',randint(1, 20),'volador')
p8 = Pokemon('Tyrantrum','Lucha',randint(1,20))
p9 = Pokemon('Terrakion','tierra',randint(1,20))

pokemons = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


lista_entrenadores.barrido_entrenadores()
print()

#! A
pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

print()
#! B
lista_entrenadores.barrido_cantidad_torneos_ganados(6)

print()
#! C
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados

valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

pokemon_mayor = sublista.get_element_by_index(0)
for pos in range(1, sublista.size()):
    pokemon = sublista.get_element_by_index(pos)
    if pokemon.nivel > pokemon_mayor.nivel:
        pokemon_mayor = pokemon

print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')

#! D
entrenador = input("Ingrese el entrenado a encontrar: ")
busqueda = lista_entrenadores.search(entrenador, "nombre")
if busqueda != None:
    elemento = lista_entrenadores.get_element_by_index(busqueda)
    entrenador2,sublista2=elemento[0],elemento[1]
    print(entrenador2)
    sublista2.barrido()
print()
#! E
for i in range(lista_entrenadores.size()):
    value=lista_entrenadores.get_element_by_index(i)[0]
    batallas_p=value.cb_perdidas
    batallas_g=value.cb_ganadas
    BatallasTotales=batallas_g+batallas_p
    porcentaje=batallas_g*100//BatallasTotales
    
    if porcentaje >79:
        print(f'Porcentaje de {lista_entrenadores.get_element_by_index(i)[0].nombre}: {porcentaje}')
    else: 
        print(f'Porcentaje de {lista_entrenadores.get_element_by_index(i)[0].nombre} es menor al 79%')
print()
#! F
for i in range(lista_entrenadores.size()):
    elem=lista_entrenadores.get_element_by_index(i)
    entrenador3,pokemones3=elem[0],elem[1]
    for j in range (pokemones3.size()):
        if (pokemones3.get_element_by_index(j).tipo=='fuego' and pokemones3.get_element_by_index(j).subtipo=='planta') or (pokemones3.get_element_by_index(j).tipo=='agua' and pokemones3.get_element_by_index(j).subtipo=='volador'):
            print(f'{entrenador3.nombre} tiene pomenones de tipo fuego/planta o agua/volador')


#! G
entrenador4=input('Ingrese entrenador: ')
buscado=lista_entrenadores.search(entrenador4,'nombre')
promedio=0
if buscado != None:
    value=lista_entrenadores.get_element_by_index(buscado)
    pokemones4=value[1]
    acum=0
    for i in range(pokemones4.size()):
        nivel=pokemones4.get_element_by_index(i).nivel
        acum+=nivel
        promedio=acum//(pokemones4.size())
print(f'el promedio de los pokemones de {entrenador4} es de: {promedio} ')

#! H
contador = 0
pokemon = input('Ingrese el pokemon: ')
for i in range(lista_entrenadores.size()):
    valor3 = lista_entrenadores.get_element_by_index(i)
    entrenador, sublista = valor3[0], valor3[1]
    for x in range(sublista.size()):
        value = sublista.get_element_by_index(x)
        if value.nombre == pokemon:
            contador += 1
            break
print(f'La cantidad de entrenadores que tienen al {pokemon} es de {contador}.')
print()
#! I
for i in range(lista_entrenadores.size()):
    value = lista_entrenadores.get_element_by_index(i)
    entrenador, sublista = value[0], value[1]
    check = 0
    for x in range(sublista.size()-1):
        pri = sublista.get_element_by_index(x)
        siguiente = sublista.get_element_by_index(x+1)
        if pri.nombre == siguiente.nombre:
            check += 1
            break
    if check == 1:
        print(f'El entrenador {entrenador.nombre} tiene pokemons repetidos.')
        print('--------')
    else:
        print(f'El entrenador {entrenador.nombre} no tiene pokemons repetidos.')
        print('--------')
#! J
L1 = ['Tyrantrum', 'Terrakion', 'Wingull']

for i in range(lista_entrenadores.size()):
    valor4 = lista_entrenadores.get_element_by_index(i)
    entrenador, sublista = valor4[0], valor4[1]
    cont = 0
    for i in range(sublista.size()):
        pokemon = sublista.get_element_by_index(i)
        if pokemon.nombre in L1:
            print(f'{entrenador.nombre} tiene a Willgull o Terrakion o Tyrantrum en su equipo.')
            cont += 1
    if cont == 0:
        print(f'El entrenador {entrenador.nombre} no tiene a Willgull o Terrakion o Tyrantrum en su equipo.')
    else: 
        pass
print()
#! K
entren=input('Ingrese Entrenador: ')
buscado5= lista_entrenadores.search(entren, 'nombre')

if buscado5 != None:
    elem2=lista_entrenadores.get_element_by_index(buscado5)
    sublista=elem2[1]
    pokemon=input('Ingrese pokemon a consultar: ')
    buscado2=sublista.search(pokemon,'nombre')
    if buscado2 !=None:
        print(f'El entrenador{entren} tiene a {pokemon}')
    else:
        print(f'El entrenador {entren} no tiene a {pokemon}')
else:
    print(f'El entrenador no esta')