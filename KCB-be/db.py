import boto3
from boto3.dynamodb.conditions import Key

from model.recipe import Recipe, from_json
from model.ingredient import Ingredient
from model.unit import Unit
from datetime import datetime
import json
import base64
import hashlib

dynamodb = boto3.resource("dynamodb", "us-east-2")

recipe_table = dynamodb.Table("recipe")

def get_recipe(id: str) -> Recipe|None:
    recipe_json = recipe_table.query(IndexName="id-index", KeyConditionExpression=Key('id').eq(id))["Items"]
    if len(recipe_json) == 0:
        return None
    
    return from_json(recipe_json[0])

def get_all_recipes() -> list[Recipe]:
    return [from_json(r) for r in recipe_table.scan()["Items"]]

def save_recipe(recipe: Recipe) -> None:
    recipe.id = base64.b64encode(hashlib.sha1((recipe.title + recipe.url).encode('utf-8')).digest()).decode("utf-8")
    result = recipe_table.put_item(Item=json.loads(recipe.toJson()))
    print(result)
