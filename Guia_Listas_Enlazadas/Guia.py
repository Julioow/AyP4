# ============================================================
# GUÍA DE LISTAS ENLAZADAS Y RECURSIÓN
# Estructuras de Datos - Algoritmos 4
# ============================================================
#
# IDEA PRINCIPAL:
#
# Una lista enlazada está formada por NODOS.
#
# Cada nodo guarda:
#   - un dato
#   - una referencia al siguiente nodo
#
# Ejemplo:
#
#       cabeza
#          ↓
#       [10] → [20] → [30] → None
#
# "cabeza" pertenece a la lista.
# "siguiente" pertenece a cada nodo.
#
# ============================================================


# ============================================================
# 1. CREAR UN NODO
# ============================================================

class Nodo:

    def __init__(self, dato):
        # Guardamos el dato dentro del nodo.
        self.dato = dato

        # Al principio el nodo no apunta a ningún otro nodo.
        self.siguiente = None


# ============================================================
# 2. CREAR LA LISTA
# ============================================================

class Lista:

    def __init__(self):
        # La lista comienza vacía.
        #
        # "cabeza" guarda la referencia al primer nodo.
        #
        # Si está vacía:
        #
        # cabeza → None
        #
        self.cabeza = None


# ============================================================
# 3. INSERTAR AL FINAL
# ============================================================
#
# Ejemplo:
#
# Antes:
#
# [10] → [20] → None
#
# Agregamos 30:
#
# [10] → [20] → [30] → None
#
# ============================================================

    def agregar(self, dato):

        # Creamos un nuevo nodo.
        nuevo = Nodo(dato)

        # Si la lista está vacía, el nuevo nodo
        # se convierte en la cabeza.
        if self.cabeza is None:
            self.cabeza = nuevo

        else:
            # Empezamos desde el primer nodo.
            actual = self.cabeza

            # Avanzamos hasta encontrar el último nodo.
            #
            # Mientras actual.siguiente exista,
            # seguimos avanzando.
            while actual.siguiente is not None:
                actual = actual.siguiente

            # Cuando llegamos al último nodo,
            # conectamos el nuevo nodo.
            actual.siguiente = nuevo


# ============================================================
# 4. INSERTAR AL INICIO
# ============================================================
#
# Esta es una de las operaciones MÁS IMPORTANTES.
#
# Antes:
#
# cabeza
#   ↓
# [20] → [30] → None
#
# Agregamos 10:
#
# cabeza
#   ↓
# [10] → [20] → [30] → None
#
# ============================================================

    def insertar_inicio(self, dato):

        # Creamos el nuevo nodo.
        nuevo = Nodo(dato)

        # El nuevo nodo apunta a la antigua cabeza.
        nuevo.siguiente = self.cabeza

        # Ahora el nuevo nodo se convierte en la cabeza.
        self.cabeza = nuevo


# ============================================================
# 5. RECORRER / MOSTRAR LA LISTA
# ============================================================
#
# Usamos "actual" para movernos nodo por nodo.
#
# actual = self.cabeza
# actual = actual.siguiente
#
# ============================================================

    def mostrar(self):

        # Comenzamos desde el primer nodo.
        actual = self.cabeza

        # Recorremos mientras exista un nodo.
        while actual is not None:

            print(actual.dato)

            # Avanzamos al siguiente nodo.
            actual = actual.siguiente


# ============================================================
# 6. CONTAR NODOS CON RECURSIÓN
# ============================================================
#
# Ejemplo:
#
# [10] → [20] → [30] → None
#
# Resultado: 3
#
# La función recibe el nodo en el que estamos.
#
# ============================================================

    def contar_nodos(self, nodo=None):

        # CASO BASE:
        #
        # Si no existe nodo, ya terminamos.
        #
        # No sumamos nada.
        if nodo is None:
            return 0

        # Contamos el nodo actual (1)
        # y seguimos con el siguiente.
        return 1 + self.contar_nodos(nodo.siguiente)


# ============================================================
# 7. SUMAR LOS DATOS CON RECURSIÓN
# ============================================================
#
# Ejemplo:
#
# [10] → [20] → [30] → None
#
# Resultado:
#
# 10 + 20 + 30 = 60
#
# ============================================================

    def sumar(self, nodo=None):

        # CASO BASE:
        #
        # Si llegamos al final, no hay nada más que sumar.
        if nodo is None:
            return 0

        # Sumamos el dato actual
        # y luego el resultado de los siguientes nodos.
        return nodo.dato + self.sumar(nodo.siguiente)


