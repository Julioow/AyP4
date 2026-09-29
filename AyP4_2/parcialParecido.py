"""
═══════════════════════════════════════════════════════════════════════════════
                    PARCIAL SIMULADO - TODOS LOS TEMAS
                Algoritmos y Programación 4 - Evaluación Integral
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
---------------
1. Completar las funciones donde dice TODO
2. No modificar el código base proporcionado
3. Tiempo estimado: 90 minutos
4. Temas: Listas Enlazadas, Recursión, Expresiones Regulares, Conjuntos, 
         Estructuras de Datos (Pilas/Colas), Búsqueda y Análisis de Complejidad

═══════════════════════════════════════════════════════════════════════════════
                PARTE 1: EXPRESIONES REGULARES - VALIDACIÓN (1.5 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

import re

# PUNTO 1.1 (0.5 pts): Validar correo electrónico
def validar_correo(correo):
    """
    Valida si un correo tiene formato correcto.
    Formato: usuario@dominio.extension
    
    Ejemplo:
        validar_correo("juan@example.com") -> True
        validar_correo("juan@.com") -> False
        validar_correo("juan.perez@empresa.co") -> True
    """
    # TODO: Implementar utilizando expresiones regulares
    pass


# PUNTO 1.2 (0.5 pts): Validar contraseña segura
def validar_contraseña(contraseña):
    """
    Una contraseña válida debe tener:
    - Mínimo 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un dígito
    - Al menos un carácter especial (@, #, $, %, &, !)
    
    Ejemplo:
        validar_contraseña("Abc@1234") -> True
        validar_contraseña("abcd1234") -> False (sin mayúscula)
        validar_contraseña("Abc@123") -> False (menos de 8 caracteres)
    """
    # TODO: Implementar utilizando expresiones regulares
    pass


# PUNTO 1.3 (0.5 pts): Extraer URLs de un texto
def extraer_urls(texto):
    """
    Extrae todas las URLs de un texto.
    Las URLs pueden empezar con http://, https://, o simplemente www.
    
    Ejemplo:
        texto = "Visita https://google.com y www.python.org"
        extraer_urls(texto) -> ['https://google.com', 'www.python.org']
    """
    # TODO: Implementar utilizando expresiones regulares
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
               PARTE 2: RECURSIÓN - PROBLEMAS CLÁSICOS (2.0 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 2.1 (0.5 pts): Fibonacci con memoización
memo_fib = {}

def fibonacci_memo(n):
    """
    Calcula el n-ésimo número de Fibonacci usando memoización.
    OBLIGATORIO usar diccionario para guardar resultados.
    
    Ejemplo:
        fibonacci_memo(10) -> 55
        fibonacci_memo(15) -> 610
    """
    # TODO: Implementar usando diccionario para memoización
    pass


# PUNTO 2.2 (0.75 pts): Verificar si un número es palíndromo
def es_numero_palindromo(n):
    """
    Retorna True si un número es palíndromo.
    OBLIGATORIO usar recursión.
    
    Un palíndromo numérico se lee igual de izquierda a derecha 
    que de derecha a izquierda.
    
    Ejemplo:
        es_numero_palindromo(121) -> True
        es_numero_palindromo(12321) -> True
        es_numero_palindromo(123) -> False
    """
    # TODO: Implementar usando recursión
    pass


# PUNTO 2.3 (0.75 pts): Contar dígitos de un número
def contar_digitos(n):
    """
    Cuenta la cantidad de dígitos en un número.
    OBLIGATORIO usar recursión.
    
    Ejemplo:
        contar_digitos(12345) -> 5
        contar_digitos(999) -> 3
        contar_digitos(0) -> 1
    """
    # TODO: Implementar usando recursión
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 3: LISTAS ENLAZADAS (2.5 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# PUNTO 3.1 (1.0 pts): Implementar búsqueda en lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar_al_inicio(self, dato):
        """Agrega un elemento al inicio de la lista"""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
    
    def buscar(self, valor):
        """
        Busca un valor en la lista y retorna True si existe.
        
        Ejemplo:
            lista = ListaEnlazada()
            lista.agregar_al_inicio(10)
            lista.agregar_al_inicio(20)
            lista.buscar(10) -> True
            lista.buscar(30) -> False
        """
        # TODO: Implementar búsqueda secuencial
        pass
    
    def contar_elementos(self):
        """
        Retorna la cantidad de elementos en la lista.
        OBLIGATORIO usar recursión a través de función auxiliar.
        
        Ejemplo:
            lista = ListaEnlazada()
            lista.agregar_al_inicio(1)
            lista.agregar_al_inicio(2)
            lista.contar_elementos() -> 2
        """
        # TODO: Implementar usando recursión
        return self._contar_recursivo(self.cabeza)
    
    def _contar_recursivo(self, actual):
        """Función auxiliar recursiva para contar elementos"""
        # TODO: Implementar
        pass
    
    def suma_elementos(self):
        """
        Retorna la suma de todos los elementos.
        OBLIGATORIO usar recursión a través de función auxiliar.
        
        Ejemplo:
            lista = ListaEnlazada()
            lista.agregar_al_inicio(5)  # Ahora: 5 -> None
            lista.agregar_al_inicio(3)  # Ahora: 3 -> 5 -> None
            lista.agregar_al_inicio(2)  # Ahora: 2 -> 3 -> 5 -> None
            lista.suma_elementos() -> 10
        """
        # TODO: Implementar usando recursión
        return self._suma_recursiva(self.cabeza)
    
    def _suma_recursiva(self, actual):
        """Función auxiliar recursiva para sumar elementos"""
        # TODO: Implementar
        pass
    
    def invertir_lista(self):
        """
        Invierte el orden de los elementos en la lista.
        OBLIGATORIO usar recursión.
        
        Ejemplo:
            lista = ListaEnlazada()
            lista.agregar_al_inicio(3)
            lista.agregar_al_inicio(2)
            lista.agregar_al_inicio(1)
            # Antes: 1 -> 2 -> 3 -> None
            lista.invertir_lista()
            # Después: 3 -> 2 -> 1 -> None
        """
        # TODO: Implementar usando recursión
        self.cabeza = self._invertir_recursivo(self.cabeza)
    
    def _invertir_recursivo(self, actual):
        """Función auxiliar recursiva para invertir"""
        # TODO: Implementar
        pass


# PUNTO 3.2 (1.5 pts): Eliminar elementos duplicados
def eliminar_duplicados_lista(valores):
    """
    Crea e inserta valores en una lista enlazada eliminando duplicados.
    Un valor duplicado es el que ya existe en la lista.
    
    Retorna la cabeza de la lista enlazada con elementos únicos.
    
    Ejemplo:
        resultado = eliminar_duplicados_lista([1, 2, 2, 3, 1, 4, 3])
        # Lista resultante: 4 -> 3 -> 2 -> 1 -> None
    """
    # TODO: Implementar
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 4: CONJUNTOS Y OPERACIONES (1.5 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 4.1 (0.5 pts): Encontrar intersección de dos listas
def interseccion_listas(lista1, lista2):
    """
    Retorna una lista con los elementos comunes entre dos listas.
    No debe haber duplicados en el resultado.
    
    Usar conjuntos para optimizar.
    
    Ejemplo:
        interseccion_listas([1, 2, 3, 4], [3, 4, 5, 6]) -> [3, 4]
        interseccion_listas([1, 1, 2], [2, 2, 3]) -> [2]
    """
    # TODO: Implementar usando conjuntos
    pass


# PUNTO 4.2 (0.5 pts): Encontrar elementos únicos
def elementos_unicos(lista):
    """
    Retorna una lista con los elementos que aparecen SOLO UNA VEZ.
    
    Ejemplo:
        elementos_unicos([1, 2, 2, 3, 3, 3, 4]) -> [1, 4]
        elementos_unicos([5, 5, 10, 10]) -> []
    """
    # TODO: Implementar
    pass


# PUNTO 4.3 (0.5 pts): Verificar si un conjunto es subconjunto de otro
def es_subconjunto(conjunto_a, conjunto_b):
    """
    Retorna True si todos los elementos de conjunto_a están en conjunto_b.
    
    Ejemplo:
        es_subconjunto({1, 2}, {1, 2, 3, 4}) -> True
        es_subconjunto({1, 5}, {1, 2, 3}) -> False
    """
    # TODO: Implementar
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 5: BÚSQUEDA AVANZADA (1.0 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 5.1 (1.0 pts): Búsqueda binaria recursiva
def busqueda_binaria(lista, objetivo, izquierda=0, derecha=None):
    """
    Implementa búsqueda binaria de forma RECURSIVA.
    LA LISTA DEBE ESTAR ORDENADA.
    
    Retorna el índice del elemento si lo encuentra, -1 si no existe.
    
    OBLIGATORIO: Usar recursión, no ciclos.
    
    Ejemplo:
        lista = [1, 3, 5, 7, 9, 11, 13]
        busqueda_binaria(lista, 7) -> 3
        busqueda_binaria(lista, 6) -> -1
    """
    # TODO: Implementar usando recursión
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 6: ANÁLISIS Y MODIFICACIÓN (1.5 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 6.1 (0.5 pts): Filtrar números pares
def filtrar_pares(numeros):
    """
    Retorna una lista solo con los números pares.
    
    Ejemplo:
        filtrar_pares([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
        filtrar_pares([1, 3, 5]) -> []
    """
    # TODO: Implementar
    pass


# PUNTO 6.2 (0.5 pts): Encontrar el segundo número más grande
def segundo_mayor(numeros):
    """
    Retorna el segundo número más grande de la lista.
    
    Retorna None si no hay segundo mayor (lista con menos de 2 elementos
    o todos iguales).
    
    Ejemplo:
        segundo_mayor([1, 5, 3, 9, 2]) -> 5
        segundo_mayor([5, 5, 5]) -> None
        segundo_mayor([10]) -> None
    """
    # TODO: Implementar
    pass


# PUNTO 6.3 (0.5 pts): Rotar lista
def rotar_lista(lista, k):
    """
    Rota los elementos de la lista k posiciones a la derecha.
    
    Ejemplo:
        rotar_lista([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
        rotar_lista([1, 2, 3], 1) -> [3, 1, 2]
        rotar_lista([1, 2], 5) -> [1, 2]  # 5 % 2 = 1, es como rotar 1
    """
    # TODO: Implementar
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                        CÓDIGO DE PRUEBA - NO MODIFICAR
═══════════════════════════════════════════════════════════════════════════════
"""

if __name__ == "__main__":
    print("=" * 70)
    print("PARTE 1: EXPRESIONES REGULARES")
    print("=" * 70)
    
    print("\n[CORREOS] Validacion de correos:")
    correos = [
        "juan@example.com",
        "maria.perez@empresa.co",
        "invalido@",
        "@example.com",
        "user+tag@domain.org"
    ]
    for correo in correos:
        resultado = validar_correo(correo)
        print(f"  {correo}: {'V' if resultado else 'X'}")
    
    print("\n[CONTRASENAS] Validacion de contrasenas:")
    contrasenas = [
        "Abc@1234",
        "abcd1234",
        "Abc@123",
        "ValidPass#2024",
        "weakpass"
    ]
    for pwd in contrasenas:
        resultado = validar_contraseña(pwd)
        print(f"  {pwd}: {'V' if resultado else 'X'}")
    
    print("\n[URLS] Extraccion de URLs:")
    texto_urls = "Visita https://google.com, www.python.org y http://github.com para mas info"
    urls = extraer_urls(texto_urls)
    print(f"  Texto: {texto_urls}")
    print(f"  URLs encontradas: {urls}")
    
    print("\n" + "=" * 70)
    print("PARTE 2: RECURSION")
    print("=" * 70)
    
    print("\n[FIBONACCI] Fibonacci con memorizacion:")
    for n in [5, 10, 15, 20]:
        resultado = fibonacci_memo(n)
        print(f"  fibonacci({n}) = {resultado}")
    
    print("\n[PALINDROMOS] Numeros palindromos:")
    numeros_prueba = [121, 12321, 123, 1001, 100]
    for num in numeros_prueba:
        resultado = es_numero_palindromo(num)
        print(f"  {num}: {'V Palindromo' if resultado else 'X No palindromo'}")
    
    print("\n[DIGITOS] Contar digitos:")
    for num in [123, 45678, 0, 1000000]:
        resultado = contar_digitos(num)
        print(f"  {num}: {resultado} digitos")
    
    print("\n" + "=" * 70)
    print("PARTE 3: LISTAS ENLAZADAS")
    print("=" * 70)
    
    print("\n[BUSQUEDA] Busqueda en lista enlazada:")
    lista = ListaEnlazada()
    for val in [30, 20, 10, 40]:
        lista.agregar_al_inicio(val)
    print(f"  Existe 20? {lista.buscar(20)}")
    print(f"  Existe 50? {lista.buscar(50)}")
    
    print("\n[CONTAR] Contar elementos:")
    print(f"  Total de elementos: {lista.contar_elementos()}")
    
    print("\n[SUMA] Suma de elementos:")
    print(f"  Suma total: {lista.suma_elementos()}")
    
    print("\n[INVERTIR] Invertir lista:")
    lista2 = ListaEnlazada()
    for val in [3, 2, 1]:
        lista2.agregar_al_inicio(val)
    print(f"  Antes de invertir: 1 -> 2 -> 3")
    lista2.invertir_lista()
    print(f"  Despues de invertir: 3 -> 2 -> 1")
    
    print("\n[DUPLICADOS] Eliminar duplicados:")
    resultado = eliminar_duplicados_lista([1, 2, 2, 3, 1, 4, 3])
    print(f"  Lista con duplicados: [1, 2, 2, 3, 1, 4, 3]")
    print(f"  Lista sin duplicados: elementos únicos agregados")
    
    print("\n" + "=" * 70)
    print("PARTE 4: CONJUNTOS Y OPERACIONES")
    print("=" * 70)
    
    print("\n🔀 Intersección de listas:")
    l1 = [1, 2, 3, 4, 5]
    l2 = [3, 4, 5, 6, 7]
    print(f"  Lista 1: {l1}")
    print(f"  Lista 2: {l2}")
    print(f"  Intersección: {interseccion_listas(l1, l2)}")
    
    print("\n✨ Elementos únicos:")
    lista_dup = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    print(f"  Lista: {lista_dup}")
    print(f"  Únicos: {elementos_unicos(lista_dup)}")
    
    print("\n[SUBCONJUNTOS] Subconjuntos:")
    print(f"  Es {1, 2} subconjunto de {{1, 2, 3, 4}}? {es_subconjunto({1, 2}, {1, 2, 3, 4})}")
    print(f"  Es {1, 5} subconjunto de {{1, 2, 3}}? {es_subconjunto({1, 5}, {1, 2, 3})}")
    
    print("\n" + "=" * 70)
    print("PARTE 5: BÚSQUEDA AVANZADA")
    print("=" * 70)
    
    print("\n[BINARIA] Busqueda binaria:")
    lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(f"  Lista: {lista_ordenada}")
    for objetivo in [7, 1, 17, 10]:
        indice = busqueda_binaria(lista_ordenada, objetivo)
        if indice != -1:
            print(f"  {objetivo} encontrado en índice {indice} ✓")
        else:
            print(f"  {objetivo} no encontrado ✗")
    
    print("\n" + "=" * 70)
    print("PARTE 6: ANÁLISIS Y MODIFICACIÓN")
    print("=" * 70)
    
    print("\n[PARES] Filtrar pares:")
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"  Original: {numeros}")
    print(f"  Pares: {filtrar_pares(numeros)}")
    
    print("\n[SEGUNDO] Segundo mayor:")
    listas_prueba = [
        [1, 5, 3, 9, 2],
        [5, 5, 5],
        [10]
    ]
    for l in listas_prueba:
        resultado = segundo_mayor(l)
        print(f"  {l} -> {resultado}")
    
    print("\n[ROTAR] Rotar lista:")
    lista_orig = [1, 2, 3, 4, 5]
    for k in [1, 2, 3]:
        rotada = rotar_lista(lista_orig.copy(), k)
        print(f"  Rotar {lista_orig} {k} posiciones: {rotada}")
    
    print("\n" + "=" * 70)
    print("OK PARCIAL SIMULADO 1 COMPLETADO")
    print("=" * 70)


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARCIAL SIMULADO 2 - TODOS LOS TEMAS
                Algoritmos y Programación 4 - Evaluación Integral
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
---------------
1. Completar las funciones donde dice TODO
2. No modificar el código base proporcionado
3. Tiempo estimado: 90 minutos
4. Temas: Listas Enlazadas, Recursión, Expresiones Regulares, Conjuntos, 
         Estructuras de Datos (Pilas/Colas), Búsqueda y Análisis de Complejidad

═══════════════════════════════════════════════════════════════════════════════
                PARTE 1: EXPRESIONES REGULARES - VALIDACIÓN (1.5 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 1.1 (0.5 pts): Validar número de teléfono
def validar_telefono(telefono):
    """
    Valida si un teléfono colombiano es válido.
    Formato: 3XX-XXXX (10 dígitos, puede tener espacios o guiones)
    
    Ejemplo:
        validar_telefono("310-5551234") -> True
        validar_telefono("3105551234") -> True
        validar_telefono("300 555 1234") -> True
        validar_telefono("555-1234") -> False
    """
    # TODO: Implementar utilizando expresiones regulares
    pass


# PUNTO 1.2 (0.5 pts): Validar fecha en formato DD/MM/YYYY
def validar_fecha(fecha):
    """
    Valida si una fecha tiene formato correcto dd/mm/yyyy
    Validar que día sea 01-31, mes sea 01-12, año sea 1900-2100
    
    Ejemplo:
        validar_fecha("25/12/2024") -> True
        validar_fecha("32/12/2024") -> False
        validar_fecha("25/13/2024") -> False
        validar_fecha("25-12-2024") -> False
    """
    # TODO: Implementar utilizando expresiones regulares
    pass


# PUNTO 1.3 (0.5 pts): Extraer números de un texto
def extraer_numeros(texto):
    """
    Extrae todos los números (enteros y decimales) de un texto.
    
    Ejemplo:
        extraer_numeros("Precio: $19.99, cantidad: 5, descuento: 10%") 
        -> ['19.99', '5', '10']
        extraer_numeros("No hay números aquí") -> []
    """
    # TODO: Implementar utilizando expresiones regulares
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
               PARTE 2: RECURSIÓN - PROBLEMAS CLÁSICOS (2.0 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 2.1 (0.5 pts): Factorial de un número
def factorial_recursivo(n):
    """
    Calcula el factorial de n usando recursión.
    n! = n * (n-1) * (n-2) * ... * 1
    
    Ejemplo:
        factorial_recursivo(5) -> 120
        factorial_recursivo(0) -> 1
        factorial_recursivo(1) -> 1
    """
    # TODO: Implementar usando recursión
    pass


# PUNTO 2.2 (0.75 pts): Potencia de un número
def potencia_recursiva(base, exponente):
    """
    Calcula base^exponente usando recursión.
    OBLIGATORIO usar recursión, no usar ** ni pow()
    
    Ejemplo:
        potencia_recursiva(2, 3) -> 8
        potencia_recursiva(5, 2) -> 25
        potencia_recursiva(3, 0) -> 1
    """
    # TODO: Implementar usando recursión
    pass


# PUNTO 2.3 (0.75 pts): Suma de primeros N números
def suma_n_numeros(n):
    """
    Calcula la suma de los primeros n números naturales.
    OBLIGATORIO usar recursión.
    
    Suma = 1 + 2 + 3 + ... + n
    
    Ejemplo:
        suma_n_numeros(5) -> 15  (1+2+3+4+5)
        suma_n_numeros(10) -> 55
        suma_n_numeros(1) -> 1
    """
    # TODO: Implementar usando recursión
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 3: LISTAS ENLAZADAS (2.5 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

class Nodo2:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# PUNTO 3.1 (1.0 pts): Implementar eliminar nodo
class ListaEnlazada2:
    def __init__(self):
        self.cabeza = None
    
    def agregar_al_final(self, dato):
        """Agrega un elemento al final de la lista"""
        nuevo = Nodo2(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def eliminar(self, valor):
        """
        Elimina la PRIMERA ocurrencia de un valor.
        
        Ejemplo:
            lista = ListaEnlazada2()
            lista.agregar_al_final(10)
            lista.agregar_al_final(20)
            lista.agregar_al_final(30)
            lista.eliminar(20)
            # Resultado: 10 -> 30
        """
        # TODO: Implementar
        pass
    
    def obtener_ultimo(self):
        """
        Retorna el último elemento de la lista.
        OBLIGATORIO usar recursión.
        
        Si la lista está vacía, retorna None.
        """
        # TODO: Implementar usando recursión
        return self._obtener_ultimo_recursivo(self.cabeza)
    
    def _obtener_ultimo_recursivo(self, actual):
        """Función auxiliar recursiva"""
        # TODO: Implementar
        pass
    
    def longitud(self):
        """
        Retorna la longitud de la lista.
        OBLIGATORIO usar recursión.
        """
        # TODO: Implementar usando recursión
        return self._longitud_recursiva(self.cabeza)
    
    def _longitud_recursiva(self, actual):
        """Función auxiliar recursiva"""
        # TODO: Implementar
        pass


# PUNTO 3.2 (1.5 pts): Buscar máximo en lista enlazada
def encontrar_maximo(lista_enlaces):
    """
    Encuentra el máximo valor en una lista enlazada.
    OBLIGATORIO usar recursión.
    
    Retorna el valor máximo o None si la lista está vacía.
    
    Ejemplo:
        lista = ListaEnlazada2()
        lista.agregar_al_final(5)
        lista.agregar_al_final(2)
        lista.agregar_al_final(8)
        lista.agregar_al_final(3)
        encontrar_maximo(lista) -> 8
    """
    # TODO: Implementar usando recursión
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 4: CONJUNTOS Y OPERACIONES (1.5 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 4.1 (0.5 pts): Unión de múltiples conjuntos
def union_conjuntos(*conjuntos):
    """
    Retorna la unión de todos los conjuntos pasados como argumentos.
    
    Ejemplo:
        union_conjuntos({1, 2}, {2, 3}, {3, 4}) -> {1, 2, 3, 4}
        union_conjuntos({5}, {10}, {15}) -> {5, 10, 15}
    """
    # TODO: Implementar
    pass


# PUNTO 4.2 (0.5 pts): Diferencia simétrica
def diferencia_simetrica(conjunto_a, conjunto_b):
    """
    Retorna los elementos que están en A o en B pero NO en ambos.
    
    Ejemplo:
        diferencia_simetrica({1, 2, 3}, {2, 3, 4}) -> {1, 4}
        diferencia_simetrica({1, 2}, {1, 2}) -> set()
    """
    # TODO: Implementar
    pass


# PUNTO 4.3 (0.5 pts): Complemento de un conjunto
def complemento(conjunto, universo):
    """
    Retorna los elementos que están en universo pero NO en conjunto.
    
    Ejemplo:
        complemento({1, 3}, {1, 2, 3, 4, 5}) -> {2, 4, 5}
        complemento({1, 2}, {1}) -> set()  # No hay elementos en universo fuera del conjunto
    """
    # TODO: Implementar
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 5: BÚSQUEDA AVANZADA (1.0 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 5.1 (1.0 pts): Búsqueda lineal con retorno de índices
def buscar_todas_ocurrencias(lista, objetivo):
    """
    Encuentra TODOS los índices donde aparece el objetivo.
    OBLIGATORIO usar recursión.
    
    Retorna una lista de índices, vacío si no hay ocurrencias.
    
    Ejemplo:
        buscar_todas_ocurrencias([1, 2, 3, 2, 4, 2], 2) -> [1, 3, 5]
        buscar_todas_ocurrencias([5, 6, 7], 8) -> []
    """
    # TODO: Implementar usando recursión
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 6: ANÁLISIS Y MODIFICACIÓN (1.5 pts)
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 6.1 (0.5 pts): Encontrar pares que suman un valor
def pares_suma(lista, suma_objetivo):
    """
    Encuentra todos los pares de números que suman el valor objetivo.
    
    Ejemplo:
        pares_suma([1, 5, 3, 2, 4], 6) -> [(2, 4), (1, 5)]
        pares_suma([1, 2, 3], 10) -> []
    """
    # TODO: Implementar
    pass


# PUNTO 6.2 (0.5 pts): Compresión de lista (remover consecutivos)
def comprimir_lista(lista):
    """
    Remueve elementos consecutivos duplicados.
    
    Ejemplo:
        comprimir_lista([1, 1, 2, 2, 2, 3, 3, 1]) -> [1, 2, 3, 1]
        comprimir_lista([1, 2, 3]) -> [1, 2, 3]
        comprimir_lista([5, 5, 5]) -> [5]
    """
    # TODO: Implementar
    pass


# PUNTO 6.3 (0.5 pts): Encontrar elementos frecuentes
def elementos_frecuentes(lista, k):
    """
    Retorna los k elementos más frecuentes de la lista.
    
    Ejemplo:
        elementos_frecuentes([1, 1, 1, 2, 2, 3], 2) -> [1, 2]
        elementos_frecuentes([4, 4, 4, 4], 1) -> [4]
        elementos_frecuentes([1, 2, 3, 4], 2) -> [1, 2]  # cualquier 2
    """
    # TODO: Implementar
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                        CÓDIGO DE PRUEBA - NO MODIFICAR
═══════════════════════════════════════════════════════════════════════════════
"""

if __name__ == "__main__":
    print("\n\n" + "=" * 70)
    print("PARCIAL SIMULADO 2 - NUEVA VARIACION")
    print("=" * 70)
    
    print("\n" + "=" * 70)
    print("PARTE 1: EXPRESIONES REGULARES")
    print("=" * 70)
    
    print("\n[TELEFONOS] Validacion de telefonos:")
    telefonos = [
        "310-5551234",
        "3105551234",
        "310 555 1234",
        "555-1234",
        "3215551234"
    ]
    for tel in telefonos:
        resultado = validar_telefono(tel)
        print(f"  {tel}: {'V' if resultado else 'X'}")
    
    print("\n[FECHAS] Validacion de fechas:")
    fechas = [
        "25/12/2024",
        "32/12/2024",
        "25/13/2024",
        "01/01/2000",
        "29/02/2020"
    ]
    for fecha in fechas:
        resultado = validar_fecha(fecha)
        print(f"  {fecha}: {'V' if resultado else 'X'}")
    
    print("\n[NUMEROS] Extraccion de numeros:")
    textos = [
        "Precio: $19.99, cantidad: 5, descuento: 10%",
        "No hay numeros aqui",
        "Este producto cuesta 1234.56 pesos"
    ]
    for texto in textos:
        numeros = extraer_numeros(texto)
        print(f"  '{texto}'")
        print(f"    -> {numeros}")
    
    print("\n" + "=" * 70)
    print("PARTE 2: RECURSION")
    print("=" * 70)
    
    print("\n[FACTORIAL] Factorial:")
    for n in [0, 1, 5, 10]:
        resultado = factorial_recursivo(n)
        print(f"  {n}! = {resultado}")
    
    print("\n[POTENCIA] Potencia:")
    potencias = [(2, 3), (5, 2), (3, 0), (10, 2)]
    for base, exp in potencias:
        resultado = potencia_recursiva(base, exp)
        print(f"  {base}^{exp} = {resultado}")
    
    print("\n[SUMA] Suma de N numeros:")
    for n in [1, 5, 10, 15]:
        resultado = suma_n_numeros(n)
        print(f"  Suma(1..{n}) = {resultado}")
    
    print("\n" + "=" * 70)
    print("PARTE 3: LISTAS ENLAZADAS")
    print("=" * 70)
    
    print("\n[ELIMINAR] Eliminar elemento:")
    lista3 = ListaEnlazada2()
    for val in [10, 20, 30, 40]:
        lista3.agregar_al_final(val)
    print(f"  Antes: 10 -> 20 -> 30 -> 40")
    lista3.eliminar(20)
    print(f"  Despues de eliminar 20: 10 -> 30 -> 40")
    
    print("\n[ULTIMO] Obtener ultimo elemento:")
    print(f"  Ultimo elemento: {lista3.obtener_ultimo()}")
    
    print("\n[LONGITUD] Longitud:")
    print(f"  Longitud: {lista3.longitud()}")
    
    print("\n[MAXIMO] Encontrar maximo:")
    lista_max = ListaEnlazada2()
    for val in [5, 2, 8, 3, 7]:
        lista_max.agregar_al_final(val)
    print(f"  Lista: 5 -> 2 -> 8 -> 3 -> 7")
    maximo = encontrar_maximo(lista_max)
    print(f"  Maximo: {maximo}")
    
    print("\n" + "=" * 70)
    print("PARTE 4: CONJUNTOS Y OPERACIONES")
    print("=" * 70)
    
    print("\n[UNION] Union de conjuntos:")
    conj1 = {1, 2}
    conj2 = {2, 3}
    conj3 = {3, 4}
    print(f"  {conj1} U {conj2} U {conj3} = {union_conjuntos(conj1, conj2, conj3)}")
    
    print("\n[DIFERENCIA] Diferencia simetrica:")
    a = {1, 2, 3}
    b = {2, 3, 4}
    print(f"  {a} D {b} = {diferencia_simetrica(a, b)}")
    
    print("\n[COMPLEMENTO] Complemento:")
    conjunto = {1, 3}
    universo = {1, 2, 3, 4, 5}
    print(f"  Complemento de {conjunto} en {universo} = {complemento(conjunto, universo)}")
    
    print("\n" + "=" * 70)
    print("PARTE 5: BUSQUEDA AVANZADA")
    print("=" * 70)
    
    print("\n[BUSCAR] Buscar todas las ocurrencias:")
    lista_busqueda = [1, 2, 3, 2, 4, 2, 5]
    print(f"  Lista: {lista_busqueda}")
    indices = buscar_todas_ocurrencias(lista_busqueda, 2)
    print(f"  Indices donde aparece 2: {indices}")
    
    print("\n" + "=" * 70)
    print("PARTE 6: ANALISIS Y MODIFICACION")
    print("=" * 70)
    
    print("\n[PARES] Pares que suman:")
    lista_pares = [1, 5, 3, 2, 4]
    suma = 6
    print(f"  Lista: {lista_pares}")
    print(f"  Pares que suman {suma}: {pares_suma(lista_pares, suma)}")
    
    print("\n[COMPRIMIR] Comprimir lista:")
    lista_comp = [1, 1, 2, 2, 2, 3, 3, 1]
    print(f"  Original: {lista_comp}")
    print(f"  Comprimida: {comprimir_lista(lista_comp)}")
    
    print("\n[FRECUENTES] Elementos frecuentes:")
    lista_freq = [1, 1, 1, 2, 2, 3]
    print(f"  Lista: {lista_freq}")
    print(f"  2 mas frecuentes: {elementos_frecuentes(lista_freq, 2)}")
    
    print("\n" + "=" * 70)
    print("OK PARCIAL SIMULADO 2 COMPLETADO")
    print("=" * 70)
