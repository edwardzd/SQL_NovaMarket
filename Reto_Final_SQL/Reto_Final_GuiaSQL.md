# 🏆 RETO FINAL — Guía Oficial SQL
**Consejo de Analistas NovaMarket | Énfasis II — Análisis de Datos**
**Docente:** Edward Zúñiga Dorado

Esta guía es tu "receta paso a paso" para lograr el objetivo del Reto Final utilizando **SQL puro (SQLite)**. Llegarás exactamente a las mismas conclusiones de negocio que los grupos de Python y Power BI, demostrando el poder del lenguaje universal de bases de datos.

---

## FASE I: Creación e Importación de Datos
El archivo `S01_Ventas_Novamarket_Datos_Sucios.csv` tiene 662 registros llenos de errores. Tu primer objetivo es importarlo a una base de datos y limpiarlo.

### Paso 1: Crear la Base de Datos y la Tabla
1. Abre VS Code o tu gestor de SQLite preferido.
2. Crea una nueva base de datos llamada `Reto_NovaMarket.db`.
3. Ejecuta este script para crear la tabla que recibirá los datos crudos:

```sql
-- CREATE TABLE: Crea la estructura "vacía" donde guardaremos los datos que vienen del Excel/CSV.
-- Definimos cada columna y qué tipo de dato guardará: 
-- TEXT (para letras), INTEGER (para números enteros), REAL (para decimales)
CREATE TABLE Ventas_Sucias (
    ID_Transaccion INTEGER,
    Fecha TEXT,
    Producto TEXT,
    Categoria TEXT,
    Ciudad TEXT,
    Cantidad INTEGER, -- Esta columna contiene nulos o casillas vacías
    Precio_Unitario REAL,
    Costo_Unitario REAL,
    Descuento_pct REAL,
    Costo_Envio REAL
);
```

### Paso 2: Importar el CSV
Usando la terminal de SQLite (o la extensión de VS Code), importa el archivo CSV que se te ha entregado:
```bash
# Entramos al motor de SQLite
sqlite3 Reto_NovaMarket.db

# Le decimos a SQLite que vamos a trabajar con archivos CSV
sqlite> .mode csv

# .import toma el archivo CSV y mete todos sus datos en la tabla que acabamos de crear
sqlite> .import S01_Ventas_Novamarket_Datos_Sucios.csv Ventas_Sucias
```

*(Asegúrate de borrar la primera fila si el import metió los títulos de las columnas como si fueran un dato real de venta):*
```sql
-- DELETE FROM borra filas. Aquí le decimos que borre la fila donde el ID_Transaccion sea la palabra literal 'ID_Transaccion'
DELETE FROM Ventas_Sucias WHERE ID_Transaccion = 'ID_Transaccion';
```

---

## FASE II: Limpieza de Datos (UPDATE y DELETE)
En SQLite no hay botones para "Reemplazar Valores"; todo se hace con código. Ejecuta estas sentencias para limpiar los datos paso a paso.

### Paso 1: Eliminar Duplicados
```sql
-- DELETE FROM: Borra registros de la tabla.
-- ROWID: Es un identificador oculto y único que SQLite le asigna a cada fila automáticamente.
-- NOT IN (SELECT MIN(ROWID)...): Esta lógica matemática conserva la primera aparición de un registro y elimina sus copias exactas.
DELETE FROM Ventas_Sucias
WHERE ROWID NOT IN (
    SELECT MIN(ROWID) 
    FROM Ventas_Sucias 
    GROUP BY ID_Transaccion, Fecha, Producto, Categoria, Precio_Unitario, Costo_Unitario, Ciudad, Cantidad, Descuento_pct, Costo_Envio
);
```
*(Al verificar con `SELECT COUNT(*) FROM Ventas_Sucias;`, debes obtener exactamente **650**).*

### Paso 2: Estandarizar Texto (Ciudades y Categorías)
```sql
-- UPDATE y SET: Actualizan la tabla cambiando valores existentes.
-- TRIM(): Es una función que recorta (elimina) los espacios vacíos accidentales al inicio o al final de un texto.
UPDATE Ventas_Sucias SET Ciudad = TRIM(Ciudad), Categoria = TRIM(Categoria);

-- WHERE: Especifica la condición. Aquí le decimos "cambia la ciudad a 'Bogotá' si empieza con 'bogot' (sin importar las mayúsculas)".
UPDATE Ventas_Sucias SET Ciudad = 'Bogotá' WHERE Ciudad LIKE 'bogot%' OR Ciudad = 'BOGOTÁ';

-- Corregimos el error ortográfico de Cartagena
UPDATE Ventas_Sucias SET Ciudad = 'Cartagena' WHERE Ciudad = 'Cartajena';

-- Corregimos los errores de las categorías aplicando la misma lógica de UPDATE y WHERE
UPDATE Ventas_Sucias SET Categoria = 'Wearables' WHERE Categoria = 'Wereables';
UPDATE Ventas_Sucias SET Categoria = 'Laptops' WHERE Categoria = 'laptops';
```

