#Ejercicio 3: Escribir un programa que tome una lista de números (entre 5 y 10 números) 
# y haga una lista con el primero y el último de los elementos; otra con el valor máximo y mínimo, y las muestre en pantalla.
import random

max_elementos = 5
lista = []

for i in range(0, max_elementos):
    #n = input("Indique un número: ")
    #lista.append(int(n))
    lista.append(random.randint(1, 100))

print("lista =>", lista)
print("[lista(0), lista(1)] =>", [lista[0], lista[max_elementos-1]])
print("[max(lista), min(lista)] =>", [max(lista), min(lista)])
