"""
═══════════════════════════════════════════════════════════════════════════════
                 QUIZ CONJUNTOS - EJEMPLOS SIMILARES AL EXAMEN
                    Algoritmos y Programación 4 - Preparación
═══════════════════════════════════════════════════════════════════════════════

ESTRUCTURA ESPERADA EN EL QUIZ:
- PARTE 1: Validación usando conjuntos de Python (3-4 puntos)
  ✓ Validar filas/elementos sin repetir
  ✓ Validar columnas/grupos
  ✓ Validar subcuadros/secciones

- PARTE 2: Verificación de relaciones con Conjunto en listas (2-3 puntos)
  ✓ Función es_subconjunto()
  ✓ Función tiene_permisos() o similar
  ✓ Recorrer la lista enlazada correctamente

TIPS:
✓ Usa set() en Parte 1, clase Conjunto en Parte 2
✓ Recuerda: set(lista) automáticamente elimina duplicados
✓ Para subconjuntos: recorre A y verifica cada elemento en B
✓ es_subconjunto retorna True solo si TODOS están en B
"""

# ═══════════════════════════════════════════════════════════════════════════════
#                    CLASE NODO Y CONJUNTO (Para Parte 2)
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
#                    PARTE 1: VALIDADOR DE CUADRO LATINO 4x4
# ═══════════════════════════════════════════════════════════════════════════════

"""
SIMILAR AL EXAMEN DE SUDOKU PERO CON MATRIZ 4x4
Validar que cada fila, columna y subcuadro 2x2 tenga {1,2,3,4}
"""

NUMEROS_VALIDOS_4 = {1, 2, 3, 4}


CUADRO_LATIN = [
    [1, 2, 3, 4],
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [4, 3, 2, 1]
]

# Solucion 1.1: Validar fila
def validar_fila_latin(cuadro, num_fila):
    """Validar que una fila tenga {1,2,3,4} sin repetir"""
    fila = set(cuadro[num_fila])
    return fila == NUMEROS_VALIDOS_4

# Solucion 1.2: Validar columna
def validar_columna_latin(cuadro, num_columna):
    """Validar que una columna tenga {1,2,3,4} sin repetir"""
    columna = set(cuadro[i][num_columna] for i in range(4))
    return columna == NUMEROS_VALIDOS_4

# Solucion 1.3: Validar subcuadro 2x2
def validar_subcuadro_2x2(cuadro, fila_inicio, col_inicio):
    """Validar que un subcuadro 2x2 tenga {1,2,3,4} sin repetir"""
    subcuadro = set()
    for i in range(fila_inicio, fila_inicio + 2):
        for j in range(col_inicio, col_inicio + 2):
            subcuadro.add(cuadro[i][j])
    return subcuadro == NUMEROS_VALIDOS_4

print("="*70)
print("EJEMPLO 1: VALIDADOR DE CUADRO LATINO 4x4")
print("="*70)

print(f"\n📋 Validando filas:")
for i in range(4):
    resultado = validar_fila_latin(CUADRO_LATIN, i)
    print(f"  Fila {i+1}: {'✓' if resultado else '✗'}")

print(f"\n📋 Validando columnas:")
for j in range(4):
    resultado = validar_columna_latin(CUADRO_LATIN, j)
    print(f"  Columna {j+1}: {'✓' if resultado else '✗'}")

print(f"\n📋 Validando subcuadros 2x2:")
for fi in [0, 2]:
    for ci in [0, 2]:
        resultado = validar_subcuadro_2x2(CUADRO_LATIN, fi, ci)
        print(f"  Subcuadro ({fi//2+1},{ci//2+1}): {'✓' if resultado else '✗'}")


# ═══════════════════════════════════════════════════════════════════════════════
#                    PARTE 2: VALIDADOR DE HORARIO - SIMILAR SUDOKU
# ═══════════════════════════════════════════════════════════════════════════════

"""
Cada profesor tiene 5 clases de 1 hora.
Validar que cada fila (profesor), columna (hora) y subcuadro 2x5
tenga números 1-5 sin repetir
"""

NUMEROS_VALIDOS_5 = {1, 2, 3, 4, 5}

HORARIOS = [
    [1, 2, 3, 4, 5],  # Profesor 1
    [3, 4, 5, 1, 2],  # Profesor 2  
    [5, 1, 2, 3, 4],  # Profesor 3
    [2, 3, 4, 5, 1],  # Profesor 4
    [4, 5, 1, 2, 3]   # Profesor 5
]

def validar_fila_horario(tabla, num_fila):
    """Validar fila de horarios"""
    fila = set(tabla[num_fila])
    return fila == NUMEROS_VALIDOS_5

def validar_columna_horario(tabla, num_columna):
    """Validar columna de horarios"""
    columna = set(tabla[i][num_columna] for i in range(5))
    return columna == NUMEROS_VALIDOS_5

print("\n" + "="*70)
print("EJEMPLO 2: VALIDADOR DE HORARIOS (Similar a Sudoku 5x5)")
print("="*70)

print(f"\n📋 Validando profesores (filas):")
for i in range(5):
    resultado = validar_fila_horario(HORARIOS, i)
    print(f"  Profesor {i+1}: {'✓' if resultado else '✗'}")

