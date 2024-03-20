from Enum_classes.Enum import *
from Enum_classes.PropostaFornecedor import PropostaFornecedor
from Enum_classes.Item import Item
from typing import Optional, List

class PropostasItem(Item):
    def __init__(self,
            propostasItem: Optional[List[PropostaFornecedor]] = None,
            prazosFaseRecursal: Optional[dict] = None,
            qtdeAceitaSrp: Optional[int] = None,
            qtdeAdjudicadaSrp: Optional[int] = None,
            **kwargs
        ):
        super().__init__(**kwargs)
        self.qtdeAceitaSrp = qtdeAceitaSrp
        self.qtdeAdjudicadaSrp = qtdeAdjudicadaSrp
        self.prazosFaseRecursal = prazosFaseRecursal
        self.propostasItem = [PropostaFornecedor(**fornecedor).to_dict() for fornecedor in propostasItem]

# # Leitura do arquivo JSON
# with open('enums_externo.json', 'r', encoding='utf-8') as arquivo:
#     enum_externo = json.load(arquivo)
    
# with open('propostas.json', 'r', encoding='utf-8') as arquivo:
#     propostas = json.load(arquivo)

#Enum.feed(enum_externo)

#empresa1 = propostas[0]

#pprint(empresa1['propostasItem'][0])
#pprint(Empresa(**empresa1['propostasItem'][0]))

# propostasItem = list()
# for item in propostas:
#     print(PropostasItem(**item), '\n')