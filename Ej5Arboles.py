# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

from Arboles import BinaryTree

#lista diccionario con los heroes y villanos

lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'Capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': False},
    {'name': 'deadpool', 'heroe': True},
]


#creamos un arbol general y uno para villanos y heroes
arbol = BinaryTree()
arbol_villanos = BinaryTree()
arbol_heroes = BinaryTree()


#A) además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano 
#   que indica si es un héroe o un villano, True y False respectivamente
for heroe in lista_heroes:
    arbol.insert_node(heroe["name"], heroe["heroe"])

print("B")
#B) listar los villanos ordenados alfabéticamente;
arbol.inorden_super_or_villano(False)
print("------------------------")

print("C")
#C) mostrar todos los superhéroes que empiezan con C
arbol.inorden_start_with("C")
print("------------------------")


print("D")
#D) determinar cuántos superhéroes hay el árbol
arbol.contar_heroes()
print("la cantidad de heroes en el arbol es de: ", arbol.contar_heroes())
print("------------------------")


print("E")
#E) Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#   encontrarlo en el árbol y modificar su nombre
buscado = input("que heroe desea modificar")
posi = arbol.search(buscado) #guardamos la posicion/ref al nodo q queremos buscar

if posi:
    is_hero = posi.other_values
    arbol.delete_node(buscado)
    new_valor = input("ingrese el nuevo nombre: ")
    arbol.insert_node(new_valor, is_hero)
else:
    print('no esta')
print()
arbol.inorden()
print("--------------------------")


print("F")
#F) listar los superhéroes ordenados de manera descendente
print("Superhéroes ordenados de manera descendente: ")
arbol.postorden_heroes()
print()

print("G1")
#G) generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

arbol.SepararArbol(arbol_villanos,arbol_heroes)  #separamos el arbol
print(f'Numero de Heroes en el arbol de heroes: {arbol_heroes.contar_heroes()}')
print(f'Numero de Villanos en el arbol de villanos: {arbol_villanos.contar_villanos()}')  
print("---------------------")


print("G2")
print("Superheroes ordenados alfabéticamente:")
arbol_heroes.inorden()
print()

print("Villanos ordenados alfabéticamente:")
arbol_villanos.inorden()
print()




