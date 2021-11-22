import json

# Ejemplo de string en JSON
persona = '{"nombre": "Juan", "lenguajes": ["Python", "Shellscripts"]}'
print(persona)
print("Tipo:", type(persona))

# Parsing usando el método json.loads()
# Crea un diccionario en python
persona_dic = json.loads(persona)
print(persona_dic['lenguajes'])
print("Tipo:", type(persona_dic))

# Convierte diccionario a JSON
# .dumps (encode) toma un diccionario como input y devuelve un string
persona_json = json.dumps(persona_dic)
print(persona_json)
print("Tipo:", type(persona_json))
