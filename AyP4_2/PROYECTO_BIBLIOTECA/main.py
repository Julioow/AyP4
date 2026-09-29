# ============================================================================
# PUNTO DE ENTRADA - DEMOSTRACIÓN DEL SISTEMA
# ============================================================================

from estructura_datos import Libro, Usuario
from modulos_gestion import GestorCatalogo, GestorUsuarios, SistemaRecomendaciones
from analizador_patrones import AnalizadorPatrones


def demo_basico():
    """Demostración básica del sistema"""
    
    print("=" * 80)
    print("GESTOR DE BIBLIOTECA INTELIGENTE - DEMOSTRACION")
    print("=" * 80)
    
    # 1. Inicializar módulos
    print("\n[1] Inicializando módulos...")
    catalogo = GestorCatalogo()
    usuarios = GestorUsuarios(catalogo)
    recomendaciones = SistemaRecomendaciones(usuarios, catalogo)
    analizador = AnalizadorPatrones(usuarios, catalogo)
    
    # 2. Agregar libros al catálogo
    print("\n[2] Cargando catálogo de libros...")
    libros_data = [
        (1, "Harry Potter 1", "J.K. Rowling", 1997, "Fantasía", 3),
        (2, "Harry Potter 2", "J.K. Rowling", 1998, "Fantasía", 2),
        (3, "El Señor de los Anillos", "J.R.R. Tolkien", 1954, "Fantasía", 2),
        (4, "1984", "George Orwell", 1949, "Ficción", 1),
        (5, "Clean Code", "Robert Martin", 2008, "Programación", 3),
        (6, "Python Avanzado", "Guido van Rossum", 2020, "Programación", 2),
        (7, "El Código Da Vinci", "Dan Brown", 2003, "Misterio", 2),
        (8, "Sherlock Holmes", "Arthur Conan Doyle", 1887, "Misterio", 1),
    ]
    
    for libro_id, titulo, autor, año, genero, copias in libros_data:
        libro = Libro(libro_id, titulo, autor, año, genero, copias)
        catalogo.agregar_libro(libro)
    
    print(f"✓ {catalogo.cantidad_total_libros()} libros cargados")
    print(f"  Géneros: {catalogo.generos_disponibles()}")
    
    # 3. Registrar usuarios
    print("\n[3] Registrando usuarios...")
    usuarios_data = [
        ("U001", "Juan Pérez", "juan@email.com"),
        ("U002", "María García", "maria@email.com"),
        ("U003", "Carlos López", "carlos@email.com"),
    ]
    
    for user_id, nombre, email in usuarios_data:
        usuarios.registrar_usuario(user_id, nombre, email)
    
    print(f"✓ {usuarios.usuarios_conectados()} usuarios registrados")
    
    # 4. Agregar preferencias
    print("\n[4] Configurando preferencias de usuarios...")
    usuario1 = usuarios.obtener_usuario("U001")
    usuario1.agregar_genero_favorito("Fantasía")
    usuario1.agregar_genero_favorito("Programación")
    
    usuario2 = usuarios.obtener_usuario("U002")
    usuario2.agregar_genero_favorito("Misterio")
    usuario2.agregar_genero_favorito("Fantasía")
    
    usuario3 = usuarios.obtener_usuario("U003")
    usuario3.agregar_genero_favorito("Programación")
    usuario3.agregar_genero_favorito("Ficción")
    
    print("✓ Preferencias configuradas")
    
    # 5. Realizar préstamos
    print("\n[5] Realizando préstamos...")
    
    prestamos = [
        ("U001", 1, "2026-05-07"),  # Juan → Harry Potter 1
        ("U001", 5, "2026-05-07"),  # Juan → Clean Code
        ("U002", 7, "2026-05-07"),  # María → El Código Da Vinci
        ("U003", 6, "2026-05-07"),  # Carlos → Python Avanzado
        ("U003", 4, "2026-05-08"),  # Carlos → 1984
    ]
    
    for user_id, libro_id, fecha in prestamos:
        exito, mensaje = usuarios.prestar_libro(user_id, libro_id, fecha)
        if exito:
            print(f"  ✓ {mensaje}")
        else:
            print(f"  ✗ {mensaje}")
    
    # 6. Mostrar préstamos activos
    print("\n[6] Préstamos activos por usuario:")
    for user_id in ["U001", "U002", "U003"]:
        usuario = usuarios.obtener_usuario(user_id)
        activos = usuarios.obtener_prestamos_activos(user_id)
        print(f"  {usuario.nombre}: {len(activos)} libro(s)")
    
    # 7. Análisis de disponibilidad
    print("\n[7] Estado del catálogo:")
    disponibles = catalogo.libros_disponibles()
    print(f"  Libros disponibles: {len(disponibles)}/{catalogo.cantidad_total_libros()}")
    print("  Primer libro disponible:", disponibles[0])
    
    # 8. Recomendaciones
    print("\n[8] Sistema de recomendaciones:")
    recomendados = recomendaciones.recomendar_por_genero("U001", limite=3)
    print(f"  Recomendaciones para Juan Pérez:")
    for libro in recomendados:
        print(f"    - {libro.titulo} ({libro.genero})")
    
    # 9. Libros similares
    print("\n[9] Libros similares:")
    similares = recomendaciones.libros_similares(1, limite=3)
    print(f"  Similar a 'Harry Potter 1':")
    for libro in similares:
        print(f"    - {libro.titulo}")
    
    # 10. Devoluciones
    print("\n[10] Procesando devoluciones...")
    exito, mensaje = usuarios.devolver_libro("U001", 1)
    print(f"  {mensaje}")
    
    # 11. Análisis de patrones
    print("\n[11] Análisis de patrones:")
    
    # Libros más solicitados
    top_libros = analizador.libros_mas_solicitados(limite=3)
    print(f"  Libros más solicitados:")
    for libro in top_libros:
        if libro.copias_totales > libro.copias_disponibles:
            print(f"    - {libro.titulo} ({libro.copias_totales - libro.copias_disponibles}/{libro.copias_totales} prestados)")
    
    # Géneros trending
    trending = analizador.generos_trending()
    print(f"  Géneros trending:")
    for genero, cantidad in trending[:3]:
        if cantidad > 0:
            print(f"    - {genero}: {cantidad} libro(s) en préstamo")
    
    # Usuarios más activos
    activos = analizador.usuarios_mas_activos(limite=2)
    print(f"  Usuarios más activos:")
    for usuario in activos:
        cantidad = len(usuario.historial_prestamos.obtener_historial())
        if cantidad > 0:
            print(f"    - {usuario.nombre}: {cantidad} préstamo(s)")
    
    # Intereses comunes
    comunes = analizador.usuarios_con_intereses_comunes("U001", "U002")
    print(f"  Intereses comunes (Juan & María): {comunes}")
    
    # 12. Estadísticas
    print("\n[12] Estadísticas de la biblioteca:")
    stats = analizador.estadisticas_biblioteca()
    for clave, valor in stats.items():
        print(f"  {clave}: {valor}")
    
    print("\n" + "=" * 80)


