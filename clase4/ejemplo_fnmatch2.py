import fnmatch
import os

patron = 'clase*.py'
print('Patrón :', patron)
print('*****')

ficheros = os.listdir('./')
print('Nombre: ', ficheros)
print ('Coinciden: ', fnmatch.filter(ficheros, patron))