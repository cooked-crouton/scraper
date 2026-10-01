from cc_scraper.models.website import Website

LE_JOURNAL_DES_FEMMES_VIANDES = Website(
    name="le_journal_des_femmes_viandes",
    url="https://cuisine.journaldesfemmes.fr/recette-plat-viande/preferes",
    pagination="-page",
    title="h1",
    recipes_url_element="a[href*='/recette/']",
    ingredients=".app_recipe_ing_item",
    ingredient_name=".jHiddenHref",
    quantity=".jIngredientQuantity",
    steps=".recipe-step",
    cook_time='div:has(> strong:-soup-contains("Temps total")) > span',
    image="meta[property='og:image']",
)

LE_JOURNAL_DES_FEMMES_LEGUMES = Website(
    name="le_journal_des_femmes_legumes",
    url="https://cuisine.journaldesfemmes.fr/recette-legume-gratin/preferes",
    pagination="-page",
    title="h1",
    recipes_url_element="a[href*='/recette/']",
    ingredients=".app_recipe_ing_item",
    ingredient_name=".jHiddenHref",
    quantity=".jIngredientQuantity",
    steps=".bu_cuisine_recette_prepa",
    cook_time='div:has(> strong:-soup-contains("Temps total")) > span',
    image="meta[property='og:image']",
)