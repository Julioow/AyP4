"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL - CONJUNTOS
                    Validador de Sudoku + Sistema de Permisos
═══════════════════════════════════════════════════════════════════════════════

Este ejercicio trabaja principalmente con:

1. Conjuntos de Python usando set()
2. Recorrido de matrices usando filas y columnas
3. Recorrido de listas enlazadas
4. Uso de métodos de una clase
5. Subconjuntos

IDEAS IMPORTANTES PARA EL QUIZ
--------------------------------

Cuando tengas un ejercicio parecido, primero piensa:

- ¿Qué me están pidiendo comprobar?
- ¿Necesito recorrer una fila, una columna o un bloque?
- ¿Necesito recorrer una lista enlazada?
- ¿Tengo algún método que ya haga parte del trabajo?
- ¿Estoy buscando TODOS los elementos o solamente ALGUNO?

No memorices solamente el código. Intenta reconocer estos patrones.
"""


# ═══════════════════════════════════════════════════════════════════════════════
# PARTE 1: VALIDADOR DE SUDOKU
# ═══════════════════════════════════════════════════════════════════════════════

"""
En un Sudoku válido, cada fila, columna y subcuadro 3x3 debe contener
exactamente los números del 1 al 9 sin repetir.

Usamos un conjunto para comprobarlo:

    set(lista) == NUMEROS_VALIDOS

¿Por qué funciona?

Si tenemos:

    [5, 3, 4, 6, 7, 8, 9, 1, 2]

al convertirlo en conjunto obtenemos:

    {1, 2, 3, 4, 5, 6, 7, 8, 9}

Si coincide con NUMEROS_VALIDOS, la fila es válida.

IMPORTANTE:
Un conjunto elimina los elementos repetidos. Por eso también podemos detectar
que falta algún número o que hay un número repetido.
"""

NUMEROS_VALIDOS = {1, 2, 3, 4, 5, 6, 7, 8, 9}


TABLERO = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 1.1 - VALIDAR UNA FILA
# ═══════════════════════════════════════════════════════════════════════════════

def validar_fila(tablero, num_fila):
    """
    Comprueba si una fila contiene exactamente los números del 1 al 9.

    num_fila indica qué fila queremos revisar.

    Ejemplo:

        validar_fila(TABLERO, 0)

    significa:

        "Revisa la fila 0 del tablero."

    PASOS PARA PENSAR ESTE TIPO DE EJERCICIO:
    1. Sacar la fila que nos interesa.
    2. Convertirla en conjunto.
    3. Compararla con los números válidos.
    """

    return set(tablero[num_fila]) == NUMEROS_VALIDOS


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 1.2 - VALIDAR UNA COLUMNA
# ═══════════════════════════════════════════════════════════════════════════════

def validar_columna(tablero, num_columna):
    """
    Comprueba si una columna contiene exactamente los números del 1 al 9.

    IMPORTANTE:

    En una fila podemos hacer directamente:

        tablero[num_fila]

    porque una fila ya está almacenada como una lista.

    Pero para una columna necesitamos recorrer las filas:

        tablero[i][num_columna]

    Aquí:

        i              -> va cambiando la fila
        num_columna    -> indica la columna que queremos mantener

    Por ejemplo, si num_columna = 2:

        tablero[0][2]
        tablero[1][2]
        tablero[2][2]
        ...

    Así obtenemos todos los elementos de la columna 2.
    """

    columna = []

    # Recorremos las 9 filas del tablero.
    for i in range(9):

        # Tomamos el elemento de la fila i y de la columna indicada.
        columna.append(tablero[i][num_columna])

    # Comparamos los elementos encontrados con los números válidos.
    return set(columna) == NUMEROS_VALIDOS


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 1.3 - VALIDAR UN SUBCUADRO 3x3
# ═══════════════════════════════════════════════════════════════════════════════

def validar_subcuadro(tablero, fila_inicio, col_inicio):
    """
    Comprueba si un subcuadro 3x3 contiene exactamente los números del 1 al 9.

    fila_inicio y col_inicio indican dónde comienza el subcuadro.

    Los posibles valores son:

        0, 3, 6

    Por ejemplo:

        fila_inicio = 3
        col_inicio = 6

    significa que comenzamos en:

        fila 3
        columna 6

    Como el subcuadro mide 3x3, necesitamos recorrer:

        filas:    3, 4, 5
        columnas: 6, 7, 8

    Por eso usamos:

        range(fila_inicio, fila_inicio + 3)
        range(col_inicio, col_inicio + 3)

    IMPORTANTE:
    Necesitamos dos for porque tenemos que recorrer filas Y columnas.
    """

    subcuadro = []

    # Recorremos las 3 filas del subcuadro.
    for i in range(fila_inicio, fila_inicio + 3):

        # Dentro de cada fila recorremos las 3 columnas.
        for j in range(col_inicio, col_inicio + 3):

            # Guardamos el elemento ubicado en fila i, columna j.
            subcuadro.append(tablero[i][j])

    # Verificamos si los 9 elementos son exactamente los números válidos.
    return set(subcuadro) == NUMEROS_VALIDOS


# ═══════════════════════════════════════════════════════════════════════════════
# PARTE 2: SISTEMA DE PERMISOS CON LISTAS ENLAZADAS
# ═══════════════════════════════════════════════════════════════════════════════

"""
Ahora trabajamos con una clase Conjunto construida mediante nodos.

