from Enum_classes.PropostasItem import PropostasItem
from typing import List

class Propostas:
    def __init__(self, propostas: List[dict]):
        self.propostas = [PropostasItem(**proposta).to_dict() for proposta in propostas]
        
    def __repr__(self):
        return str(self.propostas)
    
    def to_list(self) -> List[PropostasItem]:
        return self.propostas
    
# import json
# from Enum import *

# # Leitura do arquivo JSON
# with open('enums_externo.json', 'r', encoding='utf-8') as arquivo:
#     enum_externo = json.load(arquivo)
    
# with open('propostas.json', 'r', encoding='utf-8') as arquivo:
#     propostas = json.load(arquivo)

# Enum.feed(enum_externo)

# print(type(Propostas(propostas).to_list()))