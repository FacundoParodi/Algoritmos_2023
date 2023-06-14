"""Dada una lista con nombres de personajes de la saga de Avengers
ordenados por nombre del superhéroes, de los cuales se conoce:
nombre del superhéroe, nombre del personaje (puede ser vacio),
grupo al que (perteneces puede ser vacio), año de aparición, por
ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
Resolver las siguientes tareas:


h. Cargue al menos 20 superheroes a la lista.
a. Determinar si “Capitana Marvel” está en la lista y mostrar su
nombre de personaje;
b. Almacenar los superhéroes que pertenezcan al grupo
“Guardianes de la galaxia” en una cola e indicar cuantos son.
c. Mostrar de manera descendente los superhéroes que
pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de
la galaxia”.
d. Listar los superhéroes que tengan nombre de personajes cuyo
año de aparición sea posterior a 1960.
e. Hemos detectado que la superhéroe “Black Widow” está mal
cargada por un error de tipeo, figura como “Vlanck Widow”,
modifique dicho superhéroe para solucionar este problema.
f. Dada una lista auxiliar con los siguientes personajes (‘Black
Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la
información), agregarlos a la lista principal en el caso de no
estar cargados.
g. Mostrar todos los personajes que comienzan con C, P o S."""


from listaupdate import Lista 
from colaa import Cola

cola = Cola()
listaa = Lista()
listaf = Lista()

class Avengers:
    def __init__(self, nom_superheroe, nom_pj, grupo, anio):
        self.nom_superheroe = nom_superheroe
        self.nom_pj = nom_pj
        self.grupo = grupo
        self.anio = anio

    def __str__(self):
        return f"{self.nom_superheroe} - {self.nom_pj} - {self.grupo} - {self.anio}"
    
# la info de los pjs fue generada con chatgpt, perdon si no es del todo correcta
avenger1 = Avengers("iron man", "tony stark", "avengers", 1963)
avenger2 = Avengers("captain america", "steve rogers", "avengers", 1941)
avenger3 = Avengers("thor", "", "avengers", 1962)
avenger4 = Avengers("hawkeye", "clint barton", "avengers", 1964)
avenger5 = Avengers("vlanck widow", "natasha romanoff", "avengers", 1964)
avenger6 = Avengers("hulk", "bruce banner", "avengers", 1962)
avenger7 = Avengers("black panther", "t'challa", "avengers", 1966)
avenger8 = Avengers("scarlet witch", "wanda maximoff", "avengers", 1964)
avenger9 = Avengers("vision", "", "avengers", 1968)
avenger10 = Avengers("ant-man", "scott lang", "avengers", 1979)
avenger11 = Avengers("wasp", "hope van dyne", "avengers", 1963)
avenger12 = Avengers("doctor strange", "", "", 1963)
avenger13 = Avengers("spider-man", "peter parker", "", 1962)
avenger14 = Avengers("star-lord", "peter quill", "guardians of the galaxy", 1976)
avenger15 = Avengers("gamora", "", "guardians of the galaxy", 1975)

listaa.insert(avenger1, "nom_superheroe")
listaa.insert(avenger2, "nom_superheroe")
listaa.insert(avenger3, "nom_superheroe")
listaa.insert(avenger4, "nom_superheroe")
listaa.insert(avenger5, "nom_superheroe")
listaa.insert(avenger6, "nom_superheroe")
listaa.insert(avenger7, "nom_superheroe")
listaa.insert(avenger8, "nom_superheroe")
listaa.insert(avenger9, "nom_superheroe")
listaa.insert(avenger10, "nom_superheroe")
listaa.insert(avenger11, "nom_superheroe")
listaa.insert(avenger12, "nom_superheroe")
listaa.insert(avenger13, "nom_superheroe")
listaa.insert(avenger14, "nom_superheroe")
listaa.insert(avenger15, "nom_superheroe")

listaa.barrido()

avengerf1 = Avengers("black cat", "felicia hardy", "", 1979)
avengerf2 = Avengers("hulk", "bruce banner", "avengers", 1962)
avengerf3 = Avengers("rocket racoonn", "rocket", "guardians of the galaxy", 1976)
avengerf4 = Avengers("loki", "loki laufeyson", "", 1962)

listaf.insert(avengerf1, "nom_superheroe")
listaf.insert(avengerf2, "nom_superheroe")
listaf.insert(avengerf3, "nom_superheroe")
listaf.insert(avengerf4, "nom_superheroe")




def a():
    for i in range (listaa.size()):
        if listaa.get_element_by_index(i).nom_superheroe == "capitana marvel":
            print(listaa.get_element_by_index(i).nom_pj)
    else:
        print("no esta en la lista")

a()

def b():
    for i in range (listaa.size()):
        guardianes = listaa.get_element_by_index(i)
        if listaa.get_element_by_index(i).grupo == "guardians of the galaxy":
            cola.arrive(guardianes) 

    cantidad = cola.size()
    print(f"son:{cantidad}")

b()

def c():
    aux_sup = []
    for i in range (listaa.size()):
        superh = listaa.get_element_by_index(i)
        if superh.grupo == "los 4 fantasticos" or superh.grupo == "guardians of the galaxy":
            aux_sup.append(superh)

    aux_sup = sorted(aux_sup, key=lambda x: x.nom_superheroe.lower(), reverse=True) # esto lo saque de internet


    for superh in aux_sup:
        print(superh)

c()

def d():
    for i in range (listaa.size()):
        if listaa.get_element_by_index(i).anio > 1960:
            print(listaa.get_element_by_index(i).nom_superheroe)

d()

def e():
    for i in range (listaa.size()):
        if listaa.get_element_by_index(i).nom_superheroe == "Vlanck Widow":
            listaa.get_element_by_index(i).nom_superheroe = "Black Widow"
            print("corregido")

    listaa.barrido()

e()
        
def g():
    for i in range (listaa.size()):
        if (listaa.get_element_by_index(i).nom_pj) == "c" or listaa.get_element_by_index(i).nom_pj[0] == "p" or listaa.get_element_by_index(i).nom_pj[0] == "s":
            print(listaa.get_element_by_index(i).nom_pj)

g() # esta me tiro un error que no supe solucionar ni siquiera googleandolo, el resto
    #compila y creo que la logica esta bien


   


    
    














        


        