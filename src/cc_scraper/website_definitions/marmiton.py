from cc_scraper.models.website import Website

MARMITON = Website(
    name="marmiton",
    url="https://www.marmiton.org/recettes/",
    pagination="?page=",
    title="h1",
    recipes_url_element="a[href*='/recettes/recette_']",
    ingredients=".card-recipe-ingredient",
    ingredient_name=".card-recipe-ingredient__name",
    quantity=".card-recipe-ingredient__quantity",
    unit=".card-recipe-ingredient__unit",
    steps=".recipe-step",
    cook_time="[class*='time'], [class*='temps']",
    image="meta[property='og:image']",
)
