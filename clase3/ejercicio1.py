# Ejercicio 1: Crear un programa que le pregunte al usuario su nombre y edad y le muestre el año en que cumplirá los 100 años. 
import datetime

anhoActual = date.today().year

nombre = input("Indique su nombre: ")
edad = input("Indique su edad: ")
calculo = int(anhoActual) + (100 - int(edad))
print(nombre + ", cumplirás 100 años en el", calculo)
