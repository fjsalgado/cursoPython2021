import datetime
from FestivalMusical import FestivalMusical

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

#FestivalMusical.valor_ticket(50)
#print(FestivalMusical.valor_ticket) # Accede a la clase
print(festival2.valor_ticket) # Accede a la instancia

dia1 = datetime.date(2021, 11, 9)
#FestivalMusical.dia_evento(dia1)