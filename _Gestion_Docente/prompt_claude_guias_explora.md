# Contexto y Prompt para Claude: Guías Oficiales Reto Explo-Ra

Copia y pega el siguiente texto en tu chat con Claude para que te genere las versiones actualizadas de las guías oficiales.

***

## [Copia desde aquí hacia abajo]

¡Hola Claude! Necesito que actúes como un Experto en Creación de Material Educativo Técnico y me ayudes a generar (o reescribir) las **Guías Oficiales del Reto Explo-Ra 2026** (Énfasis II - Análisis de Datos, Unicomfacauca). 

Tenemos tres rutas o "tracks" tecnológicos que los estudiantes pueden elegir: **Python**, **Power BI** y **SQL**. El objetivo de las tres guías es llevar a los estudiantes a realizar el mismo proceso (Limpieza de datos, Verificación Matemática y Análisis de Negocio) para responder exactamente a las mismas preguntas de la Junta Directiva de "NovaMarket".

### ⚠️ REGLA DE ORO PARA ESTA ACTUALIZACIÓN (DATASETS)
Actualmente tenemos los datos originales tanto en Excel (`.xlsx`) como en `.csv`. En versiones anteriores, el track de Python iniciaba importando el Excel. **A partir de ahora, es un requerimiento estricto que LOS TRES TRACKS (Python, Power BI y SQL) inicien importando el archivo CSV (`S01_Ventas_Novamarket_Datos_Sucios.csv`)**. Esto garantizará que todos arranquen en igualdad de condiciones con el mismo set de datos plano. 
*Nota:* Menciona que el Excel existe como respaldo original, pero el trabajo técnico debe hacerse sobre el CSV.

Por favor, genera una guía independiente para cada track (3 guías en total) asegurándote de incluir la siguiente información de configuración técnica y validación de negocio para cada caso:

---

### 1. Guía de Python (Data Science & Streamlit)
**Configuración y Pasos:**
* **Entorno:** Usaremos VS Code y la extensión de Jupyter para ejecutar el archivo `.ipynb`.
* **Librerías a instalar:** Se debe correr en la terminal `pip install plotly streamlit pandas openpyxl` (pandas leerá el CSV). Menciona que el motor `ipykernel` debe estar instalado al correr la primera celda.
* **Fase de Limpieza (Pandas):** 
    * Cargar el CSV `S01_Ventas_Novamarket_Datos_Sucios.csv`.
    * Eliminar duplicados (de 662 a 650 registros).
    * Estandarizar ciudades (ej. "bogota", "BOGOTÁ" a "Bogotá") y categorías.
    * Imputar nulos en la columna `Cantidad` usando la mediana de cada categoría.
* **El "Número de Oro" (Verificación):** Al filtrar por la ciudad de **Leticia**, los cálculos financieros deben dar exactamente una Utilidad Neta de **−$79,342** y un Margen de **−50.4%**.
* **Dashboard Completo:** En el notebook se usa el comando mágico `%%writefile dashboard_novamarket.py` para autogenerar el código de Streamlit. Luego se debe levantar desde la terminal con `streamlit run dashboard_novamarket.py`. El dashboard debe incluir KPIs, Heatmap, Gráfico de Cascada de Costos (para explicar Leticia), Boxplot (para anomalías) y Serie de Tiempo diaria.

---

### 2. Guía de Power BI (Data Analytics)
**Configuración y Pasos:**
* **Entorno:** Microsoft Power BI Desktop.
* **Carga de Datos:** Obtener datos -> Texto/CSV (Cargar el archivo `S01_Ventas_Novamarket_Datos_Sucios.csv`). MUY IMPORTANTE: Hacer clic en "Transformar datos" para abrir Power Query.
* **Fase de Limpieza (Power Query):**
    * Quitar duplicados (de 662 a 650 registros).
    * Estandarizar valores (Reemplazar valores en Ciudades y Categorías).
    * Imputar nulos: Crear "Columna condicional" para la cantidad basada en la mediana de cada categoría.
