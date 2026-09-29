# -----------------------------
# Clase Cancion
# -----------------------------
class Cancion:
    def __init__(self, nombre, duracion_segundos):
        self.nombre = nombre
        self.duracion = duracion_segundos  # duración en segundos

    def tiempo_formato(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{minutos}:{segundos:02d}"


# -----------------------------
# Clase Reproductor
# -----------------------------
class Reproductor:
    def __init__(self):
        self.lista = []       # Lista de canciones
        self.indice = 0       # Canción actual

    def esta_vacia(self):
        return not self.lista

    def agregar_cancion(self, nombre, duracion_segundos):
        cancion = Cancion(nombre, duracion_segundos)
        self.lista.append(cancion)
        print("Canción agregada correctamente.")

    # Método recursivo para agregar canción
    def agregar_cancion_recursivo(self, nombre, duracion_segundos, idx=0):
        if idx == len(self.lista):
            self.lista.append(Cancion(nombre, duracion_segundos))
            print("Canción agregada correctamente (recursivo).")
            return
        else:
            return self.agregar_cancion_recursivo(nombre, duracion_segundos, idx + 1)

    def reproducir(self):
        if self.esta_vacia():
            print("No hay canciones en la lista.")
            return

        actual = self.lista[self.indice]
        print(f" Reproduciendo: {actual.nombre} ({actual.tiempo_formato()} min)")

    # Método recursivo para reproducir
    def reproducir_recursivo(self, idx=None):
        if self.esta_vacia():
            print("No hay canciones en la lista.")
            return
        if idx is None:
            idx = self.indice
        if idx >= len(self.lista):
            return
        actual = self.lista[idx]
        print(f" Reproduciendo (recursivo): {actual.nombre} ({actual.tiempo_formato()} min)")

    def siguiente(self):
        if self.esta_vacia():
            print("No hay canciones.")
            return

        if self.indice < len(self.lista) - 1:
            self.indice += 1
        else:
            print("Ya estás en la última canción.")

        self.reproducir()

    # Método recursivo para siguiente
    def siguiente_recursivo(self, idx=None):
        if self.esta_vacia():
            print("No hay canciones.")
            return
        if idx is None:
            idx = self.indice
        if idx < len(self.lista) - 1:
            idx += 1
            self.indice = idx
            self.reproducir_recursivo(idx)
        else:
            print("Ya estás en la última canción.")
            self.reproducir_recursivo(idx)

    def anterior(self):
        if self.esta_vacia():
            print("No hay canciones.")
            return

        if self.indice > 0:
            self.indice -= 1
        else:
            print("Ya estás en la primera canción.")

        self.reproducir()

    # Método recursivo para anterior
    def anterior_recursivo(self, idx=None):
        if self.esta_vacia():
            print("No hay canciones.")
            return
        if idx is None:
            idx = self.indice
        if idx > 0:
            idx -= 1
            self.indice = idx
            self.reproducir_recursivo(idx)
        else:
            print("Ya estás en la primera canción.")
            self.reproducir_recursivo(idx)

    def mostrar(self):
        if self.esta_vacia():
            print("Lista vacía.")
            return

        print("\n--- Lista de canciones ---")
        for i, cancion in enumerate(self.lista):
            print(f"{i + 1}. {cancion.nombre} ({cancion.tiempo_formato()} min)")
        print("--------------------------")

    # Método recursivo para mostrar
    def mostrar_recursivo(self, idx=0):
        if self.esta_vacia():
            print("Lista vacía.")
            return
        if idx == 0:
            print("\n--- Lista de canciones (recursivo) ---")
        if idx < len(self.lista):
            cancion = self.lista[idx]
            print(f"{idx + 1}. {cancion.nombre} ({cancion.tiempo_formato()} min)")
            self.mostrar_recursivo(idx + 1)
        else:
            print("--------------------------")

    #buscar de forma recursiva
    def buscar(self, nodo=None, dato=None, primera_llamada=True):
        if primera_llamada:
            nodo = self.cabeza
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        return seft.buscar(nodo.siguiente, dato, False)        

# -----------------------------
# Programa principal (main)
# -----------------------------
reproductor = Reproductor()

while True:

# Versión recursiva del menú principal
  def menu_reproductor_recursivo(reproductor):
    print("\n--- MENÚ REPRODUCTOR (Recursivo) ---")
    print("1. Agregar canción")
    print("2. Reproducir canción actual")
    print("3. Siguiente canción")
    print("4. Canción anterior")
    print("5. Mostrar lista de canciones")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la canción: ")
        duracion_segundos = input("Duración (segundos): ")
        try:
            duracion_segundos = int(duracion_segundos)
        except ValueError:
            print("Duración inválida. Debe ser un número entero de segundos.")
            return menu_reproductor_recursivo(reproductor)
        reproductor.agregar_cancion(nombre, duracion_segundos)
        return menu_reproductor_recursivo(reproductor)

    elif opcion == "2":
        reproductor.reproducir()
        return menu_reproductor_recursivo(reproductor)

    elif opcion == "3":
        # reproductor = Reproductor()
        #
        # while True:
        #     ... (menú original comentado)

        reproductor = Reproductor()
        menu_reproductor_recursivo(reproductor)

 