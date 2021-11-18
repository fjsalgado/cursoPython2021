entrada = \
"""Primera parte del ingenioso hidalgo don Quijote de la Mancha

"""

# Creamos un fichero y pegamos el texto de la variable entrada
with open("quijote-ext01.txt", 'x') as file:
    file.write(entrada)