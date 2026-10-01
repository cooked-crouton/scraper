from cc_scraper.utils.scraper import Scraper
from cc_scraper.website_definitions.marmiton import MARMITON

def main():
    recipe_url = Scraper().get_recipes_url(MARMITON, 50)
    recipes = Scraper().scrape(MARMITON)
    
    cpt = 1
    for recipe in recipes:
        #print(recipe)
        print(str(cpt) + ". " + recipe.title)
        cpt += 1

if __name__ == "__main__":
    main()
