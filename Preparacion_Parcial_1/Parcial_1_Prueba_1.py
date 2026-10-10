import re


# ============================================================
# PUNTO 1 (20%): EXPRESIONES REGULARES
# ============================================================

"""
En este punto trabajamos con expresiones regulares.

re.match() permite comprobar si un texto coincide con un patrón
desde el principio.

re.findall() permite encontrar todas las coincidencias de un patrón.
"""


# ------------------------------------------------------------
# 1.1 Validar correo institucional
# ------------------------------------------------------------

def validar_correo_institucional(correo):
    """
    Comprueba que el correo tenga el formato:
        nombre.apellido@elpoli.edu.co

    Reglas:
    - nombre: mínimo 2 letras minúsculas.
    - apellido: mínimo 2 letras minúsculas.
    - Deben estar separados por un punto.
    - El dominio debe ser exactamente @elpoli.edu.co.
    """

    # ^ significa comienzo del texto.
    # [a-z] acepta letras minúsculas.
    # {2,} exige al menos 2 letras.
    # \. representa un punto literal.
    # $ significa final del texto.
    patron = r"^[a-z]{2,}\.[a-z]{2,}@elpoli\.edu\.co$"

    resultado = re.match(patron, correo)

    # re.match devuelve una coincidencia si funciona,
    # o None si el texto no cumple el patrón.
    # Por eso convertimos el resultado en True o False.
    return resultado is not None


# ------------------------------------------------------------
# 1.2 Extraer menciones de un texto
# ------------------------------------------------------------

def extraer_menciones(texto):
    """
    Extrae menciones que comienzan con @ y contienen:
    - Letras mayúsculas o minúsculas.
    - Números.
    - Guion bajo.

    Ejemplo:
    "Hola @juan_dev y @maria99" -> ["@juan_dev", "@maria99"]
    """

    patron = r"@[a-zA-Z0-9_]+"

    # findall devuelve una lista con todas las coincidencias.
    menciones = re.findall(patron, texto)

    return menciones


# ============================================================
# PUNTO 2 (30%): LISTAS ENLAZADAS Y RECURSIVIDAD
# ============================================================

"""
Una lista enlazada está formada por nodos.

Cada nodo tiene:
- Sus datos.
- Un enlace al siguiente nodo.

La cabeza (self.cabeza) apunta al primer nodo.
Si la lista está vacía, self.cabeza es None.
"""


# ------------------------------------------------------------
# Clase Paciente
# ------------------------------------------------------------

class Paciente:

    def __init__(self, nombre, edad, urgencia, atendido=False):
        self.nombre = nombre
        self.edad = edad
        self.urgencia = urgencia
        self.atendido = atendido
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.atendido else "○"

        return (
            f"[{estado}] {self.nombre} "
            f"(edad:{self.edad}) - Urgencia:{self.urgencia}"
        )


# ------------------------------------------------------------
# Clase ListaPacientes
# ------------------------------------------------------------

class ListaPacientes:

    def __init__(self):
        self.cabeza = None

    # --------------------------------------------------------
    # Método para mostrar la lista
    # --------------------------------------------------------

    def mostrar(self):
        actual = self.cabeza

        if actual is None:
            print("Sin pacientes")
            return

        # Aquí usamos un recorrido con while, no recursividad.
        while actual:
            print(actual)
            actual = actual.siguiente

    # --------------------------------------------------------
    # 2.1 Agregar pacientes por nivel de urgencia
    # --------------------------------------------------------

    def agregar(self, nombre, edad, urgencia):
        """
        Inserta al paciente de mayor a menor urgencia.

        Si dos pacientes tienen la misma urgencia, el nuevo
        se coloca después de los que ya tenían esa urgencia.
        """

        # Crear el nuevo nodo.
        nuevo = Paciente(nombre, edad, urgencia)

        # CASO 1: la lista está vacía.
        if self.cabeza is None:
            self.cabeza = nuevo
            return

        # CASO 2: el nuevo paciente debe ir al principio.
        if nuevo.urgencia > self.cabeza.urgencia:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        # CASO 3: buscar la posición usando recursividad.
        self.agregar_recursivo(self.cabeza, nuevo)

    def agregar_recursivo(self, actual, nuevo):
        """
        Método auxiliar recursivo.

        actual: nodo donde estamos.
        nuevo: paciente que queremos insertar.
        """

        # Si llegamos al final, o el nuevo tiene más urgencia
        # que el siguiente, encontramos la posición correcta.
        if (
            actual.siguiente is None
            or nuevo.urgencia > actual.siguiente.urgencia
        ):
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            return

        # Si todavía no encontramos la posición, avanzamos.
        self.agregar_recursivo(actual.siguiente, nuevo)

    # --------------------------------------------------------
    # 2.2 Contar pacientes críticos que no han sido atendidos
    # --------------------------------------------------------

    def contar_criticos(self):
        """
        Inicia el conteo desde la cabeza de la lista.
        """

        return self.contar_criticos_recursivo(self.cabeza)

    def contar_criticos_recursivo(self, actual):
        """
        Cuenta los pacientes con urgencia >= 4 que no han
        sido atendidos.
        """

        # CASO BASE: se acabaron los nodos.
        if actual is None:
            return 0

        contador = 0

        # Las dos condiciones deben cumplirse.
        if actual.urgencia >= 4 and not actual.atendido:
            contador = 1

        # Sumamos lo del paciente actual al resto de la lista.
        return contador + self.contar_criticos_recursivo(
            actual.siguiente
        )

    # --------------------------------------------------------
    # 2.3 Filtrar pacientes por edad mínima
    # --------------------------------------------------------

    def filtrar_mayores(self, edad_minima):
        """
        Devuelve una NUEVA lista con pacientes cuya edad
        sea mayor o igual a edad_minima.

        La lista original no se modifica.
        """

        # Creamos una lista vacía para guardar los resultados.
        nueva_lista = ListaPacientes()

        # Empezamos a recorrer la lista original.
        self.filtrar_mayores_recursivo(
            self.cabeza,
            edad_minima,
            nueva_lista
        )

        # Devolvemos la nueva lista completa.
        return nueva_lista

    def filtrar_mayores_recursivo(
        self, actual, edad_minima, nueva_lista
    ):
        """
        Recorre la lista original y copia a la nueva lista
        los pacientes que cumplen la edad mínima.
        """

        # CASO BASE: ya no quedan pacientes.
        if actual is None:
            return

        # Si cumple la condición, lo agregamos a la nueva lista.
        if actual.edad >= edad_minima:
            nueva_lista.agregar(
                actual.nombre,
                actual.edad,
                actual.urgencia
            )

        # Continuamos con el siguiente paciente.
        self.filtrar_mayores_recursivo(
            actual.siguiente,
            edad_minima,
            nueva_lista
        )


