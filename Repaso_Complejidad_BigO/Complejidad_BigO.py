
# ============================================================
#                 REPASO DE COMPLEJIDAD BIG-O
#                    ALGORITMOS 4
# ============================================================
#
# Este archivo contiene:
#
# 1. Identificación de complejidades Big-O.
# 2. Mejor y peor caso.
# 3. Optimización de un código O(n²) a O(n).
# 4. Trucos para reconocer rápidamente las complejidades.
#
# IMPORTANTE:
# La idea no es memorizar las respuestas, sino aprender a
# reconocer qué está haciendo cada código y cómo analizarlo.
#
# ============================================================
# PUNTO 1. IDENTIFICAR LA COMPLEJIDAD BIG-O
# VALOR: 30%
# ============================================================


# ------------------------------------------------------------
# A) COMPLEJIDAD O(1) - CONSTANTE
# ------------------------------------------------------------

def func_a(lista):
    return lista[0] + lista[-1]


# EXPLICACIÓN:
#
# Esta función suma el primer y el último elemento de la lista.
#
# Aunque la lista tenga 10, 100 o 1000 elementos, solamente
# accedemos a dos posiciones específicas.
#
# No necesitamos recorrer toda la lista.
#
# COMPLEJIDAD: O(1)
#
# ¿CÓMO RECONOCERLA EN OTROS EJERCICIOS?
#
# Si encuentras operaciones como:
#
# - lista[0]
# - lista[5]
# - lista[-1]
# - Una suma o una comparación sencilla.
#
# Y no hay ciclos que dependan del tamaño de los datos,
# probablemente sea O(1).
#
# RECUERDA:
# Acceder directamente a una posición de una lista es O(1).


# ------------------------------------------------------------
# B) COMPLEJIDAD O(log n) - LOGARÍTMICA
# ------------------------------------------------------------

def func_b(n):
    i = 1

    while i < n:
        i *= 2


# EXPLICACIÓN:
#
# La variable i comienza valiendo 1.
# En cada vuelta se multiplica por 2.
#
# Los valores van siendo:
#
# 1 -> 2 -> 4 -> 8 -> 16 -> 32 -> 64...
#
# Observa que no aumenta de uno en uno.
# Cada vez se acerca mucho más rápido al valor de n.
#
# Por eso, aunque n sea muy grande, el ciclo necesita
# relativamente pocas repeticiones.
#
# COMPLEJIDAD: O(log n)
#
# ¿CÓMO RECONOCERLA EN OTROS EJERCICIOS?
#
# Fíjate si dentro de un while aparece algo parecido a:
#
# i = i * 2
# i = i * 3
# i = i // 2
#
# Es decir, si la variable se multiplica o se divide
# por un número en cada vuelta.
#
# Eso normalmente indica O(log n).
#
# OJO:
# Si en vez de multiplicar o dividir, haces i = i + 1,
# normalmente estaríamos hablando de O(n).


# ------------------------------------------------------------
# C) COMPLEJIDAD O(n²) - CUADRÁTICA
# ------------------------------------------------------------

def func_c(lista):
    for x in lista:
        for y in lista:
            print(x, y)


# EXPLICACIÓN:
#
# Tenemos dos ciclos for.
#
# El primero recorre toda la lista.
# Por cada vuelta del primer ciclo, el segundo también
# recorre toda la lista.
#
# Si la lista tiene 5 elementos:
#
# Primer ciclo: 5 vueltas.
# Segundo ciclo: 5 vueltas por cada vuelta del primero.
#
# Total: 5 x 5 = 25 repeticiones.
#
# Si la lista tiene n elementos:
#
# n x n = n²
#
# COMPLEJIDAD: O(n²)
#
# ¿CÓMO RECONOCERLA EN OTROS EJERCICIOS?
#
# Cuando encuentres un ciclo dentro de otro ciclo,
# revisa cuántas veces se repite cada uno.
#
# Si ambos recorren una lista de tamaño n:
# O(n x n) = O(n²).
#
# IMPORTANTE:
# No basta con contar cuántos for hay.
# Debes mirar si están uno dentro del otro.


