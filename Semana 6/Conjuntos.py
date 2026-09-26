#algoritmos = {"Ana", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Helena", "Ivan"}

#bases_de_datos = {"Carlos", "Diana", "Juan", "Karen", "Gabriel", "Luis", "Maria"}

#redes = {"Diana", "Eduardo", "Gabriel", "Karen", "Natalia", "Oscar", "Ivan"}

#print((algoritmos - bases_de_datos - redes) | (bases_de_datos - algoritmos - redes) | (redes - algoritmos - bases_de_datos))

#-------------------------------------------------------------------------------------------------------------------

catalogo = {
    "Inception" : {"ciencia ficción", "acción", "thriller", "drama"},
    "The Matrix" : {"ciencia ficción", "acción", "thriller"},
    "Titanic" : {"romance", "drama", "hirtórica"},
    "Avengers" : {"acción", "ciencia ficción", "aventura"},
    "John Wick" : {"acción", "thriller", "crimen"},
    "Interstellar" : {"ciencia ficción", "drama", "aventura"},
    "Toy Story" : {"animación", "comedia", "aventura"},
    "Shrek" : {"animación", "comedia", "aventura"}
}

peliculas = list(catalogo.keys()) 

for i in range(len(peliculas)):
    for j in range(i+1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        comunes = catalogo[p1] & catalogo[p2]
        if len(comunes) >= 2:
            print(f"   {p1} <--> {p2}")
            print(f"Géneros en común: {comunes}")    

favoritos = {"acción", "ciencia ficción", "aventura"}

recomendaciones = []
for pelicula, generos in catalogo.items():
    coincidencias = favoritos & generos
    
    if coincidencias:
        puntaje = len(coincidencias) / len(favoritos)
        recomendaciones.append((pelicula, puntaje * 100, coincidencias))
        
recomendaciones.sort(key=lambda x:x[1], reverse=True)
print(recomendaciones)

todos_los_generos = set()

for genero in catalogo.values():
    todos_los_generos = todos_los_generos | genero
    
print(todos_los_generos)


#Mostrar las peliculas por género
for genero in todos_los_generos:
    peliculas_genero = set()
    for pelicula, generos in catalogo.items():
        if genero in generos:
            peliculas_genero.add(pelicula)
            
    print(f"{genero}: {peliculas_genero}")
    
#Indice de Jaccard = (A & B) / (A | B)
def similitud_jaccard(pelicula1, pelicula2):
    g1 = catalogo[pelicula1]
    g2 = catalogo[pelicula2]
    
    interseccion = len(g1 & g2)
    union = len(g1 | g2)
    return interseccion / union if union > 0 else 0

pares = [
    ("Inception", "The Matrix"),
    ("Inception", "Titanic"),
    ("Toy Story", "Shrek"),
    ("Interstellar", "John Wick")
]

for p1, p2 in pares:
    sim = similitud_jaccard(p1, p2)
    print(f"Índice Jaccard entre {p1} y {p2} es {round(sim*100, 2)}%")