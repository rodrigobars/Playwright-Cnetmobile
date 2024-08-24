from typing import Optional

class Valor:
    def __init__(self, valorTotal: float, valorUnitario: Optional[float] = None):
        self.valorTotal = valorTotal
        self.valorUnitario = valorUnitario
        
    def __repr__(self):
        return str(vars(self))
    
    def to_dict(self):
        return vars(self)