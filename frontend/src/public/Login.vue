<template>
    <form class="form-signin" @submit.prevent="submit">
    <h1 class="h3 mb-3 fw-normal">Login</h1>
      
      <input type="email" class="form-control" id="email" placeholder="Email" v-model="email">
      
      <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
    

      <button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>

  </form>

</template>

<script>
import { ref } from "vue";
import axios from 'axios';
import {useRouter} from 'vue-router'

export default {
  name: 'Login',
  setup() {

    const email = ref('');
    const password = ref('');
    const router = useRouter()

    const submit = async () => {
        await axios.post('login/', {
          email: email.value,
          password: password.value
        });
        await router.push('/')
    }

    return {
      email,
      password,
      submit
    }
    
  },
}
</script>

<style scoped>
html,
body {
  height: 100%;
}

body {
  display: flex;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: 0px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 0px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}


</style>