# ------------------------------------------------------------
# D) COMPLEJIDAD O(n) - LINEAL
# ------------------------------------------------------------

def func_d(lista):
    conteo = {}

    for x in lista:
        conteo[x] = conteo.get(x, 0) + 1

    return conteo


# EXPLICACIÓN:
#
# Primero creamos un diccionario vacío llamado conteo.
#
# Un diccionario guarda información mediante:
#
# CLAVE : VALOR
#
# Por ejemplo:
#
# "manzana" : 2
# "pera"    : 3
# "uva"     : 1
#
# El ciclo recorre la lista una sola vez.
#
# Esta instrucción:
#
# conteo.get(x, 0)
#
# Busca si el elemento x ya existe en el diccionario.
# Si existe, devuelve su cantidad.
# Si no existe, devuelve 0.
#
# Después sumamos 1 para contar una nueva aparición.
#
# EJEMPLO:
#
# lista = ["manzana", "pera", "manzana"]
#
# Primera vuelta:
# manzana no existe, entonces comienza en 0 y suma 1.
#
# Segunda vuelta:
# pera no existe, entonces comienza en 0 y suma 1.
#
# Tercera vuelta:
# manzana ya existe y tenía 1.
# Entonces ahora tiene 2.
#
# Resultado:
# {"manzana": 2, "pera": 1}
#
# COMPLEJIDAD: O(n) PROMEDIO.
#
# ¿CÓMO RECONOCERLA EN OTROS EJERCICIOS?
#
# Si encuentras:
#
# - Un diccionario vacío.
# - Un solo ciclo que recorre la lista.
# - Operaciones como diccionario.get() para consultar.
#
# Generalmente puede ser O(n), porque consultar o actualizar
# una clave de un diccionario cuesta O(1) en promedio.
#
# IMPORTANTE:
# No confundas el diccionario con un ciclo.
# El diccionario no recorre toda la lista por sí solo.


# ------------------------------------------------------------
# E) COMPLEJIDAD O(2^n) - EXPONENCIAL
# ------------------------------------------------------------

def func_e(n):
    if n <= 0:
        return 0

    return func_e(n - 1) + func_e(n - 1)


# EXPLICACIÓN:
#
# Esta función utiliza RECURSIVIDAD.
#
# La recursividad ocurre cuando una función se llama a sí misma.
#
# Tenemos una condición:
#
# if n <= 0:
#     return 0
#
# Esta condición es el caso base.
# Sirve para detener las llamadas.
#
# Pero cuando n es mayor que 0, la función se llama DOS veces:
#
# func_e(n - 1)
# func_e(n - 1)
#
# Esto provoca que las llamadas crezcan muy rápidamente.
#
# Por ejemplo, la cantidad total de llamadas es:
#
# n = 0 -> 1 llamada
# n = 1 -> 3 llamadas
# n = 2 -> 7 llamadas
# n = 3 -> 15 llamadas
# n = 4 -> 31 llamadas
#
# COMPLEJIDAD: O(2^n)
#
# ¿CÓMO RECONOCERLA EN OTROS EJERCICIOS?
#
# Primero busca si la función se llama a sí misma.
#
# Después fíjate cuántas llamadas nuevas genera:
#
# - Una llamada recursiva por ejecución: normalmente O(n).
# - Dos llamadas recursivas por ejecución: puede ser O(2^n).
#
# OJO:
# No todas las funciones recursivas tienen la misma complejidad.
# Debes revisar cuántas llamadas generan y cómo cambia n.


# ============================================================
# RESUMEN DEL PUNTO 1
# ============================================================
#
# func_a -> O(1)
# func_b -> O(log n)
# func_c -> O(n²)
# func_d -> O(n)
# func_e -> O(2^n)
#
# ============================================================
# PUNTO 2. MEJOR Y PEOR CASO
# VALOR: 20%
# ============================================================


