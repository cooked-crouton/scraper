from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    quantity: str | None = None
    unit: str | None = None
