from dataclasses import dataclass, field

@dataclass
class Website:
    name: str
    url: str
    title: str
    pagination: str | None = None
    recipes_url: list[str] = field(default_factory=list)
    ingredients: str| None = None
    ingredient_name: str | None = None
    quantity: str | None = None
    unit: str | None = None
    steps: str| None = None
    cook_time: str | None = None
    image: str | None = None
