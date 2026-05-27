import pandas as pd
df = pd.read_excel('S01_Ventas_Novamarket_Datos_Sucios.xlsx', skiprows=2)
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