# ============================================================================
# ANÁLISIS DE COMPLEJIDAD
# ============================================================================

def mostrar_analisis_complejidad():
    """Muestra análisis de complejidad de operaciones"""
    
    print("\n" + "=" * 80)
    print("ANÁLISIS DE COMPLEJIDAD - GESTOR DE BIBLIOTECA")
    print("=" * 80)
    
    analisis = {
        "BÚSQUEDAS": {
            "Buscar libro por ID": {
                "complejidad": "O(1)",
                "razon": "Diccionario -> acceso directo",
                "alternativa": "Lista -> O(n)"
            },
            "Buscar por título": {
                "complejidad": "O(n)",
                "razon": "Necesita recorrer todos los libros",
                "alternativa": "Índice invertido -> O(1)"
            },
            "Buscar por género": {
                "complejidad": "O(m)",
                "razon": "m = cantidad libros en ese género",
                "alternativa": "Sin índice -> O(n)"
            },
        },
        
        "PRÉSTAMOS": {
            "Agregar préstamo": {
                "complejidad": "O(1)",
                "razon": "Lista ligada: inserción al inicio",
                "alternativa": "Array -> O(n) si está lleno"
            },
            "Obtener historial": {
                "complejidad": "O(n)",
                "razon": "n = cantidad de préstamos del usuario",
                "alternativa": "Array -> O(n) igual, pero con acceso aleatorio"
            },
            "Contar activos": {
                "complejidad": "O(n)",
                "razon": "Recursión recorre toda la lista",
                "alternativa": "Iterativo -> O(n) igual"
            },
        },
        
        "ANÁLISIS": {
            "Libros trending": {
                "complejidad": "O(n log n)",
                "razon": "n = cantidad libros, incluye sort",
                "alternativa": "Heap -> O(n log k) si k top"
            },
            "Géneros comunes": {
                "complejidad": "O(m)",
                "razon": "m = tamaño conjunto más pequeño",
                "alternativa": "Loop -> O(n*m) sin conjunto"
            },
            "Usuarios frecuentes": {
                "complejidad": "O(u log u)",
                "razon": "u = usuarios, incluye sort",
                "alternativa": "Conteo -> O(u) sin ordenar"
            },
        }
    }
    
    for categoria, operaciones in analisis.items():
        print(f"\n### {categoria}")
        for op, detalles in operaciones.items():
            print(f"\n  {op}:")
            print(f"    Complejidad: {detalles['complejidad']}")
            print(f"    Razón: {detalles['razon']}")
            print(f"    Alternativa: {detalles['alternativa']}")
    
    print("\n" + "=" * 80)


