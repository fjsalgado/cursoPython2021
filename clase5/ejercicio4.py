#CLASE EMPLEADOS
#1.- Crear una clase "empleados" en un fichero denominado clase_empleados.py
#2.- Crear una clase que herede de empleados denominada "aptitudes" con: lenguajes(programación), so(sistemas operativos que domina), e idioma.
#3.- Crear dos empleados utilizando esas clases
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class EmpleadoConAptitudes(Empleado):
    def __init__(self, nombre, lenguajes, so, idioma):
        super().__init__(nombre)
        self.lenguajes = lenguajes
        self.so = so
        self.idioma = idioma
        
empleado_con_aptitudes_1 = EmpleadoConAptitudes('Jose','Python, Bash','Unix, Windows','Castellano, Inglés')
empleado_con_aptitudes_2 = EmpleadoConAptitudes('Pepe','C++, PHP', 'Red Hat, Ubuntu','Swahili')
print(f'EmpleadoConAptitudes1: Lenguajes --> {empleado_con_aptitudes_1.lenguajes}')
print(f'EmpleadoConAptitudes2: Idioma --> {empleado_con_aptitudes_2.idioma}')
# Propiedad de la clase padre
print(f'EmpleadoConAptitudes1: Nombre --> {empleado_con_aptitudes_1.nombre}')
