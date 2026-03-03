from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
import uuid
from domain.entities import EstadoEnum, TipoVehiculoEnum

Base = declarative_base()

class VehiculoModel(Base):
    __tablename__ = "vehiculos"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    placa = Column(String, unique=True, nullable=False)
    marca = Column(String)
    modelo = Column(String)
    anio = Column(Integer)
    tipo_vehiculo = Column(SQLEnum(TipoVehiculoEnum), default=TipoVehiculoEnum.AUTO)
    kilometraje = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)

class ComponenteModel(Base):
    __tablename__ = "componentes"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String, nullable=False)
    tipo = Column(String)
    codigo = Column(String, unique=True, nullable=True)
    estado = Column(SQLEnum(EstadoEnum), default=EstadoEnum.NUEVO)
    vehiculo_placa = Column(String, ForeignKey("vehiculos.placa"))
    foto_url = Column(String, nullable=True)
    mediciones = relationship("MedicionModel", backref="componente")
    
class MedicionModel(Base):
    __tablename__ = "mediciones"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    componente_id = Column(String, ForeignKey("componentes.id"), nullable=False)
    valor_metrico = Column(Float) # type: ignore
    kilometraje = Column(Integer)
    fecha_registro = Column(DateTime, default=datetime.now)
    foto_url = Column(String, nullable=True)
    vehiculo_placa = Column(String, ForeignKey("vehiculos.placa"))
    