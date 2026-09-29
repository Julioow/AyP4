# ============================================================================
# ESTRUCTURAS DE DATOS - GESTOR DE BIBLIOTECA INTELIGENTE
# ============================================================================

class Nodo:
    """Nodo para lista ligada de préstamos"""
    def __init__(self, libro_id, fecha, estado):
        self.libro_id = libro_id
        self.fecha = fecha
        self.estado = estado  # 'activo' o 'devuelto'
        self.siguiente = None


class HistorialPrestamos:
    """
    Lista ligada que mantiene el historial de préstamos de un usuario.
    
    Ventajas:
    - O(1) inserción al inicio
    - Orden cronológico natural
    - No requiere asignación de memoria fija
    - Fácil de iterar
    
    Complejidad:
    - Agregar préstamo: O(1)
    - Obtener historial: O(n)
    - Buscar préstamo específico: O(n)
    """
    
    def __init__(self):
        self.cabeza = None
    
    def agregar_prestamo(self, libro_id, fecha):
        """Agrega un nuevo préstamo al inicio - O(1)"""
        nuevo_nodo = Nodo(libro_id, fecha, 'activo')
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def obtener_historial(self):
        """Retorna lista de todos los préstamos - O(n)"""
        historial = []
        actual = self.cabeza
        while actual:
            historial.append({
                'libro_id': actual.libro_id,
                'fecha': actual.fecha,
                'estado': actual.estado
            })
            actual = actual.siguiente
        return historial
    
    def contar_activos(self):
        """Cuenta préstamos activos (no devueltos) - O(n)"""
        def _recursivo(nodo):
            if nodo is None:
                return 0
            cuenta = 1 if nodo.estado == 'activo' else 0
            return cuenta + _recursivo(nodo.siguiente)
        
        return _recursivo(self.cabeza)
    
    def marcar_devuelto(self, libro_id):
        """Marca un préstamo como devuelto - O(n)"""
        actual = self.cabeza
        while actual:
            if actual.libro_id == libro_id and actual.estado == 'activo':
                actual.estado = 'devuelto'
                return True
            actual = actual.siguiente
        return False
    
    def __str__(self):
        items = []
        actual = self.cabeza
        while actual:
            items.append(f"Libro {actual.libro_id} ({actual.estado})")
            actual = actual.siguiente
        return " → ".join(items) if items else "Vacío"


# ============================================================================
# LIBRO - Entidad básica
# ============================================================================

class Libro:
    """Representa un libro en la biblioteca"""
    
    def __init__(self, libro_id, titulo, autor, año, genero, copias_disponibles=1):
        self.id = libro_id
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.genero = genero
        self.copias_disponibles = copias_disponibles
        self.copias_totales = copias_disponibles
    
    def __str__(self):
        return f"{self.titulo} ({self.autor}, {self.año}) - Copias: {self.copias_disponibles}/{self.copias_totales}"
    
    def __repr__(self):
        return f"Libro(id={self.id}, titulo='{self.titulo}')"


# ============================================================================
# USUARIO - Entidad con historial
# ============================================================================

class Usuario:
    """Representa un usuario con sus préstamos y preferencias"""
    
    def __init__(self, user_id, nombre, email):
        self.id = user_id
        self.nombre = nombre
        self.email = email
        self.historial_prestamos = HistorialPrestamos()  # Lista ligada
        self.generos_favoritos = set()  # Conjunto: géneros preferidos
        self.libros_favoritos = set()   # Conjunto: IDs de libros favoritos
    
    def agregar_genero_favorito(self, genero):
        """Agrega género a favoritos - O(1)"""
        self.generos_favoritos.add(genero)
    
    def agregar_libro_favorito(self, libro_id):
        """Agrega libro a favoritos - O(1)"""
        self.libros_favoritos.add(libro_id)
    
    def libros_en_comun_con(self, otro_usuario):
        """
        Retorna libros favoritos en común con otro usuario - O(m)
        donde m es el tamaño del conjunto más pequeño
        """
        return self.libros_favoritos.intersection(otro_usuario.libros_favoritos)
    
    def __str__(self):
        return f"Usuario: {self.nombre} ({self.email}) - Préstamos activos: {self.historial_prestamos.contar_activos()}"
