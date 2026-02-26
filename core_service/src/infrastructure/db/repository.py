from domain.entities import Vehiculo
from domain.interfaces import IVehiculoRepository

class MemoryVehiculoRepository(IVehiculoRepository):
    def __init__(self):
        self.vehiculos = []
        
    def save(self, vehiculo: Vehiculo): # type: ignore
        self.vehiculos.append(vehiculo) # type: ignore
        return vehiculo

    def get_by_placa(self, placa: str) -> Vehiculo:
        for v in self.vehiculos: # type: ignore
            if v.placa == placa.upper(): # type: ignore
                return v # type: ignore
            
        return None # type: ignore