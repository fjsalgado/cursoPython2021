import os
import shutil

# Copiar ficheros situados en el mismo directorio
shutil.copy(src="quijote-ext01.txt", dst="quijote-ext02.txt")

# Copiar ficheros preservando los metadatos
shutil.copy2(src="quijote-ext01.txt", dst="quijote-ext03.txt")
