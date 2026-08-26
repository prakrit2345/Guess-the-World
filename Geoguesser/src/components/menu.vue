<template>
    <Background>
        <div class="overlay">
            <h1>Guess The World</h1>
            <p>MENU</p>
        
                <div class="row text-center gy-4">
                    <div class="col-6"> <button type="button" class="btn btn-secondary btn-lg" id="login" @click="handleNavigate('/login')">Login</button></div>
                    <div class="col-6"> <button type="button" class="btn btn-secondary btn-lg" @click="handleNavigate('/register')">Register</button></div>

                    <div class="col-6"> <button type="button" class="btn btn-secondary btn-lg" @click="handleNavigate('/multiplayer')">Multiplayer</button></div>
                    <div class="col-6"> <button type="button" class="btn btn-secondary btn-lg" @click="handleNavigate('/guest')">Play As Guest</button></div>
                </div>
           
        </div>
    </Background>
</template>

<script setup>
  import Background from './background.vue'
  const emit=defineEmits(['navigate'])
  function handleNavigate(path) {
    emit('navigate', path)
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
</style>