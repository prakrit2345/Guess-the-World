<template>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <HomePage v-if="showHomePage" @menu="menu" />
  <Menu v-else />
</template>

<script setup>
import { ref } from 'vue'
import HomePage from './components/homepage.vue'
import Menu from '@/components/menu.vue'

const showHomePage = ref(true)

function menu() {
  showHomePage.value = false
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