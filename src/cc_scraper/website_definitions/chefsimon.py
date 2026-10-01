from cc_scraper.models.website import Website

CHEFSIMON = Website(
    name="chefsimon",
    url="https://www.chefsimon.com/recettes/all/",
    pagination="?page=",
    title="h1",
    recipes_url_element="a[href*='/gourmets/'][href*='/recettes/']",
    ingredients='[data-recipe-show-target="ingredientsBloc"] .grid.grid-cols-1.gap-2.mb-3 > div.flex.flex-row.items-start',
    ingredient_name=".link_cs",
    quantity=None,
    unit=None,
    steps=".w-full.my-7.p-7.border-2.border-dashed .leading-relaxed",
    cook_time=".text-center.bg-gray-for-bg3.p-4 span",
    image="img[fetchpriority='high']",
)
