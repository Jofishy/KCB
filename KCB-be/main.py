from typing import Annotated
from fastapi import FastAPI, Response, Path, status
from fastapi.middleware.cors import CORSMiddleware

from scrape import scrape_url

from db import get_all_recipes, get_recipe, save_recipe

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/recipe")
async def getRecipes():
    return {"recipes":get_all_recipes()}

@app.get("/recipe/{recipe_id}", status_code=status.HTTP_200_OK)
async def getRecipe(recipe_id: Annotated[str, Path(title="The id of the recipe to get")], response: Response):
    recipe = get_recipe(recipe_id)

    if recipe:
        return {"recipe": recipe}
    
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"message": "recipe id not found"}

@app.post("/recipe")
async def postRecipe(url: str):
    recipe = scrape_url(url)
    save_recipe(recipe)
    return {"message": "ok"}
