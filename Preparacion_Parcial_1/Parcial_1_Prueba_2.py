import re


# ============================================================
# PUNTO 1: EXPRESIONES REGULARES
# ============================================================

"""
En este punto trabajamos con expresiones regulares.

re.match() permite comprobar si un texto coincide con un patrón
desde el principio.

re.findall() permite encontrar todas las coincidencias de un patrón
y devolverlas en una lista.

Cuando nos piden VALIDAR algo, normalmente devolvemos True o False.

Cuando nos piden EXTRAER coincidencias, normalmente devolvemos una lista.
"""


# ------------------------------------------------------------
# 1.1 Validar placas de vehículos
# ------------------------------------------------------------

def validar_placa_vehiculo(placa):
    """
    Comprueba que la placa tenga el formato:

        ABC123
        ABC-123

    Reglas:
    - Exactamente 3 letras mayúsculas.
    - El guion es opcional.
    - Exactamente 3 números.
    - No debe haber caracteres adicionales.
    """

    # ^ significa comienzo del texto.
    # [A-Z] acepta letras mayúsculas de la A a la Z.
    # {3} exige exactamente 3 letras.
    # -? permite cero o un guion.
    # \d{3} exige exactamente 3 números.
    # $ significa final del texto.
    patron = r"^[A-Z]{3}-?\d{3}$"

    resultado = re.match(patron, placa)

    # Si encuentra una coincidencia, devuelve True.
    # Si no encuentra una coincidencia, devuelve False.
    return resultado is not None


# Pruebas
print("=== PUNTO 1: Validación de Placas ===")

print(f"ABC123: {validar_placa_vehiculo('ABC123')}")       # True
print(f"ABC-123: {validar_placa_vehiculo('ABC-123')}")     # True
print(f"AB1234: {validar_placa_vehiculo('AB1234')}")       # False
print(f"abc123: {validar_placa_vehiculo('abc123')}")       # False
print(f"ABCD123: {validar_placa_vehiculo('ABCD123')}")     # False
print(f"ABC-12: {validar_placa_vehiculo('ABC-12')}")       # False
print()


# ------------------------------------------------------------
# EJERCICIO EXTRA: EXTRAER HASHTAGS
# ------------------------------------------------------------

def extraer_hashtags(texto):
    """
    Extrae todos los hashtags de un texto.

    Ejemplo:
        "Hola #python y #genial"

    Resultado:
        ['#python', '#genial']
    """

    # # busca el símbolo del hashtag.
    # \w+ busca uno o más caracteres de palabra:
    # letras, números o guion bajo.
    patron = r"#\w+"

    # findall devuelve una lista con todas las coincidencias.
    return re.findall(patron, texto)


texto = "Hola #python es #genial y #100dias"

print("=== HASHTAGS ===")
print(f"Texto: {texto}")
print(f"Hashtags: {extraer_hashtags(texto)}")
print()


# ============================================================
# PUNTO 2: LISTAS ENLAZADAS Y RECURSIVIDAD
# ============================================================

"""
Una lista enlazada está formada por nodos.

Cada nodo tiene sus datos y una referencia al siguiente nodo.

La cabeza (self.cabeza) apunta al primer nodo.

Si la lista está vacía:
    self.cabeza = None

La estructura se ve así:

    cabeza
      |
      v
    [Pedido] -> [Pedido] -> [Pedido] -> None

None significa que no hay otro nodo después del actual.

Para recorrer la lista usamos:

    actual = self.cabeza

Y para avanzar:

    actual = actual.siguiente

Cuando el enunciado exige recursividad, podemos utilizar un método
auxiliar que reciba el nodo actual y continúe desde allí.
"""


# ------------------------------------------------------------
# Clase Pedido
# ------------------------------------------------------------

class Pedido:

    def __init__(self, cliente, direccion, valor, entregado=False):
        # Datos del pedido.
        self.cliente = cliente
        self.direccion = direccion
        self.valor = valor
        self.entregado = entregado

        # Al crear el pedido, todavía no apunta a otro nodo.
        self.siguiente = None

    def __str__(self):
        """
        Define cómo se muestra el pedido cuando usamos print().
        """

        estado = "✓" if self.entregado else "○"

        return (
            f"[{estado}] {self.cliente} "
            f"- ${self.valor:,} - {self.direccion}"
        )


# ------------------------------------------------------------
# Clase ListaPedidos
# ------------------------------------------------------------

