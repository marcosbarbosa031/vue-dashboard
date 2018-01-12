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
            <button class="ui animated fade bottom attached primary button" @click.prevent="postLogin">
                <div class="visible content">Login</div>
                <div class="hidden content">
                    <i class="chevron right icon"></i>
                </div>
            </button>
        </div>
    </div>
</template>

<script>
export default {
  name: "Login",
  data () {
      return {
            username: null,
            password: null,
      }
  },
  methods: {
      postLogin () {
          this.$http.post('https://jsonplaceholder.typicode.com/posts', {
              title: this.username,
              body: this.password
          }).then(function (data) {
              console.log(data)
          })
      }
  }
}
</script>

<style>

</style>
