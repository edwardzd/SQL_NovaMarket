# 🏆 GUÍA TÉCNICA — Dashboard Analítico en Python (Streamlit)
**Caso NovaMarket Tech: El Problema de Leticia y el Black Friday**

**Énfasis II - Análisis de Datos | EXPLO-RA 2026**
**Docente:** Edward Samir Zúñiga Dorado
**Quantum Analytics Group - Popayán, Cauca, Colombia**

**🌐 Enlace Oficial del Proyecto (Live):** [NovaMarket Explora en Streamlit](https://novamarket-explora.streamlit.app/)

---

## 1. Introducción y Contexto del Caso
Este documento es la guía técnica completa del Reto de Análisis de Datos para el track de **Python**. A lo largo del proyecto, transformamos un archivo CSV sucio mediante un proceso de ETL estructurado utilizando la librería **Pandas**, verificamos la integridad financiera del negocio, y construimos un dashboard web interactivo con **Streamlit** y **Plotly** que fue publicado en internet.

Este flujo demuestra el poder de Python para automatizar procesos analíticos de principio a fin (End-to-End).

---

## 2. FASE I: ETL en Pandas (Limpieza de Datos)
El proceso de ETL (Extract, Transform, Load) ocurre dentro del Jupyter Notebook `NM_Galacticos_Antigravity_FINAL.ipynb`. El objetivo es transformar 662 registros con errores en 650 transacciones perfectas.

### 2.1 Los 3 Pasos Críticos de Limpieza
1. **Eliminación de Duplicados:**
   Se utiliza el método `drop_duplicates()` basándose en las transacciones para eliminar registros clonados que inflaban artificialmente las ventas.
   ```python
   df = df.drop_duplicates(subset=['ID_Transaccion'], keep='first')
   ```

2. **Estandarización de Ciudades y Categorías:**
   Los errores humanos de digitación ("bogota", "BOGOTÁ", "Cartajena") se corrigen utilizando diccionarios y el método `.replace()`.
   ```python
   ciudad_map = {'bogota': 'Bogotá', 'BOGOTÁ': 'Bogotá', 'Cartajena': 'Cartagena'}
   df['Ciudad'] = df['Ciudad'].str.strip().replace(ciudad_map)
   ```

3. **Imputación de Nulos:**
   En lugar de eliminar transacciones con campos en blanco (`NaN`) en la columna "Cantidad", rellenamos esos vacíos con la **mediana estadística** de la categoría correspondiente para no alterar el comportamiento normal de ventas.

---

## 3. FASE II: El "Número de Oro" (Métricas Financieras)
Una vez el DataFrame está limpio (`S01_Ventas_Novamarket_Datos_Limpios.csv`), calculamos las métricas financieras fila por fila. En Python, esto se hace vectorizando operaciones matemáticas sobre las columnas:

### 3.1 Cálculo del Dinero Real
```python
# Ingreso Total = Cantidad × Precio × (1 - Porcentaje de Descuento)
df['Ingreso_Total'] = df['Cantidad'] * df['Precio_Unitario'] * (1 - df['Descuento_pct'])

# Costo Total = (Cantidad × Costo Unitario) + Costo de Envío Fijo
df['Costo_Total'] = (df['Cantidad'] * df['Costo_Unitario']) + df['Costo_Envio']

# Utilidad Neta
df['Utilidad_Neta'] = df['Ingreso_Total'] - df['Costo_Total']
```

### 3.2 La Prueba de Ácido (El Número de Oro)
Para confirmar que el ETL fue perfecto, filtramos el DataFrame para aislar a **Leticia**. 
La `Utilidad_Neta` total de Leticia debe ser exactamente **-$79,342** y su Margen del **-50.4%**. Si el código arroja estos números, los datos están listos para pasar a la interfaz visual.

---

## 4. FASE III: Construcción del Dashboard (Streamlit & Plotly)
A diferencia de Power BI, en Python el Dashboard se genera mediante código. Utilizamos la celda mágica `%%writefile dashboard_novamarket.py` al final del Notebook para autogenerar el archivo web.

### 4.1 Inyección de Diseño CSS
Streamlit nos permite personalizar los colores corporativos inyectando código HTML y CSS nativo:
```python
st.markdown("""
<style>
    .metric-card {
        background-color: #2b2b36;
        border-radius: 10px;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)
```

### 4.2 Gráficos y Layout
- Usamos `st.columns(4)` para estructurar el panel superior con tarjetas de KPIs (Ingresos, Costos, Utilidad, Margen).
- Integramos gráficos interactivos (`go.Waterfall`, `go.Box`, `go.Scatter`) creados con **Plotly Graph Objects**, y los renderizamos en la web usando `st.plotly_chart(fig, use_container_width=True)` para que se adapten automáticamente al tamaño de la pantalla.

---

## 5. FASE IV: Despliegue en Streamlit Community Cloud
El paso final para que el Dashboard de NovaMarket esté disponible a nivel mundial en [https://novamarket-explora.streamlit.app/](https://novamarket-explora.streamlit.app/).

### Pasos Técnicos para el Despliegue:
1. **GitHub:** Se subieron tres archivos fundamentales a un repositorio público:
   - `dashboard_novamarket.py` (el script de la aplicación).
   - `S01_Ventas_Novamarket_Datos_Limpios.csv` (la base de datos limpia de donde lee).
   - `requirements.txt` (lista de dependencias: `streamlit`, `pandas`, `plotly`).
2. **Streamlit Cloud:** Se inició sesión en `share.streamlit.io` vinculando la cuenta de GitHub.
3. **Conexión:** Se seleccionó el repositorio, se apuntó al archivo `dashboard_novamarket.py` y se configuró el subdominio personalizado (`novamarket-explora`). ¡Despliegue exitoso!

---

## 6. FASE V: Conclusiones para la Junta Directiva
Al interactuar con el Dashboard publicado, llegamos a las conclusiones de negocio fundamentales que salvan a la empresa:

1. **El Problema de Leticia:** Leticia tiene excelentes ventas, pero una matriz de **costos de envío fijos masivos** que devoran la utilidad transaccional, resultando en pérdidas netas astronómicas.
2. **El Espejismo de Noviembre:** Noviembre (Black Friday) fue el mes con el mayor volumen de ventas brutas, pero los descuentos excesivos (+40%) generaron un margen negativo general. Se vendió mucho más inventario, pero se perdió dinero. 
3. **La Solución (Escenarios):** Cerrar operaciones deficitarias en Leticia o limitar estrictamente los topes de descuento en Black Friday dispara inmediatamente la utilidad global de la empresa de ~$39K a más de ~$119K.
