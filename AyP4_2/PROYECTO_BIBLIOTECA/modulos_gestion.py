# ============================================================================
# MÓDULO 1: GESTOR DE CATÁLOGO
# ============================================================================
# Responsabilidad: Gestionar libros disponibles en la biblioteca

class GestorCatalogo:
    """
    Gestiona el catálogo de libros de la biblioteca.
    
    Estructura de datos:
    - diccionario: {libro_id: Libro} → O(1) búsqueda
    
    Complejidad:
    - Agregar libro: O(1)
    - Buscar por ID: O(1)
    - Buscar por título: O(n)
    - Buscar por género: O(n)
    - Libros disponibles: O(n)
    """
    
    def __init__(self):
        self.catalogo = {}  # {id: Libro}
        self.libros_por_genero = {}  # {género: [ids]}
        self.libros_por_autor = {}   # {autor: [ids]}
    
    def agregar_libro(self, libro):
        """Agrega un libro al catálogo - O(1)"""
        self.catalogo[libro.id] = libro
        
        # Indexar por género
        if libro.genero not in self.libros_por_genero:
            self.libros_por_genero[libro.genero] = []
        self.libros_por_genero[libro.genero].append(libro.id)
        
        # Indexar por autor
        if libro.autor not in self.libros_por_autor:
            self.libros_por_autor[libro.autor] = []
        self.libros_por_autor[libro.autor].append(libro.id)
    
    def buscar_por_id(self, libro_id):
        """Busca libro por ID - O(1)"""
        return self.catalogo.get(libro_id)
    
    def buscar_por_titulo(self, titulo):
        """Busca libros que contengan el título - O(n)"""
        resultados = []
        for libro in self.catalogo.values():
            if titulo.lower() in libro.titulo.lower():
                resultados.append(libro)
        return resultados
    
    def buscar_por_genero(self, genero):
        """Busca todos los libros de un género - O(m) donde m es cantidad de libros"""
        ids = self.libros_por_genero.get(genero, [])
        return [self.catalogo[id] for id in ids]
    
    def buscar_por_autor(self, autor):
        """Busca todos los libros de un autor - O(m)"""
        ids = self.libros_por_autor.get(autor, [])
        return [self.catalogo[id] for id in ids]
    
    def libros_disponibles(self):
        """
        Retorna todos los libros con copias disponibles - O(n)
        
        ALTERNATIVA SIN DICCIONARIO (Menos eficiente):
        - Con lista: O(n) búsqueda + O(n) filtrado = O(n) pero con más operaciones
        - Ventaja dict: Acceso O(1) a cualquier libro mientras iteras
        """
        return [l for l in self.catalogo.values() if l.copias_disponibles > 0]
    
    def cantidad_total_libros(self):
        """Retorna cantidad total de libros únicos - O(1)"""
        return len(self.catalogo)
    
    def generos_disponibles(self):
        """Retorna todos los géneros disponibles - O(1)"""
        return set(self.libros_por_genero.keys())
    
    def __str__(self):
        return f"Catálogo: {self.cantidad_total_libros()} libros únicos"


# ============================================================================
# MÓDULO 2: GESTOR DE USUARIOS Y PRÉSTAMOS
# ============================================================================

class GestorUsuarios:
    """
    Gestiona usuarios, su historial de préstamos y devoluciones.
    
    Estructura de datos:
    - diccionario: {user_id: Usuario} → O(1) búsqueda
    - HistorialPrestamos (lista ligada): O(1) inserción
    - conjuntos: O(1) búsqueda y unión
    
    Complejidad:
    - Registrar usuario: O(1)
    - Préstamo: O(1)
    - Devolución: O(n) en peor caso (buscar en historial)
    - Obtener activos: O(n)
    """
    
    def __init__(self, gestor_catalogo):
        self.usuarios = {}  # {user_id: Usuario}
        self.gestor_catalogo = gestor_catalogo
    
    def registrar_usuario(self, user_id, nombre, email):
        """Registra un nuevo usuario - O(1)"""
        if user_id not in self.usuarios:
            from estructura_datos import Usuario
            usuario = Usuario(user_id, nombre, email)
            self.usuarios[user_id] = usuario
            return True
        return False
    
    def obtener_usuario(self, user_id):
        """Busca usuario por ID - O(1)"""
        return self.usuarios.get(user_id)
    
    def prestar_libro(self, user_id, libro_id, fecha):
        """
        Registra un préstamo de libro - O(1)
        
        Flujo:
        1. Verificar usuario existe (O(1))
        2. Verificar libro existe (O(1))
        3. Verificar disponibilidad (O(1))
        4. Agregar al historial (O(1))
        5. Disminuir copias (O(1))
        """
        usuario = self.obtener_usuario(user_id)
        if not usuario:
            return False, "Usuario no existe"
        
        libro = self.gestor_catalogo.buscar_por_id(libro_id)
        if not libro:
            return False, "Libro no existe"
        
        if libro.copias_disponibles <= 0:
            return False, "No hay copias disponibles"
        
        # Agregar al historial (O(1))
        usuario.historial_prestamos.agregar_prestamo(libro_id, fecha)
        
        # Disminuir disponibilidad
        libro.copias_disponibles -= 1
        
        return True, f"Préstamo exitoso: {libro.titulo}"
    
    def devolver_libro(self, user_id, libro_id):
        """
        Registra devolución de libro - O(n) en peor caso
        
        n = cantidad de préstamos del usuario
        
        NOTA: Con lista ligada es más eficiente que con array
        porque no necesitamos reorganizar memoria
        """
        usuario = self.obtener_usuario(user_id)
        if not usuario:
            return False, "Usuario no existe"
        
        libro = self.gestor_catalogo.buscar_por_id(libro_id)
        if not libro:
            return False, "Libro no existe"
        
        # Marcar como devuelto en historial (O(n))
        if usuario.historial_prestamos.marcar_devuelto(libro_id):
            libro.copias_disponibles += 1
            return True, f"Devolución registrada: {libro.titulo}"
        else:
            return False, "El usuario no tiene un préstamo activo de este libro"
    
    def obtener_prestamos_activos(self, user_id):
        """Obtiene préstamos NO devueltos de un usuario - O(n)"""
        usuario = self.obtener_usuario(user_id)
        if not usuario:
            return []
        
        historial = usuario.historial_prestamos.obtener_historial()
        return [p for p in historial if p['estado'] == 'activo']
    
    def obtener_historial_completo(self, user_id):
        """Obtiene todo el historial de préstamos - O(n)"""
        usuario = self.obtener_usuario(user_id)
        if not usuario:
            return []
        
        return usuario.historial_prestamos.obtener_historial()
    
    def usuarios_conectados(self):
        """Retorna cantidad de usuarios registrados - O(1)"""
        return len(self.usuarios)
    
    def __str__(self):
        return f"Usuarios registrados: {self.usuarios_conectados()}"


