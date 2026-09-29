"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL - CONJUNTOS (C)
            Verificador de Lotería + Catálogo de Biblioteca con Listas
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
--------------
1. Completar las funciones donde dice TODO
2. No modificar el código base proporcionado
3. Tiempo: 90 minutos
4. Calificación: 0.0 a 5.0

═══════════════════════════════════════════════════════════════════════════════
                    PARTE 1: VERIFICADOR DE LOTERÍA (2.5)
═══════════════════════════════════════════════════════════════════════════════

Un sistema de lotería tiene 3 boletos con números del 1 al 45.
Cada boleto tiene 6 números. Los números ganadores también son 6.
Usar conjuntos de Python para verificar aciertos y premios.
"""

numeros_ganadores = {7, 14, 21, 28, 35, 42}

boleto_ana = {7, 12, 21, 33, 42, 45}
boleto_luis = {3, 14, 28, 35, 40, 42}
boleto_sara = {1, 8, 15, 22, 29, 36}


# PUNTO 1.1 (0.8): Aciertos de un boleto
def aciertos(numeros_ganadores, boleto_ana, boleto_luis, boleto_sara ):
    """
    Retorna el conjunto de números que el boleto acertó
    (números que están en el boleto Y en los ganadores).

    Ejemplo:
        aciertos(boleto_ana) -> {7, 21, 42}
    """
    # TODO: Implementar
    boleto = Conjunto()
    actual = numeros_ganadores.cabeza
    while actual:
        if boleto_ana.pertenece(actual.dato):
            boleto.agregar(actual.dato)
        actual = actual.siguiente
    return boleto
     
    boleto = Conjunto()
    actual = numeros_ganadores.cabeza
    while actual:
        if boleto_luis.pertenece(actual.dato):
            boleto.agregar(actual.dato)
        actual = actual.siguiente
    return boleto 
    
    boleto = Conjunto()
    actual = numeros_ganadores.cabeza
    while actual:
        if boleto_sara.pertenece(actual.dato):
            boleto.agregar(actual.dato)
        actual = actual.siguiente
    return boleto 
    pass


# PUNTO 1.2 (0.8): Números que le faltaron
def numeros_faltantes(boleto):
    """
    Retorna el conjunto de números ganadores que NO estaban en el boleto.

    Ejemplo:
        numeros_faltantes(boleto_ana) -> {14, 28, 35}
    """
    # TODO: Implementar
    faltantes_de_ana = diferencia(boleto_ana, numeros_ganadores ) 
    print(f"numeros_faltantes: {faltantes_de_ana}")
    
    faltantes_de_luis = diferencia(boleto_luis, numeros_ganadores ) 
    print(f"numeros_faltantes: {faltantes_de_luis}")

    faltantes_de_sara = diferencia(boleto_sara, numeros_ganadores ) 
    print(f"numeros_faltantes: {faltantes_de_sara}")
    pass


# PUNTO 1.3 (0.9): Números que ningún boleto acertó
def sin_acertar_nadie():
    
    """
    Retorna el conjunto de números ganadores que NINGUNO de los 3 boletos tenía.

    Pista: Primero unir todos los números de los 3 boletos,
    luego ver cuáles ganadores no están en esa unión.

    Ejemplo esperado: los ganadores que no aparecen en ningún boleto
    """
    # TODO: Implementar

    boleto_ana = {7, 12, 21, 33, 42, 45}
    boleto_luis = {3, 14, 28, 35, 40, 42}
    boleto_sara = {1, 8, 15, 22, 29, 36}
    numeros_ganadores = {7, 14, 21, 28, 35, 42}

    union_de_boletos = union(boleto_ana, boleto_luis)
    union_de_boletos = union(union_de_boletos, boleto_sara)

    ningun_acierto = diferencia(numeros_ganadores, union_de_boletos)
    print(f"\nlos ganadores que no aparecen en ningun boleto = {ningun_acierto}")
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                PARTE 2: CATÁLOGO DE BIBLIOTECA CON LISTAS (2.5)
═══════════════════════════════════════════════════════════════════════════════

Dos bibliotecas tienen libros almacenados como conjuntos con listas enlazadas.
Implementar operaciones para gestionar el catálogo.
"""


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO BASE - NO MODIFICAR
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
        """Retorna True si x está en el conjunto"""
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, x):
        """Agrega x si no existe"""
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
# PUNTOS A IMPLEMENTAR
# ═══════════════════════════════════════════════════════════════════════════════

# PUNTO 2.1 (0.8): Libros en ambas bibliotecas (intersección)
def libros_en_ambas(biblio_a, biblio_b):
    """
    Retorna un NUEVO Conjunto con los libros que están en AMBAS bibliotecas.

    Recorrer biblio_a y agregar al resultado solo los que también
    están en biblio_b.

    Ejemplo:
        A = Conjunto(["Quijote", "Hamlet", "1984"])
        B = Conjunto(["Hamlet", "Odisea", "1984"])
        libros_en_ambas(A, B) -> {Hamlet, 1984}
    """
    # TODO: Implementar
    A = Conjunto(["Quijote", "Hamlet", "1984"])
    B = Conjunto(["Hamlet", "Odisea", "1984"])

