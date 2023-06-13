<script setup lang="ts">
    import ImportURL from './ImportURL.vue';
</script>

<template>
    <div class="landing">
        <h1>Kiana's Cookbook</h1>
        <ImportURL />
    </div>
</template>

<style>
    .recipe-input a {
        margin-left: 20px;
        display: inline-block;
        vertical-align: middle;
    }
    .recipe-input a img {
        width: 44px;
        height: 44px;
    }

    .landing {
        width: 100vw;
        height: 100vh;
        background-image: url('@/assets/pexels-kaboompics-com-6245.jpg');
        background-size: cover;
    }

    .recipe-input {
        position: relative;
        top: 22%;
        left: 50%;
        width: 800px;
        margin-left: -400px;
    }

    .recipe-input input {
        width: 600px;
        height: 30px;
        padding: 5px;
        border-radius: 10px 0px 0px 10px;
        border-width: 2px;
        border-color: #000000ad;
        font-size: 17px;
        border-style: solid;
        border-right: none;
    }

    .recipe-input button {
        height: 44px;
        font-size: 17px;
        border-radius: 0px 10px 10px 0px;
        border-width: 2px;
        border-left-width:1px;
        border-color: #000000ad;
        border-style: solid;
    }

    .landing h1 {
        margin: 0;
        font-weight: 400;
        padding: 20px 115px;
        font-size: 49px;
    }
</style>