# Busca a partir del carácter 18 e imprime los 42 caracteres siguientes
with open("quijote-ext01.txt", 'r') as file:
    file.seek(18)
    contenido = file.read(42)
    print(contenido)