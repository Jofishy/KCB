from recipe_scrapers import scrape_me
from datetime import datetime

from model.recipe import Recipe
from model.ingredient import Ingredient
from model.unit import Unit

def scrape_url(url: str) -> Recipe:
    scraped = scrape_me(url, wild_mode=True)
    ingredients = {ingredient for ingredient in scraped.ingredients()}
    
    return Recipe(scraped.title(), 
                  None, 
                  ingredients, 
                  scraped.instructions_list(), 
                  scraped.host(), 
                  url, 
                  datetime.now(), 
                  prepTime=scraped.total_time())