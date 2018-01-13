<template>
    <div id="login">
        <div class="ui centered card">
            <div class="content">
                <div class="ui form">
                    <div class="field">
                        <label></label>
                        <input type="text" v-model="username" @click="changeinputBorder($event, 'Username')" id="username" placeholder="Username" required="required">
                    </div>
                    <div class="field">
                        <label></label>
                        <input type="password" v-model="password"  @click="changeinputBorder($event, 'Password')" id="password" placeholder="Password" required="required">
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
        var user = document.getElementById ("username")
        var pass = document.getElementById ("password")
        if (this.username == null || this.username == '') {
            user.setAttribute("placeholder", "You must enter a username")
            user.style.border = "1px solid #db2828"
        }
        else if (this.password == null || this.password == '') {
            pass.setAttribute("placeholder", "You enter a password")
            pass.style.border = "1px solid #db2828"
        }
        else {
            this.loading = true
            user.setAttribute("disabled", "disabled")
            pass.setAttribute("disabled", "disabled")
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
    },
    changeinputBorder: function (event, name) {
        event.target.placeholder = name
        document.getElementById(event.target.id).style.border = "1px solid rgba(34,36,38,.15)"
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
        margin-top: 10%!important;
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

    *::-webkit-input-placeholder {
        color: red;
    }
    *:-moz-placeholder {
        /* FF 4-18 */
        color: red;
    }
    *::-moz-placeholder {
        /* FF 19+ */
        color: red;
    }
    *:-ms-input-placeholder {
        /* IE 10+ */
        color: red;
    }
    
</style>
