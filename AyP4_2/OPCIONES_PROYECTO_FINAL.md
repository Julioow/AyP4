# 🎯 OPCIONES DE PROYECTO FINAL - Algoritmos y Programación 4

**Entrega:** Semana del 25 de mayo | **Integrantes:** 2-3 personas | **Duración presentación:** 10-15 min

---

## ✅ REQUISITOS CLAVE
- ✓ Listas ligadas
- ✓ Conjuntos (sets)
- ✓ Diccionarios
- ✓ Recursividad
- ✓ Análisis de complejidad Big-O
- ✓ Presentación enfocada en **ventajas de implementación**, no en código

---

## 📊 OPCIÓN 1: GESTOR DE BIBLIOTECA INTELIGENTE
**Dificultad:** ⭐⭐⭐ (Media) | **Potencial de presentación:** Alto

### Descripción
Sistema de gestión para una biblioteca que optimiza búsquedas de libros, recomendaciones y control de usuarios.

### Estructuras de datos
- **Lista Ligada:** Historial de préstamos de cada usuario (orden cronológico)
- **Conjuntos:** Géneros disponibles, libros favoritos, libros compartidos entre usuarios
- **Diccionario:** Catálogo de libros {ID: {título, autor, año, disponible, copias}}
- **Recursión:** Búsqueda de autores similares, recomendaciones basadas en historial

### Módulos
1. `GestorCatalogo` - Agregar/buscar libros
2. `GestorUsuarios` - Registro, préstamos, historial
3. `SistemaRecomendaciones` - Sugerencias por género/autor
4. `AnalizadorPatrones` - Libros más solicitados

### Ventajas en presentación
- Reduce búsqueda de O(n) a O(1) con diccionarios
- Conjuntos eliminan duplicados automáticamente
- Lista ligada permite historial eficiente
- Recursión para análisis profundo de similitudes

### Complejidad esperada
| Función | Complejidad |
|---------|-------------|
| Buscar libro | O(1) |
| Historial usuario | O(n) |
| Recomendaciones | O(n log n) |
| Libros compartidos | O(n) |

---

## 🎮 OPCIÓN 2: SISTEMA DE RANKING Y LOGROS DE VIDEOJUEGOS
**Dificultad:** ⭐⭐⭐⭐ (Media-Alta) | **Potencial de presentación:** Muy Alto

### Descripción
Plataforma que gestiona jugadores, calificaciones, logros desbloqueados y estadísticas personalizadas.

### Estructuras de datos
- **Lista Ligada:** Historial de partidas (fecha, puntuación, duración)
- **Conjuntos:** Logros desbloqueados, amigos conectados, logros especiales
- **Diccionario:** Perfiles de jugadores {username: {nivel, XP, logros, amigos}}
- **Recursión:** Cálculo de bonificaciones por combos, búsqueda de rutas más cortas en árbol de amigos

### Módulos
1. `GestorJugadores` - Registro, login, perfil
2. `GestorPartidas` - Guardar resultados, calcular XP
3. `SistemaLogros` - Desbloquear logros, verificar condiciones
4. `RedSocial` - Amigos, comparación de perfiles

### Ventajas en presentación
- Conjuntos garantizan logros sin duplicados
- Diccionario permite acceso O(1) a cualquier jugador
- Lista ligada mantiene orden cronológico eficientemente
- Recursión calcula bonificaciones automáticas en cadena

### Complejidad esperada
| Función | Complejidad |
|---------|-------------|
| Buscar jugador | O(1) |
| Historial partidas | O(n) |
| Desbloquear logro | O(1) |
| Amigos en común | O(m) |

---

## 🏥 OPCIÓN 3: SISTEMA DE GESTIÓN HOSPITALARIA
**Dificultad:** ⭐⭐⭐⭐ (Media-Alta) | **Potencial de presentación:** Alto

### Descripción
App para gestionar pacientes, citas médicas, historiales clínicos y disponibilidad de médicos/salas.

### Estructuras de datos
- **Lista Ligada:** Cola de espera de pacientes (FIFO para urgencias)
- **Conjuntos:** Diagnósticos por paciente, síntomas coincidentes, especialidades disponibles
- **Diccionario:** Base de datos de pacientes {cédula: {nombre, edad, alergias, historial}}
- **Recursión:** Búsqueda de especialista más cercano, análisis de síntomas relacionados

### Módulos
1. `GestorPacientes` - Registro, búsqueda, historial
2. `GestorCitas` - Agendar, cancelar, reschedule
3. `GestorMedicos` - Disponibilidad, especialidades
4. `AnalizadorDiagnósticos` - Síntomas → diagnóstico sugerido

### Ventajas en presentación
- Cola (lista ligada) optimiza atención prioritaria
- Conjuntos permiten análisis de síntomas comunes rápidamente
- Diccionario acceso O(1) a historia clínica completa
- Recursión identifica patrones en diagnósticos

### Complejidad esperada
| Función | Complejidad |
|---------|-------------|
| Buscar paciente | O(1) |
| Cola espera | O(1) agregar/O(n) procesar |
| Diagnóstico sugerido | O(n log n) |
| Síntomas comunes | O(n) |

---

## 🛒 OPCIÓN 4: PLATAFORMA DE E-COMMERCE CON CARRITO INTELIGENTE
**Dificultad:** ⭐⭐⭐ (Media) | **Potencial de presentación:** Muy Alto

### Descripción
Tienda virtual con catálogo dinámico, carrito de compras, recomendaciones y análisis de tendencias.

