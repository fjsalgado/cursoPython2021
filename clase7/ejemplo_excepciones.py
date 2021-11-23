def funcion_excepciones():
    try:
        print(10/1)
    except ZeroDivisionError:
        print("Error. No se puede dividir por cero.")
    else:
        #pass
        print("La excepción no ha ocurrido")
    finally:
        print("Finalizada la gestión de excepciones")

funcion_excepciones()