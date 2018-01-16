<template>
  <div class="dashHome">
      <div class="ui centered card">
          <p>Dashboard</p>
          <p>{{ dados.username }}</p>
      </div>
  </div>
</template>

<<script>
export default {
    props: ['dados'],
    data () {
        return {
            
        }
    },
    created () {
        
    }
}
</script>

<style>

</style>