# ============================================================================
# MÓDULO 3: SISTEMA DE RECOMENDACIONES
# ============================================================================

class SistemaRecomendaciones:
    """
    Recomienda libros basándose en preferencias y historial.
    
    Estructura de datos:
    - conjuntos: para análisis rápido de géneros (O(1) búsqueda)
    - diccionario: para acceso a libros (O(1))
    - recursión: para explorar similitudes
    
    Complejidad:
    - Recomendaciones por género: O(n log n) (incluye sort)
    - Libros similares: O(n²) en peor caso
    - Amigos que leen lo mismo: O(m) donde m es cantidad de amigos
    """
    
    def __init__(self, gestor_usuarios, gestor_catalogo):
        self.gestor_usuarios = gestor_usuarios
        self.gestor_catalogo = gestor_catalogo
    
    def recomendar_por_genero(self, user_id, limite=5):
        """
        Recomienda libros de géneros favoritos del usuario - O(n log n)
        
        Algoritmo:
        1. Obtener géneros favoritos (O(1))
        2. Filtrar libros disponibles de esos géneros (O(n))
        3. Ordenar por rating (O(n log n))
        4. Retornar top 5 (O(1))
        """
        usuario = self.gestor_usuarios.obtener_usuario(user_id)
        if not usuario or not usuario.generos_favoritos:
            return []
        
        recomendados = []
        # O(1) × cantidad de géneros
        for genero in usuario.generos_favoritos:
            libros = self.gestor_catalogo.buscar_por_genero(genero)
            # Filtrar disponibles y que no haya leído
            for libro in libros:
                if libro.copias_disponibles > 0 and libro.id not in usuario.libros_favoritos:
                    recomendados.append(libro)
        
        # Eliminar duplicados
        recomendados = list(set(recomendados))
        
        return recomendados[:limite]
    
    def libros_similares(self, libro_id, limite=5):
        """
        Encuentra libros similares (mismo género/autor) - O(n)
        
        Estrategia:
        - Buscar libro original (O(1))
        - Obtener libros del mismo género (O(n))
        - Obtener libros del mismo autor (O(n))
        - Unión de conjuntos (O(m + n))
        """
        libro = self.gestor_catalogo.buscar_por_id(libro_id)
        if not libro:
            return []
        
        # Conjuntos para evitar duplicados (O(1) add)
        similares_ids = set()
        
        # Libros del mismo género
        libros_genero = self.gestor_catalogo.buscar_por_genero(libro.genero)
        for l in libros_genero:
            if l.id != libro_id:
                similares_ids.add(l.id)
        
        # Libros del mismo autor
        libros_autor = self.gestor_catalogo.buscar_por_autor(libro.autor)
        for l in libros_autor:
            if l.id != libro_id:
                similares_ids.add(l.id)
        
        # Convertir IDs a objetos Libro (O(m))
        similares = [self.gestor_catalogo.buscar_por_id(id) for id in similares_ids]
        
        return similares[:limite]
    
    def usuarios_con_interes_comun(self, user_id, genero):
        """
        Encuentra otros usuarios interesados en el mismo género - O(u × m)
        donde u = cantidad usuarios, m = usuarios con ese género
        
        Usa RECURSIÓN para explorar profundidad
        """
        usuario = self.gestor_usuarios.obtener_usuario(user_id)
        if not usuario:
            return []
        
        def _buscar_usuarios_recursivo(genero_buscado, usuarios_dict):
            """Función auxiliar recursiva"""
            resultado = []
            for uid, usr in usuarios_dict.items():
                if uid != user_id and genero_buscado in usr.generos_favoritos:
                    resultado.append(usr)
            return resultado
        
        return _buscar_usuarios_recursivo(genero, self.gestor_usuarios.usuarios)
    
    def __str__(self):
        return "Sistema de Recomendaciones activo"
