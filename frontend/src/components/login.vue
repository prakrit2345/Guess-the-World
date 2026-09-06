<template>
  <Background>

    <div class="overlay">
      <form @submit.prevent="handlelogindata">
        <div class="mb-3" id="email">
          <label for="email" class="form-label">Email address</label>
          <input type="email" class="form-control" id="email" aria-describedby="emailHelp" v-model="formdata.email">
          <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
        </div>
        <div class="mb-3" id="password">
          <label for="password" class="form-label">Password</label>
          <input type="password" class="form-control" id="password" v-model="formdata.password">
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
import router from '../router.js'
import Cookie from 'js-cookie'

import { ref } from 'vue'

const loading = ref(false)
const errormsg = ref('')
const formdata = ref({
  email: '',
  password: ''
})

const handlelogindata = async () => {
  loading.value = true 
  try {
    console.log('Form data:', formdata.value);
    const response = await api.post('/login', formdata.value);
    console.log('Login successful:', response.data);
    const accessToken = response.data.data.access_token
    const refreshToken = response.data.data.refresh_token

    Cookie.set('access_token', accessToken)
    Cookie.set('refresh_token', refreshToken)

    await router.push('/home')

    formdata.value = {

      email: '',
      password: ''
    };

  } catch (error) {
    if (error.response && error.response.data && error.response.data.message) {
      errormsg.value = error.response.data.message;
    } else {
      errormsg.value = 'An error occurred during login.';
    }
  } finally {
    loading.value = false;

  }
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