print(f"\n📋 Validando horas (columnas):")
for j in range(5):
    resultado = validar_columna_horario(HORARIOS, j)
    print(f"  Hora {j+1}: {'✓' if resultado else '✗'}")


# ═══════════════════════════════════════════════════════════════════════════════
#                    PARTE 3: VALIDACIÓN DE INVENTARIO (Parte 1)
# ═══════════════════════════════════════════════════════════════════════════════

"""
Una tienda debe validar códigos de productos.
El código debe contener exactamente 6 dígitos diferentes: {0,1,2,3,4,5}
"""

DIGITOS_VALIDOS = {0, 1, 2, 3, 4, 5}

codigos = {
    'PROD001': [0, 1, 2, 3, 4, 5],  # ✓ Válido
    'PROD002': [0, 1, 2, 3, 4],     # ✗ Incompleto
    'PROD003': [0, 0, 1, 2, 3, 4],  # ✗ Tiene repetidos
    'PROD004': [0, 1, 2, 3, 4, 6],  # ✗ Tiene código inválido
}

def validar_codigo(digitos):
    """Validar que el código tenga exactamente {0,1,2,3,4,5}"""
    codigo_set = set(digitos)
    return codigo_set == DIGITOS_VALIDOS

def digitos_faltantes(digitos):
    """Retorna los dígitos que faltan"""
    codigo_set = set(digitos)
    return DIGITOS_VALIDOS - codigo_set

print("\n" + "="*70)
print("EJEMPLO 3: VALIDACIÓN DE CÓDIGOS DE PRODUCTO")
print("="*70)

for nombre, digitos in codigos.items():
    valido = validar_codigo(digitos)
    faltantes = digitos_faltantes(digitos)
    print(f"\n{nombre}: {digitos}")
    print(f"  ¿Válido? {valido}")
    if not valido:
        print(f"  Faltantes: {faltantes if faltantes else 'Ninguno'}")


# ═══════════════════════════════════════════════════════════════════════════════
#                    PARTE 2 (DEL QUIZ): SISTEMA DE PERMISOS
# ═══════════════════════════════════════════════════════════════════════════════

# PUNTO 2.1: Verificar subconjunto
def es_subconjunto(conjunto_a, conjunto_b):
    """
    Retorna True si conjunto_a ⊆ conjunto_b
    Es decir, si TODOS los elementos de A están en B
    
    Algoritmo:
    1. Recorrer cada elemento de A (desde la cabeza)
    2. Verificar que existe en B
    3. Si alguno NO existe, retornar False
    4. Si todos existen, retornar True
    """
    actual = conjunto_a.cabeza
    while actual:
        if not conjunto_b.pertenece(actual.dato):
            return False
        actual = actual.siguiente
    return True

# PUNTO 2.2: Verificar permisos
def tiene_acceso(acceso_usuario, acceso_requerido):
    """
    Retorna True si el usuario tiene TODOS los accesos requeridos
    Usa es_subconjunto verificando si requerido ⊆ usuario
    """
    return es_subconjunto(acceso_requerido, acceso_usuario)

print("\n" + "="*70)
print("EJEMPLO 4: SISTEMA DE PERMISOS CON LISTAS ENLAZADAS")
print("="*70)

# Crear roles
admin = Conjunto(["crear_usuario", "eliminar_usuario", "leer", "escribir", "respaldar"])
moderador = Conjunto(["leer", "escribir", "bloquear"])
visitante = Conjunto(["leer"])

print(f"\n👤 Roles del sistema:")
print(f"  Admin: {admin}")
print(f"  Moderador: {moderador}")
print(f"  Visitante: {visitante}")

# Acciones con sus requisitos
accion_crear_post = Conjunto(["leer", "escribir"])
accion_bloquear = Conjunto(["bloquear"])
accion_respaldar = Conjunto(["respaldar"])
accion_leer = Conjunto(["leer"])

print(f"\n📋 Acciones y permisos requeridos:")
print(f"  Crear post: {accion_crear_post}")
print(f"  Bloquear usuario: {accion_bloquear}")
print(f"  Respaldar: {accion_respaldar}")
print(f"  Solo leer: {accion_leer}")

print(f"\n✅ ¿Quién puede hacer qué?")
print(f"  ¿Visitante puede crear post? {tiene_acceso(visitante, accion_crear_post)}")
print(f"  ¿Visitante puede leer? {tiene_acceso(visitante, accion_leer)}")
print(f"  ¿Moderador puede bloquear? {tiene_acceso(moderador, accion_bloquear)}")
print(f"  ¿Moderador puede respaldar? {tiene_acceso(moderador, accion_respaldar)}")
print(f"  ¿Admin puede respaldar? {tiene_acceso(admin, accion_respaldar)}")
print(f"  ¿Admin puede hacer todo? {tiene_acceso(admin, accion_crear_post)} + {tiene_acceso(admin, accion_bloquear)}")

# Verificar relaciones de subconjuntos
print(f"\n🔍 Relaciones de roles:")
print(f"  ¿Visitante ⊆ Moderador? {es_subconjunto(visitante, moderador)}")
print(f"  ¿Moderador ⊆ Admin? {es_subconjunto(moderador, admin)}")
print(f"  ¿Admin ⊆ Moderador? {es_subconjunto(admin, moderador)}")


