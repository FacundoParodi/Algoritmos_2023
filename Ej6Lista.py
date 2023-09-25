from listaa import lista
from random import randint

class superheroe():
     
    def _init_(self, nombre, year, casa, bibliografia):
        self.nombre = nombre
        self.year = year
        self.casa = casa
        self.bibliografia = bibliografia

    def _str_(self):
        return f'{self.nombre} - {self.year} - {self.casa}- {self.bibliografia}'

lista= lista()

superheroe1=superheroe('Linterna Verde', 1940, 'DC', 'Es Verde' )
superheroe2=superheroe('Wolverine', 1974, 'Marvel','Tiene garras')
superheroe3=superheroe('Iron Man',1968,'Marvel','Tiene una armadura')
superheroe4=superheroe('Capitana Marvel',1967,'Marvel','Tiene poderes')
superheroe5=superheroe('Mujer Maravilla',1941,'DC','Es una amazona')
superheroe6=superheroe('Flash',1940,'DC','Es rapido')
superheroe7=superheroe('Star-Lord',1976,'Marvel','Es amigo de un mapache')
superheroe8=superheroe('Dr. Strange', 1963, 'DC', 'Es magico traje' )

lista.insert(superheroe1,'nombre')
lista.insert(superheroe2,'nombre')
lista.insert(superheroe3,'nombre')
lista.insert(superheroe4,'nombre')
lista.insert(superheroe5,'nombre')
lista.insert(superheroe6,'nombre')
lista.insert(superheroe7,'nombre')
lista.insert(superheroe8,'nombre')

#a
elemento=lista.search('Linterna Verde', 'nombre')
if  elemento != None: 
    lista.delete('Linterna Verde','nombre')
print()

#b
elemento2=lista.search('Wolverine', 'nombre')
if  elemento2 != None:
    print ('AÑO: ',lista.get_element_by_index(elemento2).year)
print()  

#c
elemento3=lista.search('Dr. Strange', 'nombre')
if elemento3 != None:
    lista.get_element_by_index(elemento3).casa = 'Marvel'
print()

#d
for i in range(0,lista.size()):
   if  ('armadura' in lista.get_element_by_index(i).bibliografia) or ('traje' in lista.get_element_by_index(i).bibliografia):
       print ('Traje o Armadura: ', lista.get_element_by_index(i).nombre)
print()

#e
for i in range(lista.size()):
    if lista.get_element_by_index(i).year < 1963: 
        print('menor a 1963: ',lista.get_element_by_index(i).nombre,lista.get_element_by_index(i).casa)

#f
elemento4=lista.search('Capitana Marvel', 'nombre')
elemento5=lista.search('Mujer Maravilla', 'nombre')
if elemento4!= None:
   print('Capitana Marvel:', lista.get_element_by_index(elemento4).casa) 
print()
if elemento5!= None:
    print('Mujer Maravilla: ',lista.get_element_by_index(elemento5).casa) 
print()

#g
elemento6=lista.search('Flash', 'nombre')
elemento7=lista.search('Star-Lord', 'nombre')
if elemento6!= None:
   print(lista.get_element_by_index(elemento6)) 
print()
if elemento7!= None:
   print(lista.get_element_by_index(elemento7)) 

print()

#h
for i in range(0, lista.size()):
    if lista.get_element_by_index(i).nombre[0] in ['B', 'M', 'S']:
        print(lista.get_element_by_index(i)) 
print()

#i
cont_DC=0
cont_M=0

for i in range(0, lista.size()):
    if lista.get_element_by_index(i).casa=='DC':
        cont_DC+=1
    else:
        cont_M +=1
print(f'hay un total de {cont_DC} heroes de DC en la lista y {cont_M} de marvel')