* **Fase DAX y Verificación:** Crear columnas calculadas de `Ingreso_Total`, `Costo_Total`, `Utilidad_Neta`, y la medida (measure) de `Margen %`.
* **El "Número de Oro":** Al poner una tarjeta y filtrar por **Leticia**, debe dar exactamente Utilidad Neta **−$79,342** y Margen **−50.4%**.
* **Dashboard Visual:** Armar un lienzo interactivo idéntico al de Python: Tarjetas (KPIs), Gráfico de Cascada de Costos, Boxplot (Distribución Mensual), Serie de Tiempo Diaria y Matriz/Heatmap.

---

### 3. Guía de SQL (Data Engineering / SQLite)
**Configuración y Pasos:**
* **Entorno:** Terminal de SQLite o VS Code con extensión de SQLite.
* **Carga de Datos:** Crear la DB `Reto_NovaMarket.db`, crear la tabla `Ventas_Sucias` (con los tipos de datos correctos), usar `.mode csv` y `.import S01_Ventas_Novamarket_Datos_Sucios.csv Ventas_Sucias`. Borrar la fila de encabezados si se importó como texto.
* **Fase de Limpieza (SQL puro):**
    * Eliminar duplicados usando `DELETE FROM ... WHERE ROWID NOT IN (SELECT MIN(ROWID)...)`.
    * Estandarizar texto usando `UPDATE ... SET` con `TRIM()`, `LIKE`, y `=`.
    * Imputar nulos en `Cantidad` usando `UPDATE` condicional (ej. `WHERE Cantidad IS NULL AND Categoria = 'Audio'`).
* **El "Número de Oro" (SELECT):** Hacer una consulta que calcule el Ingreso, Costo, Utilidad y Margen, filtrando `WHERE Ciudad = 'Leticia'`. Debe dar Utilidad Neta **−79342** y Margen Pct **−50.4**.
* **Dashboard Textual:** Utilizar el archivo de script `Reto_Final_Respuestas_Junta.sql` que, al ejecutarse, escupe en consola los "Escenarios" listos para responder las preguntas.

---

### 4. Preguntas de la Junta Directiva (Deben estar idénticas al final de LAS TRES GUÍAS)
La validación de negocio final es que, sin importar la herramienta técnica, las respuestas analíticas son las mismas:

1. **"¿Por qué Leticia pierde dinero? ¿Es un problema de ventas o de costos?"**
   *Respuesta esperada:* No es problema de ventas. El costo fijo de envío ($1,650 por transacción) representa ~73% del ingreso bruto, llevando la rentabilidad a terreno negativo (evidente en la Cascada de Costos). Es un problema estructural logístico.
2. **"Si cerramos Leticia, ¿cuánto mejora el margen?"**
   *Respuesta esperada:* La utilidad global de la empresa salta de ~$39,740 a ~$119,082 (un incremento abismal). El negocio pasaría de estar casi estancado a ser altamente rentable.
3. **"¿El Black Friday mejoró nuestras utilidades?"**
   *Respuesta esperada:* No. Subió el volumen de ventas, pero los descuentos agresivos (hasta 60%) comprimieron los márgenes. Los *outliers* del Boxplot y el pico rojo en la Serie de Tiempo Diaria (24 de Noviembre) demuestran que fue una anomalía de volumen, pero financieramente destructiva.
4. **"¿Qué información adicional necesitarían para decidir si cerrar Leticia?"**
   *Respuesta esperada:* Costo fijo de la operación actual en Leticia, posibles multas por cancelación de contratos actuales, datos de competencia, y cotizaciones de nuevos proveedores logísticos para esa región.

Con este contexto actualizado, por favor, redáctame de manera muy clara, profesional y con formato Markdown atractivo, las 3 guías completas para entregarles a los estudiantes de Unicomfacauca.
