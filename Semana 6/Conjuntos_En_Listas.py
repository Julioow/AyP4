# Esta clase representa cada "casilla" o "eslabón" individual
class Nodo:
    def __init__(self, dato):
        self.dato = dato          # Guarda el valor que queremos almacenar
        self.siguiente = None     # Guarda la conexión con el siguiente nodo (al inicio no hay)


# Esta clase representa el Conjunto completo usando los nodos enlazados
class Conjunto:
    def __init__(self):
        self.cabeza = None        # Apunta al primer elemento (empieza vacío)
        self.tamaño = 0           # Cuenta cuántos elementos hay guardados

    # Comprueba si el conjunto no tiene ningún elemento
    def esta_vacio(self):
        return self.cabeza is None

    # Devuelve la cantidad total de elementos en el conjunto
    def cardinalidad(self):
        return self.tamaño

    # Busca si un elemento 'x' está dentro del conjunto
    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:   # Si encuentra el valor, confirma que sí está
                return True
            actual = actual.siguiente  # Pasa a revisar la siguiente casilla
        return False                # Si recorre todo y no lo halla, dice que no está

    # Agrega un nuevo elemento 'x' al conjunto
    def agregar(self, x):
        # Como en un conjunto NO se permiten repetidos, verifica si ya existe
        if self.pertenece(x):
            return False            # Si ya está, no lo agrega

        nuevo = Nodo(x)             # Crea el nuevo nodo con el dato
        nuevo.siguiente = self.cabeza # Conecta el nuevo nodo con el que antes era el primero
        self.cabeza = nuevo         # Ahora este nuevo nodo pasa a ser el primero
        self.tamaño += 1            # Suma 1 al contador de elementos
        return True

    # Quita un elemento 'x' del conjunto
    def eliminar(self, x):
        # Si está vacío, no hay nada que borrar
        if self.esta_vacio():
            return False

        # Caso 1: Si el dato a borrar es justamente el primer elemento
        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente # El segundo pasa a ser el primero
            self.tamaño -= 1                    # Resta 1 al contador
            return True

        # Caso 2: Si el dato está más adelante en la cadena
        actual = self.cabeza
        while actual.siguiente:
            # Pregunta si la SIGUIENTE casilla tiene el valor a borrar
            if actual.siguiente.dato == x:
                # "Salta" el nodo que queremos borrar para desconectarlo
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1                 # Resta 1 al contador
                return True
            actual = actual.siguiente            # Avanza al siguiente nodo

        return False                             # Si no lo encontró, devuelve False
    
    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print("{" + ", ".join(elementos) + "}")
        
    def union(self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
            
        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
            
        return resultado
    
    def interseccion(self, otro):
        resultado = Conjunto()
        
        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def diferencia(self, otro):
        resultado = Conjunto()
        
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def diferencia_simetrica(self, otro):
        return self.diferencia(otro).union(otro.diferencia(self))