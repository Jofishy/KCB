from datetime import datetime
from typing import Optional
from dataclasses import dataclass, asdict
import json

@dataclass
class Recipe:
    title: str
    id: str
    ingredients: set[str]
    steps: list[str]
    source: str
    url: str
    import_date: datetime
    prepTime: Optional[str] = None

    def toJson(self):
        return json.dumps(asdict(self), default=str)
    
def from_json(input: dict) -> Recipe:
    return Recipe(**input)