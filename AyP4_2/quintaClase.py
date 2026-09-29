"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 1: IMPLEMENTACIÓN DE PILA (STACK)
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════

La Pila es una estructura de datos LIFO (Last In, First Out).
El último elemento en entrar es el primero en salir.

Analogía: Una pila de platos - solo puedes poner o quitar del tope.
"""


class Nodo:
    """Nodo para la lista enlazada"""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    """
    Implementación de Pila usando lista enlazada.
    Todas las operaciones son O(1).
    """
    
    def __init__(self):
        self.tope = None
        self.tamanio = 0
    
    def esta_vacia(self):
        """Retorna True si la pila está vacía"""
        return self.tope is None
    
    def push(self, dato):
        """Agrega un elemento al tope de la pila - O(1)"""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamanio += 1
    
    def pop(self):
        """Quita y retorna el elemento del tope - O(1)"""
        if self.esta_vacia():
            raise Exception("Error: La pila está vacía")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return dato
    
    def peek(self):
        """Retorna el elemento del tope sin quitarlo - O(1)"""
        if self.esta_vacia():
            raise Exception("Error: La pila está vacía")
        return self.tope.dato
    
    def __len__(self):
        """Retorna el tamaño de la pila"""
        return self.tamanio
    
    def __str__(self):
        """Representación visual de la pila"""
        if self.esta_vacia():
            return "Pila vacía"
        
        elementos = []
        actual = self.tope
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        return "Tope → " + " → ".join(elementos) + " → None"


# ═══════════════════════════════════════════════════════════════════════════════
# DEMOSTRACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("       DEMOSTRACIÓN DE PILA (STACK)")
    print("=" * 50)
    
    pila = Pila()
    
    print("\n📥 Agregando elementos (push):")
    for valor in [10, 20, 30, 40]:
        pila.push(valor)
        print(f"   push({valor}) → {pila}")
    
    print(f"\n📊 Tamaño de la pila: {len(pila)}")
    print(f"👀 Elemento en el tope (peek): {pila.peek()}")
    
    print("\n📤 Quitando elementos (pop):")
    while not pila.esta_vacia():
        valor = pila.pop()
        print(f"   pop() = {valor} → {pila}")
    
    print("\n" + "=" * 50)
    print("💡 Observa: Los elementos salen en orden inverso")
    print("   al que entraron (LIFO)")
    print("=" * 50)

"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 2: EVALUACIÓN DE EXPRESIONES POSTFIJAS
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════

Notación Postfija (Polaca Inversa):
- El operador va DESPUÉS de los operandos
- No necesita paréntesis ni reglas de precedencia
- Se evalúa de izquierda a derecha usando una pila

Ejemplos:
    Infija: 3 + 4        →  Postfija: 3 4 +
    Infija: 3 + 4 * 2    →  Postfija: 3 4 2 * +
    Infija: (3 + 4) * 2  →  Postfija: 3 4 + 2 *
"""

from ejemplo_01_pila import Pila


def evaluar_postfija(expresion):
    """
    Evalúa una expresión en notación postfija.
    
    Algoritmo:
    1. Recorrer tokens de izquierda a derecha
    2. Si es número → push a la pila
    3. Si es operador → pop dos operandos, operar, push resultado
    4. Al final, el resultado está en el tope
    
    Args:
        expresion: String con tokens separados por espacios
    
    Returns:
        Resultado numérico de la expresión
    """
    pila = Pila()
    tokens = expresion.split()
    
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '//': lambda a, b: a // b,
        '%': lambda a, b: a % b,
        '**': lambda a, b: a ** b,
    }
    
    print(f"\n📝 Evaluando: {expresion}")
    print("-" * 40)
    
    for token in tokens:
        if token.lstrip('-').replace('.', '').isdigit():
            # Es un número (soporta negativos y decimales)
            valor = float(token) if '.' in token else int(token)
            pila.push(valor)
            print(f"   Token '{token}' → push({valor})")
        elif token in operadores:
            # Es un operador
            b = pila.pop()  # Segundo operando (sale primero)
            a = pila.pop()  # Primer operando
            resultado = operadores[token](a, b)
            pila.push(resultado)
            print(f"   Token '{token}' → {a} {token} {b} = {resultado}")
        else:
            raise ValueError(f"Token no reconocido: {token}")
        
        print(f"            Pila: {pila}")
    
    return pila.pop()


