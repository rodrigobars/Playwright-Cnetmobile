from typing import Optional, Any

class Enum:
    ALLOWED_TYPES = [None, 'Compra', 'Item', 'Licitacao', 'ItemCompra', 'PropostaItem', 'situacaoEnvioResultado', 'Fornecedor']

    def __init__(self, name: str, value: Any, type: Optional[str] = None):
        if type not in Enum.ALLOWED_TYPES:
            raise ValueError(f"Invalid type '{type}'. Allowed types are {self.ALLOWED_TYPES}")

        self.name = f"{name[0].upper() + name[1:]}{type if (type in Enum.ALLOWED_TYPES and type is not None) else ''}Enum"
        self.value = value
        self._label = self._get_label()

    enums = []

    def _get_label(self):
        for enum_group in Enum.enums:
            if enum_group["name"] == self.name:
                for enum_value in enum_group["values"]:
                    if enum_value["value"] == str(self.value):
                        return enum_value["label"]
                    
    @classmethod
    def feed(cls, enums):
        cls.enums = enums

    def __repr__(self):
        return self._label
    
    def to_str(self):
        return str(f"{self._label}")

class ItemEnum(Enum):
    def __init__(self, name: str, value: Any):
        super().__init__(name=name, value=value, type='Item')

class ItemCompraEnum(Enum):
    def __init__(self, name: str, value: Any):
        super().__init__(name=name, value=value, type='ItemCompra')
        
class CompraEnum(Enum):
    def __init__(self, name: str, value: Any):
        super().__init__(name=name, value=value, type='Compra')        

class LicitacaoEnum(Enum):
    def __init__(self, name: str, value: Any):
        super().__init__(name=name, value=value, type='Licitacao')
        
class PropostaItemEnum(Enum):
    def __init__(self, name: str, value: Any):
        super().__init__(name=name, value=value, type='PropostaItem')

class situacaoEnvioResultadoEnum(Enum):
    def __init__(self, name: str, value: Any):
        super().__init__(name=name, value=value, type='situacaoEnvioResultado')
        
class FornecedorEnum(Enum):
    def __init__(self, name: str, value: Any):
        super().__init__(name=name, value=value, type='Fornecedor')
        
def sim_ou_nao(value: bool):
    return 'Sim' if value else 'Não'