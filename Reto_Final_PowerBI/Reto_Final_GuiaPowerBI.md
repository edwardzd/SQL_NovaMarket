# 🏆 GUÍA TÉCNICA — Dashboard Analítico en Power BI
**Caso NovaMarket Tech: El Problema de Leticia y el Black Friday**

**Énfasis II - Análisis de Datos | EXPLO-RA 2026**
**Docente:** Edward Samir Zúñiga Dorado
**Quantum Analytics Group - Popayán, Cauca, Colombia**

**🌐 Enlace Oficial del Proyecto (Live):** [NovaMarket Explora en Power BI](https://app.powerbi.com/view?r=eyJrIjoiNTgzYTAyMmEtYzBmMi00ODVlLWI3ZDItYTE1NGZlYmVhMTM5IiwidCI6ImUzOGI2YjNiLWRkMTQtNDVhZi1hZjBhLWU2N2QxYjk2ODQyYSIsImMiOjR9)

---

## 1. Introducción y Contexto del Caso
Este documento es la guía técnica completa del Reto de Análisis de Datos construido durante el Corte 1 de Énfasis II. A lo largo de las sesiones, construimos un dashboard interactivo en Power BI que replica y supera el análisis realizado previamente en Python (Pandas/Streamlit), demostrando la paridad entre ambas herramientas.

### 1.1 El Caso de Negocio: NovaMarket Tech
NovaMarket Tech es una empresa colombiana de tecnología que opera en 6 ciudades: Bogotá, Medellín, Cali, Barranquilla, Cartagena y Leticia. El dataset cubre el periodo Sep-Nov 2023 con 650 transacciones limpias después del proceso de ETL.

### 1.2 Las Preguntas de Negocio
- ¿Por qué la ciudad de Leticia tiene una utilidad neta de -$79,342 a pesar de generar ingresos?
- ¿Por qué noviembre, el mes con más ventas, es el mes con peor margen?
- ¿Cuál es el impacto real del Black Friday en la rentabilidad de la empresa?
- ¿Qué pasaría si eliminamos categorías deficitarias en Leticia?
- ¿Cuál debería ser el descuento máximo permitido en el Black Friday?

---

## 2. ETL en Power Query: Limpieza de Datos
El proceso de ETL (Extract, Transform, Load) es la base de todo el análisis. Un error en esta capa invalida todos los resultados posteriores, sin importar cuán bien estén escritas las medidas DAX.

### 2.1 Problemas Encontrados en el Dataset Original
| Problema | Cantidad | Solución Aplicada |
| :--- | :--- | :--- |
| **Duplicados exactos** | 12 filas | `Table.Distinct()` por ID_Transaccion |
| **Variantes de ciudades** | 10 variantes -> 6 únicas | `Text.Trim` + reemplazos manuales |
| **Variantes de categorías**| 8 variantes -> 4 únicas | `Text.Proper` + LimpiezaCategoria |
| **Nulos en Cantidad** | 6 valores | Imputación por mediana por Categoría |
| **Decimales en Descuento_pct** | Mutilación por locale | `TransformColumnTypes` con 'en-US' |

### 2.2 El Error Crítico: Currency.Type sin Locale
El problema más importante del reto fue que Power BI, al estar configurado en español (Colombia), interpretaba el punto decimal del CSV como separador de miles. Esto causaba que `Descuento_pct = 0.40` fuera leído como `0.04`, destruyendo todos los cálculos financieros.

**La solución: forzar locale en-US**
```powerquery
// INCORRECTO - Currency.Type sin locale:
= Table.TransformColumnTypes(#"Duplicados quitados",
    {{"Descuento_pct", Currency.Type}})

// CORRECTO - type number con locale en-US:
= Table.TransformColumnTypes(#"Tipo cambiado",
    {{"Precio_Unitario", type number},
     {"Costo_Unitario", type number},
     {"Descuento_pct", type number},
     {"Costo_Envio", type number}}, "en-US")
```

### 2.3 Lección Clave: La Pirámide de Confianza en Datos
Si los datos entran mal al modelo, todo lo de arriba es incorrecto sin importar cuán bien escrito esté el DAX. El orden de confianza es:
1. **Nivel 1 - Datos fuente (CSV):** CORRECTO - los decimales estaban bien en el archivo.
2. **Nivel 2 - ETL Power Query:** ERROR - Currency.Type sin locale destruía los decimales.
3. **Nivel 3 - DAX (medidas):** CORRECTO - las fórmulas estaban bien escritas.
4. **Nivel 4 - Visualizaciones:** ERROR - mostraban números incorrectos por el ETL.

---

## 3. Medidas DAX: El Modelo de Negocio
DAX (Data Analysis Expressions) es el lenguaje de fórmulas de Power BI. La regla fundamental de este proyecto es que TODAS las métricas financieras deben calcularse fila por fila usando iteradores (`SUMX`), nunca con sumas simples (`SUM`).

### 3.1 ¿Por qué SUMX y no SUM?
Los descuentos y costos de envío se aplican a nivel de transacción individual. Si usamos `SUM`, primero sumamos y luego multiplicamos, obteniendo un resultado matemáticamente incorrecto.

### 3.2 Medidas Financieras Base

```dax
// Ingresos Netos (con descuento aplicado fila por fila)
Ingresos_Netos =
SUMX(
    S01_Ventas_Novamarket_Datos_Sucios,
    S01_Ventas_Novamarket_Datos_Sucios[Cantidad] *
    S01_Ventas_Novamarket_Datos_Sucios[Precio_Unitario] *
    (1 - S01_Ventas_Novamarket_Datos_Sucios[Descuento_pct])
)

// Costos Totales (producto + envío fila por fila)
Costos_Totales =
SUMX(
    S01_Ventas_Novamarket_Datos_Sucios,
    (S01_Ventas_Novamarket_Datos_Sucios[Cantidad] *
     S01_Ventas_Novamarket_Datos_Sucios[Costo_Unitario]) +
    S01_Ventas_Novamarket_Datos_Sucios[Costo_Envio]
)

// Utilidad Total
Utilidad_Total = [Ingresos_Netos] - [Costos_Totales]

// Margen Porcentaje
Margen_Porcentaje = DIVIDE([Utilidad_Total], [Ingresos_Netos], 0)
```

### 3.3 Checkpoints de Paridad con Python
Para verificar que el modelo DAX es correcto, los siguientes valores deben coincidir exactamente con los calculados en Python:

| Checkpoint | Python | Power BI | Estado |
| :--- | :--- | :--- | :--- |
| **Utilidad Global** | $39,740 | $39,740.50 | ✅ CORRECTO |
| **Leticia Utilidad** | -$79,342 | -$79,341.50 | ✅ CORRECTO |
| **Leticia Margen** | -50.4% | -50.4% | ✅ CORRECTO |
| **Barranquilla** | $14,434 | $14,434.50 | ✅ CORRECTO |
| **Total filas** | 650 | 650 | ✅ CORRECTO |
*Nota: Las diferencias de $0.50 son normales - Python trunca enteros con `astype(int)` mientras Power BI redondea en la imputación de medianas.*

---

## 4. Construcción de Visualizaciones

### 4.1 Gráfico de Cascada (Waterfall) - El Caso Leticia
**Objetivo Pedagógico:** Mostrar cómo el ingreso bruto de Leticia es destruido por los descuentos y costos logísticos, resultando en una pérdida neta de -$79,342.

**Tabla Auxiliar Requerida:** `TablaWaterfall` (Concepto, Orden)
| Concepto | Orden |
| :--- | :--- |
| Ingreso Bruto | 1 |
| Descuentos | 2 |
| Costo Producto | 3 |
| Costo Envio | 4 |
| Utilidad Neta | 5 |

**Medida DAX: WaterFall_Leticia**
```dax
WaterFall_Leticia =
VAR Concepto = SELECTEDVALUE(TablaWaterfall[Concepto])
RETURN
SWITCH(
    Concepto,
    "Ingreso Bruto", [Ingreso_Bruto],
    "Descuentos", [Impacto_Descuentos],
    "Costo Producto", [Impacto_Costo_Producto],
    "Costo Envio", [Impacto_Costo_Envio],
    "Utilidad Neta", [Utilidad_Total],
    BLANK()
)
```
**Concepto Clave:** Contexto de Filtro. La medida no tiene datos propios, actúa como enrutador según la categoría activa del visual.

### 4.2 Boxplot - Anomalías del Black Friday
**Objetivo Pedagógico:** Demostrar que noviembre no es un mes de crecimiento orgánico sino que está lleno de outliers atípicos por transacciones del Black Friday con descuentos extremos.

**Columna Calculada: Ingreso_Transaccion**
```dax
Ingreso_Transaccion =
S01_Ventas_Novamarket_Datos_Sucios[Cantidad] *
S01_Ventas_Novamarket_Datos_Sucios[Precio_Unitario] *
(1 - S01_Ventas_Novamarket_Datos_Sucios[Descuento_pct])
```
*¿Por qué columna calculada y no medida?* Porque los boxplots necesitan ver cada fila individual para calcular cuartiles.

### 4.3 Serie de Tiempo - Evolución de Ventas Diarias
**Objetivo Pedagógico:** Mostrar el pico dramático del 24 de noviembre (Black Friday) en la evolución de ventas diarias.

### 4.4 Heatmap - Utilidad por Ciudad x Categoría
**Objetivo Pedagógico:** Matriz donde Leticia resalta en rojo intenso, permitiendo identificar visualmente combinaciones deficitarias.
- *Filas:* Ciudad | *Columnas:* Categoría | *Valores:* Utilidad_Total
- *Formato Condicional:* Fondo degradado de Rojo a Verde (Blanco en el centro/cero).

### 4.5 Black Friday vs Periodo Normal
**Columna Calculada:**
```dax
Clasificacion_BF =
IF(
    S01_Ventas_Novamarket_Datos_Sucios[Descuento_pct] >= 0.40,
    ">= 40% (Black Friday)",
    "< 40% (Normal)"
)
```

---

## 5. Simulador de Escenarios Interactivo
Permite a la junta directiva explorar decisiones de negocio en tiempo real.

### 5.1 Escenario A: Optimizar Portafolio en Leticia
Simula cuál sería la utilidad total si se eliminan categorías específicas que generan pérdidas en Leticia. Cuando se deselecciona Wearables de Leticia (-$37,329), la utilidad proyectada sube de $39,740 a ~$77,069.

```dax
Utilidad_Proyectada_A =
VAR CategoriasExcluidas = VALUES(S01_Ventas_Novamarket_Datos_Sucios[Categoria])
VAR CiudadExcluida = VALUES(S01_Ventas_Novamarket_Datos_Sucios[Ciudad])
RETURN
CALCULATE(
    [Utilidad_Total],
    ALL(S01_Ventas_Novamarket_Datos_Sucios[Ciudad],
        S01_Ventas_Novamarket_Datos_Sucios[Categoria]),
    NOT(
        S01_Ventas_Novamarket_Datos_Sucios[Ciudad] IN CiudadExcluida &&
        S01_Ventas_Novamarket_Datos_Sucios[Categoria] IN CategoriasExcluidas
    )
)
```
**Explicación:** `ALL` elimina los filtros, y `NOT(IN ... && IN ...)` excluye solo la combinación seleccionada en los segmentadores del Escenario A. *Importante:* Se deben configurar las interacciones visuales (Editar Interacciones) para no contaminar el resto del informe.

### 5.2 Escenario B: Política de Descuentos Black Friday
Simula cuál habría sido la utilidad si se hubiera limitado el descuento máximo durante noviembre de 2023 usando un **Parámetro What-If** (`Descuento_Maximo_BF` de 0% a 50%).

```dax
Utilidad_Simulada_BF =
VAR DescuentoCap = [Valor de Descuento_Maximo_BF 2]
VAR IngresoSimulado =
    SUMX(
        S01_Ventas_Novamarket_Datos_Sucios,
        VAR DescuentoReal = S01_Ventas_Novamarket_Datos_Sucios[Descuento_pct]
        VAR FechaFila = S01_Ventas_Novamarket_Datos_Sucios[Fecha]
        VAR DescuentoAplicado =
            IF(
                MONTH(FechaFila) = 11 && YEAR(FechaFila) = 2023,
                MIN(DescuentoReal, DescuentoCap),
                DescuentoReal
            )
        RETURN
            S01_Ventas_Novamarket_Datos_Sucios[Cantidad] *
            S01_Ventas_Novamarket_Datos_Sucios[Precio_Unitario] *
            (1 - DescuentoAplicado)
    )
RETURN IngresoSimulado - [Costos_Totales]
```
**Resultados clave con el deslizador:** Si se limita el cap de descuento al **10%**, la utilidad simulada sube a **$202,940** (+$163,200).

---

## 6. Lecciones Pedagógicas Clave

### 6.1 Python vs Power BI: Equivalencias
| Concepto | Python (Pandas) | Power BI (DAX) |
| :--- | :--- | :--- |
| **Filtro condicional** | `df[df['col'] > 0]` | `CALCULATE` con filtro |
| **Columna nueva** | `df['nueva'] = df['a'] * df['b']` | Columna calculada con DAX |
| **Agrupamiento** | `df.groupby('ciudad').sum()` | Contexto de filtro automático del visual |
| **Lambda/apply** | `df.apply(lambda x: ...)` | `IF()` o `SWITCH()` en columna calculada |
| **Locale decimal** | `pd.read_csv(decimal='.')` | `TransformColumnTypes` con 'en-US' |

### 6.2 Reglas de Oro del Modelado
- **Regla 1 - ETL primero:** Si los datos entran mal, todo lo demás es incorrecto.
- **Regla 2 - SUMX siempre:** Para métricas financieras con descuentos y costos por transacción.
- **Regla 3 - Columna vs Medida:** Si el visual necesita ver cada fila, usa columna calculada.
- **Regla 4 - Locale en-US:** Siempre forzar para columnas financieras que vienen de CSV.
- **Regla 5 - Editar interacciones:** Para escenarios independientes que no deben contaminarse.
- **Regla 6 - Checkpoints:** Siempre validar contra un resultado conocido antes de seguir.

### 6.3 El Mensaje de Negocio
El dashboard responde las 5 preguntas con evidencia irrefutable:
- Leticia pierde porque el **costo de envío fijo** del Amazonas destruye el margen, sin importar las ventas.
- Noviembre parece exitoso en ingresos pero es el peor mes en utilidad por los descuentos extremos.
- El Black Friday (descuentos >= 40%) genera un **margen de -53.8%** - cada venta genera pérdida.
- Eliminar todas las categorías deficitarias de Leticia mejoraría la utilidad global a **$119,082**.
- Limitar los descuentos de noviembre al 10% elevaría la utilidad a **$202,940**.

---

## 7. Inventario de Medidas y Objetos del Modelo

### 7.1 Medidas DAX Principales
| Medida | Descripción |
| :--- | :--- |
| **Ingresos_Netos** | Ventas con descuentos aplicados fila por fila (SUMX) |
| **Costos_Totales** | Costo producto + costo envío fila por fila (SUMX) |
| **Utilidad_Total** | Ingresos_Netos - Costos_Totales |
| **Margen_Porcentaje** | DIVIDE(Utilidad_Total, Ingresos_Netos, 0) |
| **Utilidad_Proyectada_A** | Utilidad excluyendo combinación ciudad+categoría seleccionada |
| **Utilidad_Simulada_BF** | Utilidad con cap de descuento en noviembre (What-If) |
| **Ingreso_Bruto** | Ventas sin descontar descuentos |
| **Impacto_Descuentos** | Valor negativo de descuentos para waterfall |
| **Impacto_Costo_Producto**| Costo producto como valor negativo |
| **Impacto_Costo_Envio** | Costo envío como valor negativo |
| **WaterFall_Leticia** | Medida dinámica para cascada de costos |
| **KPI_Ingresos** | Ingresos formateados como texto para tarjeta |
| **KPI_Utilidad** | Utilidad formateada como texto para tarjeta |
| **KPI_Margen** | Margen formateado como porcentaje para tarjeta |

### 7.2 Columnas Calculadas
| Columna | Descripción |
| :--- | :--- |
| **Ingreso_Transaccion** | Ingreso neto por transacción individual (para Boxplot) |
| **Clasificacion_BF** | Etiqueta Black Friday vs Normal (Descuento_pct >= 0.40) |

---

## 8. Despliegue en Power BI Service (La Nube)
El paso final para que el Dashboard de NovaMarket esté disponible a nivel mundial, idéntico al enlace en vivo proporcionado al inicio.

### Pasos Técnicos para el Despliegue:
1. **Publicar desde Desktop:** Una vez terminado y guardado tu archivo `.pbix`, haz clic en el botón **"Publicar"** (Publish) situado en la cinta de opciones de inicio de Power BI Desktop.
2. **Selección del Área de Trabajo:** Selecciona "Mi área de trabajo" (My Workspace) o el área del proyecto, y espera a que el archivo se suba exitosamente a los servidores de Microsoft.
3. **Power BI Service:** Abre tu navegador, ve a [app.powerbi.com](https://app.powerbi.com/) e inicia sesión con tu cuenta corporativa o académica.
4. **Publicar en la Web (Público):** Dentro de tu área de trabajo, abre el informe que acabas de subir. Luego, haz clic en **Archivo -> Insertar informe -> Publicar en la Web (público)**.
5. **Generar Enlace:** El sistema generará una URL pública y un código iFrame. ¡Copia la URL! Este es el enlace exacto que le presentarás a la Junta Directiva para que analicen las anomalías del Black Friday y el caso de Leticia desde cualquier dispositivo web.