# ═══════════════════════════════════════════════════════════════════════════════
# DEMOSTRACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("   EVALUACIÓN DE EXPRESIONES POSTFIJAS")
    print("=" * 50)
    
    # Ejemplos de expresiones
    expresiones = [
        ("3 4 +", "3 + 4"),
        ("3 4 2 * +", "3 + 4 * 2"),
        ("3 4 + 2 *", "(3 + 4) * 2"),
        ("5 1 2 + 4 * + 3 -", "5 + (1 + 2) * 4 - 3"),
        ("2 3 ** 4 +", "2 ** 3 + 4"),
        ("10 3 /", "10 / 3"),
    ]
    
    for postfija, infija in expresiones:
        resultado = evaluar_postfija(postfija)
        print(f"\n✅ Resultado: {resultado}")
        print(f"   (Equivale a: {infija} = {eval(infija)})")
        print("=" * 50)


def evaluar_postfija(expresion):
    pila = pila()
    tokens = expresion.split()

    operadores = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,    
        '/': lambda x, y: x / y,
        '//': lambda x, y: x // y,
        '**': lambda x, y: x ** y,
        '%': lambda x, y: x % y
    }

    print(f"Evaluando la expresión postfija: {expresion}")
    print("-" * 40)

    for token in tokens:
        if token.lstrip('-').replace('.', '', 1).isdigit():  # Verificar si el token es un número (incluyendo negativos y decimales)
            valor = float(token) if '.' in token else int(token)  # Convertir a int si no es decimal
            pila.push(valor)
            print(f"Token '{token}' -> push({valor})")

        elif token in operadores:
            # es un operador, se necesitan dos operandos
            b = pila.pop() # El segundo operando se saca primero porque es una pila (LIFO)
            a = pila.pop() # El primer operando se saca después 
            resultado = operadores[token](a, b)
            pila.push(resultado)
            print(f"Token '{token}' -> pop({a}), pop({b}) -> push({resultado})")    

"""
═══════════════════════════════════════════════════════════════════════════════
SOLUCIÓN EJERCICIO 2: VERIFICADOR DE PARÉNTESIS BALANCEADOS
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.tope = None
    
    def esta_vacia(self):
        return self.tope is None
    
    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
    
    def pop(self):
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato
    
    def peek(self):
        if self.esta_vacia():
            return None
        return self.tope.dato

def infija_a_postfija(expresion):
    while (not pila.esta_vacia() and
        pila.peek() != '(' and
        pila.peek() in precedencia and
        precedencia[pila.peek()] >= precedencia[token]):
       salida.append(pila.pop())
    pila.push(token)
    print(f"Token '{token}' (operador) -> pila")      

    print(f"    salida: {salida}" )
    print(f"    pila: {pila}" )  
    
    # Al finalizar la lectura de la expresión, vaciamos la pila
    print("\n vaciando la pila restante...")
    while not pila.esta_vacia():
        salida.append(pila.pop())
        print(f"    salida: {salida}" )
        print(f"    pila: {pila}" )



def validar_balanceo(expresion):
    pares = {
        '(': ')',
        '{': '}', 
        '[': ']'
    }
    aperturas = set(pares.values())
    cierres = set(pares.keys())

    for token in expresion:
        if token in aperturas:
            pila.push(token)
            print(f"Agregando '{token}' a la pila. Pila actual: {pila}")
        elif token in cierres:
            if pila.esta_vacia() or pila.pop() != pares[token]:
                return False
    if  pila.esta_vacia():
        print("La expresión está balanceada.")
        return True
    else:
        return False



datos = [5,3,8,1,2,9,4]
import heapq
heapq.heapify(datos)
print("Heap:", datos)

heapq.heappush(datos, 6)
print("Heap después de agregar 6:", datos)

minimo = heapq.heappop(datos)
print("Elemento mínimo extraído:", minimo)
print("Heap después de extraer el mínimo:", datos)

datos2 = [(2, 'A'), (1, 'B'), (3, 'C'), (2, 'B')]
heapq.heapify(datos2)
print("Heap de tuplas:", datos2)

"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 3: CONVERSIÓN INFIJA A POSTFIJA
Algoritmos y Programación 4 - Semana 4
═══════════════════════════════════════════════════════════════════════════════

Algoritmo Shunting Yard (Dijkstra, 1961)

Convierte expresiones de notación infija a postfija usando:
- Una cola de salida (el resultado)
- Una pila de operadores

Reglas:
1. Número → va directo a la salida
2. Operador → según precedencia, puede ir a pila o mover otros a salida
3. '(' → va a la pila
4. ')' → pop hasta encontrar '('
5. Al final → vaciar pila a salida
"""

from ejemplo_01_pila import Pila


