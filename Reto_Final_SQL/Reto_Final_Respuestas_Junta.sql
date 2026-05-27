-- ═══════════════════════════════════════════════════════════════════
-- RETO FINAL SQL — CONSEJO DE ANALISTAS NOVAMARKET
-- Archivo: Reto_Final_Respuestas_Junta.sql
-- Objetivo: Responder a las preguntas de negocio mediante consultas SQL
-- ═══════════════════════════════════════════════════════════════════
-- NOTA: SQL no crea gráficos visuales (barras o líneas) nativamente. 
-- El "Dashboard" de un analista SQL son Tablas Dinámicas generadas 
-- mediante la instrucción GROUP BY. Cada consulta a continuación 
-- arrojará una tabla de resultados que responde exactamente a las dudas.

-- ───────────────────────────────────────────────────────────────────
-- PREGUNTA 1: "¿Por qué Leticia pierde dinero? ¿Es un problema de ventas o de costos?"
-- ───────────────────────────────────────────────────────────────────
SELECT 
    'Leticia' AS Analisis,
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct)), 2) AS Ingresos_Generados,
    ROUND(SUM(Costo_Envio), 2) AS Costo_Solo_Envio,
    ROUND((SUM(Costo_Envio) / SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct))) * 100, 1) AS Pct_Ingreso_Gastado_En_Envio
FROM Ventas_Sucias
WHERE Ciudad = 'Leticia';
-- CONCLUSIÓN ESPERADA: Al ejecutar esto, verán que el costo de envío devora casi el 73% de los ingresos. No es un problema de ventas (se vende bien), es logístico.

-- ───────────────────────────────────────────────────────────────────
-- PREGUNTA 2: "Si cerramos Leticia mañana, ¿cuánto mejora el margen total de la empresa?"
-- ───────────────────────────────────────────────────────────────────

-- Escenario A: Toda la empresa actual (Línea Base)
SELECT 
    'Empresa ACTUAL (Con Leticia)' AS Escenario,
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)), 2) AS Utilidad_Total,
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)) / SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct)) * 100, 1) AS Margen_Pct
FROM Ventas_Sucias;

-- Escenario B: Empresa simulada SIN Leticia (!= significa 'Diferente de')
SELECT 
    'Empresa SIMULADA (Sin Leticia)' AS Escenario,
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)), 2) AS Utilidad_Total,
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)) / SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct)) * 100, 1) AS Margen_Pct
FROM Ventas_Sucias
WHERE Ciudad != 'Leticia';
-- CONCLUSIÓN ESPERADA: El margen global de rentabilidad salta de ~10.4% a casi un 19.9%.

-- ───────────────────────────────────────────────────────────────────
-- PREGUNTA 3: "El Black Friday disparó las ventas — ¿también disparó las utilidades?"
-- ───────────────────────────────────────────────────────────────────
-- Simulamos el Dashboard agrupando por transacciones de alto descuento vs normales
SELECT 
    CASE WHEN Descuento_pct >= 0.40 THEN 'Black Friday (>= 40% dcto)' ELSE 'Días Normales (< 40% dcto)' END AS Tipo_Venta,
    COUNT(*) AS Numero_Transacciones,
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct)), 2) AS Volumen_Ingresos,
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)), 2) AS Utilidad_Neta,
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)) / SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct)) * 100, 1) AS Margen_Pct
FROM Ventas_Sucias
GROUP BY Tipo_Venta;
-- CONCLUSIÓN ESPERADA: Vendimos mucho en volumen durante BF, pero la utilidad neta cayó a números rojos por culpa de descuentos tan agresivos (Margen negativo).

-- ───────────────────────────────────────────────────────────────────
-- EXTRA: EL "DASHBOARD" EN TEXTO (Ranking de Rentabilidad)
-- ───────────────────────────────────────────────────────────────────
-- Esto es lo equivalente a tu gráfico de barras en Python/PowerBI
SELECT 
    Ciudad, 
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)), 2) AS Utilidad_Neta
FROM Ventas_Sucias
GROUP BY Ciudad
ORDER BY Utilidad_Neta DESC;