# ============================================================================
# VENTAJAS DE LAS ESTRUCTURAS ELEGIDAS
# ============================================================================

def mostrar_ventajas_estructuras():
    """Explica por qué cada estructura fue elegida"""
    
    print("\n" + "=" * 80)
    print("VENTAJAS DE LAS ESTRUCTURAS DE DATOS SELECCIONADAS")
    print("=" * 80)
    
    ventajas = {
        "📚 DICCIONARIO (Catálogo)": {
            "ventaja_principal": "Acceso O(1) a cualquier libro",
            "razon": "Hash table con índice por ID",
            "impacto": "Búsqueda instantánea sin importar cantidad",
            "caso_uso": "Sistema con 100K libros sigue siendo O(1)",
            "problema_resuelto": "Sin dict: O(n) búsqueda = lentitud con muchos libros"
        },
        
        "🔗 LISTA LIGADA (Historial)": {
            "ventaja_principal": "Inserción O(1) sin reorganizar memoria",
            "razon": "Solo enlaza nodos, no copia datos",
            "impacto": "Millones de préstamos sin degradación",
            "caso_uso": "Historial crece indefinidamente eficientemente",
            "problema_resuelto": "Sin lista: Array -> O(n) cada inserción"
        },
        
        " CONJUNTOS (Favoritos/Géneros)": {
            "ventaja_principal": "Eliminación de duplicados automática + O(1) búsqueda",
            "razon": "Hash set: sin valores duplicados",
            "impacto": "Integridad garantizada de datos",
            "caso_uso": "Géneros favoritos nunca se repiten",
            "problema_resuelto": "Sin set: validación manual = error prone"
        },
        
        " RECURSIÓN (Análisis)": {
            "ventaja_principal": "Código elegante y mantenible para operaciones profundas",
            "razon": "Naturalidad del problema: árbol de categorías",
            "impacto": "Menos bugs, más legibilidad",
            "caso_uso": "Recomendaciones en cadena de géneros relacionados",
            "problema_resuelto": "Sin recursión: loops anidados = complejidad"
        }
    }
    
    for estructura, beneficios in ventajas.items():
        print(f"\n{estructura}")
        for aspecto, descripcion in beneficios.items():
            print(f"  • {aspecto.upper()}: {descripcion}")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    # Ejecutar demostración
    demo_basico()
    
    # Mostrar análisis
    mostrar_analisis_complejidad()
    
    # Mostrar ventajas
    mostrar_ventajas_estructuras()
    
    print("\n✓ Demostración completada")
