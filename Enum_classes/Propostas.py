from Enum_classes.PropostasItem import PropostasItem
from typing import List

class Propostas:
    def __init__(self, propostas: List[dict]):
        self.propostas = [PropostasItem(**proposta).to_dict() for proposta in propostas]
        
    def __repr__(self):
        return str(self.propostas)
    
    def to_list(self) -> List[PropostasItem]:
        return self.propostas