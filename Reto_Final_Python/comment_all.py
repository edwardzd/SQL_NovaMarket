import json

file_path = '/Users/macbookpro/Developer/Learning/SQL/EXPLO_RA/NM_Galacticos_Antigravity_FINAL.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

comments_map = {
    "import os, pandas as pd, plotly, streamlit as st, openpyxl\n": 
        "# Traemos las herramientas: os (sistema), pandas (datos), plotly (gráficos), streamlit (web)\n",
    "df_raw = pd.read_excel('S01_Ventas_Novamarket_Datos_Sucios.xlsx'\n": 
        "# pd.read_excel lee el archivo de Excel. Lo guardamos en una variable llamada 'df_raw' (Dataframe Crudo)\n",
    "print(f\"  Total filas:               {len(df_raw)}\")\n":
        "# len() cuenta cuántas filas tiene nuestra tabla actualmente\n",
    "df = df_raw.drop_duplicates().reset_index(drop=True)\n": 
        "# ELIMINAR DUPLICADOS: drop_duplicates() borra filas idénticas.\n# reset_index(drop=True) reorganiza la numeración de las filas del 0 al 499.\n",
    "CIUDADES_VALIDAS = ['Bogotá','Medellín','Cali','Barranquilla','Cartagena','Leticia']\n":
        "# Creamos una lista con los nombres oficiales que aceptamos\n",
    "df['Ciudad'] = df['Ciudad'].str.strip().replace(ciudad_map)\n": 
        "# ESTANDARIZAR TEXTO: str.strip() elimina espacios. replace(ciudad_map) cambia lo malo por lo bueno.\n",
    "invalidas = df[~df['Ciudad'].isin(CIUDADES_VALIDAS)]['Ciudad'].unique()\n":
        "# Verificamos si quedó alguna ciudad que NO esté (~) en nuestra lista de ciudades válidas\n",
    "df['Categoria'] = df['Categoria'].str.strip().replace(cat_map)\n": 
        "# Aplicamos la misma lógica: quitamos espacios y usamos el diccionario cat_map para corregir.\n",
    "mediana_cat = df.groupby('Categoria')['Cantidad'].median()\n": 
        "# CALCULAR MEDIANA: groupby() agrupa por producto y median() saca el valor central de Cantidad.\n",
    "def imputar(row):\n":
        "# Creamos una función (regla) llamada 'imputar' que revisará cada fila individualmente\n",
    "    if pd.isna(row['Cantidad']):\n":
        "# pd.isna() pregunta: ¿Esta casilla de cantidad está vacía (nula)?\n",
    "        return mediana_cat[row['Categoria']]\n":
        "# Si está vacía, entregamos el valor de la mediana que le corresponde a esa categoría\n",
    "df['Cantidad'] = df.apply(imputar, axis=1).astype(int)\n": 
        "# RELLENAR NULOS: apply() ejecuta la función fila por fila. astype(int) convierte todo a números enteros.\n",
    "df['Ingreso_Total'] = df['Cantidad'] * df['Precio_Unitario'] * (1 - df['Descuento_pct'])\n": 
        "# FÓRMULA FINANCIERA: Ingreso = Cantidad * Precio * (100% - Porcentaje de Descuento)\n",
    "df['Costo_Total']   = df['Cantidad'] * df['Costo_Unitario']  + df['Costo_Envio']\n": 
        "# FÓRMULA FINANCIERA: Costo = (Cantidad * Costo Unitario) + Costo Fijo de Envío\n",
    "df['Utilidad_Neta'] = df['Ingreso_Total'] - df['Costo_Total']\n": 
        "# FÓRMULA FINANCIERA: Utilidad Neta = Lo que entró (Ingreso) - Lo que salió (Costo)\n",
    "leticia   = df[df['Ciudad'] == 'Leticia']\n": 
        "# FILTRO: Creamos una tabla nueva ('leticia') que solo contiene las ventas de Leticia.\n",
    "util_let  = leticia['Utilidad_Neta'].sum()\n": 
        "# SUMA: Sumamos toda la columna de Utilidad Neta de la tabla filtrada de Leticia.\n",
    "margen_let = util_let / ingr_let * 100\n":
        "# El margen se calcula dividiendo la utilidad sobre el ingreso total, multiplicado por 100 para dar %.\n",
    "if abs(util_let - (-79341.5)) < 1:\n":
        "# Validamos si la utilidad calculada es igual al número de oro (-79,342). abs() es el valor absoluto.\n",
    "bf  = df[df['Descuento_pct'] >= 0.40]\n":
        "# Creamos una tabla 'bf' filtrando solo las ventas que tuvieron 40% o más de descuento.\n",
    "nbf = df[df['Descuento_pct']  < 0.40]\n":
        "# Creamos una tabla 'nbf' (No Black Friday) con las ventas de menos del 40% de descuento.\n",
    "barr        = df[df['Ciudad']=='Barranquilla']['Utilidad_Neta'].sum()\n":
        "# Filtramos las ventas de Barranquilla y sumamos inmediatamente su utilidad neta.\n",
    "util_sim    = util_actual + barr\n":
        "# Simulamos el escenario: Utilidad de toda la empresa + otra vez la utilidad de Barranquilla (duplicar)\n",
    "cat = df.groupby('Categoria')[['Ingreso_Total','Utilidad_Neta']].sum()\n":
        "# Agrupamos todas las ventas por Categoría y sumamos sus Ingresos y Utilidades\n",
    "cat = cat.sort_values('Margen%', ascending=False)\n":
        "# sort_values() ordena la tabla de mayor a menor (ascending=False) basándose en el Margen%\n",
    "%%writefile dashboard_novamarket.py\n":
        "# MAGIC COMMAND: Esta instrucción toma todo el código debajo de ella y crea el archivo del Dashboard.\n",
    "import streamlit as st\n":
        "# Streamlit es la herramienta que convierte código Python en una página web interactiva.\n",
    "st.set_page_config(\n":
        "# Configuramos la pestaña del navegador: Título, ícono, y decimos que use toda la pantalla (wide).\n",
    "@st.cache_data\n":
        "# cache_data guarda los datos en memoria para que la página web cargue súper rápido al filtrar.\n",
    "def cargar():\n":
        "# Definimos una función llamada 'cargar' que va a leer el CSV limpio y prepararlo para los gráficos.\n",
    "df = cargar()\n":
        "# Ejecutamos la función cargar() y guardamos los datos listos en la variable 'df'\n",
    "st.sidebar.markdown(\"## 🔍 Filtros\")\n":
        "# sidebar crea un panel lateral en la página web. Añadimos un título 'Filtros'.\n",
    "ciudades   = st.sidebar.multiselect(\"Ciudad\",\n":
        "# Creamos una caja de selección múltiple en el panel lateral para elegir las Ciudades.\n",
    "dff = df[\n":
        "# Creamos una tabla 'dff' que filtrará los datos según lo que el usuario elija en la barra lateral.\n",
    "ventas   = dff['Ingreso_Total'].sum()\n":
        "# Sumamos todo el ingreso total de los datos filtrados para mostrarlo en el indicador superior.\n",
    "c1, c2, c3, c4 = st.columns(4)\n":
        "# st.columns() divide la pantalla en 4 columnas invisibles para acomodar nuestros indicadores (KPIs).\n",
    "c1.metric(\"💰 Ventas Totales\",     f\"${ventas:,.0f}\")\n":
        "# metric() crea esas cajas bonitas de números grandes. Aquí mostramos las Ventas Totales.\n",
    "ca, cb = st.columns([1.2, 1])\n":
        "# Dividimos la pantalla en 2 columnas: la izquierda (ca) un poco más ancha que la derecha (cb).\n",
    "fig1 = go.Figure(go.Bar(\n":
        "# plotly.graph_objects (go) nos permite crear gráficos interactivos. Aquí creamos un gráfico de Barras.\n",
    "st.plotly_chart(fig1, use_container_width=True, theme=None)\n":
        "# plotly_chart() toma el gráfico que creamos y lo dibuja en la página web de Streamlit.\n",
    "pv = dff.pivot_table(\n":
        "# pivot_table() funciona exactamente igual que una Tabla Dinámica de Excel.\n",
    "techo = st.slider(\"Descuento máximo permitido (%)\", 10, 50, 30, step=5)\n":
        "# st.slider() crea la barra deslizable interactiva para que el usuario juegue con los descuentos.\n"
}

for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        new_source = []
        for line in cell.get('source', []):
            # Check if this line is in our map (by starting with the target string or exactly matching)
            replaced = False
            for target, comment in comments_map.items():
                if line.startswith(target):
                    # Check if the comment is already there from previous run
                    if len(new_source) == 0 or new_source[-1] != comment:
                        new_source.append(comment)
                    new_source.append(line)
                    replaced = True
                    break
            if not replaced:
                new_source.append(line)
        
        # Clean up double comments if the previous add_comments.py left some 
        # Actually our map is appending before the line, let's filter out consecutive identical comments
        filtered_source = []
        for l in new_source:
            if not filtered_source or l != filtered_source[-1]:
                # check if it's an old comment that we are now replacing/improving
                if l.startswith("# ELIMINAR DUPLICADOS") and "drop_duplicates" in l:
                    pass # handled by checking next lines, let's just keep it simple and overwrite everything cleanly
                filtered_source.append(l)
                
        cell['source'] = new_source

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Comentarios globales agregados exitosamente.")
