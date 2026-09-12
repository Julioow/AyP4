class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None
        self.tam = 0

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tam += 1

    def pop(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tam -= 1
        return dato

    def peek(self):
        if self.esta_vacia():
            return None
        return self.tope.dato


def parentesis_balanceados(expresion):
    pila = Pila()

    pares = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    aperturas = set(pares.values())
    cierres = set(pares.keys())

    for caracter in expresion:
        if caracter in aperturas:
            pila.push(caracter)
        elif caracter in cierres:
            if pila.esta_vacia():
                return False
            tope = pila.pop()
            if tope != pares[caracter]:
                return False

    return pila.esta_vacia()