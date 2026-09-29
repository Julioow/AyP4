"""
═══════════════════════════════════════════════════════════════════════════════
                QUIZ B - ALGORITMOS DE ORDENAMIENTO
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
- En cada caso debes:
    1. ELEGIR el mejor algoritmo justificando complejidad temporal,
       espacial y estabilidad.
    2. EXPLICAR brevemente por qué los OTROS algoritmos no son los más
       adecuados.
    3. IMPLEMENTAR el algoritmo aplicado a la estructura de datos del caso.

═══════════════════════════════════════════════════════════════════════════════
"""

import time
import random


# ═══════════════════════════════════════════════════════════════════════════════
# CASO 1 (1.7): Sistema de Triaje en Urgencias
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
Un hospital atiende ~80,000 pacientes al mes en urgencias. Cada paciente
recibe una PRIORIDAD entera del 1 al 5 al ingresar (1 = crítico, 5 = leve).
Al final de cada turno se genera un reporte ordenado por prioridad para
auditar la atención.

Cada registro tiene esta estructura:

    {
      "id_atencion": 33421,
      "paciente": "Maria Lopez",
      "prioridad": 2,                # entero 1..5
      "hora_ingreso": "08:14",       # cuándo LLEGÓ a urgencias
      "estado": "atendido"           # "atendido" | "abandono"
    }

REGLAS DEL REPORTE:
  R1) Solo entran al reporte los pacientes con estado "atendido".
  R2) Se ordena ASCENDENTE por prioridad (los críticos primero).
  R3) Si dos pacientes tienen la misma prioridad, debe quedar primero
      el que LLEGÓ ANTES (orden cronológico de ingreso). Esto importa
      porque el hospital evalúa tiempos de espera y el orden de atención
      esperado dentro de cada nivel de gravedad.

ANÁLISIS (justifica de forma concreta, no genérica):
  1. ¿Qué algoritmo eliges? R/: Para este caso el mejor algoritmo es el counting sort porque la secuencia ordena numeros enteros de muy poquita longitud.el bucket no es adecuado ya que divide los archivos y no hay necesidad, el radix aunque es un algoritmo de ordenamiento lineal y sirve para numeros no es el mejor para este caso ya que se utiliza para ordenar numeros enteros de longitud de los numeros la cual no es necesaria en este caso, el merge sort no es adecuado porque tiene una complejidad temporal de O(n log n) y el quicksort tampoco es adecuado porque tiene una complejidad temporal de O(n log n) en promedio y O(n a la2) en el peor caso, el heap sort no es adecuado porque tiene una complejidad temporal de O(n log n) y no es estable, el insertion sort no es adecuado porque tiene una complejidad temporal de O(n a la 2) lo cual lo hace muy ineficiente, el insertion sort no es adecuado porque tiene una complejidad temporal de O(n a la 2) y tampoco es estable
  2. Complejidad temporal: R/= O(80,000+5)
  3. Complejidad espacial: R/= O(80,000+5) 
  4. Estabilidad: ¿es estable? ¿por qué importa AQUÍ? R/= Si es estable porque mantiene el orden original de los elementos con la misma clave a pesar de que ordene y mueva tantos


IMPLEMENTACIÓN:
  Implementa `ordenar_pacientes(pacientes)` que:
    - Filtre los abandonos.
    - Ordene por 'prioridad' manteniendo el orden de ingreso en empates.
    - Reciba la lista TAL CUAL llega (puede tener abandonos mezclados).
    - Devuelva una NUEVA lista (no mutar la original).