# ============================================================
# PUNTO 3 (20%): OPERACIONES CON CONJUNTOS
# ============================================================

"""
Un conjunto guarda elementos sin repetir.

Operadores importantes:
&  -> intersección: elementos compartidos.
|  -> unión: elementos de ambos conjuntos.
-  -> diferencia: elementos del primero que no están en el segundo.

En este punto las funciones deben RETORNAR sus resultados.
No necesitan imprimirlos dentro de la función.
"""


peliculas_juan = {
    "Inception", "Matrix", "Interstellar", "Avengers", "Dune"
}

peliculas_maria = {
    "Matrix", "Avengers", "Titanic", "Dune", "Coco"
}

peliculas_pedro = {
    "Inception", "Titanic", "Coco", "Matrix", "Parasite"
}


# ------------------------------------------------------------
# 3.1 Películas que los tres han visto
# ------------------------------------------------------------

def peliculas_en_comun():
    """
    Retorna un conjunto con las películas presentes
    en los tres conjuntos.
    """

    return peliculas_juan & peliculas_maria & peliculas_pedro


# ------------------------------------------------------------
# 3.2 Recomendar películas a Juan
# ------------------------------------------------------------

def recomendar_a_juan():
    """
    Retorna películas que María o Pedro han visto,
    pero Juan todavía no ha visto.
    """

    # Primero unimos las películas de María y Pedro.
    # Después quitamos las películas que Juan ya vio.
    return (peliculas_maria | peliculas_pedro) - peliculas_juan


# ------------------------------------------------------------
# 3.3 Películas exclusivas de cada persona
# ------------------------------------------------------------

def exclusivas_de_cada_uno():
    """
    Retorna un diccionario.

    Cada clave es el nombre de una persona.
    Cada valor es un conjunto con sus películas exclusivas.
    """

    return {
        "Juan": (
            peliculas_juan - peliculas_maria - peliculas_pedro
        ),

        "Maria": (
            peliculas_maria - peliculas_juan - peliculas_pedro
        ),

        "Pedro": (
            peliculas_pedro - peliculas_juan - peliculas_maria
        )
    }


# ============================================================
# PUNTO 4 (30%): RECURSIVIDAD Y MEMORIZACIÓN
# ============================================================

"""
El objetivo es calcular la cantidad de caminos en una cuadrícula.

Solo se puede avanzar:
- Hacia la derecha.
- Hacia abajo.

En este ejercicio, m y n representan las dimensiones
de la cuadrícula.

CASO BASE:
Si m == 1 o n == 1, solo existe un camino.
"""


# ------------------------------------------------------------
# 4.1 Caminos usando recursividad normal
# ------------------------------------------------------------

def caminos_sin_memo(m, n):
    """
    Calcula el número de caminos usando recursividad normal.

    No guarda resultados anteriores, por lo que puede repetir
    los mismos cálculos varias veces.
    """

    # CASO BASE:
    # Si hay una sola fila o una sola columna,
    # solo existe un camino posible.
    if m == 1 or n == 1:
        return 1

    # Dividimos el problema en dos problemas más pequeños.
    # Sumamos sus resultados para obtener el total.
    return (
        caminos_sin_memo(m - 1, n)
        + caminos_sin_memo(m, n - 1)
    )


# ------------------------------------------------------------
# 4.2 Caminos usando recursividad con memorización
# ------------------------------------------------------------

