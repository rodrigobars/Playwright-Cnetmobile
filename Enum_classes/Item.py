from Enum_classes.Enum import *

class Item:
    def __init__(self,
            numero: Optional[int] = None,
            tipo: Optional[str] = None,
            disputaPorValorUnitario: Optional[bool] = None,
            possuiOrcamentoSigiloso: Optional[bool] = None,
            identificador: Optional[str] = None,
            descricao: Optional[str] = None,
            criterioJulgamento: Optional[str] = None,
            homologado: Optional[bool] = None,
            numeroSessaoJulgHab: Optional[int] = None,
            tipoTratamentoDiferenciadoMeEpp: Optional[str] = None,
            participacaoExclusivaMeEppOuEquiparadas: Optional[bool] = None,
            situacao: Optional[str] = None,
            fase: Optional[str] = None,
            criterioValor: Optional[str] = None,
            valorEstimadoTotal: Optional[float] = None,
            julgHabEncerrada: Optional[bool] = None,
            situacaoEnvioResultado: Optional[str] = None,
            valorEstimadoUnitario: Optional[float] = None,
            valorEstimado: Optional[float] = None,
            priorizarAbertura: Optional[bool] = None,
            quantidadeSolicitada: Optional[int] = None,
            qtdeItensDoGrupo: Optional[int] = None,
            dataHoraLimiteEtapaFaseRecursal: Optional = None,
            tipoItemCatalogo: Optional = None,
            utilizaMargemPreferencia: Optional = None,
            grupo: Optional[str] = None,
            dataHoraReaberturaJulgHab: Optional[str] = None,
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
        self.dataHoraLimiteEtapaFaseRecursal = dataHoraLimiteEtapaFaseRecursal
        self.tipoItemCatalogo = tipoItemCatalogo
        self.utilizaMargemPreferencia = utilizaMargemPreferencia
        self.grupo = grupo
        self.dataHoraReaberturaJulgHab = dataHoraReaberturaJulgHab

    def __str__(self):
        return str({var_name: getattr(self, var_name) for var_name in vars(self)})

    def to_dict(self):
        return vars(self)