# ------------------------------------------------------------
# ¿QUÉ SIGNIFICAN MEJOR Y PEOR CASO?
# ------------------------------------------------------------
#
# MEJOR CASO:
# Es cuando el programa necesita hacer menos trabajo.
#
# PEOR CASO:
# Es cuando el programa necesita hacer más trabajo.
#
# IMPORTANTE:
# No siempre significa que el código sea rápido o lento.
# Depende de los datos que recibe y de cómo está escrito.


# ------------------------------------------------------------
# A) ELIMINAR DUPLICADOS
# ------------------------------------------------------------

def eliminar_duplicados(lista):
    resultado = []

    for x in lista:
        if x not in resultado:
            resultado.append(x)

    return resultado


# EXPLICACIÓN:
#
# Creamos una lista vacía llamada resultado.
#
# Después recorremos la lista original.
#
# La condición:
#
# if x not in resultado:
#
# Comprueba si el elemento ya está en la lista resultado.
#
# Si no está, lo agregamos.
# Si ya está, no hacemos nada.
#
# Así evitamos guardar elementos repetidos.
#
# EJEMPLO:
#
# Entrada:
# [2, 2, 3, 4, 4]
#
# Resultado:
# [2, 3, 4]
#
#
# ------------------ MEJOR CASO ------------------------------
#
# ¿CUÁNDO OCURRE?
#
# Cuando todos los elementos de la lista son iguales.
#
# Ejemplo:
#
# [5, 5, 5, 5, 5]
#
# ¿POR QUÉ?
#
# El primer 5 se agrega a resultado.
# Cuando aparecen los siguientes 5, el programa encuentra
# rápidamente que ese elemento ya está en resultado.
#
# Como resultado solamente tiene un elemento,
# las búsquedas son muy pequeñas.
#
# El ciclo principal recorre n elementos.
#
# MEJOR CASO: O(n)
#
#
# ------------------ PEOR CASO ------------------------------
#
# ¿CUÁNDO OCURRE?
#
# Cuando todos los elementos son diferentes.
#
# Ejemplo:
#
# [1, 2, 3, 4, 5]
#
# ¿POR QUÉ?
#
# Como todos son diferentes, cada elemento se agrega
# a la lista resultado.
#
# Pero la condición:
#
# x not in resultado
#
# tiene que revisar cada vez una lista más grande.
#
# Por ejemplo:
#
# Primera vuelta: busca en 0 elementos.
# Segunda vuelta: busca en 1 elemento.
# Tercera vuelta: busca en 2 elementos.
# Cuarta vuelta: busca en 3 elementos.
# Quinta vuelta: busca en 4 elementos.
#
# Cada búsqueda puede tardar más que la anterior.
#
# PEOR CASO: O(n²)
#
#
# ¿CÓMO RECONOCER ESTE TIPO DE EJERCICIO?
#
# Fíjate especialmente en:
#
# if x not in resultado
#
# Buscar un elemento dentro de una lista puede costar O(n).
#
# Si esa búsqueda está dentro de un for que también recorre
# n elementos, el peor caso puede ser O(n²).
#
# RECUERDA:
# Un for puede ser O(n), pero si dentro tiene una búsqueda
# que también cuesta O(n), el trabajo puede llegar a O(n²).


# ------------------------------------------------------------
# EJEMPLO ADICIONAL: BUSCAR UN VALOR
# ------------------------------------------------------------
#
# OJO:
# El enunciado original menciona buscar_valor, pero el código
# que aparece en el examen es eliminar_duplicados.
#
# Este es un ejemplo diferente de búsqueda para que sepas
# resolverlo si el profesor realmente pregunta por buscar_valor.


def buscar_valor(lista, valor):
    for x in lista:
        if x == valor:
            return True

    return False


