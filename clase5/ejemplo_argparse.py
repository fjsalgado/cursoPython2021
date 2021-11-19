import argparse
import os
import sys

# Crea el parser
mi_parser = argparse.ArgumentParser(prog='ejemplo_argparse.py', \
    description='Listado del contenido del directorio', epilog='Muchas gracias')

# Agrega los argumentos
mi_parser.add_argument('Path', metavar='Ruta', type=str, help='La ruta al directorio')

# Ejecuta el método parse_args()
args = mi_parser.parse_args()
dir_ruta = args.Path

if not os.path.isdir(dir_ruta):
    print('Este directorio no existe')
    sys.exit()

print('\n'.join(os.listdir(dir_ruta)))

# Desde línea de comandos se lanzaría lo siguiente:
# python ejemplo_argparse.py directorio => muestra nombres de ficheros
# python ejemplo_argparse.py -h => muestra ayuda para lanzar el script