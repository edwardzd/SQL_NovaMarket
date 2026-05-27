# Informe de Estado: Estandarización de Datos NovaMarket (Pandas vs. SQL)

Este documento sirve como registro para retomar el trabajo en futuras sesiones, enfocado en la trazabilidad de los datos del proyecto NovaMarket y la integración pedagógica de la limpieza de datos en el curso de SQL.

---

## 1. El Set de Datos "Sucio" (Punto de Partida)
**Archivo:** `EXPLO_RA/S03_Ventas_Datos_Sucios_v4.xlsx`

Este es el dataset crudo y realista que simula una extracción deficiente de un sistema transaccional. Sus características principales (y errores intencionales) son:
- **Volumen:** 512 registros.
- **Duplicados:** Contiene 12 filas exactamente duplicadas.
- **Inconsistencia de Texto (Ciudades):** Variaciones de mayúsculas, minúsculas, espacios y errores ortográficos que generan 16 variantes en lugar de 5 (ej. `BOGOTÁ`, `Bogota `, `bogota`, `Barranqilla`).
- **Inconsistencia de Texto (Categorías):** Múltiples variantes para 4 categorías reales (ej. `LAPTOP`, `laptops`, `AUDIO`, `audio`).
- **Datos Faltantes:** Valores nulos en la columna `Cantidad`.

> [!NOTE]
> En la presentación de EXPLO-RA, este archivo es limpiado con éxito utilizando Python (Pandas) mediante métodos como `drop_duplicates()`, `.str.upper()`, `replace()` y `fillna(median)`.

---

## 2. El Set de Datos "Limpio" (Dataset Canónico)
**Archivo:** `NovaMarket_S01_Dataset_v2.csv`

Es el resultado final tras la limpieza. Es considerado el "Golden Record" o verdad absoluta del proyecto.
- **Volumen:** 500 registros exactos.
- **Datos unificados:** Solo existen 5 ciudades (Bogotá, Medellín, Cali, Barranquilla, Leticia) y 4 categorías (Laptops, Smartphones, Audio, Wearables).
- **Métrica de Validación (El Número de Oro):** Tras calcular ingresos y costos, la utilidad neta filtrada para **Leticia** debe dar exactamente **−$79,342** (con un margen de −50.4%). Este es el faro que indica que los datos están correctos.
- **Uso actual:** Alimenta directamente el Dashboard de Streamlit.

---

## 3. Estado Actual del Ecosistema SQL (Sesiones 7, 8 y 9)
Actualmente, las bases de datos SQLite (`Novamarket_S07.db` y `Novamarket_S08S09.db`) **no realizan ningún proceso de limpieza**. 

El archivo `S06_INSERT_FactVentas_Fixed.sql` actúa como un "atajo". Lo que hace es tomar los datos ya pulcros e inyectarlos directamente en las tablas `FactVentas` y `DimCiudad` mediante sentencias `INSERT INTO` masivas y estáticas. Esto garantiza que las matemáticas cuadren con el Dashboard, **pero le roba a los estudiantes la oportunidad de aprender a limpiar datos usando SQL**.

---

## 4. Oportunidad Pedagógica (Para la Próxima Iteración)
Tal como has notado, lo más lógico e instructivo para las **Sesiones 7, 8 y 9** sería replicar el reto de EXPLO-RA pero usando únicamente SQL (Data Engineering).

**Propuesta de implementación para el curso:**
1. **Carga en Staging:** Importar el archivo *sucio* (`v4.xlsx` o su equivalente CSV) en una tabla temporal o "raw" (ej. `stg_ventas_sucias`).
2. **Limpieza con SQL (Data Cleansing):** 
   - Enseñar `UPPER()`, `LOWER()`, y `TRIM()` para estandarizar textos.
   - Usar `REPLACE()` o sentencias `CASE WHEN` para mapear "Barranqilla" a "BARRANQUILLA".
   - Enseñar a remover duplicados agrupando datos (ej. `CTE` con `ROW_NUMBER()` o `GROUP BY`).
   - Usar `COALESCE()` o `IFNULL()` para imputar los vacíos en cantidades.
3. **Poblar el Modelo Estrella:** Usar `INSERT INTO FactVentas SELECT ... FROM stg_ventas_sucias` una vez los datos hayan sido transformados en la consulta.

> [!TIP]
> Dejar este puente construido permitirá que los estudiantes vean que **Python/Pandas y SQL son herramientas complementarias**, y que los mismos conceptos de calidad de datos se pueden resolver en ambos lenguajes.

---
*Este informe queda guardado como referencia para cuando decidas diseñar la refactorización de las guías y bases de datos de las Sesiones 7 a 9.*
