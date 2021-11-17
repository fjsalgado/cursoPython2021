# Ejemplo de función
def multiplicar(x, y):
    return x * y
print(multiplicar(5, 6))

# La misma función con lambdas
multiplicar2 = lambda x, y: x * y
print(multiplicar2(5, 6))

# Ejemplo de lambda sacado de PEP 498 (Python Enhancement Proposals)
print(f'{(lambda x: x*5)(6)}')
