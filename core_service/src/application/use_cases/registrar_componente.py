from domain.entities import Componente, EstadoEnum

class RegistrarComponenteUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, placa: str, nombre: str, tipo: str, codigo: str, estado: EstadoEnum):
        # 1. Verificar que el vehiculo exista
        vehiculo = self.repository.get_by_placa(placa)
        
        if not vehiculo:
            raise ValueError(f"El vehiculo con placa {placa} no existe.")
        
        # 2. Crear la entidad del dominio
        nuevo_componente = Componente(
            nombre=nombre,
            tipo=tipo,
            codigo_impreso=codigo,
            estado=estado
        )
        
        # 3. Guardar en la base de datos (pasando la placa para el vehiculo)
        return self.repository.save_componente(nuevo_componente, placa)