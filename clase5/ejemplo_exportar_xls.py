import pandas as pd

# Convierte un fichero con formato .csv a .xlsx
leer_fichero = pd.read_csv(r'./catalogo_cf.csv', encoding="ISO-8859-1")
leer_fichero.to_excel(r'./catalogo_cf.xlsx', index=None, header=True)

