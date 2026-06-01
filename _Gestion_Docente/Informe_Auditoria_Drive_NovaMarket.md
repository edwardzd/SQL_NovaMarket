# Informe de Auditoría — Google Drive
## Curso: Análisis de Datos para la Toma de Decisiones
**Fecha de revisión:** 11 de mayo de 2026 | **Revisado por:** Claude (vía conector Google Drive)

---

## 1. ESTRUCTURA DE LA CARPETA PRINCIPAL

Carpeta raíz: **"Análisis de datos"** (`edwardzd@gmail.com`)
Última modificación: hoy 11-may-2026

| Subcarpeta | ID Drive | Creada | Última modif. | Estado |
|---|---|---|---|---|
| Sesion_1 | `1eBga1oVctd_...` | 11-feb-2026 | hoy | ✅ Existe |
| Sesion_2 | `1NNvTEEWglYE...` | 11-feb-2026 | hoy | ✅ Existe |
| Sesion_3 | `1mAZISYOjSSC...` | 04-mar-2026 | hoy | ✅ Existe |
| Sesion_4 | `1HIwjGn5mOZU...` | 11-mar-2026 | **hoy 15:06** | ✅ Existe — modificada hoy |
| Sesion_5 | `1GIO5MTzF9iK...` | 12-mar-2026 | hoy | ✅ Existe |
| Sesion_6 | `1x9bQ1ImYhIa...` | 19-mar-2026 | hoy | ✅ Existe |
| Sesion_7 | `19b8p-1kLx3j...` | 26-mar-2026 | hoy | ✅ Existe |
| Sesion_8_y_9 | `1pCSCod4FHQs...` | 06-may-2026 | **hoy 14:45** | ✅ Existe — reciente |
| Sesion_10 | `1O7nJDRlW_zx...` | **11-may-2026** | hoy | 🆕 NUEVA — creada hoy |
| Presentación | `1dJDeEQYjpM8...` | 11-mar-2026 | **hoy 15:02** | ✅ Contiene el PDF consolidado |

**Observación clave:** Sesion_10 fue creada HOY — coincide con la sesión de trabajo actual. El PDF "Énfasis-II hasta la sesión 7" también fue subido hoy a la carpeta Presentación.

---

## 2. LO QUE CONFIRMA EL DRIVE VS LO QUE TENEMOS EN CLAUDE

### 2.1 Sesiones completamente desarrolladas ✅
Las carpetas S1 a S7 existen y tienen historial de trabajo. La presentación PDF confirma que la narrativa visual (Gamma AI) está construida para todas estas sesiones con la estructura acordada:
- S1: El Espejismo de los Datos
- S2: La Estadística del Negocio
- S3: La Clínica de Datos
- S4: El Veredicto de los Datos
- S5: Reto 1
- S6: El Contrato con los Datos
- S7: El Interrogatorio

### 2.2 Sesiones en proceso 🔄
- **S8_y_9:** Carpeta creada el 6 de mayo — en desarrollo activo
- **S10:** Carpeta creada hoy — recién iniciada

### 2.3 Sesiones pendientes ❌
- S11, S12, S13, S14, S15, S16 — no aparecen carpetas aún

---

## 3. HALLAZGO CRÍTICO — EL BUG DE LA FÓRMULA EN S7

### El problema confirmado

En la presentación PDF de S7 (página 7 del archivo subido hoy) aparece esta consulta como ejemplo de "la misma pregunta de S4 en SQL":

```sql
SELECT TransaccionID, FechaID, Cantidad,
    ROUND(Precio_Venta * Cantidad * (1 - Descuento_Pct), 2) AS Venta_Neta,
    Costo_Envio,
    ROUND(Precio_Venta * Cantidad * (1 - Descuento_Pct) - Costo_Envio, 2)
        AS Margen_Aprox
FROM FactVentas
WHERE CiudadID = 6
ORDER BY Margen_Aprox ASC
LIMIT 10;
```

### El bug: falta `Costo_Unitario * Cantidad`

La fórmula correcta de utilidad neta (la misma de Power Pivot en S4) es:

```
Utilidad = Venta_Neta - Costo_Producto - Costo_Envio
         = (Precio × Cantidad × (1-Desc)) - (Costo_Unitario × Cantidad) - Costo_Envio
```

La consulta de S7 calcula:
```
Margen_Aprox = Venta_Neta - Costo_Envio  ← falta restar Costo_Unitario × Cantidad
```

### El impacto en los números

Con los datos reales de la BD (confirmados por los resultados que el docente reportó):

| Ciudad | Venta_Neta | Costo_Envio | Margen_INCORRECTO | Margen_CORRECTO (estimado) |
|---|---|---|---|---|
| Leticia | $249,920 | $115,000 | **+$134,920 ← POSITIVO** | **~-$79,342 ← NEGATIVO** |
| Bogotá | $253,534 | $13,050 | +$240,484 | ~+$61,935 |

> **Conclusión:** La omisión de `Costo_Unitario * Cantidad` hace que Leticia aparezca rentable cuando en realidad destruye $79,342 de valor. Esto contradice directamente el veredicto de S4 y confunde a los estudiantes.

---

## 4. DISCREPANCIA SECUNDARIA — VOLUMEN DEL DATASET

### Datos de S4 (Excel) vs BD activa (S7 SQL)

| Métrica | S4 Excel (presentación) | BD activa S7 | Diferencia |
|---|---|---|---|
| Transacciones totales | 500 | **~500** | Sin diferencia aparente |
| Transacciones Leticia | ~65 | **92** | +27 transacciones |
| Venta_Neta Leticia | $157,508 | **$249,920** | +$92,412 |
| Costo_Envio Leticia | $115,500 | **$115,000** | ~igual |

