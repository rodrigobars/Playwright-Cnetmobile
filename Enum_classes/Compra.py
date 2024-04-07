from Enum_classes.Enum import *

def sim_ou_nao(bool: bool):
    return 'Sim' if bool else 'Não'

class Compra:
    def __init__(
            self,
            numeroUasg: int,
            modalidade: int,
            numero: int,
            ano: int,
            chaveCompraPncp: int,
            nomeUasg: str,
            caracteristica: str,
            formaRealizacao: str,
            criterioJulgamento: str,
            fundamentoLegal: str,
            equalizacaoIcms: bool,
            situacaoCompraFaseExterna: str,
            faseCompraFaseExterna: str,
            homologada: bool,
            possuiAvisoDeEvento: bool,
            possuiEventoQueImpedeAcaoNaCompra: bool,
            modoDisputa: str,
            tipoObjeto: str,
            dataHoraPrevisaoAbertura: str,
            dataHoraInicioPropostas: str,
            dataHoraFimPropostas: str,
            dataHoraAbertura: str,
            emergencial: bool,
            objeto: str,
            julgamentoIniciado: bool,
            tipoEventoImpeditivoVigente: Optional[str] = None
        ):
        self.numeroUasg = numeroUasg
        self.modalidade = CompraEnum(name='modalidade', value=modalidade).to_str()
        self.numero = numero
        self.ano = ano
        self.chaveCompraPncp = chaveCompraPncp
        self.nomeUasg = nomeUasg
        self.caracteristica = CompraEnum(name='caracteristica', value=caracteristica).to_str()
        self.formaRealizacao =  CompraEnum(name='formaRealizacao', value=formaRealizacao).to_str()
        self.criterioJulgamento =  CompraEnum(name='criterioJulgamento', value=criterioJulgamento).to_str()
        self.fundamentoLegal =  Enum(name='fundamentoLegal', value=fundamentoLegal).to_str()
        self.equalizacaoIcms = sim_ou_nao(equalizacaoIcms)
        self.situacaoCompraFaseExterna =  Enum(name='situacaoCompraFaseExterna', value=situacaoCompraFaseExterna).to_str()
        self.faseCompraFaseExterna =  Enum(name='faseCompraFaseExterna', value=faseCompraFaseExterna).to_str()
        self.homologada = sim_ou_nao(homologada)
        self.possuiAvisoDeEvento = sim_ou_nao(possuiAvisoDeEvento)
        self.possuiEventoQueImpedeAcaoNaCompra = sim_ou_nao(possuiEventoQueImpedeAcaoNaCompra)
        self.modoDisputa =  CompraEnum(name='modoDisputa', value=modoDisputa).to_str()
        self.tipoObjeto = LicitacaoEnum(name='tipoObjeto', value=tipoObjeto).to_str()
        self.dataHoraPrevisaoAbertura = dataHoraPrevisaoAbertura
        self.dataHoraInicioPropostas = dataHoraInicioPropostas
        self.dataHoraFimPropostas = dataHoraFimPropostas
        self.dataHoraAbertura = dataHoraAbertura
        self.emergencial = sim_ou_nao(emergencial)
        self.objeto = objeto
        self.julgamentoIniciado = sim_ou_nao(julgamentoIniciado)
        self.tipoEventoImpeditivoVigente = tipoEventoImpeditivoVigente

    def __str__(self):
        return str({var_name: getattr(self, var_name) for var_name in vars(self)})

    def to_dict(self):
        return vars(self)