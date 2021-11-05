<template>
    <form class="form-signin" @submit.prevent="submit">
    <h1 class="h3 mb-3 fw-normal">Please Register</h1>
      <input type="text" class="form-control" id="first_name" placeholder="First Name" v-model="first_name">
      
      <input type="text" class="form-control" id="last_name" placeholder="Last Name" v-model="last_name">
      
      <input type="email" class="form-control" id="email" placeholder="Email" v-model="email">
      
      <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
      
      <input type="password" class="form-control" id="password_confirm" placeholder="Confirm Password" v-model="password_confirm">

      <button class="btn btn-lg btn-primary btn-block" type="submit">Register</button>

  </form>

</template>

<script>
import { ref } from "vue";
import axios from 'axios';
import {useRouter} from 'vue-router'

export default {
    name: 'Register',
    setup() {
        const first_name = ref('');
        const last_name = ref('');
        const email = ref('');
        const password = ref('');
        const password_confirm = ref('');
        const router = useRouter();

        const submit = async () => {
            await axios.post('register/', {
                first_name: first_name.value,
                last_name: last_name.value,
                email: email.value,
                password: password.value,
                password_confirm: password_confirm.value,
            });
            await router.push('/login');
        }

        return {
            first_name,
            last_name,
            email,
            password,
            password_confirm,
            submit
        }
    }
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