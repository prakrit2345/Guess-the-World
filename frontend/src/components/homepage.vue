<template>
  <Background>
    <div class="overlay">
      <h1>Guess the World</h1>
      <p>Test your geography skills!</p>
      <div class="menu">
        <i class="bi bi-list"></i>
        <button type="button" class="btn btn-secondary" @click="navigate">Menu</button>
      </div>
    </div>
  </Background>
</template>

<script setup>
import Background from './background.vue'

const emit = defineEmits(['navigate'])

function navigate() {
  emit('navigate', '/menu')
}
</script>

<style scoped>
.overlay {
  text-align: center;
  color: white;
  background: rgba(0, 0, 0, 0.4);
  padding: 2rem 3rem;
  border-radius: 12px;
}

.menu {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-top: 1rem;
}

button {
  margin-top: 0;
  padding: 0.6rem 1.5rem;
  font-size: 1rem;
  cursor: pointer;
}

i {
  font-size: 2rem;
  margin-top: 0.3rem;
  line-height: 1;
}
</style>