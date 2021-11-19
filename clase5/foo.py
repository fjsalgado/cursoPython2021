#-*- coding: utf-8 -*-
# Ejemplo variables __name__ y __main__
# Fichero foo.py
import math

print("Antes import")

print("Antes función A")
def funcionA():
    print("Función A")

print("Antes función B")
def funcionB():
    print("Función B: {}".format(math.sqrt(100)))

print("Antes del control __name__")
print("__name__ =>", __name__)
if __name__ == "__main__":
    # Este código solo se ejecutaría si se ejecuta desde el propio fichero
    # Si se importa como módulo de otro fichero este código nunca se ejecutaría
    # Protegería este código para que no se ejecute al importarse como módulo de otro fichero
    funcionA()
    funcionB()
print("Después del control __name__")
