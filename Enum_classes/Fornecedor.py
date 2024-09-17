from Enum_classes.Enum import FornecedorEnum
from typing import Optional

class Fornecedor:
    def __init__(self,
                 identificacao: str,
                 nome: str,
                 tipo: str,
                 endereco: Optional[str] = None):
        self.identificacao = identificacao
        self.nome = nome
        self.tipo = FornecedorEnum(name='tipo', value=tipo).to_str()
        self.endereco = endereco
        
    def __repr__(self):
        return str(vars(self))
    
    def to_dict(self):
        return vars(self)