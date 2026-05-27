# 🏆 RETO FINAL — Guía Oficial Power BI
**Consejo de Analistas NovaMarket | Énfasis II — Análisis de Datos**
**Docente:** Edward Zúñiga Dorado

Esta guía es tu "receta paso a paso" para lograr el objetivo del Reto Final utilizando **Microsoft Power BI**. Llegarás exactamente a las mismas conclusiones de negocio que el grupo de Python, porque la verdad de los datos es la misma sin importar la herramienta.

---

## FASE I: Extracción y Limpieza (Power Query)
El archivo `S01_Ventas_Novamarket_Datos_Sucios.xlsx` tiene 512 registros llenos de errores. Tu primer objetivo es limpiarlo hasta obtener exactamente 500 registros perfectos.

### Paso 1: Cargar los Datos
1. Abre Power BI Desktop.
2. Clic en **Obtener datos** -> **Libro de Excel**.
3. Selecciona el archivo `S01_Ventas_Novamarket_Datos_Sucios.xlsx`.
4. Selecciona la hoja `Ventas_Datos_Sucios`.
5. ⚠️ **MUY IMPORTANTE:** Haz clic en **Transformar datos** (NO en Cargar). Esto abrirá el editor de *Power Query*.

### Paso 2: Limpieza de la Tabla
En la ventana de Power Query, realiza los siguientes pasos exactos:
1. **Quitar las primeras filas vacías:** Clic en `Quitar filas` -> `Quitar filas superiores` -> Escribe `2`. Luego, clic en `Usar la primera fila como encabezado`.
2. **Eliminar Duplicados:** Selecciona todas las columnas (o haz clic en la esquina superior izquierda de la tabla) -> `Quitar filas` -> `Quitar duplicados`. *Pasarás de 512 filas a 500.*
3. **Estandarizar Ciudades:** Haz clic derecho sobre el encabezado de la columna `Ciudad` -> `Reemplazar los valores`. Reemplaza "bogota" por "Bogotá", "BOGOTÁ" por "Bogotá", "Cartajena" por "Cartagena", etc., hasta que solo queden las 6 ciudades válidas.
4. **Estandarizar Categorías:** Haz lo mismo con la columna `Categoria` (ej. "laptops" por "Laptops", "Wereables" por "Wearables").
5. **Imputar Nulos en Cantidad:** La regla de negocio indica que si falta la cantidad, se debe usar la mediana de esa categoría.
   - Ve a `Agregar columna` -> `Columna condicional`.
   - Llámala `Cantidad_Limpia`.
   - Crea reglas como: Si `Cantidad` es `null` y `Categoria` es `Audio` -> Salida `3`. Si es `Laptops` -> `2`, `Smartphones` -> `2`, `Wearables` -> `3`.
   - Si ninguna se cumple, Salida -> Selecciona la columna original `Cantidad`.
   - Borra la columna `Cantidad` vieja y renombra la nueva a `Cantidad`.
   - Asegúrate de que el tipo de dato de esta nueva columna sea **Número entero**.

Haz clic en **Cerrar y aplicar** en la esquina superior izquierda de Power Query.

---

## FASE II: El "Número de Oro" (DAX)
Ahora que los datos están limpios en el modelo, calcularemos el dinero real del negocio.

### Paso 1: Crear las Columnas Financieras
En la vista de "Datos" (icono de tabla a la izquierda), haz clic en **Nueva Columna** para crear estas 3 fórmulas:

1. `Ingreso_Total = Ventas_Datos_Sucios[Cantidad] * Ventas_Datos_Sucios[Precio_Unitario] * (1 - Ventas_Datos_Sucios[Descuento_pct])`
2. `Costo_Total = (Ventas_Datos_Sucios[Cantidad] * Ventas_Datos_Sucios[Costo_Unitario]) + Ventas_Datos_Sucios[Costo_Envio]`
3. `Utilidad_Neta = Ventas_Datos_Sucios[Ingreso_Total] - Ventas_Datos_Sucios[Costo_Total]`

### Paso 2: Crear Medidas (Measures) para los KPIs
Haz clic en **Nueva Medida**:
`Margen % = SUM(Ventas_Datos_Sucios[Utilidad_Neta]) / SUM(Ventas_Datos_Sucios[Ingreso_Total])`
*(Selecciona la medida creada y aplícale el formato de Porcentaje % en la cinta de opciones superior).*

### Paso 3: Verificación del "Número de Oro"
Ve a la vista de "Informe" (el lienzo en blanco).
1. Inserta un visual de **Tarjeta (Card)** y pon ahí la `Utilidad_Neta`.
2. Inserta una **Segmentación de datos (Slicer)** con la `Ciudad`.
3. Selecciona **Leticia** en el filtro.
4. Si la tarjeta muestra **−$79,342** (o -$79k) y el Margen % da **−50.4%**, ¡tu limpieza fue perfecta! Si da otro número, debes volver a revisar los pasos en Power Query.

---

## FASE III: Construcción del Dashboard Visual
Para impresionar a la Junta Directiva, tu lienzo debe tener al menos:

1. **Indicadores (KPIs):** Tarjetas en la parte superior mostrando Ventas Totales, Utilidad Neta y Margen Global.
2. **Utilidad por Ciudad:** Un gráfico de barras horizontales (Barras agrupadas). Pon `Ciudad` en el Eje Y, y `Utilidad_Neta` en el Eje X. *(Aplica formato condicional rojo/verde a los colores de los datos).*
3. **El Efecto Black Friday:** Un gráfico de "Líneas y columnas agrupadas".
   - Eje X: `Fecha` (resumido por Mes o Año/Mes).
   - Eje Y de columna: `Ingreso_Total` (Ventas).
   - Eje Y de línea: `Utilidad_Neta`.
4. **El Heatmap:** Usa el visual de **Matriz**. Filas: `Ciudad`, Columnas: `Categoria`, Valores: `Utilidad_Neta`. Aplica un formato condicional de color de fondo a los valores (Rojo para valores bajos, Verde para altos).

---

## FASE IV: Respuestas a la Junta Directiva (El As bajo la manga)

Usa tu Dashboard interactivo (haciendo clic en las barras y meses) para responder con seguridad:

| 🎯 Pregunta de la Junta | 💡 Respuesta Analítica Esperada (basada en Power BI) |
| :--- | :--- |
| **"¿Por qué Leticia pierde dinero? ¿Es un problema de ventas o de costos?"** | *"El costo de envío ($1,650 por transacción) representa ~73% del ingreso bruto. **No es un problema de ventas** —vende muy bien—. Es un problema estructural logístico."* |
| **"Si cerramos Leticia, ¿cuánto mejora el margen?"** | *(Filtra excluyendo Leticia en tu slicer)* *"La utilidad total pasa de ~$121,930 a ~$201,272 (un aumento del ~65%). El margen global mejora dramáticamente del 10.4% a casi un **19.9%**."* |
| **"¿El Black Friday mejoró nuestras utilidades?"** | *(Filtra noviembre en tu gráfico)* *"No. Subió el volumen de ventas, pero los descuentos agresivos (hasta 60%) comprimieron los márgenes hasta lo negativo. Vendimos más, pero perdimos rentabilidad."* |
| **"¿Qué información adicional necesitarían para decidir?"** | *"El costo fijo de mantener la operación en Leticia, los contratos logísticos actuales (para evitar multas por cierre temporal), y cotizaciones de nuevos aliados logísticos para la región."* |
