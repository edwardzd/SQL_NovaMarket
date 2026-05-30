import json

with open('/Users/macbookpro/Developer/Learning/SQL/Reto_Final_Python/NM_Galacticos_Antigravity_FINAL.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    source = cell.get('source', [])
    for i in range(len(source)):
        if "import pandas as pd" in source[i]:
            if "import os" not in "".join(source):
                source[i] = "import pandas as pd\nimport os\n"
                
        if "df = pd.read_csv('S01_Ventas_Novamarket_Datos_Limpios.csv')" in source[i]:
            source[i] = source[i].replace(
                "df = pd.read_csv('S01_Ventas_Novamarket_Datos_Limpios.csv')",
                "current_dir = os.path.dirname(os.path.abspath(__file__))\n    csv_path = os.path.join(current_dir, 'S01_Ventas_Novamarket_Datos_Limpios.csv')\n    df = pd.read_csv(csv_path)"
            )
            
    cell['source'] = source

with open('/Users/macbookpro/Developer/Learning/SQL/Reto_Final_Python/NM_Galacticos_Antigravity_FINAL.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook path logic updated.")
