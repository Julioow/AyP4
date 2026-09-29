""" Contexto: Debes crear un sistema para gestionar tareas pendientes usando una lista enlazada. Cada tarea tiene un nombre, una prioridad (1 a 5) y un tiempo estimado de ejecución.
Requerimientos:
Nodo (Tarea): Almacena nombre, prioridad, tiempo y el enlace al siguiente.
Lista (ListaTareas): Las nuevas tareas se agregan al FINAL (a diferencia de tu examen anterior, para practicar otra variante).
Método Recursivo - Sumar Tiempo: Calcular el tiempo total de todas las tareas.
Método Recursivo - Filtrar por Prioridad: Retornar una nueva lista solo con tareas de prioridad > 3.
Método Recursivo - Eliminar Tareas Cortas: Eliminar de la lista original las tareas que duren menos de 5 minutos. """

# PUNTO 1: Definición de Estructuras
class Tarea:
    def __init__(self, nombre, prioridad, tiempo):
        self.nombre = nombre
        self.prioridad = prioridad
        self.tiempo = tiempo
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.inicio = None

    # PUNTO 2: Agregar al FINAL (Variante útil para practicar)
    def agregar_tarea(self, nombre, prioridad, tiempo):
        nueva = Tarea(nombre, prioridad, tiempo)
        if not self.inicio:
            self.inicio = nueva
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva

    # PUNTO 3: Tiempo Total (RECURSIVO)
    def calcular_tiempo_total(self):
        def _recursivo(nodo):
            if nodo is None:
                return 0
            return nodo.tiempo + _recursivo(nodo.siguiente)
        
        return _recursivo(self.inicio)

    # PUNTO 4: Filtrar Prioridad Alta (RECURSIVO)
    # Crea una nueva lista sin afectar la original
    def obtener_prioritarias(self):
        nueva_lista = ListaTareas()
        
        def _recursivo(nodo):
            if nodo is None:
                return
            # Si cumple la condición, la agregamos a la nueva lista
            if nodo.prioridad > 3:
                nueva_lista.agregar_tarea(nodo.nombre, nodo.prioridad, nodo.tiempo)
            _recursivo(nodo.siguiente)
            
        _recursivo(self.inicio)
        return nueva_lista

    # PUNTO 5: Eliminar Tareas Cortas (RECURSIVO)
    # Esta es la parte más difícil: reconstruir los enlaces al volver de la recursión
    def eliminar_tareas_cortas(self, tiempo_minimo):
        def _recursivo(nodo):
            if nodo is None:
                return None
            
            # Si el nodo actual debe ser eliminado...
            if nodo.tiempo < tiempo_minimo:
                # Saltamos este nodo y retornamos lo que diga el resto de la lista
                return _recursivo(nodo.siguiente)
            
            # Si el nodo se queda, conectamos su siguiente con el resultado de la recursión
            nodo.siguiente = _recursivo(nodo.siguiente)
            return nodo
            
        self.inicio = _recursivo(self.inicio)

    def mostrar(self):
        actual = self.inicio
        while actual:
            print(f"[{actual.nombre} | Prioridad: {actual.prioridad} | {actual.tiempo} min]")
            actual = actual.siguiente

# --- PRUEBA DEL SISTEMA ---
if __name__ == "__main__":
    gestor = ListaTareas()
    gestor.agregar_tarea("Estudiar Python", 5, 60)
    gestor.agregar_tarea("Lavar platos", 2, 4)
    gestor.agregar_tarea("Proyecto Final", 5, 120)
    gestor.agregar_tarea("Revisar correo", 1, 3)

    print("📋 Lista Original:")
    gestor.mostrar()

    print(f"\n⏱️ Tiempo total estimado: {gestor.calcular_tiempo_total()} min")

    print("\n🔥 Tareas de Alta Prioridad (>3):")
    prioritarias = gestor.obtener_prioritarias()
    prioritarias.mostrar()

    print("\n🗑️ Eliminando tareas de menos de 5 min...")
    gestor.eliminar_tareas_cortas(5)
    gestor.mostrar()