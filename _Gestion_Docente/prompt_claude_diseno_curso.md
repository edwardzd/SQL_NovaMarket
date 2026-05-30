# Mega-Prompt para Claude: Rediseño del Syllabus "Análisis de Datos"

**Instrucción para el Usuario:** Copia el siguiente texto y pégalo en un nuevo chat con Claude para que rediseñe toda tu estructura curricular del curso.

---
*(Copia desde aquí)*

**ACTÚA COMO UN DISEÑADOR CURRICULAR SENIOR Y EXPERTO EN DATA SCIENCE.**
Tu tarea es reformular y estructurar el syllabus completo de mi curso universitario de "Análisis de Datos" (16 semanas/sesiones). 

En el pasado, tuvimos el problema de que cambiaste los datasets entre sesiones, causando confusión. El objetivo principal de este rediseño es que **TODO el semestre de 16 semanas gire en torno a un ÚNICO dataset transversal:** `S01_Ventas_Novamarket_Datos_Sucios.csv` (y su contraparte en `.xlsx`).

El curso se divide en 3 "Cortes" (evaluaciones). **La regla de oro es que en CADA corte se debe vivir el ciclo completo de los datos (Cargar Data Sucia -> Limpiar -> Analizar -> Visualizar/Dashboard)** pero usando herramientas tecnológicas diferentes, aumentando la complejidad. El objetivo final de los 3 cortes siempre es llegar a la misma verdad financiera ("Los Números de Oro").

### LOS "NÚMEROS DE ORO" (El faro de cada Corte)
Sin importar la herramienta que usen, al final del corte, el estudiante debe lograr demostrar que:
- El dataset limpio pasa de 662 a 650 registros.
- La utilidad global de la empresa es de ~$39,740.
- Leticia pierde -$79,342 por culpa de los costos de envío.
- El Black Friday disparó ventas pero destruyó el margen por culpa de los descuentos.

---

### DIRECTRICES PEDAGÓGICAS Y DE INSTALACIÓN
- **Progresión "De menos a más":** Cada corte debe empezar desde lo más básico con su herramienta y aumentar gradualmente en complejidad.
- **Claridad en Instalaciones:** En las sesiones donde se requiera instalar software (ej. VS Code, librerías de Python, SQLite), debes proporcionar un bloque claro de "Instalación de Entorno" que especifique **qué** instalar, **dónde**, **cuándo** y **para qué**, garantizando el éxito técnico del estudiante desde el primer minuto.
- **Archivos Versionados:** Cada sesión debe indicar el nombre exacto de la versión del archivo que el estudiante usará o creará (ej. `S11_Limpieza.ipynb`, `S14_Dashboard_v1.py`), facilitando la continuidad técnica en Colab o Antigravity.
- **Gestión del Tiempo (3 horas por sesión):** Sabiendo que cada sesión dura exactamente 3 horas, tú tienes la libertad y la responsabilidad de distribuir los tiempos y pausas de la clase (ej. teoría vs. práctica) de acuerdo con la carga cognitiva y complejidad técnica del tema a tratar.

---

### ESTRUCTURA DE LAS 16 SESIONES QUE DEBES DESARROLLAR:

#### CORTE 1: El enfoque analista tradicional (Excel & Power BI)
*Historia previa a respetar:* Empezamos viendo un dashboard mal hecho para generar shock. Luego fuimos a Excel, luego a Power Query y terminamos en Power BI.
* **Sesión 1:** El Diagnóstico. Presentación del problema de NovaMarket y muestra de un dashboard mal formulado en Power BI. Exploración cruda en Excel con estadística básica y limpieza manual.
* **Sesión 2:** La Automatización inicial. Limpieza del dataset en Excel usando Power Query.
* **Sesión 3:** Modelado de Datos. Creación de relaciones y medidas usando Power Pivot / DAX básico.
* **Sesión 4:** Visualización. Creación del Dashboard final en Power BI con los datos limpios (KPIs, Cascada de Costos, Boxplot).
* **Sesión 5:** Reto Evaluativo 1. Llegar a los Números de Oro de forma autónoma con Power BI.

#### CORTE 2: Data Engineering (SQL)
*Historia previa a respetar:* Vimos sentencias `SELECT`, `JOIN` y `GROUP BY`, pero faltó cargar el CSV sucio y limpiarlo en SQL. Hay que integrarlo.
* **Sesión 6:** Introducción a Bases de Datos Relacionales (SQLite). Importación pura del archivo `S01_Ventas_Novamarket_Datos_Sucios.csv` a una tabla cruda.
* **Sesión 7:** Limpieza de datos en SQL. Uso de sentencias `DELETE` (para duplicados), `UPDATE`, `TRIM`, e imputación de nulos condicional con SQL puro.
* **Sesión 8:** Análisis de datos. Uso avanzado de `SELECT`, `JOIN`, `GROUP BY` y funciones de agregación para encontrar los "Números de Oro".
* **Sesión 9:** Visualización y Reportería en SQL. Creación de Vistas (`VIEWS`) y un "Dashboard Textual" por consola que responda las preguntas de la Junta.
* **Sesión 10:** Reto Evaluativo 2. Limpiar y consultar la base de datos de manera autónoma para responder el caso de Leticia.

#### CORTE 3: Data Science e IA (Python, Colab & Antigravity)
*Historia previa a respetar:* Usamos Colab, Pandas y Matplotlib. Luego pasamos a VS Code usando agentes de IA (Antigravity) para programar Streamlit.
* **Sesión 11:** Introducción profunda a las bases: Python, `pandas`, `matplotlib`, `numpy` y la visión hacia `streamlit`. Carga del CSV sucio en Google Colab e inicio de los procesos de limpieza algorítmica.
* **Sesión 12:** Análisis de Datos Exploratorio (EDA). Uso de `matplotlib` y `seaborn` en Colab para encontrar visualmente el impacto del Black Friday en los datos limpios.
* **Sesión 13:** Presentación e Infraestructura Local. Transición a VS Code, configuración del entorno e introducción a la IA Antigravity. Creación de un script formal de Python para calcular el Número de Oro.
* **Sesión 14:** Desarrollo del Dashboard Web. Construcción paso a paso de `dashboard_novamarket.py` usando `streamlit` y `plotly`, integrando los análisis de la sesión 12.
* **Sesión 15:** Despliegue en la Nube. Publicación del dashboard en Streamlit Community Cloud. Preparación de la sustentación (juego de roles).
* **Sesión 16:** EXPLO-RA 2026. Reto Final (Evaluación del Corte 3 y Proyecto Final). Sustentación en juego de roles frente a la Junta Directiva.

---

### TUS ENTREGABLES (LO QUE ME DEBES DEVOLVER AHORA MISMO)
Por favor, analiza esta estructura y devuélveme un documento de diseño curricular detallado para las **16 sesiones**. Para cada sesión, debes entregarme:
1. **Guía del Profesor:** Objetivo de la clase, dinámicas a usar y conceptos clave a enseñar.
2. **Guía del Estudiante:** Lo que el estudiante debe hacer, scripts, retos o clics específicos en la herramienta.
3. **El Insumo:** Confirmar qué set de datos y qué herramientas usará en esa clase específica. 

Tu tono debe ser motivador, estructurado y enfocado en que los estudiantes sientan que, aunque repiten el análisis de la misma empresa, cada corte les da "superpoderes" tecnológicos diferentes.
