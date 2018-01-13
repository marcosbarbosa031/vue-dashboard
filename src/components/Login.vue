<template>
    <div id="login">
        <div class="ui centered card">
            <div class="content">
                <div class="ui form">
                    <div class="field">
                        <label></label>
                        <input type="text" v-model="username" placeholder="Username" required="required">
                    </div>
                    <div class="field">
                        <label></label>
                        <input type="password" v-model="password" placeholder="Password" required="required">
                    </div>
                </div>
            </div>
            <div class="ui animated fade bottom attached primary button" @click.prevent="postLogin">
                <div class="visible content">Login</div>
                <div class="hidden content">
                    <i class="chevron right icon"></i>
                </div>
            </div>
        </div>
        <transition name="fade">
            <div class="modal-bg" v-show="loading">
                <div class="modal-login ui centered card">
                    <div class="content">
                        <img src="../assets/_svg/login_loading.svg" alt="" class="loading">
                        <h2 class="centered txt-white">Loading...</h2>
                    </div>
                </div>
            </div>
        </transition>

        <transition name="fade">
            <p v-if="false">Loading lol</p>
        </transition>
    </div>
</template>

<script>
export default {
  name: "Login",
  data () {
      return {
            username: null,
            password: null,
            loading: false
      }
  },
  methods: {
      postLogin () {
          this.loading = true
          this.$http.post('https://jsonplaceholder.typicode.com/posts', {
              title: this.username,
              body: this.password
          }, response => {
              //error callback
              this.loading = false
          }).then(response => {
              console.log(response)
              this.loading = false
          })
      }
  }
}
</script>

<style>
    .loading{
        width: 100px;
    }

    .modal-login{
        box-shadow: none!important;
        margin-top: 20%!important;
        background: #fff0!important;
    }

    .txt-white{
        color: white;
    }

    .modal-bg{
        position: absolute;
        top: 0;
        width: 100%;
        height: 100%;
        z-index: 5;
        background: #2185d0;
    }

    /* Fade Transition Animation */
    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s;
    }
    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
        opacity: 0;
    }
    
</style>