"""


def ordenar_pacientes(pacientes):
    """

    """

    # Encuentra el valor máximo en el arreglo
    max_val = max(pacientes)
    min_val = min(pacientes)

    # Rango de los números en el arreglo
    rango = max_val - min_val + 1

    # Inicializa el arreglo de conteo
    conteo = [0] * rango

    # Cuenta la ocurrencia de cada elemento
    for paciente in pacientes:
        conteo[paciente['prioridad'] - min_val] += 1

    # Modifica el arreglo de conteo para almacenar posiciones acumuladas
    for i in range(1, rango):
        conteo[i] += conteo[i - 1]

    # Crea el arreglo de salida
    salida = [0] * len(pacientes)

    # Coloca los elementos en la posición correcta (recorrido inverso para estabilidad)
    for paciente in reversed(pacientes):
        salida[conteo[paciente['prioridad'] - min_val] - 1] = paciente
        conteo[paciente['prioridad'] - min_val] -= 1

    # Copia los elementos ordenados al arreglo original
    for i in range(len(pacientes)):
        pacientes[i] = salida[i]



# ══════════════════════════════════════════════════════════════════════════════
# CASO 2 (1.7): Ranking de Productos en E-commerce
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
Una tienda en línea tiene 2 MILLONES de productos y debe ordenarlos por
RATING promedio para mostrarlos en la página principal. Al cierre de
cada día se reconstruye el ranking completo.

Cada producto es una tupla:

    (id_producto, rating, ventas_mes)
    # rating: float de 0.0 a 5.0 (con decimales)
    # ventas_mes: entero, ventas del último mes

RESTRICCIONES OPERACIONALES:
  R1) El servidor tiene RAM SUFICIENTE para usar memoria auxiliar.
  R2) El proceso debe ser PREDECIBLE.
  R3) Si dos productos tienen el mismo rating, debe respetarse el orden
      original (que viene priorizado por ventas del mes).

ANÁLISIS:
  1. ¿Qué algoritmo eliges? R/: Merge Sort porque es un algoritmo de ordenamiento estable y tiene una complejidad temporal de O(n log n) lo cual es adecuado para ordenar 2 millones de productos, el counting sort no es adecuado porque el rating es un float con decimales y no se puede usar, el radix sort no es adecuado porque el rating es un float con decimales y no se puede usar, el bucket sort no es adecuado porque el rating es un float con decimales y no se puede usar por que seria ineficiente, el quicksort no es adecuado porque tiene una complejidad temporal de O(n log n) en promedio pero O(n a la 2) en el peor caso, el heap sort no es adecuado porque tiene una complejidad temporal de O(n log n) y no es estable, el insertion sort no es adecuado porque tiene una complejidad temporal de O(n a la 2) lo cual lo hace muy ineficiente.
  2. Complejidad temporal(peor / promedio): R/:O(n log n) con n=2,000,000
  3. Complejidad espacial: R/: O(n)
  4. Estabilidad: Si es estable, es importante para el ranking saber cual es el primero en la lista y asi mantener la integridad del ranking 



IMPLEMENTACIÓN:
  Implementa `ordenar_productos(lista)` que:
    - Reciba la lista de tuplas (id, rating, ventas_mes).
    - Ordene por RATING DESCENDENTE (mayor rating primero).
    - Conserve el orden original cuando hay empate.
    - Devuelva la lista ordenada.

"""


def ordenar_productos(lista, left, middle, right):
    """

    """

    # Tamaño de las sublistas
    n1 = middle - left + 1
    n2 = right - middle

    # Crear listas temporales
    L = lista[left:middle + 1]
    R = lista[middle + 1:right + 1]

    # Índices iniciales de las sublistas y de la lista principal
    i = j = 0
    k = left

    # Combinar las sublistas siguiendo las reglas de ordenamiento
    while i < n1 and j < n2:
        if L[i][1] < R[j][1] or (L[i][1] == R[j][1] and L[i][2] < R[j][2]):
            lista[k] = L[i]
            i += 1
        else:
            lista[k] = R[j]
            j += 1
        k += 1

    # Copiar los elementos restantes de L si quedan
    while i < n1:
        lista[k] = L[i]
        i += 1
        k += 1

    # Copiar los elementos restantes de R si quedan
    while j < n2:
        lista[k] = R[j]
        j += 1
        k += 1


def mergesort(lista, left, right):
    if left < right:
        # Encontrar el punto medio de la lista
        middle = (left + right) // 2

        # Ordenar la primera y la segunda mitad
        mergesort(lista, left, middle)
        mergesort(lista, middle + 1, right)

        # Combinar las dos mitades ordenadas
        ordenar_productos(lista, left, middle, right)
 