# EXPLICACIÓN:
#
# El ciclo revisa los elementos uno por uno.
#
# Si encuentra el valor, devuelve True y termina.
# Si llega al final sin encontrarlo, devuelve False.
#
#
# MEJOR CASO:
#
# El valor está en la primera posición.
#
# El programa lo encuentra inmediatamente.
#
# COMPLEJIDAD: O(1)
#
#
# PEOR CASO:
#
# El valor está en la última posición o no está en la lista.
#
# El programa necesita revisar todos los elementos.
#
# COMPLEJIDAD: O(n)
#
#
# ¿CÓMO RECONOCERLO?
#
# Si encuentras un return dentro de un for, pregúntate:
#
# ¿Puede terminar antes de recorrer toda la lista?
#
# Si puede terminar antes, analiza el mejor caso.
# Si debe llegar hasta el final, analiza el peor caso.


# ------------------------------------------------------------
# B) BUBBLE SORT - ORDENAMIENTO BURBUJA
# ------------------------------------------------------------

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        intercambio = False

        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True

        if not intercambio:
            break

    return lista


# EXPLICACIÓN:
#
# Bubble Sort es un método para ordenar una lista.
#
# Compara elementos que están uno al lado del otro.
#
# Si el elemento de la izquierda es mayor que el de la derecha,
# los intercambia.
#
# EJEMPLO:
#
# Lista inicial:
# [5, 2, 4, 1]
#
# Compara 5 y 2:
# Como 5 es mayor, los intercambia.
# [2, 5, 4, 1]
#
# Compara 5 y 4:
# Los intercambia.
# [2, 4, 5, 1]
#
# Compara 5 y 1:
# Los intercambia.
# [2, 4, 1, 5]
#
# Continúa haciendo lo mismo hasta ordenar la lista.
#
#
# ¿PARA QUÉ SIRVE intercambio?
#
# Comienza en False.
#
# Si se realiza algún intercambio, cambia a True.
#
# Si termina una pasada completa y sigue en False,
# significa que no hubo ningún intercambio.
#
# Eso quiere decir que la lista ya estaba ordenada.
#
# Por eso aparece:
#
# if not intercambio:
#     break
#
# El break permite detener el ciclo antes de tiempo.
#
#
# ------------------ MEJOR CASO ------------------------------
#
# ¿CUÁNDO OCURRE?
#
# Cuando la lista ya está ordenada.
#
# Ejemplo:
#
# [1, 2, 3, 4, 5]
#
# ¿POR QUÉ?
#
# El programa compara los elementos.
# Como ya están ordenados, no necesita intercambiar ninguno.
#
# intercambio continúa siendo False.
#
# Entonces ejecuta break y termina después de una sola pasada.
#
# Esa pasada revisa aproximadamente n elementos.
#
# MEJOR CASO: O(n)
#
#
# ------------------ PEOR CASO ------------------------------
#
# ¿CUÁNDO OCURRE?
#
# Cuando la lista está ordenada al revés.
#
# Ejemplo:
#
# [5, 4, 3, 2, 1]
#
# ¿POR QUÉ?
#
# El programa tiene que hacer muchas comparaciones
# e intercambios para ordenar todos los elementos.
#
# Los ciclos se repiten varias veces.
#
# El trabajo crece aproximadamente como:
#
# n x n = n²
#
# PEOR CASO: O(n²)
#
#
# ¿CÓMO RECONOCERLO EN OTROS EJERCICIOS?
#
# Fíjate en:
#
# 1. Si hay dos ciclos for anidados.
# 2. Si hay comparaciones entre elementos vecinos.
# 3. Si aparece un intercambio de posiciones.
# 4. Si hay un break que puede detener el ciclo antes.
#
# IMPORTANTE:
# Si el profesor elimina el break o la condición que permite
# detener el algoritmo antes, el mejor caso podría cambiar.
#
# No asumas que todos los Bubble Sort tienen mejor caso O(n).
# En este código es O(n) precisamente por el break.


