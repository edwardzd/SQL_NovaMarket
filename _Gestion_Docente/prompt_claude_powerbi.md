# Prompt de Rescate para Power BI (Vía Claude MCP)

Copia y pega este prompt en tu chat con Claude para reconducir la sesión y terminar el dashboard de Power BI sin errores ni "alucinaciones" técnicas:

---
*(Copia desde aquí)*

**ACTÚA COMO UN ARQUITECTO EXPERTO EN POWER BI Y DAX.**
Actualmente estás conectado a mi modelo de Power BI vía MCP. Ayer tuvimos problemas con la limpieza de datos, pero **ya logramos estabilizar la data y calcular los primeros KPIs correctamente**. La utilidad neta total es de ~$39,740.

**TU NUEVO OBJETIVO ESTRICTO:** 
Necesitamos construir las visualizaciones exactas para llegar al mismo nivel analítico que logramos en nuestro dashboard de Python, demostrando el caso de Leticia y el Black Friday.

**REGLA DE ORO SOBRE TUS LIMITACIONES (MCP):** 
Sé que a través de MCP puedes leer el esquema, ejecutar consultas y crear/modificar medidas DAX, pero **NO PUEDES construir ni editar objetos visuales en el lienzo gráficamente**. Por lo tanto, tu tarea a partir de ahora se divide estrictamente en dos pasos por cada gráfico:
1. Usar MCP solo para **escribir y validar las Medidas DAX exactas** que necesitemos en el modelo.
2. Darme **instrucciones paso a paso (clics en la interfaz)** para que YO construya los gráficos manualmente en Power BI Desktop (arrastrando campos al Eje X, Eje Y, Leyenda, etc.). Deja de intentar soluciones programáticas para lo visual; guíame como un tutor por la interfaz gráfica.

### EL DASHBOARD QUE DEBEMOS CONSTRUIR HOY:
Debes guiarme paso a paso, uno por uno, para construir estos 5 elementos exactos:

1. **El Gráfico de Cascada (Waterfall) para el Problema de Leticia:**
   - *Objetivo:* Mostrar cómo el Ingreso Bruto es devorado por el 'Costo_Envio' (costo logístico fijo) y los 'Descuentos', dejando una utilidad final negativa.
   - *Tu Tarea:* Dime qué medida DAX de variación crear (si aplica) y exactamente qué campos arrastrar a "Categoría", "Desglose" y "Valores".

2. **El Boxplot (Cajas y Bigotes) de Anomalías Mensuales:**
   - *Objetivo:* Demostrar que noviembre no es un mes de crecimiento orgánico, sino que está lleno de *outliers* atípicos por transacciones del Black Friday.
   - *Tu Tarea:* Como Power BI no tiene Boxplot nativo, indícame exactamente qué Custom Visual descargar (ej. Box and Whisker chart de MAQ Software) y cómo configurarlo, o dame la mejor alternativa nativa (gráfico de dispersión) para mostrar anomalías y concentración.

3. **Serie de Tiempo (El Colapso del Black Friday):**
   - *Objetivo:* Un gráfico de líneas de utilidad diaria que muestre cómo el margen se hunde a terreno negativo exactamente el 24 de Noviembre de 2023.
   - *Tu Tarea:* Guíame para configurar el eje X continuo y cómo agregar una línea de referencia o marcador de color rojo en esa fecha usando formato condicional.

4. **Matriz / Mapa de Calor (Heatmap) de Ciudades:**
   - *Objetivo:* Una tabla cruzada (Ciudades vs. Categorías) donde Leticia resalte en color rojo intenso por sus pérdidas (-$79,342).
   - *Tu Tarea:* Guíame paso a paso en la configuración del "Formato Condicional" (Color de fondo) dentro de un objeto visual de Matriz.

5. **El Simulador de Escenarios (Slicer):**
   - *Objetivo:* Un Segmentador de ciudades donde, al desmarcar "Leticia", nuestros KPIs pasen mágicamente de ~$39,740 a ~$119,082 de utilidad.

### EXTRA: DOCUMENTACIÓN PEDAGÓGICA (MUY IMPORTANTE)
A medida que vayamos construyendo cada uno de estos 5 gráficos, debes **documentar internamente paso a paso todo lo que hagamos** (incluyendo el proceso de limpieza en Power Query y el modelado DAX que ya resolvimos). 
Cuando terminemos de construir el último gráfico, tu tarea final será entregarme un documento compilado y bien estructurado que sirva como la **"Guía Técnica del Reto en Power BI"** para mis estudiantes. Este documento será la base fundamental para dictar las clases del "Corte 1" de mi curso.

**¿ENTENDIDO?** Si comprendes estas restricciones tecnológicas, el objetivo de negocio y la necesidad de generar la guía final, responde "ENTENDIDO" y comienza entregándome exclusivamente las medidas DAX y las instrucciones de clics para el **Gráfico de Cascada (Punto 1)**.
