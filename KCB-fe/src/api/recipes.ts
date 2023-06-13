import type { Recipe }from './recipe';

const endpoint = import.meta.env.VITE_API_ENDPOINT;

export async function getAllRecipes(): Promise<Array<Recipe>>{
    console.log("retrieving all recipes");
    const recipes:Array<Recipe> = (await (await fetch(endpoint+"/recipe")).json()).recipes as Array<Recipe>;
    console.log(`Recieved recipes!`, recipes);

    return Promise.resolve(recipes);
}

export async function postRecipe(url:string): Promise<Array<Recipe>>{
    console.log("saving recipe", url);
    const recipes:Array<Recipe> = (await (await fetch(endpoint+"/recipe?url="+url, {
        method: "POST"
    })).json()).recipes as Array<Recipe>;
    console.log(`recipe saved`, url);

    return Promise.resolve(recipes);
}