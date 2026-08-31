<template>
 <Background>

 <div class="overlay">
 <form @submit.prevent="submitForm">
    <div class="mb-3">
    <label for="username" class="form-label">Username</label>
    <input type="text" class="form-control" id="username" v-model="username" >
  </div>
  <div class="mb-3">
    <label for="email" class="form-label">Email address</label>
    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" v-model="email">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="password" class="form-label">Password</label>
    <input type="password" class="form-control" id="password" v-model="password">
  </div>

 
  <button type="submit" class="btn btn-primary" :disabled="loading">Submit</button>
</form>

  <div v-if="errormsg" class="alert alert-danger mt-3" role="alert">
    {{ errormsg }}
  </div>
</div>
 </Background>

</template>
<script setup>
    import Background from './background.vue'
    import api from '../api.js'
    import { ref } from 'vue'
    
    const errormsg=ref('')
    const loading = ref(false)
    const formdata=ref({
      username: '',
      email: '',
      password: ''
    })
    const submitForm = async () => {
      try {
        const response = await api.post('/register', formdata);
        console.log('Registration successful:', response.data);
        formdata.value = {
          username: '',
          email: '',
          password: ''
        };
      } catch (error) {
        if  (error.response && error.response.data && error.response.data.message) {
          errormsg.value = error.response.data.message;
        } else {
          errormsg.value = 'An error occurred during registration.';
        }
       } finally {
        loading.value = false;
      }
    };


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
