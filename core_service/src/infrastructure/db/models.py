from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class VehiculoModel(Base):
    __tablename__ = "vehiculos"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    placa = Column(String, unique=True, nullable=False)
    marca = Column(String)
    modelo = Column(String)
    anio = Column(Integer)
    kilometraje_total = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)
    
class MedicionModel(Base):
    __tablename__ = "mediciones"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    componente_id = Column(String, nullable=False)
    valor_metrico = Column(Float) # type: ignore
    kilometraje_momento = Column(Integer)
    fecha_registro = Column(DateTime, default=datetime.now)
    vehiculo_placa = Column(String, ForeignKey("vehiculos.placa"))
    