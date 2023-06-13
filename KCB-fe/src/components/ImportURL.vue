<script lang="ts">
    import { postRecipe } from '@/api/recipes';
    export default {
        data() {
            return {
                inputtedUrl: null
            }
        },
        methods: {
            async postNewRecipe() {
                if (this.inputtedUrl !== null){
                    try {
                        await postRecipe(this.inputtedUrl);
                        this.inputtedUrl = null;
                    } catch (e) { 
                        console.error(e);
                    }
                }
            }
        }
    }
</script>

<template>
    <div class="recipe-input">
        <input type="text" placeholder="Paste a recipe url to load" @keyup.enter="postNewRecipe" v-model="inputtedUrl">
        <button @on-click="postNewRecipe">Load recipe</button>
        <router-link to="/about"><img src="@/assets/question-mark-button-svgrepo-com.svg"></router-link>
    </div>
</template>