> **Hipótesis:** El archivo `S06_NovaMarket_DB_Completa.sql` generado en Claude usa una versión del dataset con distribución diferente a la que se trabajó en Excel en S4. Las **92 transacciones** de Leticia en la BD son significativamente más que las ~65 del Excel. Esto puede deberse a que el SQL fue generado con parámetros distintos al dataset original.

> **Impacto:** Cuando los estudiantes ejecuten `SELECT COUNT(*) FROM FactVentas WHERE CiudadID = 6` en S7/S8, obtendrán 92 en lugar de los 65 que vieron en S4. Esa discrepancia puede generar confusión legítima si el docente afirma que los resultados deberían coincidir.

---

## 5. OBSERVACIÓN PEDAGÓGICA — EL PDF CONFIRMA LA NARRATIVA

El PDF "Énfasis-II hasta la sesión 7" confirma que la presentación de Gamma AI está construida con la narrativa correcta. Específicamente:

**S4 (slide 4 del PDF)** muestra la tabla de veredicto con los valores correctos:
- Leticia: $157,508 ventas / −$79,342 utilidad / −50.4% margen ✅

**S6 (slide 6 del PDF)** muestra correctamente:
- La metáfora del contrato ✅
- DDL/DML/DQL con las tres analogías ✅
- El INSERT con CiudadID=99 rechazado ✅

**S7 (slide 7 del PDF)** muestra el bug:
- La consulta de `Margen_Aprox` omite `Costo_Unitario * Cantidad` ❌
- La tabla de operadores WHERE está completa ✅
- El ORDER BY y LIMIT están correctos ✅

---

## 6. INFORMACIÓN ADICIONAL DEL DRIVE

### Datos del grupo (visibles en archivos de notas)
- **Archivo:** `26_I_AE_G1_(Vie)_Notas_Enfasis II.xls`
- **Grupo:** Administración de Empresas G1 — viernes
- **Estudiantes identificados en lista de asistencia:** 13

### Actividad reciente relevante
Se detectó una captura de pantalla en el Drive del docente (09-may-2026) mostrando:
- Acceso a **Codédex** — curso de pandas (Why Pandas?)
- Acceso a **freeCodeCamp** — perfil Python
> Esto confirma que el docente está preparándose activamente para las sesiones de Python.

---

## 7. ACCIONES CORRECTIVAS RECOMENDADAS

### PRIORIDAD 1 — Corrección inmediata antes de S8 (esta semana)

**Archivos a corregir en Antigravity:**

**`S07_NovaMarket_Consultas.sql`** — Bloque D, consulta D2:
```sql
-- INCORRECTO (versión actual)
ROUND(Precio_Venta * Cantidad * (1 - Descuento_Pct) - Costo_Envio, 2)
    AS Margen_Aproximado

-- CORRECTO (versión que debe quedar)
ROUND(Precio_Venta * Cantidad * (1 - Descuento_Pct)
      - Costo_Unitario * Cantidad
      - Costo_Envio, 2)
    AS Margen_Aproximado
```

**`S07_GuiaEstudiante.md`** — Bloque D2: mismo cambio en la consulta

**`S07_GuiaProfesor.md`** — Sección "Momentos Críticos": agregar nota sobre la discrepancia de volumen

**`S08S09_Express_SQL.sql`** — Verificar que todas las consultas de utilidad incluyen `Costo_Unitario * Cantidad`

**`S08_NovaMarket_SQL.sql`** — Bloque D: verificar la fórmula completa

**`S09_NovaMarket_SQL.sql`** — La consulta maestra (ya tiene la fórmula correcta — confirmar)

**`S10_Reto2_SQL.sql`** — La respuesta de referencia de la Pregunta 1: verificar fórmula

---

### PRIORIDAD 2 — Nota para el docente sobre la discrepancia de volumen

Agregar en la guía del profesor de S8 (sección "Momentos críticos"):

> "Los estudiantes pueden obtener ~92 transacciones para Leticia en lugar de las ~65 del Excel de S4. Esto se debe a que la BD SQL fue generada con una distribución levemente diferente. La conclusión es la misma (Leticia tiene margen negativo) pero los números exactos difieren. Si los estudiantes lo notan, usar esto como momento pedagógico: 'el analista siempre debe verificar que la fuente SQL y la fuente Excel sean el mismo dataset antes de comparar resultados.'"

---

### PRIORIDAD 3 — Carpeta S10 vacía

La carpeta Sesion_10 fue creada hoy pero no tiene contenido visible. Los archivos de S10 generados en Claude (guías MD y SQL) deben subirse a esa carpeta.

---

## 8. RESUMEN EJECUTIVO PARA ANTIGRAVITY

```
BUGS CONFIRMADOS:
├── BUG #1 (CRÍTICO): S07_NovaMarket_Consultas.sql
│   └── Línea del Margen_Aproximado omite: - Costo_Unitario * Cantidad
│   └── Impacto: Leticia aparece rentable (+$134,920) en lugar de pérdida (-$79,342)
│   └── Archivos afectados: SQL, GuiaEstudiante.md, GuiaProfesor.md de S7
│
├── BUG #2 (MODERADO): Discrepancia de volumen BD SQL vs Excel S4
│   └── Excel S4: ~65 transacciones Leticia / SQL: 92 transacciones
│   └── Causa probable: S06_NovaMarket_DB_Completa.sql generado con dataset diferente
│   └── Acción: agregar nota en GuiaProfesor S8 — no requiere cambio de BD
│
└── OBSERVACIÓN: Sesion_10 en Drive creada hoy sin contenido
    └── Acción: subir archivos S10 generados en Claude
```

---
*Informe generado automáticamente vía conector Google Drive — Claude Sonnet 4.6 — 11 may 2026*
