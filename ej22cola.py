from cola import Cola
import os

cola = Cola()
cola_aux = Cola()
N = 4

def limpiar_consola():          #funcion para limpiar la consola
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def limpiatodo():                
    while cola.size()>0:
        cola.atention()
    while cola_aux.size()>0:
        cola_aux.atention()

def muestradatos(pers):
    if pers["genero"] == "m":
        print(pers["nombre"],' el mismisimo ',pers["superheroe"],)
    elif pers["genero"] == "f":
        print(pers["nombre"],' la mismisima ',pers["superheroe"],)

def capitanamarvel():    
    encontro = False
    for i in range(N):
        aux = cola.atention()
        if aux["superheroe"] == "capitana marvel":
            cola_aux.arrive(aux)
            encontro = True
            break
        cola_aux.arrive(aux)

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.atention())
        
    if encontro:
        return aux["nombre"]
    else:
        return None
 
def superheroesgen(genero):         
    if genero == "f":
        for i in range(N):
            aux = cola.atention()           
            if aux["genero"] == "f":
                muestradatos(aux)
            cola_aux.arrive(aux)
    else:                                     # no evaluo que genero sea "m" porque en el menu solo tiene llamadas con 2 posibles parametros
        for i in range(N):
            aux = cola.atention()           
            if aux["genero"] == "m":
                muestradatos(aux)
            cola_aux.arrive(aux)
    
    while cola_aux.size() > 0:
        cola.arrive(cola_aux.atention())
    
def encuentrasuper(quien):          
    encontrado = False
    if quien == 1:
        for i in range(N):
            aux = cola.atention()
            if aux["nombre"] == "scott lang":
                print('se encontro a:')
                muestradatos(aux)
                cola_aux.arrive(aux)
                encontrado = True
                break
            else:
                cola_aux.arrive(aux)
    if quien == 2:
        for i in range(N):
            aux = cola.atention()
            if aux["nombre"] == "carol danvers":
                print('se encontro a:')
                muestradatos(aux)
                cola_aux.arrive(aux)
                encontrado = True
                break
            else:
                cola_aux.arrive(aux)

    if not encontrado:
        if quien == 1:
            print('no se encontro a scott lang')
        else:
            print('no se encontro a carol danvers')


    while cola_aux.size() > 0:
        cola.arrive(cola_aux.atention())  

def iniciaS():           # tener en cuanta que se evalua tanto el nombre como el nombre de superheroe
    for i in range(N):
        aux = cola.atention()
        if aux["nombre"][0] == "s" or aux["superheroe"][0] == "s":
            muestradatos(aux)
        cola_aux.arrive(aux)

    while cola_aux.size() > 0:
        cola.arrive(cola_aux.atention())

def menu():
    seguir = "y" 
    while seguir == "y":
        print('--------------------------')
        print('para buscar a la capitanna marvel ingrese 1 ')
        print('para listar a los superheroes ingrese 2')
        print('para listar a las superheroinas ingrese 3')
        print('para bucar a scott lang ingrese 4')
        print('para listar los super heroes que inician con S ingrese 5')
        print('para buscar a carol danvers ingrese 6')
        print('para terminar ingrese 7')
        res = input()
        limpiar_consola()
        if res == '1':
                print(capitanamarvel())
            
        elif res == '2':
            superheroesgen("m")
        elif res == '3':
            superheroesgen("f")
        elif res == '4':
            encuentrasuper(1)
        elif res == '5':
            iniciaS()
        elif res == '6':
            encuentrasuper(2)
        elif res == '7':
            seguir = "n"

limpiatodo()


for i in range(N):
    personajes = {"nombre":"","superheroe":"","genero":""}
    personajes["superheroe"] = input('ingrese nombre de superheroe :')
    personajes["nombre"] = input('ingrese nombre de la persona :')
    personajes["genero"] = input('ingrese el genero del personaje m/f :')

    cola.arrive(personajes)


menu()  
