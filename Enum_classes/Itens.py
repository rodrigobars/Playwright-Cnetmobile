from Enum_classes.Item import Item
from typing import List

class Itens:
    def __init__(self, itens: List[dict]):
        self.itens = [Item(**item).to_dict() for item in itens]
        
    def __repr__(self):
        return str(self.itens)
    
    def to_list(self) -> List[Item]:
        return self.itens
    
# import json
# from Enum import *

# # Leitura do arquivo JSON
# with open('enums_externo.json', 'r', encoding='utf-8') as arquivo:
#     enum_externo = json.load(arquivo)
    
# with open('itens.json', 'r', encoding='utf-8') as arquivo:
#     itens = json.load(arquivo)

# Enum.feed(enum_externo)

# print(Itens(itens).to_list())