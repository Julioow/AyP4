class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def duracion_formateada(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{minutos}:{segundos}"
class Node:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None
        
class Playlist:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        
    def esta_vacia(self):
            return self.cabeza is None
    
    def insertar_inicio(self, cancion):
        nuevo_nodo = Node(cancion)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
    
    def insertar_final(self, cancion):
        nuevo_nodo = Node(cancion)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
    
    def eliminar_inicio(self):
        if self.esta_vacia():
            return None

        cancion = self.cabeza.cancion

        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None

        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
    
    def eliminar_ultimo(self):
        if self.esta_vacia():
            return None

        cancion = self.cola.cancion

        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None

        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
    
    def mostrar_playlist(self):
            actual = self.cabeza
            if actual != None:
                while actual != None:
                    print(f"{actual.cancion.titulo}-{actual.cancion.duracion_formateada()} --> ")
                    actual = actual.siguiente
                print("Fin...")
            else:
                print("Lista vacía")
            
cancion1 = Cancion("Soy una gargola", "Jowell & Randy", 212)
cancion2 = Cancion("Amor", "Zion", 215)

reproductor = Playlist()
reproductor.insertar_inicio(cancion1)
reproductor.insertar_inicio(cancion2)
reproductor.mostrar_playlist()