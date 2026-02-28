from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from enum import Enum
import uuid

# Enums
class EstadoEnum(str, Enum):
    NUEVO = "Nuevo"
    BUENO = "Bueno"
    REGULAR = "Regular"
    CRITICO = "Crítico"
    DANADO = "Dañado"

class TipoVehiculoEnum(str, Enum):
    AUTO = "Auto"
    MOTO = "Moto"
    CAMIONETA = "Camioneta"
    CAMION = "Camion"

@dataclass
class Medicion:
    """Representa una toma de datos de un componente (ej. mm de una llanada)"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    componente_id: str = ""
    valor_metrico: float = 0.0 # mm de profundidad o voltaje
    kilometraje: int = 0
    fecha_registro: datetime = field(default_factory=datetime.now)
    foto_url: Optional[str] = None

@dataclass
class Componente:
    """Representa una pieza del auto: Llanta, Bateria, etc."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    codigo_impreso: str = "" # El código de la máquina
    tipo: str = "llanta" # 'llanta', 'bateria', 'frenos'
    posicion: str = "" # 'del_der', 'tras_izq', etc
    mediciones: List[Medicion] = field(default_factory=list) # type: ignore
    
@dataclass
class Vehiculo:
    """El ente principal del sistema de talleres"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    placa: str = ""
    marca: str = ""
    modelo: str = ""
    anio: int = 0
    tipo_vehiculo: TipoVehiculoEnum = TipoVehiculoEnum.AUTO # 'moto', 'auto', 'camioneta'
    kilometraje: int = 0
    componentes: List[Componente] = field(default_factory=list) # type: ignore
    