### Paso 3: Imputar Nulos
Asignaremos la mediana a las cantidades vacías (`NULL`) basándonos en la categoría:
```sql
-- IS NULL O = '': Le pregunta a la base de datos si la celda de cantidad está literalmente vacía.
-- Si está vacía y (AND) es un producto de Audio, la rellenamos con un 3.
UPDATE Ventas_Sucias SET Cantidad = 3 WHERE (Cantidad IS NULL OR Cantidad = '') AND Categoria = 'Audio';

-- Si está vacía y es un Wearable, también la rellenamos con 3 (su mediana estadística)
UPDATE Ventas_Sucias SET Cantidad = 3 WHERE (Cantidad IS NULL OR Cantidad = '') AND Categoria = 'Wearables';

-- Laptops y Smartphones tienen un comportamiento diferente, su mediana de ventas es 2.
UPDATE Ventas_Sucias SET Cantidad = 2 WHERE (Cantidad IS NULL OR Cantidad = '') AND Categoria = 'Laptops';
UPDATE Ventas_Sucias SET Cantidad = 2 WHERE (Cantidad IS NULL OR Cantidad = '') AND Categoria = 'Smartphones';
```

---

## FASE III: El "Número de Oro" (SELECT)
Ahora que los datos están limpios, calcularemos el dinero real del negocio al vuelo (en tiempo de consulta).

Ejecuta el siguiente `SELECT` para calcular la Utilidad Neta y el Margen % **específicamente para Leticia**:

```sql
-- SELECT: Extrae y muestra datos. Aquí usamos matemáticas directas sobre las columnas.
-- SUM(): Suma todos los valores de las filas para darnos el total.
-- ROUND(..., 2): Redondea el resultado final a 2 decimales para que parezca dinero real.
SELECT 
    Ciudad,
    -- FÓRMULA FINANCIERA: Ingreso = Precio * Cantidad * (100% - Porcentaje de Descuento)
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct)), 2) AS Ingreso_Total,
    
    -- FÓRMULA FINANCIERA: Costo = (Costo Unitario * Cantidad) + Costo Fijo de Envío
    ROUND(SUM((Costo_Unitario * Cantidad) + Costo_Envio), 2) AS Costo_Total,
    
    -- FÓRMULA FINANCIERA: Utilidad Neta = Lo que entró (Ingreso) - Lo que salió (Costo)
    ROUND(SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)), 2) AS Utilidad_Neta,
    
    -- MARGEN PORCENTUAL: Es la división de la Utilidad Neta sobre el Ingreso Total multiplicada por 100.
    ROUND(
        SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct) - ((Costo_Unitario * Cantidad) + Costo_Envio)) / 
        SUM(Precio_Unitario * Cantidad * (1 - Descuento_pct)) * 100, 1
    ) AS Margen_Pct
FROM Ventas_Sucias
-- FILTRO: Solo queremos que calcule esta matemática extrema para Leticia
WHERE Ciudad = 'Leticia';
```

**⚠️ PRUEBA DE ÁCIDO:** Si tu limpieza fue perfecta, la columna `Utilidad_Neta` dará **−79342** (aprox) y el `Margen_Pct` dará **−50.4**. Si da otro número, te faltó limpiar algún registro en la fase II.

---

## FASE IV: El "Dashboard Textual"
SQL no dibuja gráficos de barras o líneas como Power BI o Python, pero genera **Tablas Dinámicas** perfectas. El equivalente a un "Dashboard" en el mundo de las bases de datos es un script lleno de consultas agrupadas (`GROUP BY`).

En tu carpeta tienes un segundo archivo llamado **`Reto_Final_Respuestas_Junta.sql`**. Este archivo es tu Dashboard.

### ¿Cómo usar el Dashboard Textual?
Simplemente ejecuta las consultas que están dentro de ese archivo. Cada consulta escupirá una pequeña tabla en tu terminal que responde de manera fulminante a las preguntas del caso.

---

## FASE V: Respuestas a la Junta Directiva (Usando el Script)

Al ejecutar el script `Reto_Final_Respuestas_Junta.sql`, obtendrás evidencia irrefutable para argumentar:

| 🎯 Pregunta de la Junta | 💡 Respuesta Analítica usando tu "Dashboard Textual" |
| :--- | :--- |
| **"¿Por qué Leticia pierde dinero? ¿Es un problema de ventas o de costos?"** | *La primera consulta del script muestra que solo el costo de envío devora casi el **73%** del ingreso. Conclusión: No es un problema de ventas (la gente compra mucho), es un problema estructural logístico.* |
| **"Si cerramos Leticia, ¿cuánto mejora el margen?"** | *Las consultas del Escenario A vs Escenario B muestran que la utilidad total salta a ~$119,082. El negocio pasaría de estar casi estancado a ser altamente rentable.* |
| **"¿El Black Friday mejoró nuestras utilidades?"** | *La tercera consulta (que usa `CASE WHEN` para separar transacciones) revela que aunque el volumen de ingresos subió, las utilidades cayeron a números rojos (margen negativo) debido a descuentos agresivos de más del 40%.* |
| **"¿Qué información adicional necesitarían para decidir?"** | *"El costo fijo de mantener la operación en Leticia, los contratos logísticos actuales (para evitar multas por cierre temporal), y cotizaciones de nuevos aliados logísticos para la región."* |
