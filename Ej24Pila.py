from pilaa import pilas

pila = pilas()
pilaux = pilas()
cont = 0
rrpos = 0
grootpos = 0
mas5 = []
viudap = 0
iniciales = ['c','d','g']
persocdg = []

for i in range(4): 
    personajes = {}
    personajes['nombre'] = input('ingrese el nombre del personaje ')
    personajes['pelis'] = int(input('ingrese la cantidad de peliculas en las que participo '))
    pila.push(personajes)

while pila.size()>0:
    aux = pila.pop()
    cont += 1

    if aux['nombre'] == 'rocket raccoon':
        rrpos = cont
    else:
        if aux['nombre'] == 'groot':
            grootpos = cont

    if aux['pelis'] >= 5:
        mas5.append(aux)
    
    if aux['nombre'] == 'viuda negra':
        viudap = aux['pelis']
    
    recorte = aux['nombre'][0:1]
    if recorte in iniciales:
        persocdg.append(aux['nombre'])

while pilaux.size()>0:
    pila.push(pilaux.pop)

if rrpos == 0:
    print('no se encontro a rocket raccon')
else:
    print(f'rocket raccon esta en la posicion {rrpos}') 

if grootpos == 0:
    print('no se encontro a groot')
else:
    print(f'groot esta en la posicion {grootpos}') 

for i in range(len(mas5)):
    print(mas5[i]['nombre'],' participo en ',mas5[i]['pelis'],' peliculas')

if viudap > 0:
    print(f'la viuda negra participo en {viudap} peliculas')
else:
    print('la viuda negra no participo en ninguna pelicula')

print('los personajes que inician con c,d,g son ',persocdg)