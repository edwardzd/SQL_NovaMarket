-- ═══════════════════════════════════════════════════════════════════
-- RETO FINAL SQL — CONSEJO DE ANALISTAS NOVAMARKET
-- Archivo: S01_Preparacion_y_Limpieza.sql
-- Objetivo: Importar datos sucios, limpiarlos y calcular la utilidad.
-- ═══════════════════════════════════════════════════════════════════

-- ╔══════════════════════════════════════════════════════════════════╗
-- ║  INSTRUCCIONES DE IMPORTACIÓN INICIAL (En la terminal SQLite)  ║
-- ║  1. sqlite3 Reto_NovaMarket.db                                 ║
-- ║  2. .mode csv                                                  ║
-- ║  3. .import S03_Ventas_Datos_Sucios_v4.csv Ventas_Sucias       ║
-- ║  4. Luego, ejecuta este script completo.                       ║
-- ╚══════════════════════════════════════════════════════════════════╝

-- ── FASE I: AJUSTES POST-IMPORTACIÓN ───────────────────────────────
-- Eliminamos la primera fila si el import arrastró los títulos del CSV
DELETE FROM Ventas_Sucias WHERE TransaccionID = 'TransaccionID';

-- ── FASE II: LIMPIEZA DE DATOS (DML) ───────────────────────────────

-- 1. ELIMINAR DUPLICADOS
-- Mantenemos solo la primera aparición (MIN(ROWID)) y borramos el resto
DELETE FROM Ventas_Sucias
WHERE ROWID NOT IN (
    SELECT MIN(ROWID) 
    FROM Ventas_Sucias 
    GROUP BY TransaccionID, Fecha, Producto, Categoria, Precio_Unitario, Costo_Unitario, Ciudad, Region, Cantidad, Descuento_pct, Costo_Envio
);

-- 2. ESTANDARIZAR TEXTOS
-- Recortar espacios invisibles al inicio y final
UPDATE Ventas_Sucias SET Ciudad = TRIM(Ciudad), Categoria = TRIM(Categoria);

-- Corregir errores ortográficos en Ciudades
UPDATE Ventas_Sucias SET Ciudad = 'Bogotá' WHERE Ciudad LIKE 'bogot%' OR Ciudad = 'BOGOTÁ';
UPDATE Ventas_Sucias SET Ciudad = 'Cartagena' WHERE Ciudad = 'Cartajena';

-- Corregir errores ortográficos en Categorías
UPDATE Ventas_Sucias SET Categoria = 'Wearables' WHERE Categoria = 'Wereables';
UPDATE Ventas_Sucias SET Categoria = 'Laptops' WHERE Categoria = 'laptops';

-- 3. IMPUTACIÓN DE NULOS
-- Rellenamos las cantidades vacías usando la mediana estadística de cada categoría
UPDATE Ventas_Sucias SET Cantidad = 3 WHERE (Cantidad IS NULL OR Cantidad = '') AND Categoria = 'Audio';
UPDATE Ventas_Sucias SET Cantidad = 3 WHERE (Cantidad IS NULL OR Cantidad = '') AND Categoria = 'Wearables';
UPDATE Ventas_Sucias SET Cantidad = 2 WHERE (Cantidad IS NULL OR Cantidad = '') AND Categoria = 'Laptops';
UPDATE Ventas_Sucias SET Cantidad = 2 WHERE (Cantidad IS NULL OR Cantidad = '') AND Categoria = 'Smartphones';

-- ── FASE III: EL NÚMERO DE ORO (Leticia) ───────────────────────────
-- Calculamos toda la matemática financiera en tiempo de ejecución (al vuelo)

SELECT 
    'RESULTADO_LETICIA' AS Analisis,
    Ciudad,
    -- Ingreso = Precio * Cantidad * (100% - Porcentaje de Descuento)
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct)), 2) AS Ingreso_Total,
    
    -- Costo = (Costo Unitario * Cantidad) + Costo Fijo de Envío
    ROUND(SUM((Costo_Unitario * Cantidad) + Costo_Envio), 2) AS Costo_Total,
    
    -- Utilidad Neta = Lo que entró (Ingreso) - Lo que salió (Costo)
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)), 2) AS Utilidad_Neta,
    
    -- Margen % = Utilidad / Ingreso
    ROUND(
        SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)) / 
        SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct)) * 100, 1
    ) AS Margen_Pct
FROM Ventas_Sucias
WHERE Ciudad = 'Leticia';
-- RESULTADO ESPERADO: Utilidad Neta = -79342 | Margen Pct = -50.4

-- ── FASE IV: RANKING GLOBAL (Para la Junta Directiva) ──────────────
SELECT 
    Ciudad, 
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)), 2) AS Utilidad_Neta
FROM Ventas_Sucias
GROUP BY Ciudad
ORDER BY Utilidad_Neta DESC;
