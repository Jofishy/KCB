from .unit import Unit
from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    amount: float
    unit: Unit

    def __key(self) -> tuple[str, float, Unit]:
        return (self.name, self.amount, self.unit)

    def __hash__(self) -> int:
        return hash(self.__key())
    
    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.__key() == other.__key()
        return NotImplemented