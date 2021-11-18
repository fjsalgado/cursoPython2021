#Ejemplo de uso de la biblioteca re (permite usar EXPRESIONES REGULARES)
import re
# Encontrar coincidencias
texto = "Hoy es un día magnífico y maravilloso"
exp_reg = re.search("^Hoy.*oso$", texto)
print(exp_reg)

exp_reg2 = re.findall("ma", texto)
print(exp_reg2)

# Reemplazar espacio vacío
exp_reg3 = re.sub("\s", "_", texto)
print(exp_reg3)
