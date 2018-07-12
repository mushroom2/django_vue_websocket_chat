<template>
  <div class="container">
    <h1 class="text-center">Let's chat!</h1>
    <div id="auth-container" class="row">
      <div class="col-sm-4 offset-sm-4">
        <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
          <li class="nav-item">
            <a class="nav-link active" id="signup-tab" data-toggle="tab" href="#signup" role="tab" aria-controls="signup" aria-selected="true">Sign Up</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" id="signin-tab" data-toggle="tab" href="#signin" role="tab" aria-controls="signin" aria-selected="false">Sign In</a>
          </li>
        </ul>

        <div class="tab-content" id="myTabContent">

          <div class="tab-pane fade show active" id="signup" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signUp">
              <div class="form-group">
                <input v-model="username" type="text" class="form-control" id="username" placeholder="Имя пользователя" required>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <input v-model="password" type="password" class="form-control" id="password" placeholder="Пароль" required>
                </div>
                <div class="form-group col-md-6">
                  <input v-model="confirm_password" type="password" class="form-control" id="confirm_password" placeholder="Пароль еще раз" required>
                </div>
              </div>
              <div class="form-group">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="toc" required>
                  <label class="form-check-label" for="gridCheck">
                    Accept terms and Conditions
                  </label>
                </div>
              </div>
              <button type="submit" class="btn btn-block btn-primary">Sign up</button>
            </form>
          </div>

          <div class="tab-pane fade" id="signin" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signIn">
              <div class="form-group">
                <input v-model="username" type="text" class="form-control" id="username" placeholder="Username" required>
              </div>
              <div class="form-group">
                <input v-model="password" type="password" class="form-control" id="password" placeholder="Password" required>
              </div>
              <button type="submit" class="btn btn-block btn-primary">Sign in</button>
            </form>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';


  export default {

    data () {
      return {
        confirm_password: '', username: '', password: ''
      }
    },

    methods: {
      signUp () {
        axios.post('http://localhost:8000/chat/register/', this.$data).then((resp) => {
          console.log(resp);
          alert('Your account has been created. You will be signed in automatically')
          //this.signIn()
        })
        .catch((err) => {
          console.log(err)
        })
      },

      signIn () {
        const credentials = {username: this.username, password: this.password};

        axios.post('http://localhost:8000/chat/login/', credentials).then( (resp) => {
          sessionStorage.setItem('authToken', resp.data.token);
          sessionStorage.setItem('username', this.username);
          console.log(resp);
          this.$router.push('/channels')
        })
        .catch((err) => {
          console.log(err)
        })
      }
    }

  }
</script>

<style scoped>
  #auth-container {
    margin-top: 50px;
  }

  .tab-content {
    padding-top: 20px;
  }
</style>
