# Fichero para consultar datos en la DB: fichero_sql_query.py
from sqlalchemy.orm import sessionmaker
from fichero_sql_tablas import Estudiante, create_engine

engine = create_engine('sqlite:///estudiantes.db', echo=True)

# Crea una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Selección de todos los objetos ordenados por id
for e in session.query(Estudiante).order_by(Estudiante.id):
    print(e.nombre, e.apellido1, e.apellido2)

# Selección de objetos filtrados por un campo
for e in session.query(Estudiante).filter(Estudiante.universidad == 'UPC'):
    print(e.nombre, e.apellido1, e.apellido2)
