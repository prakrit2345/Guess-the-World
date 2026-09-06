<script setup>
    import Background from './background.vue'
    import api from '../api.js'
    import { ref } from 'vue'
    import router from '../router.js'
    
    const errormsg=ref('')
    const loading = ref(false)
    const formdata=ref({
      firstName:'',
      lastName:'',
      address: '',
      email:'',
      password: ''
    })
    const submitForm = async () => {
      try {
        const response = await api.post('/register', formdata.value);
        console.log('Registration successful:', response.data);
        formdata.value = {
          firstName:'',
          lastName:'',
          address: '',
          email: '',
          password: '',
        };
        router.push('/login');
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
<template>
 <Background>

 <div class="overlay">
 <form @submit.prevent="submitForm">
    <div class="mb-3">
    <label for="firstName" class="form-label">First Name</label>
    <input type="text" class="form-control" id="firstName" v-model="formdata.firstName" >
  </div>
  <div class="mb-3">
    <label for="lastName" class="form-label">Last Name</label>
    <input type="text" class="form-control" id="lastName" v-model="formdata.lastName" >
  </div>
  <div class="mb-3">
    <label for="address" class="form-label">Address</label>
    <input type="text" class="form-control" id="address" v-model="formdata.address" >
  </div>
  
  <div class="mb-3">
    <label for="email" class="form-label">Email address</label>
    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" v-model="formdata.email">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
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

<style scoped>
  .overlay {
    text-align: center;
    color: white;
    background: rgba(0, 0, 0, 0.4);
    padding: 2rem 3rem;
    border-radius: 12px;
}
</style>