# ═══════════════════════════════════════════════════════════════════════════════
#                    EJEMPLO 5: SISTEMA DE PRIVILEGIOS ADICIONALES
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EJEMPLO 5: SISTEMA DE PRIVILEGIOS DE CURSOS")
print("="*70)

# Privilegios por rol  
profesor = Conjunto(["calificar", "crear_tareas", "editar_contenido", "ver_estudiantes"])
asistente = Conjunto(["crear_tareas", "ver_estudiantes"])
estudiante = Conjunto(["enviar_tareas", "ver_contenido"])

print(f"\n👥 Roles de curso:")
print(f"  Profesor: {profesor}")
print(f"  Asistente: {asistente}")
print(f"  Estudiante: {estudiante}")

# Operaciones que requieren permisos
operacion_calificar = Conjunto(["calificar"])
operacion_crear_tareas = Conjunto(["crear_tareas"])
operacion_ver_contenido = Conjunto(["ver_contenido"])
operacion_editar_todo = Conjunto(["calificar", "crear_tareas", "editar_contenido"])

print(f"\n📋 Operaciones y requisitos:")
print(f"  Calificar: {operacion_calificar}")
print(f"  Crear tareas: {operacion_crear_tareas}")
print(f"  Ver contenido: {operacion_ver_contenido}")
print(f"  Editar todo: {operacion_editar_todo}")

print(f"\n✅ Acceso a operaciones:")
print(f"  ¿Profesor puede calificar? {tiene_acceso(profesor, operacion_calificar)}")
print(f"  ¿Profesor puede editar todo? {tiene_acceso(profesor, operacion_editar_todo)}")
print(f"  ¿Asistente puede crear tareas? {tiene_acceso(asistente, operacion_crear_tareas)}")
print(f"  ¿Asistente puede calificar? {tiene_acceso(asistente, operacion_calificar)}")
print(f"  ¿Estudiante puede ver contenido? {tiene_acceso(estudiante, operacion_ver_contenido)}")
print(f"  ¿Estudiante puede calificar? {tiene_acceso(estudiante, operacion_calificar)}")


# ═══════════════════════════════════════════════════════════════════════════════
#                    EJEMPLO 6: VALIDACIÓN DE HERRAMIENTAS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EJEMPLO 6: VALIDACIÓN DE HERRAMIENTAS DE DESARROLLO")
print("="*70)

# Herramientas disponibles en diferentes máquinas
maquina_frontend = Conjunto(["VS Code", "Node.js", "npm", "Git"])
maquina_backend = Conjunto(["Python", "PostgreSQL", "Git", "Docker"])
maquina_devops = Conjunto(["Docker", "Kubernetes", "Git", "Jenkins"])

print(f"\n🖥️  Herramientas disponibles:")
print(f"  Frontend: {maquina_frontend}")
print(f"  Backend: {maquina_backend}")
print(f"  DevOps: {maquina_devops}")

# Requisitos para proyectos
proyecto_frontend = Conjunto(["VS Code", "Node.js", "npm"])
proyecto_backend = Conjunto(["Python", "PostgreSQL", "Docker"])
proyecto_fullstack = Conjunto(["Git", "Docker"])

print(f"\n📁 Requisitos de proyectos:")
print(f"  Proyecto Frontend: {proyecto_frontend}")
print(f"  Proyecto Backend: {proyecto_backend}")
print(f"  Proyecto Fullstack: {proyecto_fullstack}")

print(f"\n🚀 ¿Dónde se pueden ejecutar?")
print(f"  ¿Frontend en máquina Frontend? {tiene_acceso(maquina_frontend, proyecto_frontend)}")
print(f"  ¿Frontend en máquina Backend? {tiene_acceso(maquina_backend, proyecto_frontend)}")
print(f"  ¿Backend en máquina Backend? {tiene_acceso(maquina_backend, proyecto_backend)}")
print(f"  ¿Backend en máquina Frontend? {tiene_acceso(maquina_frontend, proyecto_backend)}")
print(f"  ¿Fullstack en cualquiera? {tiene_acceso(maquina_frontend, proyecto_fullstack)} (Frontend), {tiene_acceso(maquina_backend, proyecto_fullstack)} (Backend)")


print("\n" + "="*70)
print("✅ FIN DE LA PREPARACIÓN - ¡ÉXITO EN TU QUIZ!")
print("="*70)


# ═══════════════════════════════════════════════════════════════════════════════
#                    EJEMPLOS ADICIONALES PARA MÁS PRÁCTICA
# ═══════════════════════════════════════════════════════════════════════════════

print("\n\n" + "█"*70)
print("SECCIÓN EXTRA: EJEMPLOS ADICIONALES COMPLETOS")
print("█"*70)

# EJEMPLO EXTRA 1: OPERACIONES BÁSICAS CON CONJUNTOS
print("\n" + "="*70)
print("EJEMPLO EXTRA 1: OPERACIONES BÁSICAS CON CONJUNTOS")
print("="*70)

def union(conjuntoA, conjuntoB):
    """Retorna A ∪ B (todos los elementos de A y B)"""
    resultado = Conjunto()
    actual = conjuntoA.cabeza
    while actual:
        resultado.agregar(actual.dato)
        actual = actual.siguiente
    actual = conjuntoB.cabeza
    while actual:
        resultado.agregar(actual.dato)
        actual = actual.siguiente
    return resultado

