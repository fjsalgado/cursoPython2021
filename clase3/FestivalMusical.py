# Ejemplo de clase y creación de una instancia de la misma
class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        # Inicializa los parámetros (similar a un constructor de java)
        # self habilita la disponibilidad del resto de objetos en la clase
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical
    
    def festival_metodo(self):
        print('El mejor festival es: ', self.nombre)

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