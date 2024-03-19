from Enum_classes.Enum import *

class Item:
    def __init__(self,
            numero: int,
            tipo: str,
            disputaPorValorUnitario: bool,
            possuiOrcamentoSigiloso: bool,
            identificador: str,
            descricao: str,
            criterioJulgamento: str,
            homologado: bool,
            numeroSessaoJulgHab: int,
            tipoTratamentoDiferenciadoMeEpp: str,
            participacaoExclusivaMeEppOuEquiparadas: bool,
            situacao: str,
            fase: str,
            criterioValor: str,
            valorEstimadoTotal: float,
            julgHabEncerrada: bool,
            situacaoEnvioResultado: Optional[str] = None,
            valorEstimadoUnitario: Optional[float] = None,
            valorEstimado: Optional[float] = None,
            priorizarAbertura: Optional[bool] = None,
            quantidadeSolicitada: Optional[int] = None,
            qtdeItensDoGrupo: Optional[int] = None
        ):
        self.numero = numero
        self.tipo = ItemEnum(name='tipo', value=tipo).to_str()
        self.disputaPorValorUnitario = sim_ou_nao(disputaPorValorUnitario)
        self.possuiOrcamentoSigiloso = sim_ou_nao(possuiOrcamentoSigiloso)
        self.identificador = identificador
        self.descricao = descricao
        self.criterioJulgamento = ItemEnum(name='criterioJulgamento', value=criterioJulgamento).to_str()
        self.homologado = sim_ou_nao(homologado)
        self.situacaoEnvioResultado = situacaoEnvioResultadoEnum(name='situacaoEnvioResultado', value=situacaoEnvioResultado).to_str()
        self.numeroSessaoJulgHab = numeroSessaoJulgHab
        self.tipoTratamentoDiferenciadoMeEpp = Enum(name='tipoTratamentoDiferenciadoMeEpp', value=tipoTratamentoDiferenciadoMeEpp).to_str()
        self.participacaoExclusivaMeEppOuEquiparadas = sim_ou_nao(participacaoExclusivaMeEppOuEquiparadas)
        self.situacao = ItemCompraEnum(name='situacao', value=situacao).to_str()
        self.fase = ItemEnum(name='fase', value=fase).to_str()
        self.quantidadeSolicitada = quantidadeSolicitada
        self.criterioValor = ItemEnum(name='criterioValor', value=criterioValor).to_str()
        self.valorEstimado = valorEstimado
        self.valorEstimadoUnitario = valorEstimadoUnitario
        self.valorEstimadoTotal = valorEstimadoTotal
        self.priorizarAbertura = sim_ou_nao(priorizarAbertura)
        self.julgHabEncerrada = sim_ou_nao(julgHabEncerrada)
        self.qtdeItensDoGrupo = qtdeItensDoGrupo

    def __str__(self):
        return str({var_name: getattr(self, var_name) for var_name in vars(self)})

    def to_dict(self):
        return vars(self)