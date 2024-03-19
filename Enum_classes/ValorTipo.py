from Enum_classes.Valor import Valor
from typing import Optional

class ValorTipo:
    def __init__(self, valorCalculado: dict, valorInformado: Optional[float] = None):
        self.valorCalculado = Valor(**valorCalculado).to_dict()
        self.valorInformado = valorInformado
        
    def __repr__(self):
        return str(vars(self))
    
    def to_dict(self):
        return vars(self)