Esto es diferente de un set() normal de Python.

La estructura es aproximadamente:

    cabeza
      ↓
    [dato] → [dato] → [dato] → None

Para recorrerla usamos:

    actual = conjunto.cabeza

y luego:

    actual = actual.siguiente

La clase ya nos proporciona el método:

    pertenece(x)

que nos permite preguntar si un elemento está dentro del conjunto.

Por eso NO necesitamos programar nuevamente la búsqueda.
"""


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO BASE
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0

        if elementos:
            for e in elementos:
                self.agregar(e)

    def esta_vacio(self):
        return self.cabeza is None

    def pertenece(self, x):
        """
        Retorna True si x está en el conjunto.
        """

        actual = self.cabeza

        while actual:

            if actual.dato == x:
                return True

            actual = actual.siguiente

        return False

    def agregar(self, x):
        """
        Agrega x solamente si todavía no existe.
        """

        if self.pertenece(x):
            return False

        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1

        return True

    def __str__(self):
        elementos = []

        actual = self.cabeza

        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente

        return "{" + ", ".join(elementos) + "}"


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 2.1 - VERIFICAR SI ES SUBCONJUNTO
# ═══════════════════════════════════════════════════════════════════════════════

def es_subconjunto(conjunto_a, conjunto_b):
    """
    Retorna True si TODOS los elementos de A están en B.

    La idea matemática es:

        A ⊆ B

    Lo podemos traducir a una pregunta:

        "¿Cada elemento de A también pertenece a B?"

    PASOS PARA RESOLVERLO:

    1. Comenzamos en la cabeza de A.
    2. Recorremos todos sus nodos.
    3. Tomamos el dato del nodo actual.
    4. Preguntamos si ese dato pertenece a B.
    5. Si encontramos uno que NO pertenece, retornamos False.
    6. Si terminamos de recorrer A sin encontrar problemas,
       retornamos True.

    IMPORTANTE:

    Aquí buscamos si TODOS cumplen la condición.

    Por eso NO podemos retornar True cuando encontramos el primer
    elemento correcto, porque todavía faltan elementos por revisar.
    """

    # Comenzamos en el primer nodo de A.
    actual = conjunto_a.cabeza

    # Recorremos todos los nodos de A.
    while actual:

        # Si el elemento actual de A NO está en B,
        # entonces A no puede ser subconjunto de B.
        if not conjunto_b.pertenece(actual.dato):
            return False

        # Pasamos al siguiente nodo.
        actual = actual.siguiente

    # Llegamos hasta el final y todos los elementos estaban en B.
    return True


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 2.2 - VERIFICAR PERMISOS
# ═══════════════════════════════════════════════════════════════════════════════

def tiene_permisos(permisos_usuario, permisos_requeridos):
    """
    Retorna True si el usuario tiene TODOS los permisos requeridos.

    La pregunta realmente es:

        "¿Todos los permisos requeridos están dentro de los
         permisos que tiene el usuario?"

    Por lo tanto:

        permisos_requeridos ⊆ permisos_usuario

    IMPORTANTE:
    El orden de los parámetros importa.

    NO queremos preguntar:

        permisos_usuario ⊆ permisos_requeridos

    porque el usuario puede tener permisos adicionales y eso está bien.

    Ejemplo:

        usuario:
            {leer, escribir, eliminar}

        requeridos:
            {leer, escribir}

        Los requeridos están dentro de los permisos del usuario,
        así que el resultado es True.
    """

    return es_subconjunto(permisos_requeridos, permisos_usuario)


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    print("=" * 60)
    print("PARTE 1: VALIDADOR DE SUDOKU")
    print("=" * 60)

    # ─────────────────────────────────────────────────────────────────────────
    # Probar filas
    # ─────────────────────────────────────────────────────────────────────────

    print("\nValidando filas:")

    for i in range(9):
        resultado = validar_fila(TABLERO, i)

        print(f"  Fila {i + 1}: {'✓' if resultado else '✗'}")


    # ─────────────────────────────────────────────────────────────────────────
    # Probar columnas
    # ─────────────────────────────────────────────────────────────────────────

    print("\nValidando columnas:")

    for j in range(9):
        resultado = validar_columna(TABLERO, j)

        print(f"  Columna {j + 1}: {'✓' if resultado else '✗'}")


    # ─────────────────────────────────────────────────────────────────────────
    # Probar subcuadros
    # ─────────────────────────────────────────────────────────────────────────

    print("\nValidando subcuadros 3x3:")

    for fi in [0, 3, 6]:
        for ci in [0, 3, 6]:

            resultado = validar_subcuadro(TABLERO, fi, ci)

            print(
                f"  Subcuadro ({fi + 1},{ci + 1}): "
                f"{'✓' if resultado else '✗'}"
            )


    print("\n" + "=" * 60)
    print("PARTE 2: SISTEMA DE PERMISOS")
    print("=" * 60)


    # ─────────────────────────────────────────────────────────────────────────
    # Definir roles
    # ─────────────────────────────────────────────────────────────────────────

    admin = Conjunto([
        "leer",
        "escribir",
        "eliminar",
        "crear_usuarios"
    ])

    editor = Conjunto([
        "leer",
        "escribir"
    ])

    viewer = Conjunto([
        "leer"
    ])


    print("\nRoles definidos:")
    print(f"  Admin: {admin}")
    print(f"  Editor: {editor}")
    print(f"  Viewer: {viewer}")


    # ─────────────────────────────────────────────────────────────────────────
    # Probar subconjuntos
    # ─────────────────────────────────────────────────────────────────────────

    print("\nVerificando subconjuntos:")

    print(
        f"  ¿Viewer ⊆ Editor? "
        f"{es_subconjunto(viewer, editor)}"
    )

    print(
        f"  ¿Editor ⊆ Admin? "
        f"{es_subconjunto(editor, admin)}"
    )

    print(
        f"  ¿Admin ⊆ Editor? "
        f"{es_subconjunto(admin, editor)}"
    )


    # ─────────────────────────────────────────────────────────────────────────
    # Probar permisos
    # ─────────────────────────────────────────────────────────────────────────

    accion_editar = Conjunto([
        "leer",
        "escribir"
    ])

    accion_admin = Conjunto([
        "crear_usuarios",
        "eliminar"
    ])


    print("\nVerificando permisos:")

    print(f"  Acción editar requiere: {accion_editar}")
    print(f"  Acción admin requiere: {accion_admin}")


    print(
        f"\n  ¿Editor puede editar? "
        f"{tiene_permisos(editor, accion_editar)}"
    )

    print(
        f"  ¿Viewer puede editar? "
        f"{tiene_permisos(viewer, accion_editar)}"
    )

    print(
        f"  ¿Admin puede hacer acción admin? "
        f"{tiene_permisos(admin, accion_admin)}"
    )

    print(
        f"  ¿Editor puede hacer acción admin? "
        f"{tiene_permisos(editor, accion_admin)}"
    )


"""
═══════════════════════════════════════════════════════════════════════════════
                         GUÍA RÁPIDA PARA EL QUIZ
