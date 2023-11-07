class pilas():
    
    def __init__(self):
        self.__elements = [] # Inicializamos una pila vacia llamada "elements"

    def __eq__(self, stack_aux):
        if isinstance(stack_aux, pilas):
            return self.__elements == stack_aux.__elements
        else:
            return False  # "eq" es un metodo especial que se usa para comparar si 2 objetos de
                          # una clase son iguales, (en este caso de la clase pila, self y stack_aux)
                          #  con la funcion insistance verifica si stack_aux 
                          # es un objeto de la clase pila, si es asi compara los elementos 
                          # de stack_aux con los de self, si son iguales retorna "true" 


    def push(self, dato):
        self.__elements.append(dato) # Este metodo se usa para agregar un nuevo elemento el cual
                                     # va a la parte superior de la pila


    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop() 
            return dato # elimina y devuelve el último elemento agregado a la pila, es decir
                        # el que esta en la cima
                                

    def size(self):
        return len(self.__elements) #  devuelve la cantidad de elementos almacenados en la pila


    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1] # devuelve el elemento en la cima de la pila 
        
    def __str__(self):
        return str(self.__elements)