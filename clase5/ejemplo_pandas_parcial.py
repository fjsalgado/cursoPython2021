# Ejemplo exportar fichero con formato .xlsx
import pandas as pd

# Se crea el dataframe con pandas de un fichero Excel
dataframe_excel = pd.read_excel("catalogo_cf.xlsx")
print(dataframe_excel)

# Selecciona la primera y la cuarta columna
print(dataframe_excel.iloc[:, [0, 3]])

# se exporta a excel
dataframe_excel.iloc[:, [0, 3]].to_excel('catalogo_cf_resumen.xlsx', index=False)
