# Fichero para consultar datos en la DB: fichero_sql_query.py
from sqlalchemy.orm import sessionmaker
from fichero_sql_tablas import Estudiante, create_engine

engine = create_engine('sqlite:///estudiantes.db', echo=True)

# Crea una sesion
Session = sessionmaker(bind=engine)
session = Session()

# Selección de todos los objetos ordenados por id
for Estudiante1 in session.query(Estudiante).order_by(Estudiante.id):
    print(Estudiante1.nombre, Estudiante1.apellido1, Estudiante1.apellido2)

# Selección de objetos filtrados por un campo
for Estudiante2 in session.query(Estudiante).filter(Estudiante.universidad == 'UPC'):
    print(Estudiante2.nombre, Estudiante2.apellido1, Estudiante2.apellido2)
