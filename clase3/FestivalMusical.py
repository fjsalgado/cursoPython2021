import datetime

# Ejemplo de clase y creación de una instancia de la misma
class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        # Inicializa los parámetros (similar a un constructor de java)
        # self habilita la disponibilidad del resto de objetos en la clase
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical
    
    def festival_metodo(self):
        # Método de instancia: Recibe instancia de self que hace referencia a la instancia que llama al método
        #   Pueden acceder y modificar los atributos del objeto.
        #   Pueden acceder a otros métodos.
        #   Dado que desde el objeto self se puede acceder a la clase con ` self.class`, también pueden modificar el estado de la clase
        print('El mejor festival es: ', self.nombre)

    @classmethod
    def valor_ticket(cls, valor):
        # Método de clase: A diferencia de los métodos de instancia, los métodos de clase reciben como argumento cls, que hace referencia a la clase. Por lo tanto, pueden acceder a la clase pero no a la instancia.
        #   No pueden acceder a los atributos de la instancia.
        #   Pero si pueden modificar los atributos de la clase.
        cls.valor_ticket = valor

    @staticmethod
    def dia_evento(dia):
        # Método estático: No aceptan como parámetro ni la instancia ni la clase. Es por ello por lo que no pueden modificar el estado ni de la clase ni de la instancia
        #   Pueden resultar útil para indicar que un método no modificará el estado de la instancia ni de la clase
        #   Se podrían ver como funciones normales, con la salvedad de que van ligadas a una clase concreta
        if dia.weekday() == 5 or dia.weekday() == 6:
            return print('es un final de semana')
        return print('es un dia laboral')

# Se crea una instancia de la clase FestivalMusical
festival1 = FestivalMusical('Creamfields', 'UK', 'Dance')
festival2 = FestivalMusical('Primavera Sound', 'ES', 'Dance')

# Se accede a los atributos del objeto
festival2.festival_metodo()
print('Festival1 -> Estilo musical:', festival1.estilo_musical)
festival1.nombre = 'Sonisphere'
print('Festival1 -> Nuevo nombre:', festival1.nombre.upper())
del festival1

# Muestra la posición del objeto de la clase FestivalMusical en la memoria
print(festival2)

FestivalMusical.valor_ticket(50)
print(FestivalMusical.valor_ticket) # Accede a la clase
print(festival2.valor_ticket) # Accede a la instancia

dia1 = datetime.date(2021, 11, 9)
FestivalMusical.dia_evento(dia1)