# ============================================================
# RESUMEN DEL PUNTO 2
# ============================================================
#
# ELIMINAR DUPLICADOS:
#
# Mejor caso:
# Todos los elementos iguales.
# O(n)
#
# Peor caso:
# Todos los elementos diferentes.
# O(n²)
#
#
# BUSCAR VALOR:
#
# Mejor caso:
# El valor está en la primera posición.
# O(1)
#
# Peor caso:
# El valor está al final o no existe.
# O(n)
#
#
# BUBBLE SORT:
#
# Mejor caso:
# La lista ya está ordenada.
# O(n)
#
# Peor caso:
# La lista está ordenada al revés.
# O(n²)
#
# ============================================================
# PUNTO 3. OPTIMIZAR UN CÓDIGO O(n²) A O(n)
# VALOR: 50%
# ============================================================


# ------------------------------------------------------------
# A) VERSIÓN LENTA: O(n²)
# ------------------------------------------------------------

def mas_frecuente_lento(lista):
    """
    Busca el elemento que más veces aparece en una lista.
    Esta versión tiene complejidad O(n²).
    """

    max_elem = lista[0]
    max_count = 0

    for x in lista:
        count = 0

        for y in lista:
            if y == x:
                count += 1

        if count > max_count:
            max_count = count
            max_elem = x

    return max_elem


# EXPLICACIÓN:
#
# Esta función busca el elemento que más se repite.
#
# Primero:
#
# max_elem = lista[0]
# max_count = 0
#
# Guardamos un elemento inicial y una cantidad máxima inicial.
#
# Después tenemos dos ciclos for anidados.
#
# El primer ciclo toma un elemento x.
#
# El segundo ciclo recorre toda la lista para contar
# cuántas veces aparece ese elemento x.
#
# Cuando termina de contar, compara esa cantidad con
# max_count para saber si encontró un elemento más frecuente.
#
# ¿POR QUÉ ES O(n²)?
#
# Porque por cada elemento de la lista volvemos a recorrer
# la lista completa.
#
# Si hay n elementos:
#
# n x n = n²
#
# Por eso es O(n²).
#
# PROBLEMA:
#
# Estamos repitiendo muchas búsquedas.
# Podemos evitarlo utilizando un diccionario para guardar
# las cantidades de cada elemento.


# ------------------------------------------------------------
# B) VERSIÓN RÁPIDA: O(n)
# ------------------------------------------------------------

def mas_frecuente_rapido(lista):
    """
    Busca el elemento que más veces aparece en una lista.
    Utiliza un diccionario para contar las apariciones.
    Complejidad O(n) promedio.
    """

    # PASO 1:
    # Creamos un diccionario vacío.
    #
    # En este diccionario guardaremos:
    #
    # elemento : cantidad de apariciones

    conteo = {}

    # PASO 2:
    # Recorremos la lista una sola vez para contar
    # cuántas veces aparece cada elemento.

    for x in lista:

        # Si x ya existe, obtenemos su cantidad.
        # Si todavía no existe, comenzamos desde 0.
        #
        # Después sumamos 1.

        conteo[x] = conteo.get(x, 0) + 1

    # PASO 3:
    # Guardamos un elemento inicial como el más frecuente.
    #
    # Este código, al igual que la versión original,
    # supone que la lista no está vacía.

    max_elem = lista[0]

    # PASO 4:
    # Recorremos las claves del diccionario.
    #
    # Ya no necesitamos recorrer toda la lista original
    # para volver a contar las apariciones.
    #
    # Simplemente consultamos las cantidades guardadas.

    for x in conteo:

        # Comparamos la cantidad del elemento actual
        # con la cantidad del elemento más frecuente.

        if conteo[x] > conteo[max_elem]:

            # Si encontramos uno que aparece más veces,
            # actualizamos el elemento más frecuente.

            max_elem = x

    # PASO 5:
    # Devolvemos el elemento que más se repite.

    return max_elem