def infija_a_postfija(expresion):
    """
    Convierte una expresión infija a notación postfija.
    
    Args:
        expresion: String con expresión infija (tokens separados por espacios)
    
    Returns:
        String con expresión en notación postfija
    """
    # Precedencia de operadores (mayor número = mayor precedencia)
    precedencia = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    
    
    salida = []
    pila = Pila()
    
    # Preparar tokens (separar paréntesis)
    expresion = expresion.replace('(', ' ( ').replace(')', ' ) ')
    tokens = expresion.split()
    
    print(f"\n📝 Convirtiendo: {' '.join(tokens)}")
    print("-" * 50)
    
    for token in tokens:
        if token.lstrip('-').replace('.', '').isdigit():
            # Es un número
            salida.append(token)
            print(f"   '{token}' (número) → salida")
        
        elif token == '(':
            pila.push(token)
            print(f"   '{token}' → pila")
        
        elif token == ')':
            # Pop hasta encontrar '('
            while not pila.esta_vacia() and pila.peek() != '(':
                salida.append(pila.pop())
            if not pila.esta_vacia():
                pila.pop()  # Quitar el '('
            print(f"   '{token}' → pop hasta '('")
        
        elif token in precedencia:
            # Es un operador
            while (not pila.esta_vacia() and 
                   pila.peek() != '(' and
                   pila.peek() in precedencia and
                   precedencia[pila.peek()] >= precedencia[token]):
                salida.append(pila.pop())
            pila.push(token)
            print(f"   '{token}' (operador) → pila")
        
        print(f"      Salida: {salida}")
        print(f"      Pila: {pila}")
    
    # Vaciar la pila
    print("\n   Vaciando pila...")
    while not pila.esta_vacia():
        salida.append(pila.pop())
    
    resultado = ' '.join(salida)
    print(f"      Resultado: {resultado}")
    
    return resultado


# ═══════════════════════════════════════════════════════════════════════════════
# DEMOSTRACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("   CONVERSIÓN INFIJA → POSTFIJA (Shunting Yard)")
    print("=" * 60)
    
    expresiones = [
        "3 + 4",
        "3 + 4 * 2",
        "( 3 + 4 ) * 2",
        "3 + 4 * 2 - 1",
        "( 1 + 2 ) * ( 3 + 4 )",
        "2 ** 3 ** 2",  # Asociatividad derecha: 2^(3^2) = 512
        "10 - 5 - 2",   # Asociatividad izquierda: (10-5)-2 = 3
    ]
    
    print("\n📊 Tabla de conversiones:")
    print("-" * 60)
    print(f"{'Infija':<25} {'Postfija':<25}")
    print("-" * 60)
    
    for expr in expresiones:
        postfija = infija_a_postfija(expr)
        print(f"\n{'='*60}")
        print(f"✅ {expr:<25} → {postfija:<25}")


# Programa para gestionar la atención de pacientes en un hospital usando heapq
import heapq

class Paciente:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad  # 1 = más urgente, 3 = menos urgente
    def __lt__(self, other):
        return self.prioridad < other.prioridad
    def __repr__(self):
        return f"Paciente(nombre='{self.nombre}', prioridad={self.prioridad})"

# Lista de pacientes (heap)
pacientes = []

# Permitir al usuario agregar pacientes
while True:
    nombre = input("Ingrese el nombre del paciente (o '0' para terminar): ")
    if nombre.lower() == '0':
        break
    try:
        prioridad = int(input("Ingrese la prioridad (1=urgente, 2=media, 3=baja): "))
        if prioridad not in [1,2,3]:
            print("Prioridad inválida. Debe ser 1, 2 o 3.")
            continue
    except ValueError:
        print("Prioridad inválida. Debe ser un número.")
        continue
    heapq.heappush(pacientes, Paciente(nombre, prioridad))
    print(f"Paciente {nombre} agregado con prioridad {prioridad}.")

print("\nCola de pacientes (heap):", pacientes)

# Atender al siguiente paciente (el de mayor prioridad)
if pacientes:
    siguiente = heapq.heappop(pacientes)
    print(f"Siguiente en atender: {siguiente.nombre} (prioridad {siguiente.prioridad})")
else:
    print("No hay pacientes en la cola.")

# Mostrar el estado actual de la cola
def mostrar_cola(pacientes):
    print("Cola actual:")
    for paciente in pacientes:
        print(f"  {paciente.nombre} (prioridad {paciente.prioridad})")

mostrar_cola(pacientes)


""" ultimo ejemplo de la clase  """
import re

texto = "Python es genial"

resultados = re.match("Python", texto)
print(resultados.group())  # Imprime "Python"   