def interseccion(conjuntoA, conjuntoB):
    """Retorna A ∩ B (elementos comunes)"""
    resultado = Conjunto()
    actual = conjuntoA.cabeza
    while actual:
        if conjuntoB.pertenece(actual.dato):
            resultado.agregar(actual.dato)
        actual = actual.siguiente
    return resultado

def diferencia(conjuntoA, conjuntoB):
    """Retorna A - B (elementos en A pero NO en B)"""
    resultado = Conjunto()
    actual = conjuntoA.cabeza
    while actual:
        if not conjuntoB.pertenece(actual.dato):
            resultado.agregar(actual.dato)
        actual = actual.siguiente
    return resultado

# Crear conjuntos
A = Conjunto([1, 2, 3, 4])
B = Conjunto([3, 4, 5, 6])

print(f"\nConjunto A = {A}")
print(f"Conjunto B = {B}")
print(f"\n--- Operaciones ---")
print(f"A ∪ B = {union(A, B)}")
print(f"A ∩ B = {interseccion(A, B)}")
print(f"A - B = {diferencia(A, B)}")
print(f"B - A = {diferencia(B, A)}")

print(f"\n--- Relaciones ---")
print(f"¿A ⊆ B? {es_subconjunto(A, B)}")
print(f"¿B ⊆ A? {es_subconjunto(B, A)}")


# EJEMPLO EXTRA 2: SISTEMA DE PERMISOS DE USUARIO
print("\n" + "="*70)
print("EJEMPLO EXTRA 2: SISTEMA DE PERMISOS DE USUARIO")
print("="*70)

permisos_admin = Conjunto(["crear", "leer", "editar", "eliminar", "gestionar_usuarios"])
permisos_editor = Conjunto(["crear", "leer", "editar"])
permisos_viewer = Conjunto(["leer"])

print(f"\nPermisos Admin: {permisos_admin}")
print(f"Permisos Editor: {permisos_editor}")
print(f"Permisos Viewer: {permisos_viewer}")

print(f"\n¿Editor tiene menos permisos que Admin? {es_subconjunto(permisos_editor, permisos_admin)}")
print(f"Permisos exclusivos de Admin: {diferencia(permisos_admin, permisos_editor)}")


# EJEMPLO EXTRA 3: ANÁLISIS DE LENGUAJES DE PROGRAMACIÓN
print("\n" + "="*70)
print("EJEMPLO EXTRA 3: ANÁLISIS DE LENGUAJES DE PROGRAMACIÓN")
print("="*70)

saben_python = Conjunto(["Juan", "María", "Carlos", "Ana"])
saben_java = Conjunto(["Carlos", "Ana", "Pedro", "Luis"])
saben_javascript = Conjunto(["María", "Pedro", "Sofia"])

print(f"\nSaben Python: {saben_python}")
print(f"Saben Java: {saben_java}")
print(f"Saben JavaScript: {saben_javascript}")

python_y_java = interseccion(saben_python, saben_java)
print(f"\nSaben Python Y Java: {python_y_java}")

python_no_java = diferencia(saben_python, saben_java)
print(f"Saben Python pero NO Java: {python_no_java}")

todos = union(saben_python, saben_java)
todos = union(todos, saben_javascript)
print(f"Total de estudiantes únicos: {todos}")


# EJEMPLO EXTRA 4: VALIDADOR DE ESTÁNDARES
print("\n" + "="*70)
print("EJEMPLO EXTRA 4: VALIDADOR DE ESTÁNDARES")
print("="*70)

estándares_requeridos = Conjunto(["UTF-8", "HTTP/2", "SSL"])
estándares_servidor = Conjunto(["UTF-8", "HTTP/2", "SSL", "IPv6", "CORS"])

print(f"\nEstándares Requeridos: {estándares_requeridos}")
print(f"Estándares del Servidor: {estándares_servidor}")

cumple = es_subconjunto(estándares_requeridos, estándares_servidor)
print(f"\n¿Servidor cumple con todos los estándares? {cumple}")

extras = diferencia(estándares_servidor, estándares_requeridos)
print(f"Estándares extra (no requeridos): {extras}")


# EJEMPLO EXTRA 5: CONTROL DE INVENTARIO DE TIENDA
print("\n" + "="*70)
print("EJEMPLO EXTRA 5: CONTROL DE INVENTARIO DE TIENDA")
print("="*70)

stock_actual = Conjunto(["Laptop", "Mouse", "Teclado", "Monitor", "Webcam"])
productos_solicitados = Conjunto(["Mouse", "Teclado", "Headset", "Impresora"])

print(f"\nStock Actual: {stock_actual}")
print(f"Productos Solicitados: {productos_solicitados}")

puede_entregar = interseccion(stock_actual, productos_solicitados)
print(f"\nPuede entregar: {puede_entregar}")

falta_pedir = diferencia(productos_solicitados, stock_actual)
print(f"Debe pedir: {falta_pedir}")

tiene_extra = diferencia(stock_actual, productos_solicitados)
print(f"Stock sin demanda: {tiene_extra}")


# EJEMPLO EXTRA 6: ANÁLISIS DE REDES SOCIALES
print("\n" + "="*70)
print("EJEMPLO EXTRA 6: ANÁLISIS DE REDES SOCIALES")
print("="*70)

