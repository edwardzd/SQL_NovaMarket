# MAGIC COMMAND: Esta instrucción toma todo el código debajo de ella y crea el archivo del Dashboard.
# Streamlit es la herramienta que convierte código Python en una página web interactiva.
import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

# Configuramos la pestaña del navegador: Título, ícono, y decimos que use toda la pantalla (wide).
st.set_page_config(
    page_title="NovaMarket Analytics",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
div[data-testid="metric-container"] {
    background: #f8f9fa;
    border-radius: 8px;
    padding: 12px;
    border-left: 4px solid #2E75B6;
}
</style>
""", unsafe_allow_html=True)

# cache_data guarda los datos en memoria para que la página web cargue súper rápido al filtrar.
@st.cache_data
# Definimos una función llamada 'cargar' que va a leer el CSV limpio y prepararlo para los gráficos.
def cargar():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'S01_Ventas_Novamarket_Datos_Limpios.csv')
    df = pd.read_csv(csv_path)
    df['Ingreso_Total'] = df['Cantidad'] * df['Precio_Unitario'] * (1 - df['Descuento_pct'])
    df['Costo_Total']   = df['Cantidad'] * df['Costo_Unitario']  + df['Costo_Envio']
    df['Utilidad_Neta'] = df['Ingreso_Total'] - df['Costo_Total']
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Mes']   = df['Fecha'].dt.to_period('M').astype(str)
    df['BF']    = df['Descuento_pct'].apply(
        lambda x: '≥40% (Black Friday)' if x >= 0.40 else '<40% (Normal)')
    return df

# Ejecutamos la función cargar() y guardamos los datos listos en la variable 'df'
df = cargar()

# ── Sidebar ──────────────────────────────────────────────────────────────────
# sidebar crea un panel lateral en la página web. Añadimos un título 'Filtros'.
st.sidebar.markdown("## 🔍 Filtros")
# Creamos una caja de selección múltiple en el panel lateral para elegir las Ciudades.
ciudades   = st.sidebar.multiselect("Ciudad",
    sorted(df['Ciudad'].unique()), default=sorted(df['Ciudad'].unique()))
categorias = st.sidebar.multiselect("Categoría",
    sorted(df['Categoria'].unique()), default=sorted(df['Categoria'].unique()))
meses      = st.sidebar.multiselect("Mes",
    sorted(df['Mes'].unique()), default=sorted(df['Mes'].unique()))

# Creamos una tabla 'dff' que filtrará los datos según lo que el usuario elija en la barra lateral.
dff = df[
    df['Ciudad'].isin(ciudades) &
    df['Categoria'].isin(categorias) &
    df['Mes'].isin(meses)
]

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("## 🚀 NovaMarket Tech — Dashboard Analítico")
st.caption("Quantum Analytics Group  ·  Sep–Nov 2023  ·  650 transacciones  ·  EXPLO-RA 2026")

# ── KPIs ─────────────────────────────────────────────────────────────────────
# Sumamos todo el ingreso total de los datos filtrados para mostrarlo en el indicador superior.
ventas   = dff['Ingreso_Total'].sum()
utilidad = dff['Utilidad_Neta'].sum()
margen   = utilidad / ventas * 100 if ventas > 0 else 0

# st.columns() divide la pantalla en 4 columnas invisibles para acomodar nuestros indicadores (KPIs).
c1, c2, c3, c4 = st.columns(4)
# metric() crea esas cajas bonitas de números grandes. Aquí mostramos las Ventas Totales.
c1.metric("💰 Ventas Totales",     f"${ventas:,.0f}")
c2.metric("📈 Utilidad Neta",      f"${utilidad:,.0f}")
c3.metric("📊 Margen Global",      f"{margen:.1f}%")
c4.metric("🧾 Transacciones",      f"{len(dff):,}")
st.divider()

# ── Fila 1: Utilidad por Ciudad + Margen por Categoría ───────────────────────
# Dividimos la pantalla en 2 columnas: la izquierda (ca) un poco más ancha que la derecha (cb).
ca, cb = st.columns([1.2, 1])

with ca:
    st.markdown("### 📍 Utilidad Neta por Ciudad")
    uc = (dff.groupby('Ciudad')['Utilidad_Neta'].sum()
            .reset_index().sort_values('Utilidad_Neta'))
    fig1 = go.Figure(go.Bar(
        x=uc['Utilidad_Neta'], y=uc['Ciudad'], orientation='h',
        marker_color=['#C00000' if v < 0 else '#375623' for v in uc['Utilidad_Neta']],
        text=uc['Utilidad_Neta'].apply(lambda x: f"${x:,.0f}"),
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>Utilidad: $%{x:,.0f}<extra></extra>'
    ))
    fig1.add_vline(x=0, line_dash="dot", line_color="gray", line_width=1)
    fig1.update_layout(height=300, margin=dict(t=20, b=40, l=60, r=90),
        plot_bgcolor='white', paper_bgcolor='white', font_color='black',
        xaxis=dict(gridcolor='#eee', color='black'), yaxis=dict(color='black'))
    st.plotly_chart(fig1, use_container_width=True, theme=None)

with cb:
    st.markdown("### 📦 Margen % por Categoría")
    cd = dff.groupby('Categoria')[['Ingreso_Total','Utilidad_Neta']].sum().reset_index()
    cd['Margen%'] = cd['Utilidad_Neta'] / cd['Ingreso_Total'] * 100
    cd = cd.sort_values('Margen%', ascending=False)
    fig2 = go.Figure(go.Bar(
        x=cd['Categoria'], y=cd['Margen%'],
        marker_color=['#C00000' if v < 0 else '#2E75B6' for v in cd['Margen%']],
        text=cd['Margen%'].apply(lambda x: f"{x:.1f}%"),
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Margen: %{y:.1f}%<extra></extra>'
    ))
    fig2.add_hline(y=0, line_dash="dot", line_color="gray", line_width=1)
    fig2.update_layout(height=300, margin=dict(t=20, b=40, l=40, r=20),
        plot_bgcolor='white', paper_bgcolor='white', font_color='black',
        yaxis=dict(gridcolor='#eee', color='black'), xaxis=dict(color='black'))
    st.plotly_chart(fig2, use_container_width=True, theme=None)

st.divider()

# ── Fila 2: Evolución mensual ─────────────────────────────────────────────────
st.markdown("### 📅 Ventas vs. Utilidad por Mes — El efecto Black Friday")
md2 = dff.groupby('Mes')[['Ingreso_Total','Utilidad_Neta']].sum().reset_index()

fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=md2['Mes'], y=md2['Ingreso_Total'], name='Ventas',
    marker_color='#2E75B6', opacity=0.85, yaxis='y',
    text=md2['Ingreso_Total'].apply(lambda x: f"${x/1000:,.0f}k"),
    textposition='outside', textfont=dict(color='black'),
    hovertemplate='<b>%{x}</b><br>Ventas: $%{y:,.0f}<extra></extra>'
))
fig3.add_trace(go.Scatter(
    x=md2['Mes'], y=md2['Utilidad_Neta'], name='Utilidad Neta',
    line=dict(color='#C00000', width=3),
    mode='lines+markers+text', marker=dict(size=10), yaxis='y2',
    text=md2['Utilidad_Neta'].apply(lambda x: f"${x/1000:,.0f}k"),
    textposition='top center', textfont=dict(color='#C00000', size=11, weight='bold'),
    hovertemplate='<b>%{x}</b><br>Utilidad: $%{y:,.0f}<extra></extra>'
))
nov = md2[md2['Mes'] == '2023-11']
if not nov.empty:
    fig3.add_annotation(
        x='2023-11', y=nov['Ingreso_Total'].values[0],
        text="🛒 Black Friday<br>Ventas ↑  /  Margen ↓",
        showarrow=True, arrowhead=2, arrowcolor='#C00000',
        font=dict(color='#C00000', size=11),
        bgcolor='white', bordercolor='#C00000', ax=65, ay=-45
    )
fig3.update_layout(
    height=300, margin=dict(t=20, b=40, l=50, r=70),
    xaxis=dict(color='black'),
    yaxis=dict(title=dict(text='Ventas (USD)', font=dict(color='black')), gridcolor='#eee', tickfont=dict(color='black'), color='black'),
    yaxis2=dict(title=dict(text='Utilidad (USD)', font=dict(color='black')), overlaying='y', side='right',
                zeroline=True, zerolinecolor='gray', tickfont=dict(color='black'), color='black'),
    legend=dict(orientation='h', y=1.08, font=dict(color='black')),
    plot_bgcolor='white', paper_bgcolor='white', font_color='black'
)
st.plotly_chart(fig3, use_container_width=True, theme=None)
st.divider()

# ── Fila 3: Heatmap + Black Friday comparado ──────────────────────────────────
cc, cd2 = st.columns([1.3, 1])

with cc:
    st.markdown("### 🗺️ Heatmap — Utilidad por Ciudad × Categoría")
    pv = dff.pivot_table(
        values='Utilidad_Neta', index='Ciudad',
        columns='Categoria', aggfunc='sum', fill_value=0
    )
    fig4 = go.Figure(go.Heatmap(
        z=pv.values,
        x=pv.columns.tolist(),
        y=pv.index.tolist(),
        colorscale=[[0,'#C00000'],[0.5,'#FFFFFF'],[1,'#375623']],
        zmid=0,
        text=[[f"${v:,.0f}" for v in row] for row in pv.values],
        texttemplate="%{text}",
        hovertemplate='<b>%{y} × %{x}</b><br>Utilidad: $%{z:,.0f}<extra></extra>'
    ))
    fig4.update_layout(height=290, margin=dict(t=20, b=80, l=120, r=20), font_color='black',
        xaxis=dict(color='black'), yaxis=dict(color='black'))
    st.plotly_chart(fig4, use_container_width=True, theme=None)

with cd2:
    st.markdown("### 🎯 Black Friday vs. Período Normal")
    bf2 = dff.groupby('BF')[['Ingreso_Total','Utilidad_Neta']].sum().reset_index()
    bf2['Margen%'] = bf2['Utilidad_Neta'] / bf2['Ingreso_Total'] * 100
    fig5 = go.Figure(go.Bar(
        x=bf2['BF'], y=bf2['Margen%'],
        marker_color=['#C00000' if v < 0 else '#2E75B6' for v in bf2['Margen%']],
        text=bf2['Margen%'].apply(lambda x: f"{x:.1f}%"),
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Margen: %{y:.1f}%<extra></extra>'
    ))
    fig5.add_hline(y=0, line_dash="dot", line_color="gray")
    fig5.update_layout(height=290, margin=dict(t=20, b=40, l=40, r=20),
        plot_bgcolor='white', paper_bgcolor='white', font_color='black',
        yaxis=dict(gridcolor='#eee', color='black'), xaxis=dict(color='black'))
    st.plotly_chart(fig5, use_container_width=True, theme=None)

st.divider()

# ── Fila 4: Detección de Anomalías ────────────────────────────────────────────
st.markdown("### 🕵️ Detección de Anomalías (Efecto Black Friday)")
ca1, ca2 = st.columns(2)

with ca1:
    st.markdown("**Evolución de Ventas Diarias**")
    v_diarias = dff.groupby('Fecha')['Ingreso_Total'].sum().reset_index()
    fig_ts = go.Figure()
    
    # Línea base
    fig_ts.add_trace(go.Scatter(
        x=v_diarias['Fecha'], y=v_diarias['Ingreso_Total'],
        mode='lines', line=dict(color='#2E75B6', width=2),
        name='Ventas'
    ))
    
    # Punto rojo para Black Friday (24 Nov)
    bf_date = pd.Timestamp('2023-11-24')
    bf_data = v_diarias[v_diarias['Fecha'] == bf_date]
    if not bf_data.empty:
        fig_ts.add_trace(go.Scatter(
            x=bf_data['Fecha'], y=bf_data['Ingreso_Total'],
            mode='markers', marker=dict(color='#C00000', size=12),
            name='Black Friday'
        ))
        
    fig_ts.update_layout(
        height=320, margin=dict(t=20, b=50, l=50, r=20),
        plot_bgcolor='white', paper_bgcolor='white', font_color='black',
        yaxis=dict(gridcolor='#eee', color='black', tickformat='$,.0f'),
        xaxis=dict(color='black'),
        showlegend=False
    )
    st.plotly_chart(fig_ts, use_container_width=True, theme=None)

with ca2:
    st.markdown("**Distribución de Ventas por Mes (Boxplot)**")
    # Para el boxplot es mejor usar las ventas por transacción (dff original)
    fig_box = go.Figure()
    
    meses_orden = sorted(dff['Mes'].unique())
    colores_mes = {'2023-09': '#BDD7EE', '2023-10': '#BDD7EE', '2023-11': '#FFCCCC'}
    
    for m in meses_orden:
        df_mes = dff[dff['Mes'] == m]
        fig_box.add_trace(go.Box(
            y=df_mes['Ingreso_Total'],
            name=m,
            marker_color=colores_mes.get(m, '#BDD7EE'),
            boxpoints='outliers' # Solo mostrar puntos atípicos
        ))
        
    fig_box.update_layout(
        height=320, margin=dict(t=20, b=50, l=50, r=20),
        plot_bgcolor='white', paper_bgcolor='white', font_color='black',
        yaxis=dict(gridcolor='#eee', color='black', tickformat='$,.0f'),
        xaxis=dict(color='black'),
        showlegend=False
    )
    st.plotly_chart(fig_box, use_container_width=True, theme=None)

st.divider()

# ── Fila 5: Cascada de Costos ─────────────────────────────────────────────────
st.markdown("### 💸 Estructura de Costos (Gráfico de Cascada)")

# Cálculos de los agregados
ingreso_bruto = (dff['Cantidad'] * dff['Precio_Unitario']).sum()
descuentos = ingreso_bruto - dff['Ingreso_Total'].sum()
costo_prod = (dff['Cantidad'] * dff['Costo_Unitario']).sum()
costo_env = dff['Costo_Envio'].sum()
utilidad_neta = dff['Utilidad_Neta'].sum()

fig_waterfall = go.Figure(go.Waterfall(
    name="Costos", orientation="v",
    measure=["relative", "relative", "relative", "relative", "total"],
    x=["Ingresos Brutos", "Descuentos", "Costo Producto", "Costo Envío", "Utilidad Neta"],
    textposition="outside",
    text=[f"${ingreso_bruto:,.0f}", f"-${descuentos:,.0f}", f"-${costo_prod:,.0f}", f"-${costo_env:,.0f}", f"${utilidad_neta:,.0f}"],
    y=[ingreso_bruto, -descuentos, -costo_prod, -costo_env, utilidad_neta],
    connector={"line": {"color": "gray", "dash": "dot"}},
    decreasing={"marker": {"color": "#C00000"}},
    increasing={"marker": {"color": "#2E75B6"}},
    totals={"marker": {"color": "#375623" if utilidad_neta >= 0 else "#C00000"}}
))

fig_waterfall.update_layout(
    height=350, margin=dict(t=30, b=50, l=60, r=20),
    plot_bgcolor='white', paper_bgcolor='white', font_color='black',
    yaxis=dict(gridcolor='#eee', color='black'),
    xaxis=dict(color='black')
)
st.plotly_chart(fig_waterfall, use_container_width=True, theme=None)

st.divider()

# ── Simulador ────────────────────────────────────────────────────────────────
st.markdown("### 🔮 Simulador de Escenarios")
cs1, cs2 = st.columns(2)

with cs1:
    st.markdown("**Escenario A — Eliminar categorías en Leticia**")
    cats_let = (dff[dff['Ciudad']=='Leticia']
                .groupby('Categoria')['Utilidad_Neta'].sum())
    elim = st.multiselect(
        "Categorías a eliminar en Leticia:",
        options=cats_let.index.tolist(),
        default=[c for c in cats_let.index if cats_let[c] < 0]
    )
    mask = (dff['Ciudad']=='Leticia') & (dff['Categoria'].isin(elim))
    u_sim  = dff[~mask]['Utilidad_Neta'].sum()
    delta_a = u_sim - dff['Utilidad_Neta'].sum()
    st.metric("Utilidad proyectada", f"${u_sim:,.0f}",
              delta=f"${delta_a:+,.0f} vs. actual")

with cs2:
    st.markdown("**Escenario B — Techo de descuento Black Friday**")
    techo = st.slider("Descuento máximo permitido (%)", 10, 50, 30, step=5)
    ds = dff.copy()
    ds['Desc_sim'] = ds['Descuento_pct'].clip(upper=techo/100)
    ds['Ing_sim']  = ds['Cantidad'] * ds['Precio_Unitario'] * (1 - ds['Desc_sim'])
    ds['Util_sim'] = ds['Ing_sim'] - ds['Costo_Total']
    delta_b = ds['Util_sim'].sum() - dff['Utilidad_Neta'].sum()
    st.metric("Utilidad proyectada", f"${ds['Util_sim'].sum():,.0f}",
              delta=f"${delta_b:+,.0f} vs. actual")

st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#999;font-size:11px;'>"
    "🚀 Quantum Analytics Group · EXPLO-RA 2026 · Énfasis II · Unicomfacauca · "
    "Docente: Edward Zúñiga Dorado</p>",
    unsafe_allow_html=True
)
