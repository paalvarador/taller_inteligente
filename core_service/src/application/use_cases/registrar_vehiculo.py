from domain.entities import Vehiculo
from domain.interfaces import IVehiculoRepository

class RegistrarVehiculoUseCase:
    def __init__(self, vehiculo_repo: IVehiculoRepository):
        self.vehiculo_repo = vehiculo_repo
        
    def execute(self, placa: str, marca: str, modelo: str, anio: int):
        # 1. Regla de negocio: Validar que la placa no este vacia
        if not placa:
            raise ValueError("La placa es obligatoria")
    
        # 2. Verificar si ya existe (Evitar duplicados)
        vehiculo_existente = self.vehiculo_repo.get_by_placa(placa)
        if vehiculo_existente:
            return vehiculo_existente # Si ya existe, solamente se lo devuelve
        
        # 3. Crear la entidad si es nuevo
        nuevo_vehiculo = Vehiculo(
            placa=placa.upper(),
            marca=marca,
            modelo=modelo,
            anio=anio
        )
        
        # 4. Guardar
        return self.vehiculo_repo.save(nuevo_vehiculo)