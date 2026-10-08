from bs4 import BeautifulSoup
from urllib.parse import urljoin

from cc_scraper.models.ingredient import Ingredient
from cc_scraper.models.recipe import Recipe
from cc_scraper.models.website import Website
from cc_scraper.utils.http import get


class Scraper:
    def get_recipes_url(self, website: Website, max_links: int) -> list[str]:
        page_index = 1
        recipes_url = []
        seen = set()

        previous_count = -1;

        while len(recipes_url) < max_links:

            # guard against infinite loop if no recipes are found within the first 3 pages
            if len(recipes_url) == previous_count:
                break

            previous_count = len(recipes_url)

            page = get(f"{website.url}{website.pagination}{page_index}")
            soup = BeautifulSoup(page, "html.parser")

            for link in soup.select(f"{website.recipes_url_element}"):
                if len(recipes_url) >= max_links:
                    break

                href = link.get("href")
                if not href:
                    continue

                recipe_url = urljoin(website.url, href)
                if recipe_url not in seen:
                    seen.add(recipe_url)
                    recipes_url.append(recipe_url)

            page_index += 1

        website.recipes_url = recipes_url
        return recipes_url

    def scrape(self, website: Website) -> list[Recipe]:
        recipes = []
        for recipe_url in website.recipes_url:
            page = get(recipe_url)
            recipes.append(self.parse(website, page, recipe_url))

        return recipes

    def parse(self, website: Website, page: str, recipe_url: str) -> Recipe:
        soup = BeautifulSoup(page, "html.parser")

        title = self._text(soup, website.title)
        ingredients = self._ingredients(soup, website)
        steps = self._texts(soup, website.steps)
        cook_time = self._text(soup, website.cook_time)

        image = None
        if website.image:
            image_element = soup.select_one(website.image)
            if image_element:
                image = image_element.get("content") or image_element.get("src")

        return Recipe(
                url=recipe_url,
                title=title,
                ingredients=ingredients,
                steps=steps,
                cook_time=cook_time,
                image=image,
                )

    @staticmethod
    def _text(soup: BeautifulSoup, selector: str | None) -> str | None:
        if not selector:
            return None

        element = soup.select_one(selector)
        return element.get_text(" ", strip=True) if element else None

    @staticmethod
    def _texts(soup: BeautifulSoup, selector: str | None) -> list[str]:
        if not selector:
            return []

        return [element.get_text(" ", strip=True) for element in soup.select(selector)]

    @classmethod
    def _ingredients(cls, soup: BeautifulSoup, website: Website) -> list[Ingredient]:
        if not website.ingredients:
            return []

        result = []
        for item in soup.select(website.ingredients):
            name = cls._child_text(item, website.ingredient_name)
            quantity = cls._child_text(item, website.quantity)
            unit = cls._child_text(item, website.unit)

            if name:
                result.append(Ingredient(name=name, quantity=quantity, unit=unit))

        return result

    @staticmethod
    def _child_text(item, selector: str | None) -> str | None:
        if not selector:
            return None

        element = item.select_one(selector)
        return element.get_text(" ", strip=True) if element else None
