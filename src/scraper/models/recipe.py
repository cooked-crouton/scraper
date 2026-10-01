from dataclasses import dataclass, field

from scraper.models.ingredient import Ingredient

@dataclass
class Recipe:
    url: str
    title: str
    ingredients: list[Ingredient] = field(default_factory=list)
    steps: list[str] = field(default_factory=list)
    cook_time: str | None = None
    image: str | None = None

    def __str__(self) -> str:
        result = [f"\n{self.title}"]
        result.append(f"\tURL : {self.url}")
        result.append(f"\tTemps : {self.cook_time or 'inconnu'}")
        result.append("\tIngredients :")
        for ingredient in self.ingredients:
            result.append(f"\t- {ingredient.name} ({ingredient.quantity or ''}{ingredient.unit or ''})")
        result.append("\tEtapes :")
        for step in self.steps:
            result.append(f"\t- {step}")
        return "\n".join(result)