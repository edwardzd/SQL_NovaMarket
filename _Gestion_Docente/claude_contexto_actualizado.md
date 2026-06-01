# 🧠 Contexto Maestro de Sincronización: Reto EXPLO-RA 2026 (NovaMarket)

*Claude, por favor lee atentamente este documento. Resume todo el estado final de la arquitectura de datos, las narrativas de negocio y los archivos canónicos para el reto académico NovaMarket. A partir de ahora, cualquier código, guía o análisis que generes debe apegarse estrictamente a estos parámetros y no desviarse de ellos.*

---

## 1. Archivos Canónicos y Nomenclatura
Hemos estandarizado los nombres de los archivos en los tres tracks del curso (Python, Power BI, SQL) para evitar confusiones de los estudiantes:
- **Dataset Original Sucio:** `S01_Ventas_Novamarket_Datos_Sucios.csv` (Este es el único archivo que se le entrega a los estudiantes para arrancar).
- **Dataset Limpio (Exportado):** `S01_Ventas_Novamarket_Datos_Limpios.csv` (Este lo genera el código Python de los estudiantes tras hacer la limpieza y es el que alimenta al Dashboard).

## 2. Volumen y Forma de los Datos (El Diagnóstico Exacto)
Se hizo una inyección de registros en el backend para adaptar matemáticamente el dataset a la narrativa de la presentación (Black Friday). Aquí está la disección exacta de los datos que debes usar en tus guías:
- **Punto de Partida (Sucios):** `662` filas.
- **Paso 1 (Duplicados):** Hay exactamente `12` filas duplicadas completas. Se eliminan. (El dataset baja a `650` filas).
- **Paso 2 (Nulos):** Hay exactamente `6` registros con la columna `Cantidad` en nulo. **¡OJO! No se eliminan.** Se imputan matemáticamente usando la mediana de su categoría respectiva. (El dataset se mantiene en `650` filas).
- **Paso 3 (Ciudades mal escritas):** Hay 15 errores tipográficos a corregir. Distribución: Bogotá (BOGOTÁ, bogota, Bogota), Medellín (medellin), Cali (cali), Barranquilla (barranquilla, BARRANQUILLA, Barranqilla), Cartagena (cartagena, CARTAGENA). Leticia no tiene errores.
- **Paso 4 (Costo Unitario):** El archivo S01 SÍ trae la columna `Costo_Unitario` de fábrica. En Power BI, la fórmula DAX es directa (`Costo = Cantidad * Costo_Unitario`), NO se debe usar un factor de 0.65.
- **Registros Finales (Limpios):** `650` filas exactas para cargar al Dashboard.


## 3. Pruebas de Fuego Financieras (Los "Números de Oro")
Las decisiones de negocio dependen de que la limpieza de datos sea exacta. Si los estudiantes hacen bien la limpieza en cualquier plataforma, DEBEN llegar a estos números:
- **Utilidad Neta de Leticia:** `-$79,341.5` (Esta es la regla de oro. Si da -75k o cualquier otro valor, la limpieza quedó mal).
- **Margen de Leticia:** `-50.4%`
- **Utilidad Total de la Empresa (Global):** `~$39,740.50` (Margen global bajísimo).
- **Utilidad Total SIN Leticia:** `~$119,082` (Si se cerrara Leticia, la rentabilidad global se dispara).

## 4. La Narrativa del Black Friday
*Contexto de presentación (Gamma):* Los directivos se quejan de que a pesar de tener un volumen récord de ventas, la empresa casi no tiene utilidades.
- **Modificación realizada:** Se inyectaron 150 registros artificiales específicamente el 24 de noviembre con descuentos hiperagresivos (40%, 50%, 60%).
- **Conclusión que deben ver los alumnos:** Al graficar los datos limpios en el Dashboard, la barra de volumen/transacciones de Noviembre rompe todos los récords (superando a septiembre y octubre), pero es el mes que menos margen deja. El "Black Friday" trajo volumen, pero masacró los márgenes de ganancia.

## 5. Arquitectura del Dashboard (Streamlit)
- El dashboard interactivo no corre directamente sobre Jupyter. Se exporta desde una celda mágica `%%writefile dashboard_novamarket.py` (Asegúrate de que este comando mágico sea siempre la **Línea 1** de la celda).
- El dashboard DEBE hacer un `pd.read_csv('S01_Ventas_Novamarket_Datos_Limpios.csv')` al inicio de su ejecución, de lo contrario fallará por no encontrar el DataFrame.

---
**INSTRUCCIÓN PARA CLAUDE:**
A partir de este punto, mi entorno local está perfectamente sincronizado con esta narrativa. Si te pido crear nuevas guías, scripts en SQL o consultas en DAX para Power BI, usa siempre los nombres de archivo mencionados aquí y asegúrate de que cualquier query de validación que propongas de como resultado los Números de Oro indicados en el punto 3 y los 650 registros del punto 2. ¡Actúa como mi copiloto docente respetando esta base!
