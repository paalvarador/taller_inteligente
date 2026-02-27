from sqlalchemy.orm import Session
from domain.entities import Vehiculo, Medicion
from domain.interfaces import IVehiculoRepository, IMedicionRepository
from .models import VehiculoModel, MedicionModel

class PostgresRepository(IVehiculoRepository, IMedicionRepository):
    def __init__(self, db: Session):
        self.db = db
        
    def save_vehiculo(self, vehiculo: Vehiculo): # type: ignore
        db_vehiculo = VehiculoModel(
            id=vehiculo.id,
            placa=vehiculo.placa,
            marca=vehiculo.marca,
            modelo=vehiculo.modelo,
            anio=vehiculo.anio,
            kilometraje_total=vehiculo.kilometraje_total
        )
        self.db.add(db_vehiculo)
        self.db.commit()
        self.db.refresh(db_vehiculo)
        return vehiculo

    def get_by_placa(self, placa: str):
        return self.db.query(VehiculoModel).filter(VehiculoModel.placa == placa.upper()).first()

    def update_km(self, placa: str, nuevo_km: int):
        db_vehiculo = self.get_by_placa(placa)
        if db_vehiculo:
            db_vehiculo.kilometraje_total = nuevo_km # type: ignore
            self.db.commit()
        return db_vehiculo

    def save_medicion(self, medicion: Medicion, placa: str): # type: ignore
        db_medicion = MedicionModel(
            id=medicion.id,
            componente_id=medicion.componente_id,
            valor_metrico=medicion.valor_metrico,
            kilometraje_momento=medicion.kilometraje_momento,
            vehiculo_placa=placa.upper()
        )
        self.db.add(db_medicion)
        self.db.commit()
        return medicion