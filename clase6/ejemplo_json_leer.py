# Leer un fichero JSON
import json
with open('ejemplo_json_fichero.json') as fichero:
# .loads (decode) toma un string como input y devuelve un diccionario
datos = json.loads(fichero.read())
print(datos)
# Lee solo un dato del fichero
print(datos["Nombre"])
##
Exporta “datos” a un fichero .json
with open('ejemplo_persona_JSON.txt', 'w') as json_fichero:
json.dump(datos, json_fichero)