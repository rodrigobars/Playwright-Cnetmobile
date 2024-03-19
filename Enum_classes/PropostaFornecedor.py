from Enum_classes.Enum import *
from Enum_classes.Fornecedor import Fornecedor
from Enum_classes.Valores import Valores

class PropostaFornecedor(Enum):
    def __init__(self,
            valores: dict, # OK <- mudar
            participante: dict, 
            declaracaoMeEpp: bool, 
            canalChatAberto: bool, 
            situacaoUltimaNegociacao: Optional[str] = None,
            justificativaUltimaNegociacao: Optional[str] = None,
            situacaoNaFaseFechadaModoAbertoFechado: Optional[str] = None,
            situacao: Optional[str] = None,
            modeloVersao: Optional[str] = None,
            marcaFabricante: Optional[str] = None,
            quantidadeOfertada: Optional[int] = None,
            descricaoDetalhada: Optional[str] = None,
            situacaoUltimaSolicitacaoAnexos: Optional[str] = None,
            justificativaUltimaSolicitacaoAnexos: Optional[str] = None,
            dataHoraLimiteAtendimento: Optional[str] = None,
            motivoDesclassificacao: Optional[str] = None,
            situacaoNaDisputaFinal: Optional[str] = None,
            situacaoNoDesempateMeEpp: Optional[str] = None
        ):
        self.valores = Valores(**valores).to_dict()
        self.quantidadeOfertada = quantidadeOfertada
        self.descricaoDetalhada = descricaoDetalhada
        self.situacao = PropostaItemEnum(name='situacao', value=situacao).to_str()
        self.marcaFabricante = marcaFabricante
        self.modeloVersao = modeloVersao
        self.situacaoUltimaNegociacao = situacaoUltimaNegociacao
        self.justificativaUltimaNegociacao = justificativaUltimaNegociacao
        self.situacaoNaFaseFechadaModoAbertoFechado = situacaoNaFaseFechadaModoAbertoFechado
        self.participante = Fornecedor(**participante).to_dict()
        self.situacaoUltimaSolicitacaoAnexos = situacaoUltimaSolicitacaoAnexos
        self.justificativaUltimaSolicitacaoAnexos = justificativaUltimaSolicitacaoAnexos
        self.declaracaoMeEpp = sim_ou_nao(declaracaoMeEpp)
        self.canalChatAberto = sim_ou_nao(canalChatAberto)
        self.dataHoraLimiteAtendimento = dataHoraLimiteAtendimento
        self.motivoDesclassificacao = motivoDesclassificacao
        self.situacaoNaDisputaFinal = situacaoNaDisputaFinal
        self.situacaoNoDesempateMeEpp = situacaoNoDesempateMeEpp
        
    def __repr__(self):
        return str(vars(self))
    
    def to_dict(self):
        return vars(self)