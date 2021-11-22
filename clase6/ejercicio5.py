'''
Python Manipular ficheros en Python

1.- Descargar de Datos.gob.es los ficheros: Tabla de INE base Formación Bruta de Capital Fijo por comunidades y ciudades autónomas ramas de actividad y periodo.
http://www.ine.es/jaxi/files/_px/es/csv_c/t35/p010/fbcf/01001.csv_c

Crear el/los scripts correspondientes para:
1.- Crear una copia y luego convertir el fichero .csv a .tsv
2.- Crear un directorio y mover la copia del fichero .csv dentro
3.- Escribir en un nuevo fichero las primeras 100 líneas del fichero .tsv 
4.- Exportar las primeras 5 columnas del fichero en formato .xlsx a un nuevo fichero
'''
import os
import pandas as pd 
import shutil
from itertools import *
from pathlib import Path

# 1.- Crear una copia y luego convertir el fichero .csv a .tsv
shutil.copy(src="data.csv", dst="data_copy.csv")
leer_csv = pd.read_csv('data.csv', escapechar='\\', encoding="UTF-8")
with open('data.tsv', 'w', encoding="UTF-8") as write_tsv:
    write_tsv.write(leer_csv.to_csv(sep='\t', index=False))

#2.- Crear un directorio y mover la copia del fichero .csv dentro
carpeta_dest = Path("ej5")
if not carpeta_dest.exists():
    os.makedirs(carpeta_dest)
shutil.move(src="data_copy.csv", dst="ej5/data_copy.csv")

# 3.- Escribir en un nuevo fichero las primeras x líneas del fichero .tsv 
contenido = pd.read_csv('data.tsv', escapechar='\\', nrows=5)
with open("data_cut.tsv", 'w') as file:
    file.write(contenido.to_csv(sep='\t', index=False))

# 4.- Exportar las primeras 5 columnas del fichero en formato .xlsx a un nuevo fichero
leer_fichero = pd.read_csv(r'./data.csv', encoding="ISO-8859-1")
leer_fichero.to_excel(r'./data.xlsx', index=None, header=True)