def interseccion(A, B):
    resultado = Conjunto()
    actual = A.cabeza
    while actual:
        if B.pertenece(actual.dato):
            resultado.agregar(actual.dato)
        actual = actual.siguiente
    return resultado
    pass


# PUNTO 2.2 (0.8): Libros exclusivos de una biblioteca (diferencia)
def libros_exclusivos(biblio_a, biblio_b):
    """
    Retorna un NUEVO Conjunto con libros que están en biblio_a
    pero NO en biblio_b.

    Ejemplo:
        A = Conjunto(["Quijote", "Hamlet", "1984"])
        B = Conjunto(["Hamlet", "Odisea", "1984"])
        libros_exclusivos(A, B) -> {Quijote}
    """
    # TODO: Implementar
    A = Conjunto(["Quijote", "Hamlet", "1984"])
    B = Conjunto(["Hamlet", "Odisea", "1984"])
def diferencia(A, B):
    resultado = Conjunto()
    actual = A.cabeza
    while actual:
        if not B.pertenece(actual.dato):
            resultado.agregar(actual.dato)
        actual = actual.siguiente
    return resultado


    pass


# PUNTO 2.3 (0.9): Verificar si una biblioteca tiene todos los de otra
def contiene_todos(biblio_grande, biblio_chica):
    """
    Retorna True si biblio_grande tiene TODOS los libros de biblio_chica.
    Es decir: biblio_chica ⊆ biblio_grande

    Ejemplo:
        grande = Conjunto(["Quijote", "Hamlet", "1984", "Odisea"])
        chica = Conjunto(["Hamlet", "1984"])
        contiene_todos(grande, chica) -> True

        contiene_todos(chica, grande) -> False
    """
    # TODO: Implementar
    grande = Conjunto(["Quijote", "Hamlet", "1984", "Odisea"])
    chica = Conjunto(["Hamlet", "1984"])

    actual = grande.cabeza
    while actual:
        if not chica.pertenece(actual.dato):
            return False
        actual = actual.siguiente
    return True
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("PARTE 1: VERIFICADOR DE LOTERÍA")
    print("=" * 60)

    print(f"\n  Ganadores: {sorted(numeros_ganadores)}")
    print(f"  Ana:  {sorted(boleto_ana)}")
    print(f"  Luis: {sorted(boleto_luis)}")
    print(f"  Sara: {sorted(boleto_sara)}")

    print(f"\n🎯 Aciertos de Ana: {aciertos(boleto_ana)}")
    print(f"   Esperado: {{7, 21, 42}}")

    print(f"\n🎯 Aciertos de Luis: {aciertos(boleto_luis)}")
    print(f"   Esperado: {{14, 28, 35, 42}}")

    print(f"\n🎯 Aciertos de Sara: {aciertos(boleto_sara)}")
    print(f"   Esperado: set()")

    print(f"\n❌ Faltantes de Ana: {numeros_faltantes(boleto_ana)}")
    print(f"   Esperado: {{14, 28, 35}}")

    print(f"\n🔴 Sin acertar nadie: {sin_acertar_nadie()}")

    print("\n" + "=" * 60)
    print("PARTE 2: CATÁLOGO DE BIBLIOTECA")
    print("=" * 60)

    biblio_norte = Conjunto(["Quijote", "Hamlet", "1984", "Cien Años", "Rayuela"])
    biblio_sur = Conjunto(["Hamlet", "Odisea", "1984", "Aleph", "Rayuela"])

    print(f"\n  Norte: {biblio_norte}")
    print(f"  Sur:   {biblio_sur}")

    print(f"\n🔵 En ambas: {libros_en_ambas(biblio_norte, biblio_sur)}")
    print(f"   Esperado: {{Hamlet, 1984, Rayuela}}")

    print(f"\n🟡 Solo en Norte: {libros_exclusivos(biblio_norte, biblio_sur)}")
    print(f"   Esperado: {{Quijote, Cien Años}}")

    print(f"\n🟡 Solo en Sur: {libros_exclusivos(biblio_sur, biblio_norte)}")
    print(f"   Esperado: {{Odisea, Aleph}}")

    pedido = Conjunto(["Hamlet", "1984"])
    print(f"\n  Pedido: {pedido}")
    print(f"  ¿Norte tiene todo? {contiene_todos(biblio_norte, pedido)}")
    print(f"   Esperado: True")

    pedido2 = Conjunto(["Hamlet", "Odisea"])
    print(f"\n  Pedido: {pedido2}")
    print(f"  ¿Norte tiene todo? {contiene_todos(biblio_norte, pedido2)}")
    print(f"   Esperado: False")