### Estructuras de datos
- **Lista Ligada:** Historial de compras del usuario (orden temporal)
- **Conjuntos:** Categorías, productos favoritos, productos en tendencia, items del carrito
- **Diccionario:** Catálogo {SKU: {nombre, precio, stock, categoría, rating}}
- **Recursión:** Búsqueda de productos similares, cálculo de descuentos en cascada

### Módulos
1. `GestorCatalogo` - Productos, búsqueda, filtros
2. `CarritoCompras` - Agregar/quitar, carrito persistente
3. `SistemaRecomendaciones` - "También te puede interesar"
4. `AnalizadorTendencias` - Top vendidos, predicciones

### Ventajas en presentación
- Diccionario permite búsqueda O(1) de productos
- Conjuntos evitan duplicados en favoritos
- Lista ligada mantiene historial sin copias innecesarias
- Recursión sugiere productos relacionados automáticamente

### Complejidad esperada
| Función | Complejidad |
|---------|-------------|
| Buscar producto | O(1) |
| Recomendaciones | O(n log n) |
| Historial | O(n) |
| Carrito (actualizar) | O(1) |

---

## 🍔 OPCIÓN 5: SISTEMA DE ENTREGAS Y LOGÍSTICA (DELIVERY)
**Dificultad:** ⭐⭐⭐⭐⭐ (Alta) | **Potencial de presentación:** Muy Alto

### Descripción
App tipo Rappi/Uber Eats que gestiona órdenes, repartidores, restaurantes y rutas optimizadas.

### Estructuras de datos
- **Lista Ligada:** Cola de órdenes por repartidor (FIFO con prioridad)
- **Conjuntos:** Restaurantes activos, órdenes completadas, clientes frecuentes
- **Diccionario:** Órdenes {ID: {cliente, restaurante, items, estado, repartidor}}, Repartidores {ID: {nombre, ubicación, órdenes}}
- **Recursión:** Cálculo de ruta óptima, búsqueda de repartidor disponible más cercano

### Módulos
1. `GestorOrdenes` - Crear, rastrear, completar órdenes
2. `GestorRepartidores` - Asignación inteligente de entregas
3. `GestorRestaurantes` - Disponibilidad, tiempo de preparación
4. `OptimizadorRutas` - Encontrar ruta más eficiente (recursivo)

### Ventajas en presentación
- Conjuntos aceleran búsqueda de repartidores disponibles
- Diccionarios permiten O(1) acceso a estado de órdenes
- Lista ligada mantiene cola de entregas ordenada por prioridad
- Recursión optimiza rutas sin explorar todas las combinaciones

### Complejidad esperada
| Función | Complejidad |
|---------|-------------|
| Crear orden | O(1) |
| Asignar repartidor | O(n) |
| Rastrear orden | O(1) |
| Ruta óptima | O(2^n) - reducida con recursión inteligente |

---

## 🎬 RECOMENDACIÓN PERSONAL

### Para máxima nota + presentación impactante:
**OPCIÓN 2 (Ranking de Videojuegos)** ← Favorita
- Tema atractivo y relatable
- Todas las estructuras naturales en el contexto
- Fácil mostrar ventajas reales
- Casos de uso claros para la presentación

### Para máxima complejidad técnica:
**OPCIÓN 5 (Sistema de Entregas)** ← Desafiante
- Problema del mundo real
- Optimización genuina
- Análisis de complejidad profundo

### Para equilibrio ideal:
**OPCIÓN 3 (Hospital)** ← Versátil
- Tema serio y profesional
- Justificación clara de estructuras
- Impacto social en presentación

---

## 📋 CHECKLIST PARA SUSTENTACIÓN

```
[ ] 1. Problema claramente identificado
[ ] 2. Por qué cada estructura de datos es necesaria
[ ] 3. Alternativa sin esa estructura (mostrar desventajas)
[ ] 4. Complejidad Big-O documentada
[ ] 5. Demo en vivo o video de funcionamiento
[ ] 6. Métricas de rendimiento (tiempo, memoria)
[ ] 7. Escalabilidad: ¿Qué pasa con 1M registros?
[ ] 8. Casos de uso concretos
[ ] 9. Código modular y documentado
[ ] 10. Presentación con gráficos/diagramas (no screenshots de código)
```

---

## 💡 TIPS PRESENTACIÓN (10-15 MIN)

**Estructura sugerida:**
1. **Intro (1 min):** El problema que resuelven
2. **Arquitectura (2 min):** Diagrama de módulos + estructura de datos
3. **Ventajas (5 min):** Comparación antes/después por módulo
4. **Demo (3-4 min):** Casos de uso en acción
5. **Complejidad (2 min):** Gráfico comparativo Big-O
6. **Preguntas (1 min):** Abiertas

**NO HACER:**
- ❌ Mostrar código en la presentación
- ❌ Hablar de detalles de implementación
- ❌ Leer diapositivas

**SÍ HACER:**
- ✅ Gráficos y diagramas
- ✅ Casos reales del problema
- ✅ Comparaciones de rendimiento
- ✅ Ejemplos visuales

---

## 📁 ESTRUCTURA DE CARPETAS SUGERIDA

```
proyecto_final/
├── main.py                 (punto de entrada)
├── modulos/
│   ├── gestor_principal.py
│   ├── estructura_datos.py
│   └── utilidades.py
├── tests/
│   └── pruebas_complejidad.py
├── presentacion/
│   ├── PRESENTACION.pptx
│   └── graficos_complejidad.png
└── README.md               (explicación arquitectura)
```

---

¿Cuál opción te atrae más? Te puedo generar el código base + estructura completa para empezar.
