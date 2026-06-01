# 🚀 NovaMarket: Reto Final EXPLO-RA 2026 (Track Python)

Bienvenido a la carpeta principal del track de Python para el Reto Final de NovaMarket. Este repositorio contiene todo lo necesario para limpiar los datos financieros de la empresa y desplegar un dashboard interactivo que explique por qué Leticia está quebrando y cuál fue el verdadero impacto del Black Friday.

## 🧭 El Flujo Principal (Core Workflow)

Si eres un estudiante o el presentador final, tu flujo de trabajo se resume en estos 4 archivos:

1. **`S01_Ventas_Novamarket_Datos_Sucios.csv`**: El insumo principal. La base de datos cruda y llena de errores.
2. **`NM_Galacticos_Antigravity_FINAL.ipynb`**: El corazón del proyecto. Este Jupyter Notebook lee el CSV sucio, limpia los datos (pandas), calcula los "Números de Oro", y en su última celda **autogenera** el archivo del Dashboard.
3. **`S01_Ventas_Novamarket_Datos_Limpios.csv`**: El archivo resultante tras ejecutar la limpieza en el Notebook.
4. **`dashboard_novamarket.py`**: El código de la aplicación web de Streamlit. No lo editas a mano; nace del Notebook. Para verlo, corres `streamlit run dashboard_novamarket.py` en tu terminal.

## 📁 Estructura del Directorio

Para evitar confusiones, aquí está el mapa exacto de qué hace cada archivo en esta carpeta:

### 📊 1. Archivos de Datos (Datasets)
* `S01_Ventas_Novamarket_Datos_Sucios.csv` -> Dataset oficial a limpiar.
* `S01_Ventas_Novamarket_Datos_Sucios.xlsx` -> Respaldo en Excel (Referencia histórica).
* `S01_Ventas_Novamarket_Datos_Limpios.csv` -> Dataset limpio generado por el Notebook.
* `S06_INSERT_FactVentas_Fixed.sql` -> Archivo de datos estructurado usado por el equipo de SQL.

### 🧠 2. Proyecto y Despliegue
* `NM_Galacticos_Antigravity_FINAL.ipynb` -> Notebook principal de limpieza y creación del dashboard.
* `dashboard_novamarket.py` -> Archivo de Streamlit autogenerado.
* `requirements.txt` -> Lista de dependencias (`pandas`, `streamlit`, `plotly`) requerida para que el dashboard funcione en internet.

### 📚 3. Guías y Documentación Pedagógica
* `00_Guia_Presentacion_Explora.md` -> La "receta" oficial para que los estudiantes expongan. Contiene las respuestas a la Junta Directiva.
* `guia_entornos_virtuales.md` -> Tutorial de qué son y cómo configurar los entornos virtuales y librerías del proyecto.
* `guia_despliegue_streamlit.md` -> Instrucciones para publicar el dashboard en la nube.
* `guia_dashboard_streamlit.md` -> Explicación técnica de cómo funcionan las gráficas de Streamlit.
* `guia_basica_pandas_sintaxis.md` -> Documentación de apoyo de Python para estudiantes.

### 🛠️ 4. Scripts Utilitarios del Docente (NO son para el estudiante)
Estos archivos de Python fueron creados por el docente y la IA (Antigravity) para automatizar la construcción del material. **Los estudiantes pueden ignorarlos.**
* **`comment_all.py` / `add_comments.py`**: Scripts de automatización que leen el Notebook y le inyectan automáticamente comentarios en español celda por celda. Esto se hizo para que el código del Notebook le quedara súper bien explicado a los estudiantes.
* **`export_csv.py`**: Un pequeño script de prueba que se usó en fases tempranas para asegurar que la exportación a CSV funcionara.
* **`test_clean.py`**: Script rápido para auditar y verificar que los números financieros dieran exactos antes de pasarlos al Notebook oficial.

---
**Nota:** El éxito de EXPLO-RA radica en la secuencia. *Limpiar Data -> Autogenerar App -> Desplegar App.* ¡Mucho éxito en la presentación!