# ------------------------------------------------------------
# EXPLICACIÓN DE POR QUÉ LA VERSIÓN RÁPIDA ES O(n)
# ------------------------------------------------------------
#
# PRIMER CICLO:
#
# for x in lista:
#
# Recorre la lista completa.
# Complejidad: O(n).
#
#
# SEGUNDO CICLO:
#
# for x in conteo:
#
# Recorre las claves del diccionario.
# Como máximo puede haber n claves diferentes.
# Complejidad: O(n).
#
#
# SON DOS CICLOS SEPARADOS, NO ESTÁN ANIDADOS.
#
# Por eso sumamos:
#
# O(n) + O(n) = O(2n)
#
# En Big-O eliminamos las constantes.
#
# Resultado:
#
# O(n)
#
#
# ¿POR QUÉ UTILIZAMOS UN DICCIONARIO?
#
# Porque nos permite guardar cuántas veces aparece
# cada elemento y consultar esa cantidad rápidamente.
#
# En promedio, consultar una clave del diccionario cuesta O(1).
#
# Así evitamos recorrer la lista completa una y otra vez.
#
#
# EJEMPLO:
#
# lista = ["rojo", "azul", "rojo", "verde", "rojo", "azul"]
#
# El diccionario queda:
#
# {
#     "rojo": 3,
#     "azul": 2,
#     "verde": 1
# }
#
# El elemento más frecuente es:
#
# "rojo"
#
#
# IMPORTANTE:
# Esta versión mantiene el comportamiento de la versión lenta
# cuando hay empate: devuelve el primero que apareció en la lista.
#
# También supone que la lista no está vacía y que sus elementos
# pueden utilizarse como claves de un diccionario.
#
# ============================================================
# GUÍA RÁPIDA PARA RECONOCER COMPLEJIDADES
# ============================================================


# ------------------------------------------------------------
# 1. O(1) - CONSTANTE
# ------------------------------------------------------------
#
# ¿QUÉ DEBES MIRAR?
#
# Operaciones que no dependen del tamaño de la lista.
#
# Ejemplos:
#
# lista[0]
# lista[-1]
# a = 5 + 3
#
# No hay un ciclo que recorra n elementos.
#
# RECUERDA:
# Acceder directamente a una posición normalmente es O(1).


# ------------------------------------------------------------
# 2. O(log n) - LOGARÍTMICA
# ------------------------------------------------------------
#
# ¿QUÉ DEBES MIRAR?
#
# Un while donde una variable se multiplica o divide
# por un número en cada vuelta.
#
# Ejemplos:
#
# i = i * 2
# i = i // 2
#
# Los valores avanzan rápidamente.
#
# RECUERDA:
# Si se duplica o se divide entre 2 en cada vuelta,
# normalmente es O(log n).


# ------------------------------------------------------------
# 3. O(n) - LINEAL
# ------------------------------------------------------------
#
# ¿QUÉ DEBES MIRAR?
#
# Un ciclo que recorre una lista una sola vez.
#
# Ejemplo:
#
# for x in lista:
#     print(x)
#
# Si la lista tiene 100 elementos, hace 100 vueltas.
#
# RECUERDA:
# Un recorrido sencillo normalmente es O(n).


# ------------------------------------------------------------
# 4. O(n log n) - LINEAL LOGARÍTMICA
# ------------------------------------------------------------
#
# ¿QUÉ DEBES MIRAR?
#
# Un ciclo que se repite n veces y dentro tiene
# otro proceso que se repite log n veces.
#
# Ejemplo:
#
# for x in lista:
#     i = 1
#     while i < n:
#         i *= 2
#
# El for hace n vueltas.
# El while hace log n vueltas por cada vuelta del for.
#
# Multiplicamos:
#
# O(n) x O(log n) = O(n log n).


