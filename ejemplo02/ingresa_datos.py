from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Matricula, Estudiante, Modulo

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Estudiante 
estudiante1 = Estudiante(nombre="Tony", apellido="García")
estudiante2 = Estudiante(nombre="Annette", apellido="García")
estudiante3 = Estudiante(nombre="David", apellido="Phillips")

# Se crean objeto de tipo Modulo
m1 = Modulo(nombre="Primero")
m2 = Modulo(nombre="Segundo")
m3 = Modulo(nombre="Tercero")

# Se crean objetos de tipo Matricula
matricula1 = Matricula(periodo="periodo aa2021", modulo=m1, estudiante=estudiante1)
matricula2 = Matricula(periodo="periodo aa2020", modulo=m2, estudiante=estudiante1)
matricula3 = Matricula(periodo="periodo aa2019", modulo=m3, estudiante=estudiante1)

matricula4 = Matricula(periodo="periodo aa2021", modulo=m1, estudiante=estudiante2)
matricula5 = Matricula(periodo="periodo aa2020", modulo=m2, estudiante=estudiante2)
matricula6 = Matricula(periodo="periodo aa2019", modulo=m3, estudiante=estudiante2)

# se agrega los objetos
# a la sesión
session.add(estudiante1)
session.add(estudiante2)
session.add(estudiante3)
session.add(m1)
session.add(m2)
session.add(m3)
session.add_all([matricula1, matricula2, matricula3, matricula4, matricula5, \
        matricula6])

# se confirma las transacciones
session.commit()
