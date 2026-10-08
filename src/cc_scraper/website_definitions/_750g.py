from cc_scraper.models.website import Website

_750G = Website(
    name="750g",
    url="https://www.750g.com/recettes-plats/traditionnels/",
    pagination="?page=",
    recipes_url_element=".card-link",
    title=".u-title-page",
    ingredients=".recipe-ingredients-item",
    ingredient_name=".recipe-ingredients-item-label",
    steps=".recipe-steps-content",
    cook_time=".recipe-info-item:has(svg.u-icon-time)",
)