# ------------------------------------------------------------
# 5. O(n²) - CUADRÁTICA
# ------------------------------------------------------------
#
# ¿QUÉ DEBES MIRAR?
#
# Dos ciclos anidados que recorren n elementos.
#
# Ejemplo:
#
# for x in lista:
#     for y in lista:
#         print(x, y)
#
# Multiplicamos:
#
# O(n) x O(n) = O(n²).
#
# TAMBIÉN PUEDE APARECER CUANDO:
#
# Hay un for que recorre n elementos y dentro se hace
# una búsqueda en una lista que también puede tener n elementos.
#
# Ejemplo:
#
# for x in lista:
#     if x not in resultado:
#         resultado.append(x)
#
# En el peor caso, la búsqueda puede revisar muchos elementos.
# Por eso puede llegar a O(n²).


# ------------------------------------------------------------
# 6. O(2^n) - EXPONENCIAL
# ------------------------------------------------------------
#
# ¿QUÉ DEBES MIRAR?
#
# Una función recursiva que genera varias llamadas nuevas.
#
# Ejemplo:
#
# def funcion(n):
#     if n <= 0:
#         return
#     funcion(n - 1)
#     funcion(n - 1)
#
# Cada llamada genera dos llamadas nuevas.
#
# Esto hace que el número de llamadas crezca muy rápido.
#
# En este ejemplo la complejidad es O(2^n).


# ============================================================
# TRUCOS PARA ANALIZAR VARIOS CICLOS
# ============================================================


# ------------------------------------------------------------
# A) CICLOS SEPARADOS: SE SUMAN
# ------------------------------------------------------------
#
# Ejemplo:
#
# for x in lista:
#     print(x)
#
# for y in lista:
#     print(y)
#
# Cada ciclo cuesta O(n).
#
# Sumamos:
#
# O(n) + O(n) = O(2n)
#
# Eliminamos la constante:
#
# O(n)
#
# RECUERDA:
# Si están separados, se suman.


# ------------------------------------------------------------
# B) CICLOS ANIDADOS: SE MULTIPLICAN
# ------------------------------------------------------------
#
# Ejemplo:
#
# for x in lista:
#     for y in lista:
#         print(x, y)
#
# Cada ciclo cuesta O(n).
#
# Multiplicamos:
#
# O(n) x O(n) = O(n²)
#
# RECUERDA:
# Si uno está dentro del otro, se multiplican.


# ------------------------------------------------------------
# C) LISTAS DE DIFERENTES TAMAÑOS
# ------------------------------------------------------------
#
# Ejemplo:
#
# for x in lista1:
#     print(x)
#
# for y in lista2:
#     print(y)
#
# Si lista1 tiene n elementos y lista2 tiene m:
#
# O(n) + O(m) = O(n + m)
#
#
# OTRO EJEMPLO:
#
# for x in lista1:
#     for y in lista2:
#         print(x, y)
#
# Si lista1 tiene n elementos y lista2 tiene m:
#
# O(n) x O(m) = O(n x m)
#
#
# RECUERDA:
# No asumas que todas las listas tienen el mismo tamaño.
# Si el ejercicio utiliza n y m, conserva ambas letras.


# ------------------------------------------------------------
# D) CUANDO HAY VARIOS TÉRMINOS, NOS QUEDAMOS CON EL MAYOR
# ------------------------------------------------------------
#
# Ejemplo:
#
# O(n) + O(n²)
#
# Resultado:
# O(n²)
#
#
# Otro ejemplo:
#
# O(n) + O(log n)
#
# Resultado:
# O(n)
#
#
# Otro ejemplo:
#
# O(n²) + O(log n)
#
# Resultado:
# O(n²)
#
#
# ¿POR QUÉ?
#
# Porque Big-O se queda con el término que crece más rápido
# cuando el tamaño de los datos aumenta.
#
# También eliminamos las constantes:
#
# O(3n) = O(n)
# O(5n²) = O(n²)