# ============================================================
# 8. BUSCAR UN DATO CON RECURSIÓN
# ============================================================
#
# Devuelve True si encuentra el dato.
# Devuelve False si llega al final sin encontrarlo.
#
# ============================================================

    def buscar(self, nodo, dato):

        # CASO BASE:
        #
        # Llegamos al final y no encontramos el dato.
        if nodo is None:
            return False

        # Comparamos el dato del nodo actual.
        if nodo.dato == dato:
            return True

        # Si no coincide, avanzamos al siguiente nodo.
        return self.buscar(nodo.siguiente, dato)


# ============================================================
# 9. ELIMINAR UN DATO CON RECURSIÓN
# ============================================================
#
# Esta función elimina la primera aparición del dato.
#
# Ejemplo:
#
# [10] → [20] → [30] → None
#
# eliminar(20)
#
# Resultado:
#
# [10] → [30] → None
#
# ============================================================

    def eliminar(self, nodo, dato):

        # CASO BASE:
        #
        # Si llegamos al final, no hay nada que eliminar.
        if nodo is None:
            return None

        # Si encontramos el dato:
        #
        # retornamos el siguiente nodo.
        #
        # De esta manera "saltamos" el nodo actual.
        if nodo.dato == dato:
            return nodo.siguiente

        # Seguimos buscando en los nodos siguientes.
        nodo.siguiente = self.eliminar(nodo.siguiente, dato)

        # Conservamos el nodo actual.
        return nodo


# ============================================================
# 10. ELIMINAR NODOS SEGÚN UNA CONDICIÓN
# ============================================================
#
# Este patrón es MUY IMPORTANTE para los ejercicios del quiz.
#
# Ejemplo:
#
# Eliminar todos los nodos cuyo dato sea menor que 20.
#
# [10] → [20] → [5] → [30]
#
# Resultado:
#
# [20] → [30]
#
# ============================================================

    def eliminar_menores(self, nodo, minimo):

        # CASO BASE:
        if nodo is None:
            return None

        # PRIMERO limpiamos recursivamente
        # todos los nodos que vienen después.
        nodo.siguiente = self.eliminar_menores(
            nodo.siguiente,
            minimo
        )

        # Después revisamos el nodo actual.
        if nodo.dato < minimo:

            # Si debe eliminarse,
            # devolvemos el siguiente nodo.
            return nodo.siguiente

        # Si no debe eliminarse,
        # conservamos el nodo.
        return nodo


# ============================================================
# 11. SUMAR TIEMPOS
# ============================================================
#
# Este es el mismo patrón de "sumar",
# pero aplicado a un atributo llamado "tiempo".
#
# Ejemplo:
#
# [Google, 100] → [YouTube, 200] → [GitHub, 50]
#
# Resultado:
#
# 100 + 200 + 50 = 350
#
# ============================================================

    def tiempo_total(self, nodo):

        # CASO BASE
        if nodo is None:
            return 0

        # Tiempo actual + tiempos restantes.
        return nodo.tiempo + self.tiempo_total(nodo.siguiente)


# ============================================================
# 12. BUSCAR Y CREAR UNA NUEVA LISTA
# ============================================================
#
# IMPORTANTE:
#
# Si el ejercicio pide:
#
# "Buscar elementos y devolver una NUEVA lista"
#
# NO debemos modificar la lista original.
#
# Creamos nodos nuevos.
#
# ============================================================

    def buscar_y_copiar(self, nodo, dato, resultado):

        # CASO BASE:
        #
        # Terminamos y devolvemos la nueva lista.
        if nodo is None:
            return resultado

        # Si encontramos el dato:
        if nodo.dato == dato:

            # Creamos un nodo NUEVO.
            nueva = Nodo(nodo.dato)

            # Lo conectamos a la lista resultado.
            nueva.siguiente = resultado

            # Ahora nueva es el comienzo
            # de nuestra lista de resultados.
            resultado = nueva

        # Seguimos buscando.
        return self.buscar_y_copiar(
            nodo.siguiente,
            dato,
            resultado
        )


# ============================================================
# 13. PATRÓN GENERAL DE RECURSIÓN
# ============================================================
#
# Casi todos los ejercicios recursivos de listas
# siguen esta estructura:
#
#
# def funcion(self, nodo):
#
#     if nodo is None:
#         return ...
#
#     ...
#
#     return self.funcion(nodo.siguiente)
#
#
# Lo importante es entender:
#
# nodo
#   ↓
# nodo.siguiente
#   ↓
# nodo.siguiente.siguiente
#   ↓
# None
#
# ============================================================