seguidores_A = Conjunto(["Juan", "María", "Carlos", "Ana", "Pedro"])
seguidores_B = Conjunto(["María", "Ana", "Luis", "Sofia"])

print(f"\nSeguidores Cuenta A: {seguidores_A}")
print(f"Seguidores Cuenta B: {seguidores_B}")

comunes = interseccion(seguidores_A, seguidores_B)
print(f"\nSeguidores comunes: {comunes}")

solo_a = diferencia(seguidores_A, seguidores_B)
print(f"Solo siguen A: {solo_a}")

solo_b = diferencia(seguidores_B, seguidores_A)
print(f"Solo siguen B: {solo_b}")

total = union(seguidores_A, seguidores_B)
print(f"Total de seguidores únicos: {total}")


# EJEMPLO EXTRA 7: VERIFICACIÓN DE ACCESO A RECURSOS
print("\n" + "="*70)
print("EJEMPLO EXTRA 7: VERIFICACIÓN DE ACCESO A RECURSOS")
print("="*70)

rol_admin = Conjunto(["crear_usuario", "eliminar_usuario", "editar_contenido", "ver_reportes"])
rol_moderador = Conjunto(["editar_contenido", "bloquear_usuario"])
rol_usuario = Conjunto(["comentar", "ver_contenido"])

accion_crear_usuario = Conjunto(["crear_usuario"])
accion_bloquear = Conjunto(["bloquear_usuario"])
accion_comentar = Conjunto(["comentar"])

print(f"\nRoles:")
print(f"  Admin: {rol_admin}")
print(f"  Moderador: {rol_moderador}")
print(f"  Usuario: {rol_usuario}")

print(f"\nAcciones:")
print(f"  Crear usuario: {accion_crear_usuario}")
print(f"  Bloquear: {accion_bloquear}")
print(f"  Comentar: {accion_comentar}")

print(f"\n¿Quién puede hacer qué?")
print(f"  Admin crear usuario: {tiene_acceso(rol_admin, accion_crear_usuario)}")
print(f"  Moderador bloquear: {tiene_acceso(rol_moderador, accion_bloquear)}")
print(f"  Usuario comentar: {tiene_acceso(rol_usuario, accion_comentar)}")
print(f"  Moderador crear usuario: {tiene_acceso(rol_moderador, accion_crear_usuario)}")


# EJEMPLO EXTRA 8: VALIDACIÓN DE TIPOS DE DATOS
print("\n" + "="*70)
print("EJEMPLO EXTRA 8: VALIDACIÓN DE TIPOS DE DATOS")
print("="*70)

tipos_email = Conjunto(["string"])
tipos_edad = Conjunto(["int"])
tipos_bio = Conjunto(["string", "null"])

print(f"\nTipos permitidos:")
print(f"  Email: {tipos_email}")
print(f"  Edad: {tipos_edad}")
print(f"  Bio: {tipos_bio}")

dato_email = "string"
dato_edad = "int"
dato_bio = "null"

print(f"\nValidaciones:")
print(f"  Email ({dato_email}): {tipos_email.pertenece(dato_email)}")
print(f"  Edad ({dato_edad}): {tipos_edad.pertenece(dato_edad)}")
print(f"  Bio ({dato_bio}): {tipos_bio.pertenece(dato_bio)}")


# EJEMPLO EXTRA 9: BÚSQUEDA POR PALABRAS CLAVE
print("\n" + "="*70)
print("EJEMPLO EXTRA 9: BÚSQUEDA POR PALABRAS CLAVE")
print("="*70)

palabras_clave = Conjunto(["python", "recursion", "listas"])

doc1 = Conjunto(["python", "recursion", "algoritmos"])
doc2 = Conjunto(["python", "listas", "estructura"])
doc3 = Conjunto(["java", "clases", "herencia"])
doc4 = Conjunto(["python", "recursion", "listas", "diccionarios"])

documentos = [("doc1", doc1), ("doc2", doc2), ("doc3", doc3), ("doc4", doc4)]

print(f"\nPalabras clave de búsqueda: {palabras_clave}\n")

for nombre, doc in documentos:
    coincidencias = interseccion(palabras_clave, doc)
    cumple_todas = es_subconjunto(palabras_clave, doc)
    
    print(f"{nombre}: {doc}")
    print(f"  Coincidencias: {coincidencias}")
    print(f"  ¿Contiene TODAS las palabras clave? {cumple_todas}\n")


# EJEMPLO EXTRA 10: ANÁLISIS DE COMPETENCIAS
print("\n" + "="*70)
print("EJEMPLO EXTRA 10: ANÁLISIS DE COMPETENCIAS PARA PUESTO")
print("="*70)

competencias_juan = Conjunto(["Python", "SQL", "Git"])
competencias_maria = Conjunto(["Python", "JavaScript", "SQL", "Git", "Docker"])
competencias_carlos = Conjunto(["Java", "C++", "Manual"])

requisitos = Conjunto(["Python", "SQL", "Git"])

print(f"\nCompetencias de candidatos:")
print(f"  Juan: {competencias_juan}")
print(f"  María: {competencias_maria}")
print(f"  Carlos: {competencias_carlos}")

print(f"\nRequisitos del puesto: {requisitos}\n")

