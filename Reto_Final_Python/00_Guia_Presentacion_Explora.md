# 🚀 Guía Oficial: La Receta Paso a Paso para la Presentación EXPLO-RA
**Evento:** EXPLO-RA 2026 | Quantum Analytics Group | Énfasis II | Unicomfacauca
**Docente:** Edward Zúñiga Dorado

Esta guía es tu "receta de cocina" para asegurar que tu presentación técnica salga perfecta. Sigue los pasos en orden y tendrás garantizado el éxito técnico de tu demostración.

---

## 1. Configuración del Entorno (La Receta de Preparación)

Antes de empezar, debemos asegurarnos de que la cocina tiene todos los ingredientes. Si es la primera vez que abres este proyecto en tu computadora, sigue estos pasos:

### 1.1. Los Requisitos Base
- **Visual Studio Code (VS Code):** Tu editor principal.
- **Extensión de Jupyter en VS Code:** Fundamental para poder abrir y leer el archivo `.ipynb`. Búscala en las extensiones de VS Code e instálala.
- **Python Estándar:** El mismo que usamos en las clases.

### 1.2. Instalación de Librerías (Los Ingredientes)
Abre la terminal integrada en VS Code (`Terminal -> New Terminal`), asegúrate de estar en la carpeta `EXPLO_RA` y ejecuta **exactamente** este comando:

```bash
pip install plotly streamlit pandas openpyxl
```

**⚠️ ¿Cómo verificar que se instaló bien?**
*Nota importante sobre la terminal:* Aunque **todas** estas librerías deben instalarse obligatoriamente por la terminal usando `pip`, no todas funcionan como comandos de terminal una vez instaladas. Herramientas como `pandas`, `plotly` o `openpyxl` operan de forma interna dentro del código de Python. Por lo tanto, **no intentes verificar escribiendo `pandas --version`** en la terminal (te saldrá un error de *command not found*). 

Para verificar que todo está bien instalado, simplemente lee el resultado del comando `pip install` que acabas de ejecutar. Si ves mensajes que dicen **"Requirement already satisfied"** o **"Successfully installed"**, significa que el código de Python ya puede usarlos. ¡Estás listo y puedes continuar!

### 1.3. El Motor del Notebook (ipykernel)
La primera vez que abras el archivo `.ipynb` e intentes correr la primera celda, es muy probable que VS Code te lance un aviso azul en la parte inferior derecha diciendo algo como: *"Running cells with 'Python' requires the ipykernel package"*.
- **La solución:** Solo haz clic en el botón **Install** de ese aviso. Toma unos segundos instalar el motor para que el notebook funcione y ya no te volverá a molestar.

---

## 2. Cómo Ejecutar los Archivos (El Orden Correcto)

El orden de los factores aquí **SÍ** altera el producto. No puedes abrir el Dashboard sin antes limpiar los datos. Sigue este orden estricto:

### PASO 1: Ejecutar el Notebook Principal (`NM_Galacticos_Antigravity_FINAL.ipynb`)
Este archivo es el corazón del proyecto. Debes abrirlo y ejecutar **cada celda de arriba hacia abajo** (puedes usar el botón "Run All" en la parte superior).

**¿Por qué es obligatorio correr esto primero?**
1. **Limpia los datos:** Toma el archivo sucio original (`S01_Ventas_Novamarket_Datos_Sucios.xlsx`), lo limpia mediante código y exporta un nuevo archivo llamado `S01_Ventas_Novamarket_Datos_Limpios.csv` (este es el insumo limpio que leerá el Dashboard).
2. **Genera el Dashboard:** La ultimísima celda de este Notebook tiene un "Magic Command" (`%%writefile dashboard_novamarket.py`). Esto significa que al ejecutar esa celda, ¡se autogenera físicamente el archivo del Dashboard!

### PASO 2: Levantar el Dashboard (`dashboard_novamarket.py`)
Una vez que el Notebook terminó y verificaste que los datos están correctos (ver la fase del "Número de Oro" más abajo), abre tu terminal de VS Code, asegúrate de estar en la carpeta `EXPLO_RA` y ejecuta:

```bash
streamlit run dashboard_novamarket.py
```
Se abrirá automáticamente una pestaña en tu navegador web con la interfaz gráfica interactiva lista para presentar a la Junta.

---

## 3. Cómo Leer el Código (Explicación Sencilla para la Audiencia)

Si en la sustentación alguien de la Junta te pregunta: *"¿Qué hace exactamente ese código de Python?"*, no te compliques leyendo variables. Explica la lógica de negocio detrás de estas 3 grandes fases del Notebook:

### FASE I: Carga y Limpieza (Data Cleaning)
* *"Teníamos una base de datos con 512 registros llenos de errores de digitación y datos en blanco. El código soluciona esto de forma automatizada:"*
  - **`drop_duplicates()`**: Borra las filas que estaban repetidas. Pasamos de 512 a 500 transacciones reales.
  - **`.replace()` y los diccionarios (`ciudad_map`)**: Traduce y unifica errores humanos. Le enseña al código que "BOGOTÁ", "Bogota " y "bogota" son en realidad la misma ciudad y debe sumarlos juntos.
  - **Imputación de Nulos:** Los datos en blanco de la columna "Cantidad" se rellenaron utilizando la Mediana estadística de cada categoría de producto, para no alterar la tendencia.

### FASE II: Verificación Matemática y "El Número de Oro"
* *"Una vez limpiado el texto, calculamos el dinero (Ingreso = Cantidad × Precio × (1 - Descuento)). Luego, hicimos una prueba de calidad:"*
  - **El filtro:** Le pedimos al código que sumara exclusivamente la utilidad de **Leticia**.
  - **El Número de Oro:** Si da exactamente **−$79,342** y un margen del **−50.4%**, sabemos con 100% de certeza matemática que la limpieza de la Fase I fue perfecta y los datos son confiables.

### FASE III: Autogeneración del Dashboard
* *"Para no tener que programar la web desde cero por separado, usamos un comando especial:"*
  - **`%%writefile`**: Es un comando "mágico" de los Notebooks. Literalmente toma todo el código visual que está en esa celda y fabrica el archivo del Dashboard para que Streamlit lo lea y lo convierta en la página web que estamos viendo.

---

## 4. Respuestas a la Junta Directiva (El As bajo la manga)

El profesor y jurado evaluará tu dominio del negocio asumiendo el rol de una Junta Directiva. Aquí están las preguntas que te harán y la respuesta analítica esperada (argumenta siempre basándote en los datos que muestra tu Dashboard, ¡no opines!):

| 🎯 Pregunta de la Junta | 💡 Respuesta Analítica Esperada |
| :--- | :--- |
| **"¿Por qué Leticia pierde dinero? ¿Es un problema de ventas o de costos?"** | *"El costo de envío ($1,650 por transacción) representa aproximadamente el 73% del ingreso bruto. **No es un problema de ventas** —Leticia vende bien—. Es un problema estructural de la logística de envíos hacia esa zona que devora la rentabilidad."* |
| **"Si cerramos Leticia hoy mismo, ¿cuánto mejora el margen total?"** | *"Como vimos en el Simulador del Dashboard, la utilidad total de la empresa pasa de ~$42,914 a ~$122,256. Esto es un aumento de casi el 185%. El margen global de la compañía mejora dramáticamente pasando del 3.2% a casi un **10.4%**."* |
| **"¿El Black Friday mejoró nuestras utilidades?"** | *"No. El Black Friday aumentó considerablemente el volumen de ventas, pero los descuentos agresivos (hasta del 40-60%) comprimieron severamente los márgenes. Vendimos más productos, pero la rentabilidad general cayó. Es el clásico volumen vs. margen."* |
| **"¿Qué información adicional necesitarían para tomar una decisión final?"** | *"Para decidir si cerrar Leticia o reestructurarla, necesitaríamos: El costo fijo de mantener la operación allá, los contratos actuales con clientes (para evitar multas por cierre), datos de mercado (¿hay competidores creciendo ahí?) y cotizaciones de nuevos aliados logísticos más económicos."* |

---
*Diseñado para el triunfo en EXPLO-RA 2026. ¡Mucho éxito en la presentación!*
