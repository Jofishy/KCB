<script lang="ts">
    import type { Recipe } from '@/api/recipe';
    import { getAllRecipes } from '@/api/recipes';

    enum State {
        LOADING,
        LOADED,
        ERROR
    }

    export default {
        data() {
            return {
                state: State.LOADED,
                recipes: new Array<Recipe>(),
                State
            }
        },
        methods: {
            async updateRecipes(): Promise<void> {
                try{
                    this.state = State.LOADING;
                    this.recipes = await getAllRecipes();
                    this.state = State.LOADED;

                    return Promise.resolve();
                } catch (e) {
                    console.error(e);
                    this.state = State.ERROR;
                    return Promise.reject(e);
                }
                
            },
            async openRecipe(i: number): Promise<void> {
                
            }
        },
        mounted() {
            this.updateRecipes()
        }
    }
</script>

<template>
    <div class="recipes" v-if="state == State.ERROR">
        <p>Error loading saved recipes, try again later.</p>
    </div>
    <div class="recipes" v-if="state == State.LOADING">
        <p>Loading your saved recipes.</p>
    </div>
    <div class="recipes" v-if="state == State.LOADED">
        <h2>Your cookbook</h2>
        <table v-if="recipes.length > 0">
            <tr>
                <th>Title</th>
                <th>Source website</th>
                <th>Total Time</th>
            </tr>
            <tr v-for="recipe, i in recipes" v-bind:data-recipeId="recipe.id" @click="openRecipe(i)">
                <td>{{recipe.title}}</td>
                <td>{{recipe.source}}</td>
                <td>{{ recipe.prepTime }}</td>
            </tr>
        </table>
        <p v-if="recipes.length === 0">
            You haven't saved any recipes yet!
        </p>
    </div>
</template>

<style>
    .recipes {
        width: fit-content;
        margin: 0 auto;
    }

    .recipes th, .recipes td {
        text-align: left;
        padding-right: 100px;
        padding-bottom: 10px;
        padding-top: 10px;
        padding-left: 5px;
        
    }

    .recipes tr:not(:first-child) {
        cursor: pointer;
    }

    .recipes tr:hover:not(:first-child) {
        background-color: #6ee2ff70;
    }
</style>