class ListaPedidos:

    def __init__(self):
        # Al principio no hay pedidos.
        self.cabeza = None

    # --------------------------------------------------------
    # Mostrar los pedidos
    # --------------------------------------------------------

    def mostrar(self):
        """
        Muestra todos los pedidos.

        Este método utiliza while porque el enunciado no exige
        que mostrar los pedidos se haga recursivamente.
        """

        actual = self.cabeza

        # Si la lista está vacía, mostramos un mensaje y terminamos.
        if actual is None:
            print("  Sin pedidos")
            return

        # Recorremos todos los nodos.
        while actual:
            print(f"  {actual}")

            # Avanzamos al siguiente pedido.
            actual = actual.siguiente

    # --------------------------------------------------------
    # 2.1 Agregar un pedido al final
    # --------------------------------------------------------

    def agregar(self, cliente, direccion, valor):
        """
        Agrega un pedido al FINAL de la lista.

        Se exige utilizar recursividad.

        Primero creamos el nuevo pedido.

        Si la lista está vacía, el nuevo pedido se convierte
        en la cabeza.

        Si ya hay pedidos, buscamos el último nodo mediante
        el método auxiliar recursivo.
        """

        nuevo_pedido = Pedido(cliente, direccion, valor)

        # CASO 1: la lista está vacía.
        if self.cabeza is None:
            self.cabeza = nuevo_pedido

        # CASO 2: la lista ya tiene elementos.
        else:
            self._agregar_recursivo(self.cabeza, nuevo_pedido)

    def _agregar_recursivo(self, actual, nuevo):
        """
        Busca recursivamente el último nodo.

        actual: nodo que estamos revisando.
        nuevo: pedido que queremos agregar.

        CASO BASE:
            Si actual.siguiente es None, llegamos al último nodo.

        CASO RECURSIVO:
            Si no estamos al final, avanzamos al siguiente nodo.
        """

        if actual.siguiente is None:
            # Encontramos el último pedido.
            # Conectamos el nuevo pedido después de él.
            actual.siguiente = nuevo

        else:
            # Todavía quedan nodos por revisar.
            # Llamamos al método con el siguiente nodo.
            self._agregar_recursivo(actual.siguiente, nuevo)

    # --------------------------------------------------------
    # 2.2 Sumar el valor de los pedidos pendientes
    # --------------------------------------------------------

    def valor_pendiente(self):
        """
        Retorna la suma de los valores de los pedidos NO entregados.

        Iniciamos el recorrido desde la cabeza.

        Como necesitamos obtener una suma, usamos return.
        """

        return self._valor_pendiente_recursivo(self.cabeza)

    def _valor_pendiente_recursivo(self, actual):
        """
        Suma los valores pendientes utilizando recursividad.

        CASO BASE:
            Si actual es None, no quedan pedidos.
            La suma de los pedidos restantes es 0.

        CASO RECURSIVO:
            Si el pedido está entregado, aporta 0.
            Si no está entregado, aporta su valor.

            Después sumamos el resultado de revisar el siguiente nodo.
        """

        # CASO BASE: llegamos al final.
        if actual is None:
            return 0

        # Si el pedido ya fue entregado, no cuenta como pendiente.
        if actual.entregado:
            valor_actual = 0

        # Si no está entregado, sumamos su valor.
        else:
            valor_actual = actual.valor

        # Sumamos el valor del pedido actual con el resultado
        # de revisar el resto de la lista.
        return valor_actual + self._valor_pendiente_recursivo(
            actual.siguiente
        )

    # --------------------------------------------------------
    # 2.3 Eliminar los pedidos entregados
    # --------------------------------------------------------

    def eliminar_entregados(self):
        """
        Elimina todos los pedidos que ya fueron entregados.

        IMPORTANTE:
            Este método MODIFICA la lista original.

        Actualizamos self.cabeza con el resultado de la recursión
        porque el primer pedido también podría estar entregado.
        """

        self.cabeza = self._eliminar_entregados_recursivo(
            self.cabeza
        )

    def _eliminar_entregados_recursivo(self, actual):
        """
        Revisa los nodos y conserva solamente los pedidos pendientes.

        CASO BASE:
            Si actual es None, llegamos al final.
            Retornamos None.

        SI EL PEDIDO ESTÁ ENTREGADO:
            No conservamos el nodo actual.
            Continuamos revisando el siguiente.

        SI EL PEDIDO NO ESTÁ ENTREGADO:
            Conservamos el nodo actual y conectamos su siguiente
            con el resultado de revisar el resto de la lista.
        """

        # CASO BASE: no quedan nodos.
        if actual is None:
            return None

        # Si el pedido está entregado, lo saltamos.
        if actual.entregado:

            # Devolvemos el resultado de revisar el siguiente nodo.
            return self._eliminar_entregados_recursivo(
                actual.siguiente
            )

        else:
            # El pedido está pendiente y debemos conservarlo.
            #
            # Revisamos el resto de la lista y actualizamos su enlace.
            actual.siguiente = self._eliminar_entregados_recursivo(
                actual.siguiente
            )

            # Devolvemos el nodo actual para conservarlo en la lista.
            return actual


