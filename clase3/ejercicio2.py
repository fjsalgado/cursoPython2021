# Ejercicio 2: Preguntar al usuario un número y mostrar si es par o impar. Si el número es múltiple de 4 imprimir el mensaje apropiado al usuario.
numero = input("Indique un número: ")
m2 = int(numero) % 2 == 0
m4 = int(numero) % 4 == 0
print(numero, "es", "par" if m2 else "impar")
print(numero, "es" if m4 else "no es", "múltiplo de 4")