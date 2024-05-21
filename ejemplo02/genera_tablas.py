from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)
	
Base = declarative_base()

class Matricula(Base):
    __tablename__ = 'matricula'
    estudiante_id = Column(Integer, ForeignKey('estudiante.id'), primary_key=True)
    modulo_id = Column(Integer, ForeignKey('modulo.id'), primary_key=True)
    periodo = Column(String(50), nullable=False)
    modulo = relationship("Modulo", back_populates="estudiantes")
    estudiante = relationship("Estudiante", back_populates="modulos")

    def __repr__(self):
        return "Matricula: estudiante=%s\n modulo=%s\n"% (
                          self.estudiante,
                          self.modulo)

class Estudiante(Base):
    __tablename__ = 'estudiante'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    modulos = relationship("Matricula", back_populates="estudiante")

    def __repr__(self):
        return "Estudiante: nombre=%s - apellido=%s"% (
                          self.nombre,
                          self.apellido)

class Modulo(Base):
    __tablename__ = 'modulo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    estudiantes = relationship("Matricula", back_populates="modulo")

    def __repr__(self):
        return "Modulo: nombre=%s"% (
                          self.nombre)



Base.metadata.create_all(engine)
