from domain.entities import Medicion
from domain.interfaces import IMedicionRepository, IVehiculoRepository

class RegistrarMedicionUseCase:
    def __init__(self, medicion_repo: IMedicionRepository, vehiculo_repo: IVehiculoRepository):
        self.medicion_repo = medicion_repo
        self.vehiculo_repo = vehiculo_repo
    
    def execute(self, codigo_neumatico: str, valor_mm: float, kilometraje: int, placa: str):
        # 1. Vallidar que el kilometraje actual no sea menor al ultimo registrado
        vehiculo = self.vehiculo_repo.get_by_placa(placa)
        if not vehiculo:
            raise ValueError("El vehículo no existe.")
        
        if kilometraje < vehiculo.kilometraje_total:
            raise ValueError(f"Kilometraje inválido. El último registrado fue {vehiculo.kilometraje_total} km.")
        
        # 2. Crear la entidad de la medicion
        nueva_medicion = Medicion(
            componente_id=codigo_neumatico,
            valor_metrico=valor_mm,
            kilometraje_momento=kilometraje
        )
        
        # 3. Guardar la medicion
        self.medicion_repo.save_medicion(nueva_medicion, placa)
        
        # 4. Actualizar el kilometraje global del vehiculo
        self.vehiculo_repo.update_km(placa, kilometraje)
        
        return nueva_medicion