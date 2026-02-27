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

    def update_km(self, placa: str, nuevo_km: int): # type: ignore
        vehiculo = self.get_by_placa(placa)
        if vehiculo:
            vehiculo.kilometraje_total = nuevo_km
        
        return vehiculo
    
    def save_medicion(self, medicion: Medicion): # type: ignore
        if not hasattr(self, "mediciones"):
            self.mediciones = []
        self.mediciones.append(self.medicion) # type: ignore
        return medicion # type: ignore