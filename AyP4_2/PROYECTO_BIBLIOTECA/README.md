# 📚 GESTOR DE BIBLIOTECA INTELIGENTE

## Proyecto Final - Algoritmos y Programación 4

---

## 📋 DESCRIPCIÓN

Sistema integral de gestión para una biblioteca que utiliza estructuras de datos avanzadas para optimizar búsquedas, recomendaciones y análisis de comportamiento de usuarios.

**Fecha entrega:** Semana del 25 de mayo  
**Integrantes:** 2-3 personas  
**Presentación:** 10-15 minutos  

---

## 🏗️ ARQUITECTURA

```
GESTOR BIBLIOTECA
├── 📊 GESTOR CATÁLOGO
│   └── Diccionario {ID: Libro} → O(1) búsqueda
│
├── 👥 GESTOR USUARIOS
│   ├── Diccionario {ID: Usuario} → O(1) búsqueda
│   └── HistorialPrestamos (Lista Ligada) → O(1) inserción
│
├── 💡 SISTEMA RECOMENDACIONES
│   ├── Análisis por género (Conjuntos)
│   ├── Libros similares (Diccionario + Conjuntos)
│   └── Usuarios con interés común (Recursión)
│
└── 📈 ANALIZADOR PATRONES
    ├── Libros más solicitados (Sort → O(n log n))
    ├── Géneros trending (Diccionario + Sort)
    └── Usuarios más activos (Sort → O(u log u))
```

---

## 🔧 MÓDULOS

### 1. `estructura_datos.py`
Define las entidades base del sistema:

- **Nodo**: Para lista ligada de préstamos
- **HistorialPrestamos**: Lista ligada con operaciones recursivas
- **Libro**: Entidad con atributos de libro
- **Usuario**: Perfil con historial y preferencias

**Complejidades clave:**
| Operación | Complejidad |
|-----------|------------|
| Agregar préstamo | O(1) |
| Obtener historial | O(n) |
| Contar activos | O(n) con recursión |

---

### 2. `modulos_gestion.py`
Implementa las 3 funcionalidades principales:

#### **GestorCatalogo**
- ✓ Agregar/buscar libros (O(1) por ID)
- ✓ Indexación por género y autor
- ✓ Filtrado de disponibles

#### **GestorUsuarios**
- ✓ Registro de usuarios
- ✓ Gestión de préstamos (O(1) agregar)
- ✓ Devoluciones (O(n) búsqueda)
- ✓ Historial completo

#### **SistemaRecomendaciones**
- ✓ Recomendaciones por género (O(n log n))
- ✓ Libros similares (O(n) con conjuntos)
- ✓ Usuarios con interés común (Recursión)

---

### 3. `analizador_patrones.py`
Análisis avanzado del comportamiento:

- **Libros más solicitados**: O(n log n) ordenamiento
- **Usuarios más activos**: O(u log u)
- **Géneros trending**: O(n) con diccionario
- **Estadísticas**: O(n + u)

---

### 4. `main.py`
Punto de entrada con demostración completa:
- Carga de datos
- Ejecución de operaciones
- Análisis de complejidad
- Ventajas de estructuras

---

## 📊 COMPLEJIDAD DE OPERACIONES

| Operación | Complejidad | Estructura |
|-----------|------------|-----------|
| Buscar libro por ID | O(1) | Diccionario |
| Buscar por título | O(n) | Búsqueda lineal |
| Buscar por género | O(m) | Diccionario indexado |
| Agregar préstamo | O(1) | Lista ligada |
| Obtener historial | O(n) | Lista ligada |
| Contar activos | O(n) | Recursión |
| Recomendaciones | O(n log n) | Sort de libros |
| Géneros comunes | O(m) | Intersección de conjuntos |
| Libros trending | O(n log n) | Sort |
| Usuarios frecuentes | O(u log u) | Sort |

---

## 🎯 VENTAJAS DE LAS ESTRUCTURAS

### **Diccionario (Catálogo)**
```
PROBLEMA: Búsqueda lenta en catálogo de 100K libros

SIN DICCIONARIO (Array):
  Buscar libro ID #50000 → Recorrer 50000 items → O(n)
  
CON DICCIONARIO:
  Buscar libro ID #50000 → Hash directo → O(1)
  
IMPACTO: 50000x más rápido con muchos libros
```

### **Lista Ligada (Historial)**
```
PROBLEMA: Historial crece indefinidamente

SIN LISTA LIGADA (Array):
  Agregar préstamo #10000 → Reallocar memoria → O(n)
  
CON LISTA LIGADA:
  Agregar préstamo #10000 → Solo enlazar nodo → O(1)
  
IMPACTO: Millones de préstamos sin degradación
```

### **Conjuntos (Favoritos)**
```
PROBLEMA: Géneros duplicados y búsqueda lenta

SIN CONJUNTOS (Lista):
  Agregar género → Validar manualmente → O(n)
  
CON CONJUNTOS:
  Agregar género → Set automático → O(1)
  
IMPACTO: Cero duplicados garantizado
```