# ============================================================
# TIPS PARA MEJOR Y PEOR CASO
# ============================================================
#
# Cuando el profesor pregunte por mejor y peor caso,
# no respondas solamente mirando cuántos ciclos hay.
#
# Debes observar cómo cambian los datos.
#
#
# 1. SI HAY UN RETURN DENTRO DE UN FOR:
#
# Pregúntate:
# ¿Puede encontrar lo que busca en la primera vuelta?
#
# Si sí:
# Puede tener mejor caso O(1).
#
# Si tiene que revisar toda la lista:
# Puede tener peor caso O(n).
#
#
# 2. SI HAY UN IF DENTRO DE UN FOR:
#
# Pregúntate:
# ¿La condición hace que el programa deje de trabajar antes?
#
# Si hay un return o break, revisa cuándo se activa.
#
# Si solamente ejecuta una instrucción y continúa,
# el ciclo puede seguir recorriendo toda la lista.
#
#
# 3. SI HAY UNA BÚSQUEDA DENTRO DE UN FOR:
#
# Pregúntate:
# ¿La búsqueda puede revisar una lista que va creciendo?
#
# Si sí, el peor caso puede ser O(n²).
#
#
# 4. SI HAY UN BREAK:
#
# Pregúntate:
# ¿En qué momento se puede detener el ciclo?
#
# Puede hacer que el mejor caso sea más rápido.
#
# Ejemplo:
# Bubble Sort puede terminar después de una sola pasada
# cuando la lista ya está ordenada.
#
#
# 5. SI HAY RECURSIVIDAD:
#
# Pregúntate:
# ¿Cuántas llamadas nuevas genera cada llamada?
#
# Una llamada no significa automáticamente O(n).
# Dos llamadas no significan automáticamente O(2^n).
# Hay que revisar cómo disminuye n y cómo se ramifican
# las llamadas.


# ============================================================
# ERRORES COMUNES QUE DEBES EVITAR EN EL EXAMEN
# ============================================================
#
# ERROR 1:
# Pensar que tres for siempre significan O(n³).
#
# CORRECCIÓN:
# Mira si están separados o anidados.
#
#
# ERROR 2:
# Pensar que todo for es O(n).
#
# CORRECCIÓN:
# Mira qué instrucciones tiene dentro.
# Una búsqueda dentro del ciclo puede aumentar la complejidad.
#
#
# ERROR 3:
# Multiplicar ciclos que están separados.
#
# CORRECCIÓN:
# Ciclos separados se suman.
#
#
# ERROR 4:
# Sumar ciclos que están anidados.
#
# CORRECCIÓN:
# Ciclos anidados se multiplican.
#
#
# ERROR 5:
# Olvidar el break o el return.
#
# CORRECCIÓN:
# Revisa si el programa puede detenerse antes de recorrer
# todos los elementos.
#
#
# ERROR 6:
# Confundir una lista con un diccionario.
#
# CORRECCIÓN:
# Buscar un elemento en una lista puede costar O(n).
# Consultar una clave de un diccionario cuesta O(1)
# en promedio.
#
#
# ERROR 7:
# Creer que todos los algoritmos recursivos son O(2^n).
#
# CORRECCIÓN:
# Mira cuántas llamadas genera cada ejecución y cómo cambia n.


# ============================================================
# TABLA FINAL PARA MEMORIZAR
# ============================================================
#
# O(1)       -> Acceso directo a una posición.
#
# O(log n)   -> Un while que multiplica o divide una variable.
#
# O(n)       -> Un recorrido sencillo de n elementos.
#
# O(n log n) -> Un ciclo n con otro proceso log n dentro.
#
# O(n²)      -> Dos ciclos anidados de tamaño n.
#
# O(2^n)     -> Recursividad con crecimiento exponencial.
#
#
# REGLAS:
#
# Ciclos separados       -> SUMAR.
# Ciclos anidados        -> MULTIPLICAR.
# Diferentes tamaños     -> CONSERVAR n y m.
# Términos juntos        -> QUEDARSE CON EL MAYOR.
# Constantes             -> ELIMINARLAS.
# Mejor caso             -> MENOS TRABAJO.
# Peor caso              -> MÁS TRABAJO.
#
# ============================================================
# FIN DEL REPASO
# ============================================================
