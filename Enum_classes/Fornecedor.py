from Enum_classes.Enum import FornecedorEnum

class Fornecedor:
    def __init__(self, identificacao: str, nome: str, tipo: str):
        self.identificacao = identificacao
        self.nome = nome
        self.tipo = FornecedorEnum(name='tipo', value=tipo).to_str()
        
    def __repr__(self):
        return str(vars(self))
    
    def to_dict(self):
        return vars(self)