### **Recursión (Análisis)**
```
PROBLEMA: Análisis profundo de categorías

ITERATIVO:
  Loops anidados = complejidad exponencial
  Código difícil de mantener
  
RECURSIVO:
  Divide problema en subproblemas
  Código legible y elegante
  
IMPACTO: Mantenibilidad + Escalabilidad
```

---

## 🚀 CÓMO EJECUTAR

```bash
# Navegar a la carpeta
cd PROYECTO_BIBLIOTECA

# Ejecutar demostración completa
python main.py

# Esperado:
# - Carga de 8 libros
# - Registro de 3 usuarios
# - 5 préstamos realizados
# - Análisis de recomendaciones
# - Estadísticas finales
# - Análisis de complejidad
```

---

## 📈 CASOS DE USO DEMOSTRADOS

### Caso 1: Nueva Afiliación
```
Usuario → Registrar → Sistema asigna ID
Complejidad: O(1)
```

### Caso 2: Buscar Libro
```
"Quiero un libro de Fantasía" 
→ Buscar por género → Retorna lista disponible
Complejidad: O(m) siendo m libros en ese género
Alternativa sin índices: O(n)
```

### Caso 3: Préstamo
```
Usuario + Libro + Fecha 
→ Verificar disponibilidad (O(1))
→ Agregar a historial (O(1))
→ Actualizar stock (O(1))
Complejidad total: O(1)
```

### Caso 4: Recomendación
```
Usuario → Obtener géneros favoritos (O(1))
→ Filtrar libros disponibles (O(n))
→ Ordenar por popularidad (O(n log n))
→ Retornar top 5
Complejidad: O(n log n)
```

### Caso 5: Análisis Trending
```
Todos los libros → Contar prestados por género (O(n))
→ Ordenar (O(n log n))
→ Mostrar top
Complejidad: O(n log n)
```

---

## 💾 ESTRUCTURA DE CARPETAS

```
PROYECTO_BIBLIOTECA/
├── estructura_datos.py       # Nodo, Historial, Libro, Usuario
├── modulos_gestion.py        # GestorCatalogo, GestorUsuarios, SistemaRecomendaciones
├── analizador_patrones.py    # Análisis y estadísticas
├── main.py                   # Demostración + análisis
├── README.md                 # Este archivo
└── pruebas_complejidad.py    # Tests de rendimiento (OPCIONAL)
```

---

## 🎓 CONCEPTOS APLICADOS

- ✅ **Listas Ligadas**: Historial de préstamos con O(1) inserción
- ✅ **Conjuntos (Sets)**: Géneros favoritos, libros sin duplicados
- ✅ **Diccionarios**: Catálogo O(1), usuarios O(1)
- ✅ **Recursión**: Análisis profundo, recomendaciones
- ✅ **Análisis Big-O**: Documentado en cada módulo
- ✅ **Modularización**: Código separado por responsabilidad

---

## 🎬 PRESENTACIÓN (10-15 MIN)

### Estructura sugerida:

**1. INTRO (1 min)**
- Problema: Biblioteca necesita buscar 100K libros rápido
- Solución: Arquitectura optimizada

**2. ARQUITECTURA (2 min)**
- Diagrama de módulos
- Estructura de datos seleccionada

**3. VENTAJAS (5 min)**
```
Diccionario:        Búsqueda O(1) vs O(n)
Lista Ligada:       Inserción O(1) sin reallocar
Conjuntos:          Cero duplicados + O(1) búsqueda
Recursión:          Análisis elegante
```

**4. DEMO (4 min)**
- Cargar catálogo
- Usuarios realizan préstamo
- Sistema recomienda libros
- Mostrar trending

**5. MÉTRICAS (2 min)**
- Gráfico: Tiempo vs cantidad de libros
- Comparativa: Tu implementación vs ingenua

**6. PREGUNTAS (1 min)**

---

## 📝 CHECKLIST ENTREGA

- [x] 4 estructuras de datos: Listas ligadas, Conjuntos, Diccionarios, Recursión
- [x] 4 módulos implementados
- [x] Análisis Big-O documentado
- [x] Ventajas de cada estructura
- [x] Demostración funcional completa
- [x] Código modular y documentado
- [x] README con explicación

---

## 🔧 EXTENSIONES POSIBLES

1. **Guardar/Cargar datos** (JSON o CSV)
2. **Web app** (Flask/Django)
3. **Base de datos** (SQLite/PostgreSQL)
4. **Interfaz gráfica** (Tkinter/PyQt)
5. **Notificaciones** (correos de recordatorios)
6. **Multas por atrasos** (cálculo automático)
7. **Reservas** (cola de espera)

---

**Autor**: Tu nombre aquí  
**Integrantes**: 2-3 personas  
**Fecha**: Mayo 2026  
**Materia**: Algoritmos y Programación 4  
