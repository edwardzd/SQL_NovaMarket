-- ═══════════════════════════════════════════════════════════════
-- NOVAMARKET TECH — SESIÓN 7: EL INTERROGATORIO (SOLUCIONES)
-- ═══════════════════════════════════════════════════════════════
-- Estas consultas corresponden exactamente a los ejercicios del 
-- laboratorio '06_Laboratorio_Consultas.sql' y la guía.
-- ═══════════════════════════════════════════════════════════════
-- ══ BLOQUE A — Exploración Inicial ═════════════════════════════
-- A1: Ver las primeras 10 transacciones de 'FactVentas'.
SELECT *
FROM FactVentas
LIMIT 10;
-- A2: Contar el total de registros en 'FactVentas'.
-- Éxito: 500 filas.
SELECT COUNT(*) AS Total_Registros
FROM FactVentas;
-- A3: Ver el diccionario de productos en 'DimProducto'.
SELECT *
FROM DimProducto;
-- ══ BLOQUE B — Columnas y Cálculos ═════════════════════════════
-- B1: Mostrar TransaccionID, FechaID, Cantidad y Precio_Venta de 'FactVentas'.
SELECT TransaccionID,
  FechaID,
  Cantidad,
  Precio_Venta
FROM FactVentas;
-- B2: Calcular Venta_Bruta y Venta_Neta (redondeada a 2 decimales).
SELECT TransaccionID,
  Cantidad,
  Precio_Venta,
  (Cantidad * Precio_Venta) AS Venta_Bruta,
  ROUND(Precio_Venta * Cantidad * (1 - Descuento_Pct), 2) AS Venta_Neta
FROM FactVentas;
-- ══ BLOQUE C — Filtros WHERE (La Precisión) ═════════════════════
-- C1: Ventas realizadas en Leticia (CiudadID = 6).
-- Éxito: 76 filas.
SELECT *
FROM FactVentas
WHERE CiudadID = 6;
-- C2: Ventas con descuento superior al 15% (Descuento_Pct > 0.15).
-- Éxito: 46 filas.
SELECT *
FROM FactVentas
WHERE Descuento_Pct > 0.15;
-- C3: Ventas de Leticia CON descuento.
-- Éxito: 38 filas.
SELECT *
FROM FactVentas
WHERE CiudadID = 6
  AND Descuento_Pct > 0;
-- C4: Ventas en ciudades del Caribe (Barranquilla=4, Cartagena=5).
-- Éxito: 154 filas.
SELECT *
FROM FactVentas
WHERE CiudadID IN (4, 5);
-- C5: Ventas realizadas en Noviembre de 2023.
-- Éxito: 155 filas.
SELECT *
FROM FactVentas
WHERE FechaID BETWEEN 20231101 AND 20231130;
-- C6: Buscar categorías que empiecen por 'S' en 'DimProducto'.
-- Éxito: 2 filas.
SELECT *
FROM DimProducto
WHERE Categoria LIKE 'S%';
-- C7: ¿Hay fechas sin nombre de mes en 'DimFecha'?
-- Éxito: 0 filas.
SELECT *
FROM DimFecha
WHERE NombreMes IS NULL;
-- ══ BLOQUE D — Orden y Límites ═════════════════════════════════
-- D1: Las 10 transacciones con mayor Costo_Envio (Ordenar DESC).
SELECT *
FROM FactVentas
ORDER BY Costo_Envio DESC
LIMIT 10;
-- D2: Las 10 ventas con peor margen (Venta_Neta - Costo_Unitario*Cantidad - Costo_Envio).
SELECT TransaccionID,
  ROUND(
    Precio_Venta * Cantidad * (1 - Descuento_Pct) - Costo_Unitario * Cantidad - Costo_Envio,
    2
  ) AS Margen_Aproximado
FROM FactVentas
ORDER BY Margen_Aproximado ASC
LIMIT 10;
-- D3: Las 5 ventas de Leticia con mayor costo de envío.
SELECT *
FROM FactVentas
WHERE CiudadID = 6
ORDER BY Costo_Envio DESC
LIMIT 5;
-- ══ BLOQUE E — Desafíos Autónomos (ENTREGABLES) ════════════════
-- E1: (Fácil) ¿Cuántas ventas hubo en Septiembre de 2023?
-- Éxito: 153 filas.
SELECT *
FROM FactVentas
WHERE FechaID BETWEEN 20230901 AND 20230930;
-- E2: (Medio) Muestra las 10 transacciones con mayor Descuento_Pct que NO sean de Leticia.
SELECT TransaccionID,
  CiudadID,
  Descuento_Pct
FROM FactVentas
WHERE CiudadID <> 6
ORDER BY Descuento_Pct DESC
LIMIT 10;
-- E3: (Difícil) ¿Cuántas ventas de Noviembre tuvieron descuento > 20% Y envío > 500?
-- Éxito: 6 filas.
SELECT *
FROM FactVentas
WHERE FechaID BETWEEN 20231101 AND 20231130
  AND Descuento_Pct > 0.20
  AND Costo_Envio > 500;
-- ═══════════════════════════════════════════════════════════════
-- Fin de Soluciones Sesión 07