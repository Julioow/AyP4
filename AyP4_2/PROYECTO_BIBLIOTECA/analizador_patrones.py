# ============================================================================
# MÓDULO 4: ANALIZADOR DE PATRONES
# ============================================================================

class AnalizadorPatrones:
    """
    Analiza comportamiento de usuarios y tendencias en la biblioteca.
    
    Estructura de datos:
    - conjuntos: para análisis rápido de coincidencias
    - diccionario: para conteo de frecuencias
    - recursión: para análisis profundo
    
    Complejidad:
    - Libros más solicitados: O(n)
    - Usuarios frecuentes: O(u log u) con sort
    - Géneros trending: O(n)
    - Análisis profundo: O(u × n) con recursión
    """
    
    def __init__(self, gestor_usuarios, gestor_catalogo):
        self.gestor_usuarios = gestor_usuarios
        self.gestor_catalogo = gestor_catalogo
    
    def libros_mas_solicitados(self, limite=10):
        """
        Retorna libros más solicitados (menos copias disponibles) - O(n log n)
        
        Indica popularidad: menos copias = más demanda
        """
        catalogo = self.gestor_catalogo.catalogo.values()
        
        # Ordenar por copias disponibles (O(n log n))
        ordenados = sorted(
            catalogo,
            key=lambda l: (l.copias_disponibles, -l.copias_totales)
        )
        
        return ordenados[:limite]
    
    def usuarios_mas_activos(self, limite=10):
        """Retorna usuarios con más préstamos - O(u log u)"""
        usuarios_list = list(self.gestor_usuarios.usuarios.values())
        
        # Ordenar por cantidad de préstamos (O(u log u))
        ordenados = sorted(
            usuarios_list,
            key=lambda u: len(u.historial_prestamos.obtener_historial()),
            reverse=True
        )
        
        return ordenados[:limite]
    
    def generos_trending(self):
        """Retorna géneros más populares - O(n)"""
        conteo_generos = {}
        
        # O(n) recorrer todos los libros
        for libro in self.gestor_catalogo.catalogo.values():
            if libro.genero not in conteo_generos:
                conteo_generos[libro.genero] = 0
            # Resta: menos copias = más prestado
            conteo_generos[libro.genero] += (libro.copias_totales - libro.copias_disponibles)
        
        # O(n log n) ordenar
        return sorted(conteo_generos.items(), key=lambda x: x[1], reverse=True)
    
    def autores_mas_solicitados(self, limite=10):
        """Retorna autores más populares - O(n log n)"""
        conteo_autores = {}
        
        # O(n) contar por autor
        for libro in self.gestor_catalogo.catalogo.values():
            if libro.autor not in conteo_autores:
                conteo_autores[libro.autor] = 0
            conteo_autores[libro.autor] += (libro.copias_totales - libro.copias_disponibles)
        
        # O(n log n) ordenar
        ordenados = sorted(conteo_autores.items(), key=lambda x: x[1], reverse=True)
        
        return ordenados[:limite]
    
    def usuarios_con_intereses_comunes(self, user_id1, user_id2):
        """
        Retorna géneros en común entre dos usuarios - O(1) a O(m)
        donde m es el tamaño del conjunto más pequeño
        
        VENTAJA DE CONJUNTOS:
        - Sin conjuntos: loop O(n) para cada género
        - Con conjuntos: intersection() O(m)
        """
        usuario1 = self.gestor_usuarios.obtener_usuario(user_id1)
        usuario2 = self.gestor_usuarios.obtener_usuario(user_id2)
        
        if not usuario1 or not usuario2:
            return set()
        
        # O(m) siendo m el tamaño del conjunto más pequeño
        return usuario1.generos_favoritos.intersection(usuario2.generos_favoritos)
    
    def estadisticas_biblioteca(self):
        """
        Retorna estadísticas generales - O(n + u)
        """
        total_libros = self.gestor_catalogo.cantidad_total_libros()
        total_usuarios = self.gestor_usuarios.usuarios_conectados()
        
        # Contar total de copias
        total_copias = sum(l.copias_totales for l in self.gestor_catalogo.catalogo.values())
        copias_disponibles = sum(l.copias_disponibles for l in self.gestor_catalogo.catalogo.values())
        
        # Contar préstamos activos
        prestamos_activos = 0
        def _contar_prestamos(usuarios_dict):
            """Recursión para contar total"""
            total = 0
            for usuario in usuarios_dict.values():
                total += usuario.historial_prestamos.contar_activos()
            return total
        
        prestamos_activos = _contar_prestamos(self.gestor_usuarios.usuarios)
        
        return {
            'total_libros_unicos': total_libros,
            'total_copias': total_copias,
            'copias_disponibles': copias_disponibles,
            'copias_en_prestamo': total_copias - copias_disponibles,
            'total_usuarios': total_usuarios,
            'prestamos_activos': prestamos_activos,
            'generos_disponibles': len(self.gestor_catalogo.generos_disponibles())
        }
    
    def __str__(self):
        return "Analizador de Patrones - Análisis en tiempo real"
