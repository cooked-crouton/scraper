from cc_scraper.utils.scraper import Scraper
from cc_scraper.website_definitions.marmiton import MARMITON
from cc_scraper.website_definitions._750g import _750G
from cc_scraper.website_definitions.le_journal_des_femmes import LE_JOURNAL_DES_FEMMES_VIANDES, LE_JOURNAL_DES_FEMMES_LEGUMES
from cc_scraper.website_definitions.chefsimon import CHEFSIMON

def main():
    recipes_url = Scraper().get_recipes_url(MARMITON, 2)
    recipes = Scraper().scrape(MARMITON)
    
    recipes_url = Scraper().get_recipes_url(_750G, 2)
    recipes.extend(Scraper().scrape(_750G))

    recipes_url = Scraper().get_recipes_url(LE_JOURNAL_DES_FEMMES_VIANDES, 2)
    recipes.extend(Scraper().scrape(LE_JOURNAL_DES_FEMMES_VIANDES))

    recipes_url = Scraper().get_recipes_url(LE_JOURNAL_DES_FEMMES_LEGUMES, 2)
    recipes.extend(Scraper().scrape(LE_JOURNAL_DES_FEMMES_LEGUMES))

    recipes_url = Scraper().get_recipes_url(CHEFSIMON, 2)
    recipes.extend(Scraper().scrape(CHEFSIMON))


    cpt = 1
    for recipe in recipes:
        #print(str(cpt) + ". " + recipe.title)
        #cpt += 1
        print(recipe)

if __name__ == "__main__":
    main()
