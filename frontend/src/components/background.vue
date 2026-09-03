<template>
  <div class="home-page">
    <i v-if="musicstate" class="bi bi-volume-up-fill" @click="musicstate = false"></i>
    <i v-else class="bi bi-volume-mute-fill" @click="musicstate = true"></i>
    <slot />
  </div>
</template>
<script setup>
import {ref,watch} from 'vue'
import { audio } from '@/music.js'
const musicstate = ref(true)
watch(musicstate, (value) => {
  if (value) {
    audio.play()
  } else {
    audio.pause()
  }
}, { immediate: true })

</script>

<style scoped>
.home-page {
  position: relative;
  min-height: 100vh;
  width: 100%;
  background-image: url('../assets/homepage.avif');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.bi {
  position: absolute;
  top: 1rem;
  right: 1rem;
  z-index: 2;
  font-size: 3rem;
  cursor: pointer;
  color: white;
}
</style>