print("=== PUNTO 2: Sistema de Pedidos ===")

lista = ListaPedidos()

lista.agregar("Juan", "Calle 10 #5-20", 25000)
lista.agregar("Maria", "Carrera 15 #8-30", 30000)
lista.agregar("Carlos", "Avenida 20 #10-50", 15000)

print("Pedidos iniciales:")
lista.mostrar()

print(f"\nValor pendiente: ${lista.valor_pendiente():,}")

# Marcamos el segundo y el tercer pedido como entregados.
lista.cabeza.siguiente.entregado = True
lista.cabeza.siguiente.siguiente.entregado = True

print("\nDespués de marcar algunos como entregados:")
lista.mostrar()

print(f"\nValor pendiente: ${lista.valor_pendiente():,}")

# Eliminamos de la lista los pedidos entregados.
lista.eliminar_entregados()

print("\nDespués de eliminar entregados:")
lista.mostrar()
print()


# ============================================================
# PUNTO 3: OPERACIONES CON CONJUNTOS
# ============================================================

"""
Un conjunto almacena elementos sin repetir.

Operadores importantes:

    &  -> intersección: elementos que están en ambos conjuntos.
    |  -> unión: elementos de los conjuntos sin duplicados.
    -  -> diferencia: elementos del primero que no están en el otro.

En este punto trabajamos con estudiantes inscritos en clubes.
"""


club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}


print("=== PUNTO 3: Operaciones con Conjuntos ===")


# ------------------------------------------------------------
# Estudiantes inscritos en LOS TRES clubes
# ------------------------------------------------------------

# & obtiene los elementos que están en los tres conjuntos.
estudian_tres = club_ciencias & club_deportes & club_arte

print(f"Estudiantes en LOS TRES clubes: {estudian_tres}")


# ------------------------------------------------------------
# Estudiantes inscritos en EXACTAMENTE UN club
# ------------------------------------------------------------

"""
Primera parte:
    club_ciencias - club_deportes - club_arte

Obtiene los estudiantes que están en Ciencias, pero no en los
otros dos clubes.

Hacemos lo mismo para Deportes y Arte.

Finalmente, usamos | para unir los tres resultados.
"""

solo_una = (
    (club_ciencias - club_deportes - club_arte)
    | (club_deportes - club_ciencias - club_arte)
    | (club_arte - club_ciencias - club_deportes)
)

print(f"Estudiantes en EXACTAMENTE un club: {solo_una}")


# ------------------------------------------------------------
# Mostrar en qué clubes está cada estudiante
# ------------------------------------------------------------

# La unión reúne a todos los estudiantes sin repetir nombres.
todos = club_ciencias | club_deportes | club_arte

print("\nPertenencia a clubes:")

# sorted() devuelve los estudiantes ordenados alfabéticamente.
for estudiante in sorted(todos):

    # Creamos una lista vacía para guardar los clubes del estudiante.
    clubes = []

    # Si el estudiante pertenece al conjunto, agregamos ese club.
    if estudiante in club_ciencias:
        clubes.append("Ciencias")

    if estudiante in club_deportes:
        clubes.append("Deportes")

    if estudiante in club_arte:
        clubes.append("Arte")

    # join() une los nombres de los clubes en un solo texto.
    print(f"  {estudiante}: {', '.join(clubes)}")

print()


# ============================================================
# PUNTO 4: RECURSIVIDAD Y MEMOIZACIÓN
# ============================================================

"""
Problema:
¿Cuántas formas existen de subir una escalera de n escalones
si se puede subir 1 o 2 escalones a la vez?

Para llegar al escalón n podemos:

    1. Llegar al escalón n - 1 y subir un escalón.
    2. Llegar al escalón n - 2 y subir dos escalones.

Por eso sumamos los resultados de esos dos casos.

MEMOIZACIÓN:
Consiste en guardar resultados que ya calculamos para reutilizarlos
sin tener que repetir el mismo cálculo.
"""


print("=== PUNTO 4: Memoización ===")


# ------------------------------------------------------------
# 4.1 Recursividad simple, sin memoización
# ------------------------------------------------------------

