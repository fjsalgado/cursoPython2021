# Ejemplo 1
i = 1
while i <= 1000:
    print(i)
    i = 5 * i + 1
print("Programa terminado")

# Ejemplo 2
# Fibonacci series: the sum of two elements defines the next
a, b = 0, 1
while a < 1000:
    print(a)
    a, b = b, a+b
