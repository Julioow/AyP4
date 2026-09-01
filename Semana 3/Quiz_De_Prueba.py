class Pagina:
    def __init__(self, url, tiempo, titulo):
        self.url = url
        self.tiempo = tiempo
        self.titulo = titulo
        self.siguiente = None
        
class Historial:
    def __init__(self):
        self.cabeza = None
        
    def visitar(self, url, tiempo, titulo):
        nueva = Pagina(url, tiempo, titulo)
        nueva.siguiente = self.cabeza
        self.cabeza = nueva
        
    def tiempo_total(self, nodo):
        if nodo is None:
            return 0
        return nodo.tiempo + self.tiempo_total(nodo.siguiente)
    
    def buscar_por_dominio(self, texto):
        resultado = []
        
    def buscar(self, nodo, texto):
        if nodo is None:
            return None
        
        if texto in nodo.url:
            resultado.append((nodo.url, nodo.tiempo, nodo.titulo))
            
        return self.buscar(nodo.siguiente, texto)
    
        self.buscar(self.inicio, texto)
        return resultado

    def eliminar(self, nodo, minimo):
        if nodo is None:
            return None
        
        nodo.siguiente = self.eliminar(nodo.siguiente, minimo)
        
        if nodo.tiempo < minimo:
            return nodo.siguiente
        
        return nodo