═══════════════════════════════════════════════════════════════════════════════

1. FILA
───────────────────────────────────────────────────────────────────────────────

Si te piden revisar una fila:

    tablero[num_fila]

Y si quieren comprobar que contiene exactamente ciertos valores:

    set(tablero[num_fila]) == NUMEROS_VALIDOS


2. COLUMNA
───────────────────────────────────────────────────────────────────────────────

Una columna requiere recorrer las filas:

    columna = []

    for i in range(9):
        columna.append(tablero[i][num_columna])

    return set(columna) == NUMEROS_VALIDOS


3. SUBCUADRO
───────────────────────────────────────────────────────────────────────────────

Un bloque 3x3 necesita dos recorridos:

    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(col_inicio, col_inicio + 3):
            subcuadro.append(tablero[i][j])


4. RECORRER UN CONJUNTO ENLAZADO
───────────────────────────────────────────────────────────────────────────────

    actual = conjunto.cabeza

    while actual != None:
        # trabajar con actual.dato

        actual = actual.siguiente


5. SABER SI UN ELEMENTO PERTENECE
───────────────────────────────────────────────────────────────────────────────

La clase ya tiene:

    conjunto.pertenece(elemento)


No necesitas volver a programar la búsqueda.


6. SUBCONJUNTO
───────────────────────────────────────────────────────────────────────────────

