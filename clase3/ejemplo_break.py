# Ejemplo break
# Verifica si un número es primo
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equivale a', x, '*', n//x)
            break
    else:
        # El bucle sigue sin encontrar un factor
        print(n, 'es un número primo')

# Las sentencias de bucle pueden tener una cláusula else que es ejecutada cuando el bucle
# termina, después de agotar el iterable (con for) o cuando la condición se hace falsa (con
# while), pero NO cuando el bucle se termina con la sentencia break.