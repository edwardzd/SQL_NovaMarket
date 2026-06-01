-- 💻 SOLUCIONES PRIVADAS SESIÓN 8 Y 9 EXPRESS
-- ═══════════════════════════════════════════════════════════════
-- Estas son las soluciones a los entregables autónomos del archivo 03_Laboratorio_Consultas.sql
-- ═══════════════════════════════════════════════════════════════

-- E1: (Fácil) Muestra nombre del producto, categoría y venta neta total de cada producto. Ordena de mayor a menor.
SELECT
    p.Nombre AS Producto,
    p.Categoria,
    ROUND(SUM(f.Precio_Venta * f.Cantidad * (1-f.Descuento_Pct)), 2) AS Venta_Neta_Total
FROM FactVentas f
INNER JOIN DimProducto p ON f.ProductoID = p.ProductoID
GROUP BY p.Nombre, p.Categoria
ORDER BY Venta_Neta_Total DESC;


-- E2: (Medio) ¿Cuál producto vendió más en Leticia? Usa JOIN + WHERE + GROUP BY.
SELECT
    p.Nombre AS Producto,
    SUM(f.Cantidad) AS Unidades_Vendidas,
    ROUND(SUM(f.Precio_Venta * f.Cantidad * (1-f.Descuento_Pct)), 2) AS Venta_Neta_Total
FROM FactVentas f
INNER JOIN DimProducto p ON f.ProductoID = p.ProductoID
INNER JOIN DimCiudad c ON f.CiudadID = c.CiudadID
WHERE c.Nombre = 'Leticia'
GROUP BY p.Nombre
ORDER BY Venta_Neta_Total DESC;


-- E3: (Difícil) Reproduce la tabla del dashboard de S4 completa: Ciudad, Ventas, Utilidad, Margen%. Con nombres reales.
SELECT
    c.Nombre                                               AS Ciudad,
    COUNT(*)                                               AS Transacciones,
    ROUND(SUM(f.Precio_Venta * f.Cantidad * (1-f.Descuento_Pct)), 2) AS Venta_Neta,
    ROUND(SUM(
        f.Precio_Venta * f.Cantidad * (1-f.Descuento_Pct)
        - f.Costo_Unitario * f.Cantidad
        - f.Costo_Envio
    ), 2)                                                  AS Utilidad_Neta,
    ROUND(SUM(
        f.Precio_Venta * f.Cantidad * (1-f.Descuento_Pct)
        - f.Costo_Unitario * f.Cantidad
        - f.Costo_Envio
    ) / SUM(f.Precio_Venta * f.Cantidad * (1-f.Descuento_Pct)) * 100, 1) AS Margen_Pct
FROM FactVentas f
INNER JOIN DimCiudad c ON f.CiudadID = c.CiudadID
GROUP BY c.Nombre
ORDER BY Utilidad_Neta ASC;
