"""Contexto: Debes gestionar los juegos de una tienda. Cada juego tiene un nombre, una calificación (1-100) y un estado de "Vendido".
Inserción Ordenada: Los juegos deben estar ordenados por Calificación (mayor a menor).
Recursividad Obligatoria: En todos los métodos de gestión."""
class Videojuego:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
        self.vendido = False
        self.siguiente = None

class Inventario:
    def __init__(self):
        self.inicio = None

    # PUNTO 2 ESPEJO: Agregar Ordenado (RECURSIVO)
    def agregar_juego(self, nombre, calificacion):
        nuevo = Videojuego(nombre, calificacion)
        
        def _recursivo(nodo, nuevo_nodo):
            # Caso base 1: Llegamos al final
            # Caso base 2: El nuevo tiene mayor calificación que el actual (va antes)
            if nodo is None or nuevo_nodo.calificacion > nodo.calificacion:
                nuevo_nodo.siguiente = nodo
                return nuevo_nodo
            
            # Si no es mayor, seguimos buscando su lugar
            nodo.siguiente = _recursivo(nodo.siguiente, nuevo_nodo)
            return nodo
        
        self.inicio = _recursivo(self.inicio, nuevo)

    # PUNTO 3 ESPEJO: Contar por calificación (RECURSIVO)
    def contar_disponibles_top(self, calificacion_minima):
        def _recursivo(nodo):
            if nodo is None:
                return 0
            
            actual_cuenta = 0
            if nodo.calificacion >= calificacion_minima and not nodo.vendido:
                actual_cuenta = 1
                
            return actual_cuenta + _recursivo(nodo.siguiente)
        
        return _recursivo(self.inicio)

    # PUNTO 4 ESPEJO: Obtener Nueva Lista de Joyas (RECURSIVO)
    def obtener_joyas(self):
        nueva_lista = Inventario()
        
        def _recursivo(nodo):
            if nodo is None:
                return
            # Procesamos hacia adelante o hacia atrás
            # Si queremos mantener el orden original, procesamos y luego llamamos
            if nodo.calificacion >= 90 and not nodo.vendido:
                # Usamos el agregar_juego de la nueva lista
                nueva_lista.agregar_juego(nodo.nombre, nodo.calificacion)
            
            _recursivo(nodo.siguiente)
            
        _recursivo(self.inicio)
        return nueva_lista

    # PUNTO 5 ESPEJO: Eliminar Vendidos (RECURSIVO)
    def eliminar_vendidos(self):
        def _recursivo(nodo):
            if nodo is None:
                return None
            
            if nodo.vendido:
                # Si está vendido, lo "saltamos" retornando el siguiente
                return _recursivo(nodo.siguiente)
            
            # Si no está vendido, reconstruimos el enlace
            nodo.siguiente = _recursivo(nodo.siguiente)
            return nodo
            
        self.inicio = _recursivo(self.inicio)

    def vender(self, nombre):
        actual = self.inicio
        while actual:
            if actual.nombre == nombre:
                actual.vendido = True
            actual = actual.siguiente

    def mostrar(self):
        actual = self.inicio
        while actual:
            est = "[VENDIDO]" if actual.vendido else "[TIENDA]"
            print(f"{est} {actual.nombre} - Puntaje: {actual.calificacion}")
            actual = actual.siguiente

# --- PRUEBAS ---
tienda = Inventario()
tienda.agregar_juego("Zelda", 95)
tienda.agregar_juego("FIFA", 70)
tienda.agregar_juego("Elden Ring", 98)
tienda.agregar_juego("Indie Game", 85)

print("🎮 Inventario inicial (Ordenado por puntaje):")
tienda.mostrar()

tienda.vender("Elden Ring")
print("\n💎 Joyas (90+) no vendidas:")
joyas = tienda.obtener_joyas()
joyas.mostrar()