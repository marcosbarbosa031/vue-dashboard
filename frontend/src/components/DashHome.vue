<template>
  <div class="dash-home">
      <div class="menu-holder">
          <side-menu :menu="0"></side-menu>
      </div>
  </div>
</template>

<<script>
import SideMenu from './SideMenu'

export default {
    components: {
        'side-menu': SideMenu
    },
    data () {
        return {
            username: this.$store.state.username,
        }
    },
    beforeCreate () {
        if (this.$store.state.logged == false) {
            this.$router.push({path: '/login'});
        }
    },
    mounted () {
        $('table').tablesort()
        $('.ui.sticky').sticky()
    }
}
</script>

<style>

</style>
