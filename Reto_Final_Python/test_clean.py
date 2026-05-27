import pandas as pd
df = pd.read_excel('S03_Ventas_Datos_Sucios_v4.xlsx', skiprows=2)
df['Categoria'] = df['Categoria'].str.upper().str.strip()
df['Categoria'] = df['Categoria'].replace({'LAPTOP': 'LAPTOPS'})
print('Categories:', df['Categoria'].unique())

df['Ciudad'] = df['Ciudad'].str.upper().str.strip()
df['Ciudad'] = df['Ciudad'].replace({
    'BOGOTA': 'BOGOTÁ', 
    'MEDELLIN': 'MEDELLÍN',
    'BARRANQILLA': 'BARRANQUILLA'
})
df['Ciudad'] = df['Ciudad'].str.title()
print('Cities:', df['Ciudad'].unique())