def formas_subir_simple(n):
    """
    Calcula el número de formas de subir n escalones.

    Esta versión no guarda los resultados anteriores.
    Por eso puede repetir muchos cálculos.
    """

    # CASO BASE:
    # Si hay 0 o 1 escalón, contamos una forma.
    if n <= 1:
        return 1

    # Para 2 escalones hay dos formas:
    # 1 + 1
    # 2
    if n == 2:
        return 2

    # Sumamos las formas de llegar desde n - 1 y desde n - 2.
    return (
        formas_subir_simple(n - 1)
        + formas_subir_simple(n - 2)
    )


# ------------------------------------------------------------
# 4.2 Recursividad con memoización
# ------------------------------------------------------------

def formas_subir_memo(n, memo=None):
    """
    Calcula el número de formas de subir n escalones y guarda
    los resultados calculados en un diccionario.

    memo guarda pares de este tipo:

        clave -> cantidad de escalones
        valor -> formas de subir esa cantidad

    Ejemplo:

        memo[5] = 8

    Significa que ya calculamos que existen 8 formas de subir
    una escalera de 5 escalones.
    """

    # Si no recibimos un diccionario, creamos uno vacío.
    #
    # Usamos "is None" para crear el diccionario al iniciar
    # la función sin reemplazar uno que ya nos hayan pasado.
    if memo is None:
        memo = {}

    # CASOS BASE:
    # Estos resultados se conocen directamente.
    if n <= 1:
        return 1

    if n == 2:
        return 2

    # Antes de calcular, comprobamos si el resultado ya existe.
    if n in memo:

        # Si existe, lo devolvemos sin volver a calcularlo.
        return memo[n]

    # Si no existe, calculamos el resultado.
    #
    # Pasamos el mismo diccionario a las llamadas recursivas
    # para compartir los resultados guardados.
    resultado = (
        formas_subir_memo(n - 1, memo)
        + formas_subir_memo(n - 2, memo)
    )

    # Guardamos el resultado para reutilizarlo más adelante.
    memo[n] = resultado

    # Devolvemos el resultado calculado.
    return resultado


# Pruebas
print("Formas de subir escalera (comparativa):")

for n in [5, 10, 15, 20, 25]:

    resultado_simple = formas_subir_simple(n)

    # La función crea un diccionario nuevo porque no le pasamos
    # uno como argumento.
    resultado_memo = formas_subir_memo(n)

    print(
        f"  n={n}: "
        f"simple={resultado_simple}, "
        f"memo={resultado_memo}"
    )

print()


# ============================================================
# NOTAS PARA EL PARCIAL: EXPRESIONES REGULARES
# ============================================================

"""
Si te cambian el formato que debes validar, identifica las reglas
y modifica el patrón.

[A-Z]   -> letras mayúsculas.
[a-z]   -> letras minúsculas.
[A-Za-z] -> letras mayúsculas y minúsculas.
\d      -> un número.
{3}     -> exactamente 3 repeticiones.
{2,}    -> al menos 2 repeticiones.
+       -> una o más repeticiones.
?       -> cero o una repetición.
^       -> comienzo del texto.
$       -> final del texto.
\.      -> un punto literal.
"""

# Ejemplo de un patrón para tres letras y tres números:
# patron = r"^[A-Z]{3}\d{3}$"

# Ejemplo de un patrón para un correo:
# patron = r"^[a-z]{2,}\.[a-z]{2,}@elpoli\.edu\.co$"


# ============================================================
# NOTAS PARA EL PARCIAL: RETURN Y PRINT
# ============================================================

"""
RETURN:
    Entrega un resultado para que pueda utilizarse fuera
    de la función.

PRINT:
    Muestra un resultado en pantalla.

Si te piden RETORNAR un resultado, usa return.

Si quieres MOSTRAR el resultado, puedes hacer print() cuando
llames a la función.
"""

# Ejemplo: retornar un número.
#
# def sumar(a, b):
#     return a + b
#
# resultado = sumar(3, 4)
# print(resultado)


"""
Si te piden devolver una lista:

    def ejemplo():
        return ["Ana", "Luis"]

Si te piden devolver un conjunto:

    def ejemplo():
        return {"Ana", "Luis"}

Si te piden devolver un diccionario:

    def ejemplo():
        return {
            "Ana": 17,
            "Luis": 20
        }

Si te piden mostrar el resultado:

    print(ejemplo())

Si te piden guardar el resultado:

    resultado = ejemplo()
"""


# ============================================================
# NOTAS PARA EL PARCIAL: LISTAS ENLAZADAS
# ============================================================

