import json

file_path = '/Users/macbookpro/Developer/Learning/SQL/EXPLO_RA/NM_Galacticos_Antigravity_FINAL.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Define replacements
replacements = {
    "df = df_raw.drop_duplicates().reset_index(drop=True)\n": [
        "# ELIMINAR DUPLICADOS: drop_duplicates() borra filas idénticas.\n",
        "# reset_index(drop=True) reorganiza la numeración de las filas del 0 al 499.\n",
        "df = df_raw.drop_duplicates().reset_index(drop=True)\n"
    ],
    "df['Ciudad'] = df['Ciudad'].str.strip().replace(ciudad_map)\n": [
        "# ESTANDARIZAR TEXTO: str.strip() elimina espacios al inicio y final.\n",
        "# replace(ciudad_map) busca los nombres malos y los cambia por los buenos según el diccionario.\n",
        "df['Ciudad'] = df['Ciudad'].str.strip().replace(ciudad_map)\n"
    ],
    "df['Categoria'] = df['Categoria'].str.strip().replace(cat_map)\n": [
        "# str.strip() quita espacios, replace(cat_map) aplica el diccionario para corregir nombres.\n",
        "df['Categoria'] = df['Categoria'].str.strip().replace(cat_map)\n"
    ],
    "mediana_cat = df.groupby('Categoria')['Cantidad'].median()\n": [
        "# CALCULAR MEDIANA: groupby('Categoria') agrupa los datos por tipo de producto.\n",
        "# median() calcula el valor central estadístico de la cantidad vendida para cada grupo.\n",
        "mediana_cat = df.groupby('Categoria')['Cantidad'].median()\n"
    ],
    "df['Cantidad'] = df.apply(imputar, axis=1).astype(int)\n": [
        "# RELLENAR NULOS: apply() ejecuta la función 'imputar' fila por fila (axis=1).\n",
        "# astype(int) convierte el resultado final a números enteros.\n",
        "df['Cantidad'] = df.apply(imputar, axis=1).astype(int)\n"
    ],
    "df['Ingreso_Total'] = df['Cantidad'] * df['Precio_Unitario'] * (1 - df['Descuento_pct'])\n": [
        "# FÓRMULA FINANCIERA: Ingreso = Cantidad * Precio * (100% - Porcentaje de Descuento)\n",
        "df['Ingreso_Total'] = df['Cantidad'] * df['Precio_Unitario'] * (1 - df['Descuento_pct'])\n"
    ],
    "df['Costo_Total']   = df['Cantidad'] * df['Costo_Unitario']  + df['Costo_Envio']\n": [
        "# FÓRMULA FINANCIERA: Costo = (Cantidad * Costo Unitario) + Costo Fijo de Envío\n",
        "df['Costo_Total']   = df['Cantidad'] * df['Costo_Unitario']  + df['Costo_Envio']\n"
    ],
    "df['Utilidad_Neta'] = df['Ingreso_Total'] - df['Costo_Total']\n": [
        "# FÓRMULA FINANCIERA: Utilidad Neta = Lo que entró (Ingreso) - Lo que salió (Costo)\n",
        "df['Utilidad_Neta'] = df['Ingreso_Total'] - df['Costo_Total']\n"
    ],
    "leticia   = df[df['Ciudad'] == 'Leticia']\n": [
        "# FILTRO: Creamos una tabla nueva ('leticia') que solo contiene las filas donde la Ciudad es Leticia.\n",
        "leticia   = df[df['Ciudad'] == 'Leticia']\n"
    ],
    "util_let  = leticia['Utilidad_Neta'].sum()\n": [
        "# SUMA: Sumamos toda la columna de Utilidad Neta de la tabla filtrada de Leticia.\n",
        "util_let  = leticia['Utilidad_Neta'].sum()\n"
    ]
}

for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        new_source = []
        for line in cell.get('source', []):
            replaced = False
            for target, replacement in replacements.items():
                if line == target:
                    new_source.extend(replacement)
                    replaced = True
                    break
            if not replaced:
                new_source.append(line)
        cell['source'] = new_source

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Comentarios agregados exitosamente al Notebook.")
