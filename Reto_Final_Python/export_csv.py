import pandas as pd
import os

excel_path = '/Users/macbookpro/Developer/Learning/SQL/EXPLO_RA/S01_Ventas_Novamarket_Datos_Sucios.xlsx'
out_dir = '/Users/macbookpro/Library/CloudStorage/GoogleDrive-edwardzd@gmail.com/Mi unidad/2.Profesional/2.1 Laboral/21.Unicomfacauca_24_I/Análisis de datos/Reto/Reto_Final_SQL'
os.makedirs(out_dir, exist_ok=True)
csv_path = os.path.join(out_dir, 'S01_Ventas_Novamarket_Datos_Sucios.csv')

# Load the excel, skip first 2 decorative rows (header=2)
df = pd.read_excel(excel_path, sheet_name='Ventas_Datos_Sucios', header=2)
df.to_csv(csv_path, index=False)
print("CSV exported successfully to:", csv_path)