# ═══════════════════════════════════════════════════════════════════════════════
# CASO 3 (1.6): Sistema de Códigos de Barras EAN-13
# ══════════════════════════════════════════════════════════════════════════════
"""
CONTEXTO:
---------
Una cadena de supermercados tiene 10 MILLONES de códigos de barras EAN-13
(números enteros de exactamente 13 dígitos) en su inventario y necesita
ordenarlos para compararlos contra el catálogo del proveedor y detectar
productos faltantes.

ESTRATEGIA OPERACIONAL:
  Paso A) Ordenar todos los códigos.
  Paso B) Recorrido lineal cruzando con el catálogo del proveedor.

RESTRICCIONES:
  R1) El rango es enorme (10^13), no se puede crear un arreglo de ese
      tamaño en memoria.
  R2) Se requiere tiempo CASI LINEAL.

ANÁLISIS:
  1. ¿Qué algoritmo eliges? Radix Sort porque es un algoritmo de ordenamiento lineal que es adecuado para ordenar números enteros de longitud fija y no requiere crear un arreglo del tamaño del rango, el counting sort no es adecuado porque el rango de los números es demasiado grande (10^13), el bucket sort no es adecuado porque requeriría 10^13 cubetas lo cual seria casi imposible, el merge sort no es adecuado porque tiene una complejidad temporal de O(n log n) lo cual no cumple con la restriccion de tiempo casi lineal, el quicksort no es adecuado porque tiene una complejidad temporal de O(n log n) en promedio pero O(n a la 2) en el peor caso, el heap sort no es adecuado porque tiene una complejidad temporal de O(n log n) y no es estable, el insertion sort no es adecuado porque tiene una complejidad temporal de O(n a la 2) lo cual lo hace muy ineficiente.
  2. Complejidad temporal: O(d(n+b)) con d=13 y b=10 lo cual es O(n) para n=10,000,000.
  3. Complejidad espacial: O(n + b) con n=10,000,000 y b=10 lo cual.
  4. Estabilidad: Si es estable el algoritmo para mantener el orden de los codigos iguales.


IMPLEMENTACIÓN:
  Implementa `ordenar_codigos(codigos)` aplicando el algoritmo elegido.

"""



def ordenar_codigos(codigos, exp):
    """
    """

    n = len(codigos)
    output = [0] * n
    count = [0] * 10

    # Contar ocurrencias del dígito en la posición exp
    for i in range(n):
        index = (codigos[i] // exp) % 10
        count[index] += 1

    # Actualizar el array count para que contenga las posiciones finales de los dígitos
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el array output usando count para colocar los elementos en su lugar correcto
    i = n - 1
    while i >= 0:
        index = (codigos[i] // exp) % 10
        output[count[index] - 1] = codigos[i]
        count[index] -= 1
        i -= 1

    # Copiar el contenido de output en codigos para que codigos contenga los números ordenados según el dígito actual
    for i in range(n):
        codigos[i] = output[i]
def radix_sort(codigos):
    # Encontrar el número máximo para conocer el número de dígitos
    max_element = max(codigos)

    # Aplicar counting sort para cada dígito. exp es 10^i donde i es el dígito actual.
    exp = 1
    while max_element // exp > 0:
        ordenar_codigos(codigos, exp)
        exp *= 10





# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBAS DEL QUIZ B DE ORDENAMIENTO")
    print("=" * 60)

    # ── CASO 1 ──
    print("\n--- CASO 1: Triaje en Urgencias ---")
    pacientes = [
        {"id_atencion": 1, "paciente": "Maria",  "prioridad": 3, "hora_ingreso": "08:00", "estado": "atendido"},
        {"id_atencion": 2, "paciente": "Carlos", "prioridad": 1, "hora_ingreso": "08:05", "estado": "atendido"},
        {"id_atencion": 3, "paciente": "Lucia",  "prioridad": 3, "hora_ingreso": "08:10", "estado": "atendido"},
        {"id_atencion": 4, "paciente": "Pablo",  "prioridad": 2, "hora_ingreso": "08:15", "estado": "abandono"},
        {"id_atencion": 5, "paciente": "Sofia",  "prioridad": 1, "hora_ingreso": "08:20", "estado": "atendido"},
        {"id_atencion": 6, "paciente": "Diego",  "prioridad": 5, "hora_ingreso": "08:25", "estado": "atendido"},
    ]
    resultado = ordenar_pacientes(pacientes)
    if resultado:
        for p in resultado:
            print(f"  P{p['prioridad']} | {p['paciente']:7} | id={p['id_atencion']} | {p['hora_ingreso']}")
    else:
        print(ordenar_pacientes(pacientes))

    # ── CASO 2 ──
    print("\n--- CASO 2: Ranking de productos ---")
    productos = [
        (101, 4.5, 320),
        (102, 3.8, 150),
        (103, 4.5, 410),
        (104, 5.0, 80),
        (105, 4.2, 600),
    ]
    resultado = ordenar_productos(productos)
    if resultado:
        for p in resultado:
            print(f"  ID {p[0]} | rating={p[1]} | ventas={p[2]}")
    else:
        print( ordenar_productos(productos))


    # ── CASO 3 ──
    print("\n--- CASO 3: Códigos EAN-13 ---")
    codigos = [
        7702011223344,
        7702011000111,
        7891234567890,
        7702011223344,
        4006381333931,
        7891234567890,
    ]
    resultado = ordenar_codigos(codigos)
    if resultado:
        for c in resultado:
            print(f"  {c}")
    else:
        print(ordenar_codigos(codigos))
