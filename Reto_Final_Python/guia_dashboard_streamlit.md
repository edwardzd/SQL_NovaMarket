# Construyendo el Dashboard Interactivo con Streamlit 🚀

Para presentar a la Junta Directiva de NovaMarket, creamos una interfaz visual utilizando **Streamlit**, una librería de Python que convierte scripts de análisis de datos en páginas web interactivas en minutos. 

Esta guía te ayudará a ti y a tus estudiantes a entender línea por línea cómo funciona el código que genera el dashboard, y cómo pueden jugar con él para personalizar los estilos y el diseño.

---

## ⚠️ El Error de `%%writefile` (¿Qué pasó?)

En tu captura de pantalla, te salió el error `UsageError: Line magic function %%writefile not found`. 

**La Causa:** Los "comandos mágicos" de los Notebooks (los que empiezan con `%%`) tienen una regla de oro estricta: **Tienen que ir obligatoriamente en la línea 1 de la celda**. Ni siquiera pueden tener un comentario `#` o un salto de línea arriba de ellos. Como el comentario estaba en la línea 1, Jupyter se confundió.
*(Ya lo he corregido en tu archivo, si vuelves a correr la celda, funcionará perfectamente).*

Este comando mágico literalmemte toma todo el código Python que escribiste en esa celda y lo guarda físicamente en un nuevo archivo llamado `dashboard_novamarket.py`.

---

## 🏗️ Anatomía del Dashboard (Explicación línea a línea)

El archivo generado contiene las instrucciones de diseño. Aquí te explico los bloques principales para que aprendan a modificarlos:

### 1. La Configuración de la Página
```python
st.set_page_config(page_title="NovaMarket Analytics", page_icon="📈", layout="wide")
```
Esto le dice al navegador web cómo mostrar la pestaña.
- **¿Qué puedes cambiar?** Cambia el `page_title` por el nombre de tu equipo, o el `page_icon` por cualquier otro emoji (ej: `"🛒"`, `"📊"`). El `layout="wide"` hace que el dashboard ocupe toda la pantalla a lo ancho en lugar de verse en una columna estrecha.

### 2. Inyectando Estilos (CSS Personalizado)
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
Streamlit usa `st.markdown` para escribir texto, pero si le pasas `unsafe_allow_html=True`, ¡te permite inyectar código CSS real!
- **¿Qué puedes cambiar?** Esta es tu área de juego para el diseño estético. Puedes cambiar los colores hexadecimales (`#2b2b36` es un gris oscuro elegante), modificar el radio de los bordes (`border-radius`) para hacer las tarjetas más redondas o más cuadradas, etc. Si quieres colores corporativos de NovaMarket, este es el lugar.

### 3. Las Columnas (El Layout)
```python
c1, c2, c3, c4 = st.columns(4)
```
Esta es la magia estructural de Streamlit. Con una sola línea, divide la pantalla en 4 columnas perfectamente espaciadas e iguales.
- **¿Qué puedes cambiar?** Si pones `st.columns(3)`, tendrás 3 columnas más anchas. Si pones `st.columns([1, 2, 1])`, crearás 3 columnas pero la del medio será el doble de ancha que las de los lados. 

### 4. Las Tarjetas de KPIs (Métricas)
```python
c1.metric("Ingresos Totales", f"${ingreso:,.0f}")
```
El comando `.metric()` crea automáticamente esos rectángulos bonitos con un título pequeño y un número grande. Arriba le dijimos a `c1` (la columna 1) que dibuje ahí el Ingreso Total.
- **¿Qué puedes cambiar?** El texto del título y el formato numérico.

### 5. Renderizando los Gráficos (Plotly)
```python
st.plotly_chart(fig_ciudad, use_container_width=True)
```
A lo largo del código armamos nuestros gráficos hermosos usando la librería `plotly`. Esta línea simplemente toma ese gráfico (`fig_ciudad`) y lo incrusta en la página web.
- **`use_container_width=True`** es vital: hace que el gráfico sea "Responsive", es decir, que se estire o se encoja automáticamente dependiendo de si el usuario está viéndolo en un monitor gigante o en un portátil pequeño.

---

## 🎨 ¿Cómo jugar y personalizar el diseño?

Si tus estudiantes quieren hacer que su presentación en EXPLO-RA destaque visualmente:

1. **Cambiar de Tema Claro a Oscuro:**
   En la ventana del navegador donde corre el Dashboard, diles que hagan clic en los 3 puntitos de arriba a la derecha (menú) -> `Settings` -> `Theme`. Pueden elegir `Dark`, `Light` o crear colores personalizados para que su dashboard no se vea igual al de los demás grupos.

2. **Jugar con la paleta de colores de Plotly:**
   En el código donde se crean las figuras (`go.Bar`, `go.Scatter`), pueden cambiar las propiedades `marker_color` por colores corporativos, usando colores en inglés (`'red'`, `'royalblue'`) o códigos hexadecimales (`'#FF5733'`).

3. **Modificar el Simulador:**
   En la sección de Leticia, pueden cambiar las fórmulas para simular "Qué pasaría si..." (Ej: ¿Qué pasa si logramos negociar el costo de envío a la mitad en lugar de eliminar la ciudad por completo?). Streamlit recalculará y mostrará los resultados al instante.