La pregunta:

    "¿TODOS los elementos de A están en B?"

se convierte en:

    es_subconjunto(A, B)


La lógica es:

    recorrer A
        ↓
    si uno NO está en B
        ↓
    False

    si terminamos todo A
        ↓
    True


7. ELEMENTOS COMUNES
───────────────────────────────────────────────────────────────────────────────

Si preguntan:

    "¿Hay AL MENOS UNO que esté en ambos?"

se puede recorrer A y preguntar:

    conjunto_b.pertenece(actual.dato)

Si encontramos uno:

    return True

Si terminamos todo A sin encontrar ninguno:

    return False


8. CONTAR ELEMENTOS COMUNES
───────────────────────────────────────────────────────────────────────────────

Si preguntan:

    "¿Cuántos elementos de A están también en B?"

usamos:

    contador = 0

    recorrer A:

        si pertenece a B:
            contador += 1

    return contador


9. PERMISOS
───────────────────────────────────────────────────────────────────────────────

Si preguntan:

    "¿El usuario tiene TODOS los permisos necesarios?"

piensa:

    permisos_requeridos ⊆ permisos_usuario

Por lo tanto:

    es_subconjunto(permisos_requeridos, permisos_usuario)


═══════════════════════════════════════════════════════════════════════════════
                           IDEA PRINCIPAL
═══════════════════════════════════════════════════════════════════════════════

Antes de escribir código, identifica qué palabra describe el problema:

    "TODOS"          → probablemente necesitas comprobar un subconjunto.

    "AL MENOS UNO"   → probablemente necesitas buscar hasta encontrar uno.

    "CUÁNTOS"        → probablemente necesitas un contador.

    "COLUMNA"        → probablemente necesitas recorrer las filas.

    "SUBCUADRO 3x3"  → necesitas dos for.

    "CONJUNTO"       → revisa si tienes métodos como pertenece().

    "LISTA ENLAZADA" → piensa en cabeza, actual y siguiente.

No memorices solamente las soluciones.
Primero identifica qué te está preguntando el ejercicio.
"""