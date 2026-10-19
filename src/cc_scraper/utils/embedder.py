from sentence_transformers import SentenceTransformer

from cc_scraper.models.recipe import Recipe

DEFAULT_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"


class Embedder:
    def __init__(self, model_name: str = DEFAULT_MODEL):
        self.model = SentenceTransformer(model_name)

    def recipe_to_text(self, recipe: Recipe) -> str:
        ingredients = ", ".join(i.name for i in recipe.ingredients)
        steps = " ".join(recipe.steps)
        parts = [
            recipe.title,
            f"Temps : {recipe.cook_time}" if recipe.cook_time else "",
            f"Ingrédients : {ingredients}" if ingredients else "",
            f"Étapes : {steps}" if steps else "",
        ]
        return "\n".join(p for p in parts if p)

    def embed(self, recipes: list[Recipe], batch_size: int = 32) -> list[list[float]]:
        texts = [self.recipe_to_text(r) for r in recipes]
        vectors = self.model.encode(
            texts, batch_size=batch_size, normalize_embeddings=True
        )
        return vectors.tolist()

    def embed_query(self, text: str) -> list[float]:
        return self.model.encode(text, normalize_embeddings=True).tolist()
