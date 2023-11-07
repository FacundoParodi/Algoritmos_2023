from Grafos import grafo

stw = grafo(dirigido=False)

lista_personajes = ['Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 'C-3PO', 'Leia', 'Rey', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8']

for personaje in lista_personajes:
    stw.insert_vertice(personaje)

#A
print("A")
stw.insert_arista('Luke Skywalker', 'Leia', 4)
stw.insert_arista('Yoda', 'Boba Fett', 6)
stw.insert_arista('Leia', 'Yoda', 8)
stw.insert_arista('Boba Fett', 'Luke Skywalker', 3)
stw.insert_arista('Darth Vader', 'Luke Skywalker', 6)
stw.insert_arista('Leia', 'Boba Fett', 5)
stw.insert_arista('Boba Fett', 'Darth Vader', 7)
stw.insert_arista('Yoda', 'Darth Vader', 1)
stw.insert_arista('Leia', 'Darth Vader', 1)

stw.barrido()

#B
print("B")
stw_minima = stw.kruskal()
print (stw_minima)
print()
yoda_presente = False
for conexion in stw_minima:
    joda = conexion
    if 'Yoda' in (joda):
        yoda_presente = True
        break

if yoda_presente:
    print(f"yoda esta en el arbol de expansion minima.")
else:
    print("yoda no esta en el arbol de expansión mínima.")
print()

#C)

stw.barrido_mayor()
# no pude solucionar el problema con esta funcion ni resolver los demas puntos, creo que la logica
# dentro de todo esta bien igual