for nombre, competencias in [("Juan", competencias_juan), 
                              ("María", competencias_maria), 
                              ("Carlos", competencias_carlos)]:
    cumple = es_subconjunto(requisitos, competencias)
    extras = diferencia(competencias, requisitos)
    falta = diferencia(requisitos, competencias)
    
    print(f"{nombre}:")
    print(f"  ¿Cumple requisitos? {cumple}")
    if extras.cabeza:
        print(f"  Competencias extra: {extras}")
    if not cumple:
        print(f"  Falta: {falta}")
    print()

print("\n" + "█"*70)
print("FIN DE TODOS LOS EJEMPLOS - ¡MUCHO ÉXITO EN TU QUIZ!")
print("█"*70)


# ═══════════════════════════════════════════════════════════════════════════════
#                    CASOS EXTREMOS Y OPERACIONES COMPLEJAS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n\n" + "▓"*70)
print("SECCIÓN FINAL: CASOS EXTREMOS Y OPERACIONES COMPLEJAS")
print("▓"*70)

# CASO EXTREMO 1: CONJUNTOS VACÍOS
print("\n" + "="*70)
print("CASO EXTREMO 1: MANEJO DE CONJUNTOS VACÍOS")
print("="*70)

conjunto_vacio = Conjunto()
conjunto_lleno = Conjunto([1, 2, 3])

print(f"\nConjunto vacío: {conjunto_vacio}")
print(f"Conjunto lleno: {conjunto_lleno}")

print(f"\n¿Conjunto vacío está vacío? {conjunto_vacio.esta_vacio()}")
print(f"¿Conjunto lleno está vacío? {conjunto_lleno.esta_vacio()}")

print(f"\n¿Conjunto vacío ⊆ Conjunto lleno? {es_subconjunto(conjunto_vacio, conjunto_lleno)}")
print(f"¿Conjunto lleno ⊆ Conjunto vacío? {es_subconjunto(conjunto_lleno, conjunto_vacio)}")

print(f"\nUnión con vacío: {union(conjunto_vacio, conjunto_lleno)}")
print(f"Intersección con vacío: {interseccion(conjunto_vacio, conjunto_lleno)}")
print(f"Diferencia con vacío: {diferencia(conjunto_lleno, conjunto_vacio)}")


# CASO EXTREMO 2: CONJUNTOS IGUALES
print("\n" + "="*70)
print("CASO EXTREMO 2: COMPARACIÓN DE CONJUNTOS IGUALES")
print("="*70)

conjunto_A = Conjunto([5, 10, 15])
conjunto_B = Conjunto([15, 5, 10])  # Mismo contenido, diferente orden

print(f"\nConjunto A: {conjunto_A}")
print(f"Conjunto B: {conjunto_B}")

son_iguales = es_subconjunto(conjunto_A, conjunto_B) and es_subconjunto(conjunto_B, conjunto_A)
print(f"\n¿A = B (mismo contenido)? {son_iguales}")
print(f"¿A ⊆ B? {es_subconjunto(conjunto_A, conjunto_B)}")
print(f"¿B ⊆ A? {es_subconjunto(conjunto_B, conjunto_A)}")


# CASO EXTREMO 3: OPERACIÓN COMPLEJA - (A ∩ B) ⊆ C
print("\n" + "="*70)
print("CASO EXTREMO 3: OPERACIÓN COMPLEJA - (A ∩ B) ⊆ C")
print("="*70)

conj_A = Conjunto([1, 2, 3, 4, 5])
conj_B = Conjunto([3, 4, 5, 6, 7])
conj_C = Conjunto([2, 3, 4, 5, 8, 9])

interseccion_AB = interseccion(conj_A, conj_B)

print(f"\nConjunto A: {conj_A}")
print(f"Conjunto B: {conj_B}")
print(f"Conjunto C: {conj_C}")

print(f"\nA ∩ B = {interseccion_AB}")
print(f"¿(A ∩ B) ⊆ C? {es_subconjunto(interseccion_AB, conj_C)}")


# CASO EXTREMO 4: DIFERENCIA SIMÉTRICA A Δ B
print("\n" + "="*70)
print("CASO EXTREMO 4: DIFERENCIA SIMÉTRICA (A Δ B)")
print("="*70)

conj_X = Conjunto([1, 2, 3, 4])
conj_Y = Conjunto([3, 4, 5, 6])

# A Δ B = (A - B) ∪ (B - A)
A_menos_B = diferencia(conj_X, conj_Y)
B_menos_A = diferencia(conj_Y, conj_X)
diferencia_simetrica = union(A_menos_B, B_menos_A)

print(f"\nConjunto X: {conj_X}")
print(f"Conjunto Y: {conj_Y}")

print(f"\nX - Y = {A_menos_B}")
print(f"Y - X = {B_menos_A}")
print(f"X Δ Y = {diferencia_simetrica}")


# CASO EXTREMO 5: VALIDAR TRES CONJUNTOS
print("\n" + "="*70)
print("CASO EXTREMO 5: VERIFICACIÓN DE TRES CONJUNTOS")
print("="*70)

ciudadanos = Conjunto(["Juan", "María", "Carlos", "Ana", "Pedro"])
estudiantes = Conjunto(["Juan", "María", "Carlos"])
trabajadores = Conjunto(["Pedro", "Ana", "Luis"])

print(f"\nCiudadanos: {ciudadanos}")
print(f"Estudiantes: {estudiantes}")
print(f"Trabajadores: {trabajadores}")