"""
Para recorrer una lista enlazada:

    actual = self.cabeza

    while actual:
        # Trabajar con el nodo actual.
        actual = actual.siguiente

Para recorrerla con recursividad, normalmente creamos un método
auxiliar que recibe el nodo actual.

CASO BASE:
    Es la condición que detiene las llamadas recursivas.

CASO RECURSIVO:
    Es la llamada que continúa con un problema más pequeño.

Ejemplos de casos base:

    if actual is None:
        return

Si estamos contando nodos:

    if actual is None:
        return 0

Si estamos sumando valores:

    if actual is None:
        return 0

El resultado del caso base depende de lo que esté pidiendo
el ejercicio.
"""


# ------------------------------------------------------------
# Variación: contar pedidos que cumplen una condición
# ------------------------------------------------------------

"""
Si te piden contar pedidos cuyo valor sea superior a 20000,
no sumamos el valor del pedido: sumamos 1 cuando cumple.

Este método se podría agregar dentro de ListaPedidos.
"""

# def contar_pedidos_recursivo(self, actual):
#     if actual is None:
#         return 0
#
#     contador = 0
#
#     if actual.valor > 20000:
#         contador = 1
#
#     return contador + self.contar_pedidos_recursivo(
#         actual.siguiente
#     )


# ------------------------------------------------------------
# Variación: devolver una lista de clientes pendientes
# ------------------------------------------------------------

"""
Si te piden devolver una lista normal de Python con los clientes
que tienen pedidos pendientes, puedes usar este patrón.

Este método se podría agregar dentro de ListaPedidos.
"""

# def clientes_pendientes(self):
#     clientes = []
#     actual = self.cabeza
#
#     while actual:
#         if not actual.entregado:
#             clientes.append(actual.cliente)
#
#         actual = actual.siguiente
#
#     return clientes


# ============================================================
# NOTAS PARA EL PARCIAL: CONJUNTOS
# ============================================================

"""
OPERACIONES IMPORTANTES:

A & B
    Intersección: elementos que están en ambos conjuntos.

A | B
    Unión: elementos que están en A o en B, sin repetir.

A - B
    Diferencia: elementos de A que no están en B.

Si te piden elementos comunes:
    Usa &.

Si te piden reunir todos los elementos:
    Usa |.

Si te piden los elementos que están en un conjunto, pero no en otro:
    Usa -.

Si te piden exactamente los de un conjunto y ninguno de los otros:
    Calcula las diferencias y después une los resultados.
"""


"""
DIFERENCIA ENTRE ESTRUCTURAS:

{"Ana", "Luis"}           -> conjunto.
["Ana", "Luis"]           -> lista.
("Ana", "Luis")           -> tupla.
{"Ana": 17, "Luis": 20}   -> diccionario.
set()                     -> conjunto vacío.
{}                        -> diccionario vacío.

Un conjunto no garantiza el orden de sus elementos.
Si necesitas mostrarlos ordenados, puedes usar sorted().
"""


# ============================================================
# NOTAS PARA EL PARCIAL: MEMOIZACIÓN
# ============================================================

"""
La memoización consiste en guardar resultados para no repetir
cálculos.

En este ejercicio usamos un diccionario llamado memo.

Por ejemplo:

    memo[5] = 8

Significa que ya calculamos el resultado para 5 escalones.

Antes de calcular un resultado, preguntamos:

    if n in memo:
        return memo[n]

Si n ya está en el diccionario, devolvemos el resultado guardado.

Si no está, lo calculamos y lo guardamos:

    memo[n] = resultado

Después lo devolvemos:

    return memo[n]

La versión sin memoización puede repetir muchos cálculos.
La versión con memoización reutiliza los resultados guardados.

En este problema, la memoización reduce el tiempo de cálculo
a un orden proporcional a n, es decir, O(n).
"""


# ============================================================
# IDEA PRINCIPAL PARA RESOLVER VARIACIONES
# ============================================================

"""
VALIDAR:
    Comprobar una condición y devolver True o False.

EXTRAER:
    Encontrar coincidencias y devolver una lista.

CONTAR:
    Sumar 1 cuando un elemento cumple una condición.

SUMAR:
    Acumular los valores de los elementos que cumplen.

ELIMINAR:
    Modificar los enlaces y conservar los nodos necesarios.

FILTRAR:
    Guardar solamente los elementos que cumplen una condición.

ELEMENTOS COMUNES:
    Intersección (&).

UNIR ELEMENTOS:
    Unión (|).

ELEMENTOS EXCLUSIVOS:
    Diferencia (-).

EVITAR CÁLCULOS REPETIDOS:
    Memoización con un diccionario.

Antes de escribir código, identifica qué te están pidiendo.
Después adapta el patrón correspondiente.
"""