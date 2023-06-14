"""Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
cual se almacenaban en una pila en cada misión de caza que
emprendió (con la siguiente información planeta visitado, a quien
capturado, costo de la recompensa), resolver las siguientes
actividades:

a. Mostrar los planetas visitados en el orden hizo las misiones.
b. Determinar cuántos créditos galácticos recaudo en total.
c. Determinar el número de la misión en que capturo a Han Solo
y en que planeta fue, suponga que dicha misión está cargada."""

from pilaa import pilas
pila = pilas()
pila_aux = pilas()

class bitacora:
    def __init__(self,planeta,capturado,costo_recompensa):
        self.planeta = planeta
        self.capturado = capturado
        self.costo_recompensa = costo_recompensa

    def __str__(self):
        return f'{self.planeta} - {self.capturado} - {self.costo_recompensa}'
    
mision1 = bitacora("tatooine", "han solo", 1000000)
mision1 = bitacora("endor", "ewok", 50000)
mision2 = bitacora("coruscant", "darth vader", 2000000)
mision3 = bitacora("hoth", "luke skywalker", 750000)
mision4 = bitacora("tatooine", "jabba the hutt", 1500000)
mision5 = bitacora("naboo", "queen amidala", 300000)
mision6 = bitacora("tatooine", "han solo", 1000000)

pila.push(mision1)
pila.push(mision2)
pila.push(mision3)
pila.push(mision4)
pila.push(mision5)
pila.push(mision6)


#a
while pila.size() > 0:
    mision = pila.pop()
    pila_aux.push(mision)

while pila_aux.size() > 0:
    mision = pila_aux.pop()
    print(mision.planeta)
    pila.push(mision)

#b

creditos = 0
while pila.size() > 0:
    aux = pila.pop()
    creditos += aux.costo_recompensa
    pila_aux.push(aux)
print(f"el total es{creditos}")


while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

#c
num = 0
planeta = ""

while pila.size() > 0:
    num += 1
    aux = pila.pop()
    if aux.capturado == "han solo":
        planeta = aux.planeta
        break

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print(f"Han Solo fue capturado en la misión {num} en el planeta {planeta}")







        
