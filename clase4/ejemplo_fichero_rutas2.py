#Otros ejemplos leyendo de un directorio en la actual ruta, y de un directorio superior:
import os
from pathlib import Path

# Lee del directorio "clase4"
fichero_path = Path("../clase4", "quijote-ext01.txt")
print("[[CONTENIDO DE quijote-ext01.txt]]")
with fichero_path.open('r') as file:
    print(file.read())

# Lee del directorio superior
print("[[CONTENIDO DE pyvenv.cfg]]")
fichero_path = Path(os.pardir, "pyvenv.cfg")
with fichero_path.open('r') as file:
    print(file.read())
