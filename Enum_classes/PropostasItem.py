from Enum_classes import Propostas
from Enum_classes.Enum import *
from Enum_classes.PropostaFornecedor import PropostaFornecedor
from Enum_classes.Item import Item
from typing import Optional, List

class PropostasItem(Item):
    def __init__(self,
            propostasItem: Optional[List[PropostaFornecedor]] = None,
            propostaItem: Optional[List[PropostaFornecedor]] = None,
            prazosFaseRecursal: Optional[dict] = None,
            qtdeAceitaSrp: Optional[int] = None,
            qtdeAdjudicadaSrp: Optional[int] = None,
            subItens: Optional[dict] = None,
            **kwargs
        ):
        super().__init__(**kwargs)
        self.qtdeAceitaSrp = qtdeAceitaSrp
        self.qtdeAdjudicadaSrp = qtdeAdjudicadaSrp
        self.prazosFaseRecursal = prazosFaseRecursal

        if propostasItem:
            self.propostasItem = [PropostaFornecedor(**fornecedor).to_dict() for fornecedor in propostasItem]
        elif propostaItem:
            self.propostasItem = [PropostaFornecedor(**fornecedor).to_dict() for fornecedor in propostaItem]
        else:
            self.propostasItem = None

        if subItens:
            self.subItens = Propostas.Propostas(subItens).to_list()
        else:
            self.subItens = None