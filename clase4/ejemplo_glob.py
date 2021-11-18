import glob

# Listado de archivos en una carpeta
for fichero in glob.glob('../*'):
    print(fichero)
