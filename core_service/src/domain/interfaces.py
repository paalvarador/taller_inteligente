from abc import ABC, abstractmethod
from .entities import Vehiculo, Medicion

class IVehiculoRepository(ABC):
    @abstractmethod
    def save_vehiculo(self, vehiculo: Vehiculo):
        pass
    
    @abstractmethod
    def get_by_placa(self, placa: str) -> Vehiculo:
        pass
    
    @abstractmethod
    def update_km(self, placa: str, nuevo_km: int):
        pass


class IMedicionRepository(ABC):
    @abstractmethod
    def save_medicion(self, medicion: Medicion, placa: str):
        pass
    
    @abstractmethod
    def get_by_vehiculo(self, placa: str) -> list[Medicion]:
        pass
    
    
