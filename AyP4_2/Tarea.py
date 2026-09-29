import heapq
import time

class MatchmakingHeap:
	def __init__(self):
		self.cola = []  # heap de jugadores
		self.contador = 0  

	def agregar_jugador(self, jugador_id, nivel):
		self.contador += 1
		heapq.heappush(self.cola, (self.contador, jugador_id, nivel))

	def buscar_pareja(self, jugador_id, nivel):
		# Buscar la mejor pareja disponible
		mejor_pareja = None
		mejor_pareja_idx = None
		min_diferencia = 151
		for idx, (timestamp, id, lvl) in enumerate(self.cola):
			if id != jugador_id:
				diferencia = abs(lvl - nivel)
				if diferencia <= 150 and diferencia < min_diferencia:
					min_diferencia = diferencia
					mejor_pareja = (timestamp, id, lvl)
					mejor_pareja_idx = idx
		if mejor_pareja:
			self.cola.pop(mejor_pareja_idx)
			heapq.heapify(self.cola)
			return mejor_pareja[1], mejor_pareja[2]
		return None

	def mostrar_cola(self):
		return [(id, lvl) for (timestamp, id, lvl) in sorted(self.cola)]

# Ejemplo de uso:
if __name__ == "__main__":
	matchmaking = MatchmakingHeap()
	matchmaking.agregar_jugador("A", 1200)
	matchmaking.agregar_jugador("B", 1300)
	matchmaking.agregar_jugador("C", 1450)
	matchmaking.agregar_jugador("D", 2000)
	matchmaking.agregar_jugador("E", 1250)

	print("Cola inicial:", matchmaking.mostrar_cola())

	# Un jugador nuevo entra
	nuevo_id = "F"
	nuevo_nivel = 1270
	pareja = matchmaking.buscar_pareja(nuevo_id, nuevo_nivel)
	if pareja:
		print(f"Jugador {nuevo_id} (nivel {nuevo_nivel}) emparejado con {pareja[0]} (nivel {pareja[1]})")
	else:
		matchmaking.agregar_jugador(nuevo_id, nuevo_nivel)
		print(f"Jugador {nuevo_id} (nivel {nuevo_nivel}) agregado a la cola, sin pareja disponible.")

	print("Cola después del matchmaking:", matchmaking.mostrar_cola())
