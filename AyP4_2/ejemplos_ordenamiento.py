import random
import time

def generar_jugadores(n):
    paises = ["COL", "ARG", "BRA", "URU", "PER"]
    nombres = ["Alex", "Maria", "Juan", "Sofia", "Carlos", "Ana", "Luis", "Laura", "Diego", "Isabella"]
    jugadores= []
    for i in range(n):
        jugadores.append({
            "id": i+1,
            "nombre": f"{random.choice(nombres)}_{i}",
            "puntos" : random.randint(100, 10000),
            "pais": random.choice(paises)
        })
    return jugadores

    def merge_sort(jugadores):
        if len(jugadores) <= 1:
            return jugadores
        mid = len(jugadores) // 2
        left_half = merge_sort(jugadores[:mid])
        right_half = merge_sort(jugadores[mid:])
        return merge(left_half, right_half)
        