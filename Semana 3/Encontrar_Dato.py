class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            
    def encontrar_dato(self, dato, nodo=None):

        if nodo is None:
            return False
        
        if nodo.dato == dato:
            return True
        
        return self.buscar(dato, nodo.siguiente)