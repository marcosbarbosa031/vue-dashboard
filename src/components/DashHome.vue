<template>
  <div class="dash-home">
      <div class="ui centered card">
          <p>Dashboard</p>
          <h1>{{ username }}</h1>
      </div>
  </div>
</template>

<<script>
export default {
    data () {
        return {
            username: this.$store.state.username
        }
    },
    beforeCreate () {
        // console.log(this.$store.state.username, this.$store.state.logged)
        if (this.$store.state.logged == false) {
            this.$router.push({path: '/'});
        }
    }
}
</script>

<style>

</style>
