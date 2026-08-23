<template>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <HomePage @menu="menu" />
</template>

<script setup>
import HomePage from './components/homepage.vue'


function menu() {
  console.log('Menu clicked!')
}

</script>

<style>
/* remove any default padding/margin so background fills the screen */
html, body, #app {
  margin: 0;
  padding: 0;
  height: 100%;
}
</style>