# ============================================================
# 14. EJEMPLO DE HISTORIAL DE NAVEGADOR
# ============================================================

class Pagina:

    def __init__(self, url, tiempo, titulo):

        self.url = url
        self.tiempo = tiempo
        self.titulo = titulo

        # Referencia a la siguiente página.
        self.siguiente = None


class Historial:

    def __init__(self):

        # Referencia a la primera página.
        self.cabeza = None


# ============================================================
# INSERTAR UNA PÁGINA AL INICIO
# ============================================================

    def visitar(self, url, tiempo, titulo):

        # Creamos la nueva página.
        nueva = Pagina(url, tiempo, titulo)

        # La nueva página apunta a la antigua cabeza.
        nueva.siguiente = self.cabeza

        # Ahora la nueva página es la cabeza.
        self.cabeza = nueva


# ============================================================
# TIEMPO TOTAL
# ============================================================

    def tiempo_total(self, nodo):

        # CASO BASE
        if nodo is None:
            return 0

        # Tiempo actual + tiempo de las siguientes páginas.
        return nodo.tiempo + self.tiempo_total(nodo.siguiente)


# ============================================================
# BUSCAR POR TEXTO EN LA URL
# ============================================================
#
# Ejemplo:
#
# Buscar "youtube" en todas las URLs.
#
# IMPORTANTE:
#
# Se crean páginas NUEVAS para el resultado.
#
# ============================================================

    def buscar(self, nodo, texto, resultado):

        # CASO BASE
        if nodo is None:
            return resultado

        # Revisamos si el texto aparece en la URL.
        if texto in nodo.url:

            # Creamos una copia del nodo.
            nueva = Pagina(
                nodo.url,
                nodo.tiempo,
                nodo.titulo
            )

            # Insertamos la copia en el resultado.
            nueva.siguiente = resultado
            resultado = nueva

        # Continuamos con el siguiente nodo.
        return self.buscar(
            nodo.siguiente,
            texto,
            resultado
        )


# ============================================================
# ELIMINAR PÁGINAS SEGÚN EL TIEMPO
# ============================================================
#
# Elimina las páginas cuyo tiempo sea menor que "minimo".
#
# Ejemplo:
#
# minimo = 100
#
# [50] → [200] → [80] → [300]
#
# Resultado:
#
# [200] → [300]
#
# ============================================================

    def eliminar(self, nodo, minimo):

        # CASO BASE
        if nodo is None:
            return None

        # PRIMERO procesamos el resto de la lista.
        nodo.siguiente = self.eliminar(
            nodo.siguiente,
            minimo
        )

        # Después revisamos el nodo actual.
        if nodo.tiempo < minimo:

            # Eliminamos el nodo actual.
            return nodo.siguiente

        # Si cumple la condición,
        # lo conservamos.
        return nodo


# ============================================================
# 15. RESUMEN DE LOS PATRONES IMPORTANTES
# ============================================================
#
# INSERTAR AL INICIO:
#
# nuevo.siguiente = self.cabeza
# self.cabeza = nuevo
#
#
# AVANZAR EN LA LISTA:
#
# actual = actual.siguiente
#
#
# RECURSIÓN:
#
# if nodo is None:
#     return ...
#
# return self.funcion(nodo.siguiente)
#
#
# CONTAR:
#
# return 1 + self.contar_nodos(nodo.siguiente)
#
#
# SUMAR:
#
# return nodo.dato + self.sumar(nodo.siguiente)
#
#
# BUSCAR:
#
# if nodo.dato == dato:
#     return True
#
# return self.buscar(nodo.siguiente, dato)
#
#
# BUSCAR Y CREAR NUEVA LISTA:
#
# nueva = Nodo(...)
# nueva.siguiente = resultado
# resultado = nueva
#
#
# ELIMINAR:
#
# nodo.siguiente = self.eliminar(nodo.siguiente, ...)
#
# if condicion:
#     return nodo.siguiente
#
# return nodo
#
# ============================================================
#
# REGLA DE ORO:
#
# "nodo" = dónde estoy.
#
# "nodo.siguiente" = dónde voy después.
#
# "self.cabeza" = dónde empieza la lista.
#
# "return" = qué le devuelvo a quien me llamó.
#
# ============================================================