def caminos_con_memo(m, n, memo=None):
    """
    Calcula los caminos guardando resultados anteriores.

    memo es un diccionario que almacena resultados para
    determinadas dimensiones de la cuadrícula.

    Por ejemplo:
        memo[(3, 3)] = 6

    significa que una cuadrícula de dimensiones 3 x 3
    tiene 6 caminos según este modelo.
    """

    # Si no recibimos un diccionario, creamos uno vacío.
    if memo is None:
        memo = {}

    # Si el resultado ya está guardado, lo reutilizamos.
    if (m, n) in memo:
        return memo[(m, n)]

    # CASO BASE:
    # Solo hay un camino si una dimensión vale 1.
    if m == 1 or n == 1:
        return 1

    # Calculamos los caminos y guardamos el resultado.
    memo[(m, n)] = (
        caminos_con_memo(m - 1, n, memo)
        + caminos_con_memo(m, n - 1, memo)
    )

    # Devolvemos el resultado guardado.
    return memo[(m, n)]


# ============================================================
# NOTAS IMPORTANTES: RETURN, PRINT, CONJUNTOS Y DICCIONARIOS
# ============================================================

"""
1. SI EL PROFESOR PIDE RETORNAR UN CONJUNTO:

    def peliculas_en_comun():
        return peliculas_juan & peliculas_maria & peliculas_pedro

La función entrega el conjunto a quien la llame.


2. SI EL PROFESOR PIDE MOSTRAR EL RESULTADO:

    print(peliculas_en_comun())

No es necesario agregar print dentro de la función.


3. SI QUIERES GUARDAR EL RESULTADO:

    resultado = peliculas_en_comun()

    print(resultado)

Así puedes usar el resultado más adelante.


4. SI EL PROFESOR PIDE RETORNAR UN DICCIONARIO:

    def ejemplo():
        return {
            "Ana": {"Ciencias", "Arte"},
            "Luis": {"Deportes"}
        }

Las claves son los nombres y los valores son conjuntos.


5. SI EL PROFESOR PIDE MOSTRAR EL DICCIONARIO:

    print(ejemplo())

La función retorna el diccionario y print lo muestra.


6. DIFERENCIA ENTRE ESTRUCTURAS:

    {"Ana", "Luis"}             -> conjunto
    ["Ana", "Luis"]             -> lista
    ("Ana", "Luis")             -> tupla
    {"Ana": 17, "Luis": 20}     -> diccionario
    set()                       -> conjunto vacío
    {}                          -> diccionario vacío


7. EN RECURSIVIDAD:

    - El caso base detiene las llamadas.
    - La llamada recursiva resuelve una parte más pequeña.
    - Debe existir una forma de llegar al caso base.


8. EN MEMORIZACIÓN:

    - memo es un diccionario.
    - La clave (m, n) identifica un problema.
    - Si ya existe la clave, reutilizamos el resultado.
    - Si no existe, calculamos y guardamos el resultado.
"""


# ============================================================
# PRUEBAS DE LOS EJERCICIOS
# ============================================================

if __name__ == "__main__":

    print("=" * 55)
    print("PUNTO 1: EXPRESIONES REGULARES")
    print("=" * 55)

    print(
        validar_correo_institucional("ana.lopez@elpoli.edu.co")
    )

    print(
        extraer_menciones(
            "Hola @juan_dev y @maria99, miren esto @python"
        )
    )

    print("\n" + "=" * 55)
    print("PUNTO 2: LISTAS ENLAZADAS")
    print("=" * 55)

    pacientes = ListaPacientes()

    pacientes.agregar("Ana", 17, 3)
    pacientes.agregar("Luis", 20, 5)
    pacientes.agregar("Sara", 16, 4)
    pacientes.agregar("Carlos", 65, 4,)

    print("\nLista de pacientes por urgencia:")
    pacientes.mostrar()

    print(
        "\nPacientes críticos sin atender:",
        pacientes.contar_criticos()
    )

    mayores = pacientes.filtrar_mayores(18)

    print("\nPacientes de 18 años o más:")
    mayores.mostrar()

    print("\n" + "=" * 55)
    print("PUNTO 3: CONJUNTOS")
    print("=" * 55)

    # Ejemplo de RETORNAR y después MOSTRAR el conjunto.
    print("Películas en común:", peliculas_en_comun())

    print("Recomendaciones para Juan:", recomendar_a_juan())

    print("Películas exclusivas:", exclusivas_de_cada_uno())

    print("\n" + "=" * 55)
    print("PUNTO 4: CAMINOS EN UNA CUADRÍCULA")
    print("=" * 55)

    print("Caminos sin memo para 3 x 3:", caminos_sin_memo(3, 3))
    print("Caminos con memo para 3 x 3:", caminos_con_memo(3, 3))

    print("Caminos con memo para 4 x 4:", caminos_con_memo(4, 4))
    print("Caminos con memo para 10 x 10:", caminos_con_memo(10, 10))
    print("Caminos con memo para 15 x 15:", caminos_con_memo(15, 15))