print(f"\n¿Estudiantes ⊆ Ciudadanos? {es_subconjunto(estudiantes, ciudadanos)}")
print(f"¿Trabajadores ⊆ Ciudadanos? {es_subconjunto(trabajadores, ciudadanos)}")

todos_registrados = union(estudiantes, trabajadores)
print(f"\nEstudiantes ∪ Trabajadores = {todos_registrados}")
print(f"¿Todos están en Ciudadanos? {es_subconjunto(todos_registrados, ciudadanos)}")

solo_estudiantes = diferencia(estudiantes, trabajadores)
solo_trabajadores = diferencia(trabajadores, estudiantes)
student_y_trabalor = interseccion(estudiantes, trabajadores)

print(f"\nSolo estudiantes: {solo_estudiantes}")
print(f"Solo trabajadores: {solo_trabajadores}")
print(f"Estudiantes Y Trabajadores: {student_y_trabalor}")


# CASO EXTREMO 6: VALIDACIÓN CON CONDICIONES MÚLTIPLES
print("\n" + "="*70)
print("CASO EXTREMO 6: VALIDACIÓN CON CONDICIONES MÚLTIPLES")
print("="*70)

# Un usuario puede hacer una acción si tiene TODOS los permisos requeridos
usuario1_permisos = Conjunto(["leer", "escribir", "crear"])
usuario2_permisos = Conjunto(["leer"])
usuario3_permisos = Conjunto(["leer", "escribir", "crear", "eliminar", "admin"])

accion_1 = Conjunto(["leer"])
accion_2 = Conjunto(["leer", "escribir"])
accion_3 = Conjunto(["leer", "escribir", "crear"])
accion_4 = Conjunto(["leer", "escribir", "crear", "eliminar"])

print(f"\nPermisos Usuario 1: {usuario1_permisos}")
print(f"Permisos Usuario 2: {usuario2_permisos}")
print(f"Permisos Usuario 3: {usuario3_permisos}")

print(f"\nAcciones requeridas:")
print(f"  Acción 1: {accion_1}")
print(f"  Acción 2: {accion_2}")
print(f"  Acción 3: {accion_3}")
print(f"  Acción 4: {accion_4}")

usuarios = [
    ("Usuario 1", usuario1_permisos),
    ("Usuario 2", usuario2_permisos),
    ("Usuario 3", usuario3_permisos)
]

acciones = [
    ("Acción 1", accion_1),
    ("Acción 2", accion_2),
    ("Acción 3", accion_3),
    ("Acción 4", accion_4)
]

print(f"\nMATRIZ DE PERMISOS (¿Puede hacer?)")
print(f"{'':15} | {'Acción 1':10} | {'Acción 2':10} | {'Acción 3':10} | {'Acción 4':10}")
print("-" * 65)

for user_nombre, user_perms in usuarios:
    resultados = []
    for acc_nombre, acc_perms in acciones:
        puede = tiene_acceso(user_perms, acc_perms)
        resultados.append("Sí" if puede else "No")
    print(f"{user_nombre:15} | {resultados[0]:10} | {resultados[1]:10} | {resultados[2]:10} | {resultados[3]:10}")


# CASO EXTREMO 7: CARDINALIDAD Y COMPARACIÓN DE TAMAÑOS
print("\n" + "="*70)
print("CASO EXTREMO 7: CARDINALIDAD Y COMPARACIÓN")
print("="*70)

# Necesitamos una función para obtener tamaño
def cardinalidad(conjunto):
    """Retorna la cantidad de elementos del conjunto"""
    return conjunto.tamaño

conj_1 = Conjunto([10, 20, 30])
conj_2 = Conjunto([1, 2, 3, 4])
conj_3 = Conjunto([5, 5, 5, 5])  # El agregar elimina duplicados

print(f"\nConjunto 1: {conj_1} → Cardinalidad: {cardinalidad(conj_1)}")
print(f"Conjunto 2: {conj_2} → Cardinalidad: {cardinalidad(conj_2)}")
print(f"Conjunto 3: {conj_3} → Cardinalidad: {cardinalidad(conj_3)}")

if cardinalidad(conj_1) < cardinalidad(conj_2):
    print(f"\nConjunto 1 es más pequeño que Conjunto 2")
elif cardinalidad(conj_1) > cardinalidad(conj_2):
    print(f"\nConjunto 1 es más grande que Conjunto 2")
else:
    print(f"\nConjuntos tienen igual tamaño")


# CASO EXTREMO 8: UNIÓN DE MÚLTIPLES CONJUNTOS
print("\n" + "="*70)
print("CASO EXTREMO 8: UNIÓN E INTERSECCIÓN DE 4 CONJUNTOS")
print("="*70)

habilidades_programacion = Conjunto(["Python", "JavaScript", "Java"])
habilidades_bd = Conjunto(["SQL", "MongoDB", "PostgreSQL"])
habilidades_devops = Conjunto(["Docker", "Kubernetes", "Git"])
habilidades_comunes = Conjunto(["Git", "Python"])

print(f"\nHabilidades Programación: {habilidades_programacion}")
print(f"Habilidades BD: {habilidades_bd}")
print(f"Habilidades DevOps: {habilidades_devops}")
print(f"Habilidades Comunes: {habilidades_comunes}")

