from domain.entities import Vehiculo
from domain.interfaces import IVehiculoRepository

class RegistrarVehiculoUseCase:
    def __init__(self, vehiculo_repo: IVehiculoRepository):
        self.vehiculo_repo = vehiculo_repo
        
    def execute(self, placa: str, marca: str, modelo: str, anio: int, kilometraje: int): # type: ignore
        # 1. Regla de negocio: Validar que la placa no este vacia
        if not placa:
            raise ValueError("La placa es obligatoria")

        if kilometraje is None or kilometraje < 0: # type: ignore
            raise ValueError("El kilometraje inicial es obligatorio y debe ser mayor o igual a 0")
    
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
        return self.vehiculo_repo.save_vehiculo(nuevo_vehiculo)