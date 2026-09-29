class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0
        if elementos:
            for elemento in elementos:
                self.agregar(elemento)

    def esta_vacia(self):
        return self.cabeza is None

    def cardinalidad(self):
        return self.tamaño

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, x):
        if self.pertenece(x):
            return False
        nuevo_nodo = Nodo(x)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamaño += 1
        return True

    def eliminar(self, x):
        if self.esta_vacia():
            return False
        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == x:
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False

    def vaciar(self):
        self.cabeza = None
        self.tamaño = 0

    def union(self, otro_conjunto):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        actual = otro_conjunto.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado

    def interseccion(self, otro_conjunto):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if otro_conjunto.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado

    def diferencia(self, otro_conjunto):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if not otro_conjunto.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado

    def diferencia_simetrica(self, otro_conjunto):
        return self.diferencia(otro_conjunto).union(otro_conjunto.diferencia(self))

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def __str__(self):
        return "{" + ",".join(str(x) for x in self.a_lista()) + "}"


A = Conjunto(["A", "B", "C"])
B = Conjunto(["C", "D", "E"])
C = A.union(B)
print(C)


# ── Canciones ──────────────────────────────────────────────
canciones_juan = {
    "Despacito", "Shape of You", "Blinding Lights",
    "Uptown Funk", "Thinking Out Loud", "Can't Stop the Feeling!",
    "Happy", "Rolling in the Deep", "Shallow"
}

canciones_maria = {
    "Shape of You", "Blinding Lights", "Uptown Funk",
    "Drivers license", "Levitating", "Watermelon Sugar"
}

compartidas_alternativa = canciones_juan.intersection(canciones_maria)
print("Canciones compartidas (alternativa):", compartidas_alternativa)

recomendaciones_juan = canciones_maria - canciones_juan
print("Recomendaciones para Juan:", recomendaciones_juan)

recomendaciones_juan_alternativa = canciones_maria.difference(canciones_juan)
print("Recomendaciones para Juan (alternativa):", recomendaciones_juan_alternativa)


# ── Estudiantes ─────────────────────────────────────────────
algoritmos = {
    "Ana", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Helena", "Ivan"
}

base_datos = {
    "Carlos", "Diana", "Juan", "Karen", "Gabriel", "Luis", "Maria"
}

redes = {
    "Diana", "Eduardo", "Gabriel", "Karen", "Natalia", "Oscar", "Ivan"
}

solo_ven_una = (
    (redes - algoritmos - base_datos) |
    (algoritmos - redes - base_datos) |
    (base_datos - algoritmos - redes)
)
print("Estudiantes que solo ven una materia:", solo_ven_una)


# ── Catálogo de películas ────────────────────────────────────
catalogo = {
    "Inception": {"ciencia ficción", "acción", "thriller", "drama"},
    "The Matrix": {"ciencia ficción", "acción", "thriller"},
    "Titanic": {"drama", "romance", "historica"},
    "The Notebook": {"drama", "romance"},
    "Avengers": {"ciencia ficción", "acción", "aventura", "superhéroes"},
    "John Wick": {"acción", "thriller", "crimen"},
    "Interstellar": {"ciencia ficción", "drama", "aventura"},
    "The Godfather": {"drama", "crimen", "thriller"},
    "Toy Story": {"animación", "aventura", "comedia"},
    "Shrek": {"animación", "aventura", "comedia"},
}

peliculas_con_generos_en_comun = []
peliculas = list(catalogo.keys())
for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        comunes = catalogo[p1].intersection(catalogo[p2])
        if len(comunes) >= 2:
            peliculas_con_generos_en_comun.append((p1, p2, comunes))

print(peliculas_con_generos_en_comun)

favoritos = {"acción", "crimen", "aventura"}
recomendaciones = []
for pelicula, generos in catalogo.items():
    if generos.intersection(favoritos):
        recomendaciones.append(pelicula)
print("Peliculas recomendadas:", recomendaciones)


#como puedo mostar todos los generos que hay en el catalogo sin repetirlos?
todos_los_generos = set().union(*catalogo.values())#esto hace una union de todos los conjuntos de generos en el catalogo, resultando en un conjunto con todos los generos sin repetir.
print("Géneros en el catálogo:", todos_los_generos)

#cada genero con sus peliculas al lado
generos_unicos = set()
for generos in catalogo.values():
    generos_unicos = generos_unicos.union(generos)
print("Géneros únicos en el catálogo:", generos_unicos)   

for genero in generos_unicos:
    peliculas_del_genero = set(catalogo.keys()).intersection(
        {pelicula for pelicula, generos in catalogo.items() if genero in generos}
    )
    print(f"{genero}: {peliculas_del_genero}")


#metodo que recibe 2 peliculas y devuelve el indice de similitud jaccard
def jaccard(peliculas1, peliculas2):
    interseccion = peliculas1.intersection(peliculas2)
    union = peliculas1.union(peliculas2)
    if not union:
        return 0.0
    return len(interseccion) / len(union)


#leer dos textos
#calcular el indice de similitud ignorando las STOP WORDS
#si el indice es mayor a 0.6, se copiaron 

SPTOP_WORDS = {"el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al",
"a", "en", "con", "por", "para", "y", "o", "que", "es", "son", "se", "su", "sus", "como", "pero", "mas", "este", "esta", "estos", "estas"
}

def texto_a_conjunto(texto):
    palabras = set(texto.lower().split())
    return palabras - SPTOP_WORDS

def similitud_jaccard(texto1, texto2):
    conjunto1 = texto_a_conjunto(texto1)
    conjunto2 = texto_a_conjunto(texto2)
    return jaccard(conjunto1, conjunto2)

texto_a_conjunto("El gato está en la casa")
texto_a_conjunto("La casa del gato es grande")
similitud = similitud_jaccard("El gato está en la casa", "La casa del gato es grande")
print("Similitud Jaccard:", similitud)
print("¿Los textos son similares?", similitud > 0.6)
print("Conjunto del texto 1:", texto_a_conjunto("El gato está en la casa"))
print("Conjunto del texto 2:", texto_a_conjunto("La casa del gato es grande"))

