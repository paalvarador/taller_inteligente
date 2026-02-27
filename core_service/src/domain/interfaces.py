from abc import ABC, abstractmethod
from .entities import Vehiculo, Medicion

class IVehiculoRepository(ABC):
    @abstractmethod
    def save(self, vehiculo: Vehiculo):
        pass
    
    @abstractmethod
    def get_by_placa(self, placa: str) -> Vehiculo:
        pass
    
    @abstractmethod
    def update_km(self, placa: str, nuevo_km: int):
        pass


class IMedicionRepository(ABC):
    @abstractmethod
    def save(self, medicion: Medicion):
        pass
    
    
