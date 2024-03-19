from Enum_classes.ValorTipo import ValorTipo
from typing import Optional

class Valores:
    def __init__(self,
            valorPropostaInicial: dict,
            valorPropostaInicialOuLances: Optional[dict] = None,
            valorSugeridoNegociacao: Optional[dict] = None,
            valorNegociado: Optional[dict] = None
        ):
        self.valorPropostaInicial = ValorTipo(**valorPropostaInicial).to_dict()
        self.valorPropostaInicialOuLances = ValorTipo(**valorPropostaInicialOuLances).to_dict() if valorPropostaInicialOuLances else valorPropostaInicialOuLances
        self.valorSugeridoNegociacao = ValorTipo(**valorSugeridoNegociacao).to_dict() if valorSugeridoNegociacao else valorSugeridoNegociacao
        self.valorNegociado = ValorTipo(**valorNegociado).to_dict() if valorNegociado else valorNegociado
        
    def __repr__(self):
        return str(vars(self))
    
    def to_dict(self):
        return vars(self)