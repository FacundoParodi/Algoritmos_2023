# 23) Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas; 
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón; 
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles. 


from Arboles import BinaryTree, get_value_from_file

criaturas_arbol = BinaryTree()

lista_criaturas = [
    {'Criatura': 'Ceto', 'Derrotado': None},
    {'Criatura': 'Tifón', 'Derrotado': 'Zeus'},
    {'Criatura': 'Equidna', 'Derrotado': 'Argos Panoptes'},
    {'Criatura': 'Dino', 'Derrotado': None},
    {'Criatura': 'Pefredo', 'Derrotado': None},
    {'Criatura': 'Enio', 'Derrotado': None},
    {'Criatura': 'Escila', 'Derrotado': None},
    {'Criatura': 'Caribdis', 'Derrotado': None},
    {'Criatura': 'Euríale', 'Derrotado': None},
    {'Criatura': 'Esteno', 'Derrotado': None},
    {'Criatura': 'Medusa', 'Derrotado': 'Perseo'},
    {'Criatura': 'Ladón', 'Derrotado': 'Heracles'},
    {'Criatura': 'Águila del Cáucaso', 'Derrotado': None},
    {'Criatura': 'Quimera', 'Derrotado': 'Belerofonte'},
    {'Criatura': 'Hidra de Lerna', 'Derrotado': 'Heracles'},
    {'Criatura': 'León de Nemea', 'Derrotado': 'Heracles'},
    {'Criatura': 'Esfinge', 'Derrotado': 'Edipo'},
    {'Criatura': 'Dragón de la Cólquida', 'Derrotado': None},
    {'Criatura': 'Cerbero', 'Derrotado': None},
    {'Criatura': 'Cerda de Cromión', 'Derrotado': 'Teseo'},
    {'Criatura': 'Ortro', 'Derrotado': 'Heracles'},
    {'Criatura': 'Toro de Creta', 'Derrotado': 'Teseo'},
    {'Criatura': 'Jabalí de Calidón', 'Derrotado': 'Atalanta'},
    {'Criatura': 'Carcinos', 'Derrotado': None},
    {'Criatura': 'Gerión', 'Derrotado': 'Heracles'},
    {'Criatura': 'Láquesis', 'Derrotado': None},
    {'Criatura': 'Átropos', 'Derrotado': None},
    {'Criatura': 'Minotauro de Creta', 'Derrotado': 'Teseo'},
    {'Criatura': 'Harpías', 'Derrotado': None},
    {'Criatura': 'Argos Panoptes', 'Derrotado': 'Hermes'},
    {'Criatura': 'Aves del Estínfalo', 'Derrotado': None},
    {'Criatura': 'Talos', 'Derrotado': 'Medea'},
    {'Criatura': 'Sirenas', 'Derrotado': None},
    {'Criatura': 'Pitón', 'Derrotado': 'Apolo'},
    {'Criatura': 'Cierva de Cerinea', 'Derrotado': None},
    {'Criatura': 'Basilisco', 'Derrotado': None},
    {'Criatura': 'Jabali de Erimanto', 'Derrotado': None},
    {'Criatura': 'Cloto', 'Derrotado': None},
]

for criatura in lista_criaturas:
    criaturas_arbol.insert_node(criatura['Criatura'], {'Derrotado': criatura['Derrotado']})

print("A")
criaturas_arbol.inorden()
print()

print("B")
criaturas_arbol.inorden_add_field('Descripcion',None)
criaturas_arbol.inorden()
print()


print("C")
buscado = criaturas_arbol.search('Talos')

if buscado is not None:
    print ('La informacion de Talos es: ', buscado.value, buscado.other_values)
else:
    print ('Talos no se esta en el arbol.')
print()


print("E")
print('Heracles derroto a:')
criaturas_arbol.inorden_defeats('Heracles')
print()


print("F")
print('Inorden de criaturas que no han sido derrotadas: ')
criaturas_arbol.inorden_defeats(None)
print()


print("G")
criaturas_arbol.inorden_add_field('Capturado',None)
criaturas_arbol.inorden()
print()


print("H")
atrapados=['Cerbero','Toro de Creta','Cierva de Cerinea','Jabali de Erimanto']

criaturas_arbol.inorden_modify_fields(atrapados,'Capturado','Heracles')
criaturas_arbol.inorden()
print()


print("I")
buscado=input('Ingrese criatura que busca: ')
criaturas_arbol.search_by_coincidence(buscado)


print("J")
buscado=criaturas_arbol.search('Basilisco')
if buscado is not None:
    criaturas_arbol.delete_node('Basilisco')
    print('Se elimino al basilisco')

buscado=criaturas_arbol.search('Sirenas')
if buscado is not None:
    criaturas_arbol.delete_node('Sirenas')
    print('Se elimino a las sirenas')

print("K")
criaturas_arbol.inorden_modify_fields('Aves del Estínfalo','Derrotado','Heracles')
criaturas_arbol.inorden()
print("")


print("L")
buscado=criaturas_arbol.search('Ladón')
if buscado is not None:
    otherValuesBuscado= buscado.other_values
    criaturas_arbol.delete_node('Ladón')
    criaturas_arbol.insert_node('Dragón Ladón',otherValuesBuscado)


print("M")
print('Listado por nivel: ')
criaturas_arbol.by_level()
print()

