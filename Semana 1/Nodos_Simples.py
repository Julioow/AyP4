class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Node(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print("Nodo agregado exitosamente")
       
    def mostrar_lista(self):
        actual = self.cabeza
        if actual != None:
            while actual != None:
                print(f"{actual.dato} --> ")
                actual = actual.siguiente
            print("Fin...")
        else:
            print("Lista vacía")
           
    def __str__(self):
        if self.cabeza == None:
            return "[]"
           
        elementos = []
        actual = self.cabeza
        while actual != None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "[" + " --> ".join(elementos) + "]"
       
    def agregar_inicio(self, dato):
        nuevo_nodo = Node(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print("Nodo agregado exitosamente")

lista_ligada = Lista()
lista_ligada.agregar_nodo("Primero nodo")
lista_ligada.agregar_nodo("Segundo nodo")
#lista_ligada.mostrar_lista()
print(lista_ligada)