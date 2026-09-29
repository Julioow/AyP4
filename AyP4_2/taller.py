"""
═══════════════════════════════════════════════════════════════════════════════
        TALLER: ANÁLISIS DE ALGORITMOS
        Algoritmos y Programación 4
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES GENERALES:
------------------------
- Entregar archivo .py con todas las secciones resueltas
- El código debe ejecutar sin errores

DISTRIBUCIÓN:
- Sección A: Análisis teórico (1.0)         
- Sección B: Investigación (0.5)             
- Sección C: Resolver y optimizar (2.0)      
- Sección D: Proponer y justificar (1.5)     

═══════════════════════════════════════════════════════════════════════════════
"""

import time
import random


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN A: ANÁLISIS TEÓRICO (1.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO A.1 (0.4): Clasificar complejidad

Para cada función, escribe:
  - La complejidad Big-O
  - UNA línea explicando por qué

Escribe tus respuestas como comentarios debajo de cada función.
"""


def alpha(lista):
    total = 0
    for x in lista:
        total += x
    promedio = total / len(lista)
    return promedio

# Complejidad: O(n)
# Porque: Recorre la lista una sola vez para sumar todos los elementos


def beta(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j] and i != j:
                return True
    return False

# Complejidad: O(n²)
# Porque: Dos bucles anidados que recorren toda la lista en peor caso


def gamma(n):
    if n <= 1:
        return 1
    return gamma(n // 2) + 1

# Complejidad: O(log n)
# Porque: Divide el problema a la mitad en cada llamada recursiva


def delta(lista):
    resultado = set()
    for x in lista:
        resultado.add(x)
    return resultado

# Complejidad: O(n)
# Porque: Recorre la lista una vez y cada add en set es O(1) en promedio


def epsilon(lista):
    for x in lista:
        if x in lista:
            pass

# Complejidad: O(n²)
# Porque: El bucle exterior recorre n elementos y el `in` busca en toda la lista O(n)


def zeta(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 3

# Complejidad: O(n log n)
# Porque: El for es O(n) y el while es O(log n) porque j se multiplica por 3 cada iteración


def eta(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = eta(lista[:medio])
    der = eta(lista[medio:])
    return izq + der

# Complejidad: O(n log n)
# Porque: Es un patrón divide-y-conquista donde se procesa como merge sort


def theta(n):
    i = 1
    while i * i <= n:
        i += 1
    return i

# Complejidad: O(√n)
# Porque: El while itera mientras i² ≤ n, es decir hasta que i ≈ √n


"""
PUNTO A.2 (0.3): Ordenar de menor a mayor complejidad

Ordena las siguientes complejidades de la MÁS RÁPIDA a la MÁS LENTA:

O(n!), O(1), O(n log n), O(2^n), O(n²), O(log n), O(n), O(n³), O(√n)

Tu respuesta (de más rápida a más lenta):
1. O(1)
2. O(log n)
3. O(√n)
4. O(n)
5. O(n log n)
6. O(n²)
7. O(n³)
8. O(2^n)
9. O(n!)
"""


"""
PUNTO A.3 (0.3): Verdadero o Falso

Escribe V o F y justifica brevemente las falsas.

1. F O(2n) es más lento que O(n)
   Justificación: O(2n) = O(n) por propiedades de notación asintótica. Las constantes se descartan.

2. F Un algoritmo O(n²) siempre es más lento que uno O(n log n)
   Justificación: Depende del tamaño de n. Para n pequeños, O(n²) puede ser más rápido por factores constantes.

3. F Si un algoritmo tiene un for de n y dentro un for de 5, su complejidad es O(n²)
   Justificación: O(n * 5) = O(n). Las constantes se descartan en Big-O.

4. F `x in set` tiene la misma complejidad que `x in list`
   Justificación: `x in set` es O(1) en promedio mientras que `x in list` es O(n).

5. F Un algoritmo recursivo que se llama a sí mismo 2 veces siempre es O(2^n)
   Justificación: Depende de cómo se divide el problema. Si divide por 2 cada vez, puede ser O(n) con memorización.

6. F O(n) + O(n²) = O(n³)
   Justificación: O(n) + O(n²) = O(n²) porque tomamos el término dominante.

7. V La complejidad espacial de un algoritmo in-place es O(1)
   Justificación: Correcto, solo usa una cantidad constante de memoria adicional.

8. V Memorización mejora la complejidad temporal pero empeora la espacial
   Justificación: Correcto, cacheamos resultados para evitar cálculos repetidos (mejora temporal) pero necesitamos almacenamiento.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN B: INVESTIGACIÓN (0.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO B.1 (0.25): Complejidad de operaciones de Python

Investiga y completa la tabla con la complejidad de cada operación.
Agrega una justificación de por qué es la complejidad.
Puedes consultar: https://wiki.python.org/moin/TimeComplexity

┌──────────────────────────────┬──────────────┬──────────────┐
│ Operación                    │ Lista []     │ Set/Dict {}  │
├──────────────────────────────┼──────────────┼──────────────┤
│ Acceder por índice [i]       │ O(1)         │ N/A          │
│ Buscar elemento (x in ...)   │ O(n)         │ O(1)         │
│ Agregar al final (.append)   │ O(1) amort.  │ O(1) prom.   │
│ Insertar al inicio           │ O(n)         │ N/A          │
│ Eliminar por valor (.remove) │ O(n)         │ O(1) prom.   │
│ Obtener longitud (len)       │ O(1)         │ O(1)         │
│ Ordenar (.sort / sorted)     │ O(n log n)   │ N/A          │
│ Copiar (.copy / [:])         │ O(n)         │ O(n)         │
└──────────────────────────────┴──────────────┴──────────────┘

Justificaciones:
- Acceso por índice: arrays almacenan elementos contiguos en memoria
- Búsqueda: lista recorre linealmente, set usa hash O(1)
- Append: O(1) amortizado porque el buffer se expande dinámicamente
- Insertar al inicio: lista debe desplazar todos los elementos
- Remove: lista busca + desplaza; set usa hash
- len: información almacenada en la estructura
- Ordenar: Python usa Timsort que es O(n log n) en general
- Copiar: debe crear nuevas referencias u objetos
"""


"""
PUNTO B.2 (0.25): Caso real

Investiga y responde:

1. ¿Qué algoritmo de ordenamiento usa Python internamente (sorted/list.sort)?
   Respuesta: Timsort (hybrid de merge sort + insertion sort)

2. ¿Cuál es su complejidad en el mejor, peor y caso promedio?
   Mejor: O(n)           (cuando está parcialmente ordenado)
   Peor: O(n log n)      (cuando está completamente desordenado)
   Promedio: O(n log n)  (caso típico)

3. ¿Por qué Python eligió ese algoritmo y no Quick Sort?
   Respuesta: Timsort es más estable (mantiene orden de elementos iguales), tiene mejor 
   rendimiento en datos reales (puede aprovechar subsecuencias ordenadas), y se comporta 
   bien con memoria cache. Quick Sort es más rápido en promedio pero puede tener peor caso O(n²) 
   y es inestable. Python priorizó estabilidad y rendimiento predecible.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN C: RESOLVER Y OPTIMIZAR (2.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
En cada problema:
1. Analiza la versión LENTA y escribe su complejidad
2. Implementa la versión RÁPIDA
3. Escribe la complejidad de tu versión
4. Ejecuta las pruebas para verificar que funciona
"""


# ─── PROBLEMA C.1 (0.4): Elementos únicos ────────────────────────────────────

def unicos_lento(lista):
    """
    Retorna lista sin duplicados manteniendo el orden.
    COMPLEJIDAD: O(n²)  ← analiza y escribe
    """
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado


def unicos_rapido(lista):
    """
    Misma funcionalidad pero más eficiente.
    USA un set auxiliar para búsqueda O(1).

    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    vistos = set()
    resultado = []
    for x in lista:
        if x not in vistos:
            vistos.add(x)
            resultado.append(x)
    return resultado


# ─── PROBLEMA C.2 (0.4): Frecuencia del más común ────────────────────────────

def mas_comun_lento(lista):
    """
    Retorna el elemento que más se repite y cuántas veces.
    COMPLEJIDAD: O(n²)  ← analiza y escribe
    """
    max_elem = None
    max_count = 0
    for x in lista:
        count = 0
        for y in lista:
            if y == x:
                count += 1
        if count > max_count:
            max_count = count
            max_elem = x
    return max_elem, max_count


def mas_comun_rapido(lista):
    """
    Misma funcionalidad usando diccionario contador.

    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    contador = {}
    for x in lista:
        contador[x] = contador.get(x, 0) + 1
    # Encontrar el elemento con máxima frecuencia
    max_elem = max(contador, key=contador.get)
    return max_elem, contador[max_elem]


# ─── PROBLEMA C.3 (0.4): Pares que suman K ───────────────────────────────────

def pares_suma_lento(lista, k):
    """
    Retorna todos los pares (i, j) donde lista[i] + lista[j] == k.
    COMPLEJIDAD: O(n²)  ← analiza y escribe
    """
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))
    return pares


def pares_suma_rapido(lista, k):
    """
    Misma funcionalidad usando set para buscar complementos.

    Estrategia:
    - Para cada x, el complemento es k - x
    - Si el complemento ya está en un set de "vistos", es un par

    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    from collections import Counter
    contador = Counter(lista)
    pares = []
    
    for num in contador:
        complemento = k - num
        if complemento in contador:
            if num == complemento:
                # Si el número es su propio complemento, combinar frecuencias
                # Número de pares = C(freq, 2) = freq * (freq - 1) / 2
                freq = contador[num]
                for _ in range(freq * (freq - 1) // 2):
                    pares.append((num, num))
            elif num < complemento:
                # Para evitar duplicados (a,b) y (b,a), solo procesar si num < complemento
                freq_num = contador[num]
                freq_comp = contador[complemento]
                for _ in range(freq_num * freq_comp):
                    pares.append((num, complemento))
    
    return pares


# ─── PROBLEMA C.4 (0.4): Anagramas ───────────────────────────────────────────

def son_anagramas_lento(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas (mismas letras, diferente orden).
    COMPLEJIDAD: O(n log n)  ← analiza y escribe
    """
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1) == sorted(palabra2)


def son_anagramas_rapido(palabra1, palabra2):
    """
    Misma funcionalidad sin ordenar.

    Estrategia: contar frecuencia de cada letra con diccionario.

    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    if len(palabra1) != len(palabra2):
        return False
    contador1 = {}
    contador2 = {}
    for c in palabra1:
        contador1[c] = contador1.get(c, 0) + 1
    for c in palabra2:
        contador2[c] = contador2.get(c, 0) + 1
    return contador1 == contador2


# ─── PROBLEMA C.5 (0.4): Subarray de suma máxima ─────────────────────────────

def max_subarray_lento(lista):
    """
    Encuentra la suma máxima de un subarray contiguo.
    Ejemplo: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (subarray [4, -1, 2, 1])

    COMPLEJIDAD: O(n³)  ← analiza y escribe
    """
    n = len(lista)
    max_suma = lista[0]
    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i, j + 1):
                suma += lista[k]
            max_suma = max(max_suma, suma)
    return max_suma


def max_subarray_rapido(lista):
    """
    Algoritmo de Kadane: un solo recorrido.

    Idea: mantener la suma actual. Si se vuelve negativa, reiniciar.
    - suma_actual = max(x, suma_actual + x)
    - max_suma = max(max_suma, suma_actual)

    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    max_suma = lista[0]
    suma_actual = lista[0]
    for i in range(1, len(lista)):
        suma_actual = max(lista[i], suma_actual + lista[i])
        max_suma = max(max_suma, suma_actual)
    return max_suma


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN D: PROPONER Y JUSTIFICAR (1.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO D.1 (0.5): Diseñar un algoritmo

PROBLEMA: Sistema de autocompletado
Un buscador tiene una lista de 1 millón de palabras. Cuando el usuario
escribe las primeras letras, debe mostrar las 5 palabras que empiezan
con ese prefijo.

Ejemplo:
  palabras = ["python", "programar", "programa", "prueba", "pizza", ...]
  autocompletar("pro") → ["programar", "programa"]

Propón DOS soluciones con diferente complejidad:

SOLUCIÓN 1 (fuerza bruta):
  Descripción: Recorrer todas las palabras y filtrar las que comienzan con el prefijo, 
               luego retornar las primeras 5
  Complejidad: O(n * m) donde n es el número de palabras y m es el largo del prefijo
  Código:
"""


def autocompletar_v1(palabras, prefijo):
    """
    Versión fuerza bruta.
    TODO: Implementar
    COMPLEJIDAD: O(n * m)
    """
    resultado = []
    for palabra in palabras:
        if palabra.startswith(prefijo):
            resultado.append(palabra)
            if len(resultado) >= 5:
                break
    return resultado


"""
SOLUCIÓN 2 (optimizada):
  Descripción: Usar búsqueda binaria para encontrar la primera palabra con el prefijo,
               luego recopilar desde ese punto hasta no encontrar el prefijo o 5 resultados
  Complejidad: O(log n + k) donde n es número de palabras y k es número de resultados
  ¿Qué estructura de datos usarías? Array ordenado + búsqueda binaria, o Trie para mejor eficiencia aún
  Código:
"""


def autocompletar_v2(palabras_ordenadas, prefijo):
    """
    Versión optimizada.
    PISTA: Si las palabras están ordenadas, puedes usar búsqueda binaria
    para encontrar dónde empiezan las que tienen el prefijo.

    TODO: Implementar
    COMPLEJIDAD: O(log n + k)
    """
    import bisect
    
    # Encontrar la posición inicial donde podría estar el prefijo
    inicio = bisect.bisect_left(palabras_ordenadas, prefijo)
    resultado = []
    
    # Recopilar palabras que comienzan con el prefijo
    for i in range(inicio, len(palabras_ordenadas)):
        palabra = palabras_ordenadas[i]
        if palabra.startswith(prefijo):
            resultado.append(palabra)
            if len(resultado) >= 5:
                break
        elif palabra[:len(prefijo)] > prefijo:  # Si ya pasamos el prefijo
            break
    
    return resultado


"""
PUNTO D.2 (0.5): Analizar un sistema real

ESCENARIO: Red social con 10 millones de usuarios.
Cada usuario tiene una lista de amigos (promedio 200 amigos).

Analiza la complejidad de estas operaciones y propón la mejor
estructura de datos para cada una:

1. Verificar si dos usuarios son amigos
   - Con lista de amigos: O(200) = O(1) promedio porque es constante pequeño
   - Con set de amigos: O(1) en promedio
   - ¿Cuál elegirías? Set - mucho más rápido para esta operación

2. Encontrar amigos en común entre dos usuarios
   - Con listas: O(200²) = O(1) porque el tamaño es pequeño pero O(m*n) en general
   - Con sets: O(200) = O(1) promedio porque len(set1) es pequeño
   - ¿Cuál elegirías? Set - operación de intersección con set es más eficiente que nested loop

3. Sugerir "personas que quizás conozcas" (amigos de amigos que no son tus amigos)
   - Describe tu algoritmo: Para cada amigo del usuario, obtener sus amigos. Hacer unión de todos estos conjuntos. Eliminar al usuario y sus amigos actuales.
   - Complejidad estimada: O(200 * 200) = O(1) constante pero sería O(f * a) donde f es amigos y a es amigos prom.
   - ¿Es viable para 10M de usuarios? Sí, porque cada usuario solo procesa 200*200 = 40,000 operaciones, que es constante

4. Si cada usuario tiene en promedio 200 amigos y hay 10M de usuarios:
   - ¿Cuánta memoria ocupa almacenar TODAS las relaciones de amistad?
   - Con lista: 10M * 200 * 8 bytes (referencias) ≈ 16 GB aproximadamente
   - Con set: Similar, 10M * 200 * 8 bytes ≈ 16 GB (el overhead es similar)
   - Nota: En realidad sería menos porque las amistades son bidirecionales (cada arista se cuenta una sola vez en un grafo)
"""


"""
PUNTO D.3 (0.5): Reflexión y comparación

Escribe un párrafo (mínimo 5 líneas) respondiendo:

¿Por qué es importante analizar la complejidad de un algoritmo
ANTES de implementarlo? Da un ejemplo concreto de un caso donde
elegir el algoritmo incorrecto podría causar problemas reales
(tiempo de espera, costos de servidor, mala experiencia de usuario, etc.)

Tu respuesta:
Analizar la complejidad ANTES de implementar es crítico porque previene problemas 
costosos después. Por ejemplo, en un sistema de búsqueda de usuarios en una red social, 
si usas un algoritmo O(n²) para encontrar usuarios similares con 10 millones de usuarios, 
estarías ejecutando 100 billones de operaciones. Esto causaría timeouts de segundos, 
requeriría servidores muy costosos para ejecutarse, y crearía una experiencia terrible 
al usuario. Sin embargo, con un análisis previo, podrías elegir un algoritmo O(n log n) 
que ejecutaría en milisegundos. La diferencia es la viabilidad del proyecto. Por eso es 
fundamental pensar en la complejidad primero: pequeñas decisiones de diseño se amplifican 
exponencialmente con el tamaño real de los datos.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                         CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

def medir(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    return resultado, time.time() - inicio


if __name__ == "__main__":
    print("=" * 70)
    print("     TALLER: ANÁLISIS DE ALGORITMOS - PRUEBAS SECCIÓN C")
    print("=" * 70)

    # ── C.1: Únicos ──────────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.1: ELEMENTOS ÚNICOS")
    print("─" * 70)

    for n in [1000, 5000, 10000]:
        lista = [random.randint(1, n // 2) for _ in range(n)]

        r1, t1 = medir(unicos_lento, lista)
        r2, t2 = medir(unicos_rapido, lista) if unicos_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓ correcto" if r1 == r2 else f"  ✗ DIFERENTE")
        else:
            print("  (sin implementar)")

    # ── C.2: Más común ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.2: ELEMENTO MÁS COMÚN")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 20) for _ in range(n)]

        r1, t1 = medir(mas_comun_lento, lista)
        r2, t2 = medir(mas_comun_rapido, lista) if mas_comun_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓" if r1 == r2 else f"  resultado: {r1} vs {r2}")
        else:
            print("  (sin implementar)")

    # ── C.3: Pares que suman K ───────────────────────────────────
    print("\n" + "─" * 70)
    print("C.3: PARES QUE SUMAN K")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 100) for _ in range(n)]
        k = 50

        r1, t1 = medir(pares_suma_lento, lista, k)
        r2, t2 = medir(pares_suma_rapido, lista, k) if pares_suma_rapido(lista, k) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  pares encontrados: {len(r1)} vs {len(r2)}")
        else:
            print("  (sin implementar)")

    # ── C.4: Anagramas ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.4: ANAGRAMAS")
    print("─" * 70)

    casos_anagramas = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("anagram", "nagaram", True),
        ("python", "typhon", True),
        ("abc", "abcd", False),
    ]

    for p1, p2, esperado in casos_anagramas:
        r_lento = son_anagramas_lento(p1, p2)
        r_rapido = son_anagramas_rapido(p1, p2) if son_anagramas_rapido(p1, p2) is not None else "N/A"
        marca = "✓" if r_rapido == esperado else "✗"
        print(f"  {marca} '{p1}' vs '{p2}': lento={r_lento}, rápido={r_rapido}, esperado={esperado}")

    # ── C.5: Subarray máximo ─────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.5: SUBARRAY DE SUMA MÁXIMA")
    print("─" * 70)

    casos_subarray = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
        [5, -9, 6, -2, 3],
    ]

    for lista in casos_subarray:
        r_lento = max_subarray_lento(lista)
        r_rapido = max_subarray_rapido(lista)
        marca = "✓" if r_rapido == r_lento else "✗"
        print(f"  {marca} {lista} → lento={r_lento}, rápido={r_rapido}")

    for n in [500, 2000, 5000]:
        lista = [random.randint(-50, 50) for _ in range(n)]
        r1, t1 = medir(max_subarray_lento, lista)
        r2, t2 = medir(max_subarray_rapido, lista) if max_subarray_rapido(lista) is not None else (None, 0)
        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s")

    # ── D.1: Autocompletar ───────────────────────────────────────
    print("\n" + "─" * 70)
    print("D.1: AUTOCOMPLETAR")
    print("─" * 70)

    palabras = [f"palabra_{random.randint(1000, 9999)}" for _ in range(50000)]
    palabras.extend(["python", "programar", "programa", "prueba", "pizza",
                      "proyecto", "profesor", "promedio", "proceso", "producir"])
    random.shuffle(palabras)
    palabras_ord = sorted(palabras)

    for prefijo in ["pro", "pyt", "piz", "xyz"]:
        r1, t1 = medir(autocompletar_v1, palabras, prefijo) if autocompletar_v1(palabras, prefijo) is not None else (None, 0)
        r2, t2 = medir(autocompletar_v2, palabras_ord, prefijo) if autocompletar_v2(palabras_ord, prefijo) is not None else (None, 0)

        print(f"  Prefijo '{prefijo}': v1={t1:.4f}s  v2={t2:.4f}s", end="")
        if r1:
            print(f"  → {len(r1)} resultados")
        else:
            print("  (sin implementar)")