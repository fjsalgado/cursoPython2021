import requests
import json
from datetime import datetime

# Módulo REQUESTS
# Ejemplo utilizando la API de Open Notify http://api.open-notify.org/
# Utiliza la función request.get() para conectarse a una API inexistente
response = requests.get("http://api.open-notify.org/esta-api-no-existe")
print(response.status_code)

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)

# Función response.json() devuelve datos utilizando la API
print(response.json())
print(type(response.json()))

# Módulo JSON
# Función creada para dar formato a los datos
def json_print(obj):
    texto = json.dumps(obj, sort_keys=True, indent=4)
    print(texto)
json_print(response.json())

# Utilizar parámetros en la obtención de datos
parametros_madrid = {
    "lat": 40.4167,
    "lon": -3.70325
}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parametros_madrid)
json_print(response.json())
pass_times = response.json()['response']
json_print(pass_times)

# Módulo DATETIME
# Extrae los datos de "risetime"
risetimes = []
for d in pass_times:
    time = d['risetime']
    risetimes.append(time)
print(risetimes)

# Presenta los datos con formato fecha
times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
