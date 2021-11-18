# Ejemplo clase
# Creando la clase
class Coche:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.capacidad_gasolina = 15
        self.nivel_gasolina = 0

    def gasolina_completo(self):
        self.nivel_gasolina = self.capacidad_gasolina
        print('El depósito de gasolina está lleno')
    
    def conducir(self):
        print(f'El {self.modelo} se está conduciendo.')

# Creando las instancias de la clase Coche
objeto_coche = Coche('SEAT','Ateca', '1.0')

# Acceder a los atributos de ese objeto
print(objeto_coche.marca)
print(objeto_coche.modelo)
print(objeto_coche.tipo)

# Llamando a los métodos de la clase
print()
objeto_coche.gasolina_completo()
objeto_coche.conducir()

###################################################################

# Herencia: extendiendo la clase
class CocheElectrico(Coche):
    # El método __init__() para crear una clase hija
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, tipo)
        self.battery_size = 100
        self.charge_level = 0

    # Agregar un nuevo método a la clase
    def cargar(self):
        self.nivel_carga = 100
        print('El coche está cargado.')

    # Sobrescribir un método del padre
    def gasolina_completo(self):
        print('El coche no tiene depósito de gasolina!')

# Usar el método padre e hijo
coche_electrico = CocheElectrico('Tesla', 'Modelo 3', 'Berlina')
print(coche_electrico.modelo)
coche_electrico.cargar()
coche_electrico.conducir()

# Mostrar la o las clases de la cual se está heredando
print(CocheElectrico.__mro__)