todas_las_habilidades = union(habilidades_programacion, habilidades_bd)
todas_las_habilidades = union(todas_las_habilidades, habilidades_devops)
todas_las_habilidades = union(todas_las_habilidades, habilidades_comunes)

print(f"\nTodas las habilidades: {todas_las_habilidades}")
print(f"Total de habilidades únicas: {cardinalidad(todas_las_habilidades)}")

# Habilidades que aparecen en TODAS las categorías (intersección múltiple)
inter_1 = interseccion(habilidades_programacion, habilidades_bd)
inter_2 = interseccion(inter_1, habilidades_devops)
inter_3 = interseccion(inter_2, habilidades_comunes)

print(f"\nHabilidades en TODAS las categorías: {inter_3}")


# CASO EXTREMO 9: VALIDACIÓN COMPLEJA DE REQUISITOS
print("\n" + "="*70)
print("CASO EXTREMO 9: VALIDACIÓN COMPLEJA DE REQUISITOS LABORALES")
print("="*70)

# Requisitos para diferentes puestos
requisitos_junior = Conjunto([
    "Python",
    "Git",
    "Comunicación"
])

requisitos_senior = Conjunto([
    "Python",
    "Java", 
    "Git",
    "AWS",
    "Liderazgo",
    "SQL"
])

# Candidatos con sus habilidades
habilidades_candidato_1 = Conjunto([
    "Python",
    "Git",
    "Comunicación",
    "JavaScript"
])

habilidades_candidato_2 = Conjunto([
    "Python",
    "Java",
    "Git",
    "AWS",
    "Liderazgo",
    "SQL",
    "Docker"
])

habilidades_candidato_3 = Conjunto([
    "Python",
    "Git"
])

print(f"\nRequisitos Junior: {requisitos_junior}")
print(f"Requisitos Senior: {requisitos_senior}")

candidatos = [
    ("Candidato 1", habilidades_candidato_1),
    ("Candidato 2", habilidades_candidato_2),
    ("Candidato 3", habilidades_candidato_3)
]

print(f"\nCandidatos:")
for nombre, habilidades in candidatos:
    print(f"  {nombre}: {habilidades}")

print(f"\n¿Quién puede aplicar?")
for nombre, habilidades in candidatos:
    puede_junior = es_subconjunto(requisitos_junior, habilidades)
    puede_senior = es_subconjunto(requisitos_senior, habilidades)
    
    extras = diferencia(habilidades, requisitos_senior)
    falta_senior = diferencia(requisitos_senior, habilidades)
    
    print(f"\n{nombre}:")
    print(f"  ¿Puesto Junior? {puede_junior}")
    print(f"  ¿Puesto Senior? {puede_senior}")
    
    if not puede_senior and puede_junior:
        print(f"  → Recomendado para: Junior")
    elif puede_senior:
        print(f"  → Recomendado para: Senior")
        if extras.cabeza:
            print(f"    Habilidades adicionales: {extras}")
    else:
        print(f"  → Necesita: {falta_senior}")


# CASO EXTREMO 10: VALIDACIÓN DE PERTENENCIA EN LISTAS
print("\n" + "="*70)
print("CASO EXTREMO 10: VERIFICACIÓN DE PERTENENCIA")
print("="*70)

biblioteca = Conjunto(["El Quijote", "1984", "Cien años", "Fundación", "Neuromante"])
libros_buscados = ["El Quijote", "Harry Potter", "Fundación", "Dune"]

print(f"\nBiblioteca: {biblioteca}")
print(f"\nLibros buscados: {libros_buscados}")

disponibles = []
no_disponibles = []

for libro in libros_buscados:
    if biblioteca.pertenece(libro):
        disponibles.append(libro)
    else:
        no_disponibles.append(libro)

print(f"\nLibros disponibles: {disponibles}")
print(f"Libros NO disponibles: {no_disponibles}")


# CASO EXTREMO 11: VALIDACIÓN DE MATRIZ (Similar a Sudoku)
print("\n" + "="*70)
print("CASO EXTREMO 11: VALIDACIÓN CON MATRIZ INCOMPLETA")
print("="*70)

NUMEROS_ESPERADOS = {1, 2, 3, 4}

matriz_incompleta = [
    [1, 2, 3, 4],
    [3, 4, 1, 2],
    [2, 1, 4, 0],  # ❌ 0 en lugar de 3
    [4, 3, 2, 1]
]

print(f"\nMatriz a validar:")
for i, fila in enumerate(matriz_incompleta):
    print(f"  Fila {i+1}: {fila}")

print(f"\nValidación:")
todas_validas = True
for i in range(4):
    fila = set(matriz_incompleta[i])
    es_valida = fila == NUMEROS_ESPERADOS
    print(f"  Fila {i+1}: {'✓' if es_valida else '✗'} {fila}")
    if not es_valida:
        todas_validas = False
        falta = NUMEROS_ESPERADOS - fila
        extra = fila - NUMEROS_ESPERADOS
        if falta:
            print(f"    Falta: {falta}")
        if extra:
            print(f"    Extras: {extra}")

print(f"\n¿Matriz válida completa? {todas_validas}")


print("\n" + "▓"*70)
print("FIN - AHORA SI ESTÁS 100% PREPARADO PARA TU QUIZ")
print("▓"*70)

