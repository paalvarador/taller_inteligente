from domain.interfaces import IMedicionRepository

class ObtenerHistorialUseCase:
    def __init__(self, medicion_repo: IMedicionRepository):
        self.medicion_repo = medicion_repo
    
    def execute(self, placa: str): # type: ignore
        mediciones = self.medicion_repo.get_by_vehiculo(placa)
        
        if not mediciones:
            return [] # type: ignore
        
        return mediciones