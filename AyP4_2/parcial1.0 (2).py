import re

# ============ PUNTO 1: VALIDACIÓN DE PLACAS ============
"""
Valida si una placa de vehículo colombiana tiene formato correcto.
Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123)
También válido con guion: ABC-123
"""

def validar_placa_vehiculo(placa):
    patron = r"^[A-Z]{3}-?\d{3}$"
    return bool(re.match(patron, placa))

# Pruebas
print("=== PUNTO 1: Validación de Placas ===")
print(f"ABC123: {validar_placa_vehiculo('ABC123')}")           # True
print(f"ABC-123: {validar_placa_vehiculo('ABC-123')}")         # True
print(f"AB1234: {validar_placa_vehiculo('AB1234')}")           # False
print(f"abc123: {validar_placa_vehiculo('abc123')}")           # False
print()

# ============ EJERCICIO EXTRA: EXTRACCIÓN DE HASHTAGS ============
def extraer_hashtags(texto):
    """Extrae todos los hashtags de un texto."""
    return re.findall(r"#\w+", texto)

texto = "Hola #python es #genial y #100dias"
print("=== HASHTAGS ===")
print(f"Texto: {texto}")
print(f"Hashtags: {extraer_hashtags(texto)}")
print()
# ============ PUNTO 2: SISTEMA DE GESTIÓN DE PEDIDOS ============
"""
Sistema de gestión de pedidos para un restaurante de domicilios.
Cada pedido tiene: cliente, dirección, valor y si está entregado.
Los pedidos se almacenan en una lista enlazada.
"""

class Pedido:
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente = cliente
        self.direccion = direccion
        self.valor = valor
        self.entregado = entregado
        self.siguiente = None
    
    def __str__(self):
        estado = "✓" if self.entregado else "○"
        return f"[{estado}] {self.cliente} - ${self.valor:,} - {self.direccion}"


class ListaPedidos:
    def __init__(self):
        self.cabeza = None
    
    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("  Sin pedidos")
            return
        while actual:
            print(f"  {actual}")
            actual = actual.siguiente
    
    def agregar(self, cliente, direccion, valor):
        """Agrega un nuevo pedido al FINAL de la lista. OBLIGATORIO usar recursividad."""
        nuevo_pedido = Pedido(cliente, direccion, valor)
        
        if self.cabeza is None:
            self.cabeza = nuevo_pedido
        else:
            self._agregar_recursivo(self.cabeza, nuevo_pedido)
    
    def _agregar_recursivo(self, actual, nuevo):
        """Función auxiliar recursiva para agregar al final."""
        if actual.siguiente is None:
            actual.siguiente = nuevo
        else:
            self._agregar_recursivo(actual.siguiente, nuevo)
    
    def valor_pendiente(self):
        """
        Retorna la suma de valores de pedidos NO entregados.
        OBLIGATORIO usar recursividad.
        """
        return self._valor_pendiente_recursivo(self.cabeza)
    
    def _valor_pendiente_recursivo(self, actual):
        """Función auxiliar recursiva para sumar valores pendientes."""
        if actual is None:
            return 0
        
        valor_actual = 0 if actual.entregado else actual.valor
        return valor_actual + self._valor_pendiente_recursivo(actual.siguiente)
    
    def eliminar_entregados(self):
        """
        Elimina todos los pedidos que ya fueron entregados.
        OBLIGATORIO usar recursividad.
        Modifica la lista original.
        """
        self.cabeza = self._eliminar_entregados_recursivo(self.cabeza)
    
    def _eliminar_entregados_recursivo(self, actual):
        """Función auxiliar recursiva para eliminar pedidos entregados."""
        if actual is None:
            return None
        
        if actual.entregado:
            # Si el pedido está entregado, saltarlo y continuar
            return self._eliminar_entregados_recursivo(actual.siguiente)
        else:
            # Si no está entregado, mantenerlo y procesar el siguiente
            actual.siguiente = self._eliminar_entregados_recursivo(actual.siguiente)
            return actual


print("=== PUNTO 2: Sistema de Pedidos ===")
lista = ListaPedidos()
lista.agregar("Juan", "Calle 10 #5-20", 25000)
lista.agregar("Maria", "Carrera 15 #8-30", 30000)
lista.agregar("Carlos", "Avenida 20 #10-50", 15000)

print("Pedidos iniciales:")
lista.mostrar()

print(f"\nValor pendiente: ${lista.valor_pendiente():,}")

# Marcar algunos como entregados
lista.cabeza.siguiente.entregado = True
lista.cabeza.siguiente.siguiente.entregado = True

print("\nDespués de marcar algunos como entregados:")
lista.mostrar()

print(f"\nValor pendiente: ${lista.valor_pendiente():,}")

lista.eliminar_entregados()
print("\nDespués de eliminar entregados:")
lista.mostrar()
print()


# ============ PUNTO 3: OPERACIONES CON CONJUNTOS ============
"""
Operaciones sobre conjuntos de estudiantes inscritos en clubes.
"""

club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}

print("=== PUNTO 3: Operaciones con Conjuntos ===")

# Estudiantes inscritos en LOS TRES clubes (intersección)
estudian_tres = club_ciencias & club_deportes & club_arte
print(f"Estudiantes en LOS TRES clubes: {estudian_tres}")

# Estudiantes en EXACTAMENTE un club
solo_una = (club_ciencias - club_deportes - club_arte) | \
           (club_deportes - club_ciencias - club_arte) | \
           (club_arte - club_ciencias - club_deportes)
print(f"Estudiantes en EXACTAMENTE un club: {solo_una}")

# Mostrar en qué clubes está cada estudiante
print("\nPertenencia a clubes:")
todos = club_ciencias | club_deportes | club_arte

for estudiante in sorted(todos):
    clubes = []
    if estudiante in club_ciencias:
        clubes.append("Ciencias")
    if estudiante in club_deportes:
        clubes.append("Deportes")
    if estudiante in club_arte:
        clubes.append("Arte")
    print(f"  {estudiante}: {', '.join(clubes)}")

print()


# ============ PUNTO 4: MEMOIZACIÓN ============
"""
Problema: De cuántas formas se puede subir una escalera de n escalones
si se pueden subir 1 o 2 escalones a la vez.

Versión 1: Recursión pura (sin optimización) - INEFICIENTE
Versión 2: Memoización (guarda resultados) - EFICIENTE
"""

print("=== PUNTO 4: Memoización ===")

# Versión 1: Recursión pura (ineficiente - exponencial O(2^n))
def formas_subir_simple(n):
    """Recursión pura sin optimización."""
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return formas_subir_simple(n-1) + formas_subir_simple(n-2)


# Versión 2: Con memoización (eficiente - polinomial O(n))
memo = {}

def formas_subir_memo(n):
    """Recursión con memoización (diccionario para guardar resultados)."""
    if n <= 1:
        return 1
    if n == 2:
        return 2
    
    if n in memo:
        return memo[n]
    
    memo[n] = formas_subir_memo(n-1) + formas_subir_memo(n-2)
    return memo[n]


# Pruebas
print("Formas de subir escalera (comparativa):")
for n in [5, 10, 15, 20, 25]:
    resultado_simple = formas_subir_simple(n)
    # Limpiar memo para hacer la prueba más justa
    memo.clear()
    resultado_memo = formas_subir_memo(n)
    print(f"  n={n}: simple={resultado_simple}, memo={resultado_memo}")

print("\n✅ Parcial completamente resuelto")
