<template>
    <div id="login">
        <div class="ui centered card">
            <div class="content">
                <!-- <div class="ui form"> -->
                    <div class="field">
                        <div id="input-user" class="ui labeled input">
                            <div class="ui basic standard right pointing label">
                                <i class="blue user circle icon"></i>
                            </div>
                            <input type="text" v-model="username" @blur="onBlur($event, 'Username')" @focus="onFocus" id="username" placeholder="Username">
                        </div>
                        <label class="label-username">Username</label>
                    </div>
                    <div class="field">
                        <div id="input-password" class="ui labeled input">
                            <div class="ui basic standard right pointing label">
                                <i class="blue privacy icon"></i>
                            </div>
                            <input type="password" v-model="password"  @blur="onBlur($event, 'Password')" @focus="onFocus" @keypress="postChoice" id="password" placeholder="Password">
                        </div>
                        <label class="label-password">Password</label>
                    </div>
                <!-- </div> -->
            </div>
            <div class="ui animated fade bottom attached primary button" @click.prevent="postChoice">
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
    </div>
</template>

<script>
import { loginUrl } from "../config"
import api from "../services/api"
import userService from "../services/userService"

// import { UserStore } from "../store/store";
export default {
    name: "Login",
    data () {
        return {
            username: null,
            password: null,
            loading: false,
            // userObj: {
            //     username: null,
            //     password: null,
            //     login: null
            // }
        }
    },
    mounted () {
        // console.log(this.$store.state.logged)
    },
    methods: {
        async postLogin () {
            const postData = {
                user: this.username,
                pass: this.password
            }
            var user = document.getElementById ("username");
            var pass = document.getElementById ("password");
            if (this.username == null || this.username == '') {
                var element = document.getElementById ("input-user");
                user.setAttribute("placeholder", "You must enter a username");
                element.classList.add("error");
            }
            else if (this.password == null || this.password == '') {
                var element = document.getElementById ("input-password");
                pass.setAttribute("placeholder", "You must enter a password");
                element.classList.add("error");
            }
            else {
                this.loading = true;
                user.setAttribute("disabled", "disabled")
                pass.setAttribute("disabled", "disabled")

                await userService.login({
                    user : this.username,
                    pass : this.password
                })
                .then(response => {
                    console.log(response.data)
                    this.loading = false;
                    user.removeAttribute("disabled")
                    pass.removeAttribute("disabled")

                    if ( response.data['login'] == true) {
                        this.$store.dispatch('setLogged', true)
                        this.$store.dispatch('setUsername', this.username)
                        console.log('State: ', this.$store.state)
                        this.$router.push({path: '/'})
                    }
                }).catch(err => {
                    console.log('Error: ', err.response.data)
                })

                // this.$http.post(loginUrl, postData ,response => {
                //     //error callback
                //     this.loading = false;
                //     user.removeAttribute("disabled");
                //     pass.removeAttribute("disabled");
                // }).then(response => {
                //     //Success callback
                //     console.log(response.data)
                //     this.loading = false;
                //     user.removeAttribute("disabled");
                //     pass.removeAttribute("disabled");

                //     if ( response.data['login'] == true) {
                //         this.$store.dispatch('setLogged', true);
                //         this.$store.dispatch('setUsername', this.username);
                //         console.log('State: ', this.$store.state)
                //         this.$router.push({path: '/'});
                //     }
                // });
            }
        },
        onFocus: function (event) {
            // console.log(event)
            event.target.placeholder = ''
            document.getElementById(event.target.parentElement.id).classList.add("focus")
            document.getElementById(event.target.parentElement.id).classList.remove("error")
        },
        postChoice (event) {
            if (event.key == "Enter" || event.key == null) {
                this.postLogin()
            }
            else {
                this.onFocus(event)
            }
        },
        onBlur: function (event, placeholder) {
            event.target.placeholder = placeholder
            document.getElementById(event.target.parentElement.id).classList.remove("focus")
            // if ((event.target.value == null || event.target.value == '') && event.target.parentElement.id == 'input-user') {
            //     document.getElementById(event.target.parentElement.id).classList.add("error")
            //     document.getElementById(event.target.id).setAttribute("placeholder", "You must enter a username")
            // }
            // else if ((event.target.value == null || event.target.value == '') && event.target.parentElement.id == 'input-password') {
            //     document.getElementById(event.target.parentElement.id).classList.add("error")
            //     document.getElementById(event.target.id).setAttribute("placeholder", "You must enter a password")
            // }
        }
    }
}
</script>

<style>
    #login{
        margin: 20% auto;
    }

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

    .content label{
        font-weight: lighter!important;
        position: absolute;
        /* top: 10px; */
        left: 15px;
        z-index: -1;
        transition: .15s all ease-in-out;
    }

    .ui.input{
        width: 100%;
        margin: 10px auto;
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
