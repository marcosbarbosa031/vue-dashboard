<template>
    <div class="side-menu">
        <div class="item">
        Username: {{ username }}
            <div class="ui vertical menu">
                <a class="item"><i class="barcode icon"></i> Boleto</a>
                <a class="item"><i class="credit card alternative icon"></i> Cartão</a>
                <a class="item"><i class="money icon"></i> Depósito</a>
                <a class="item"><i class="exchange icon"></i> Transferência</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  data () {
      return {
          username: this.$store.username,
          transaction: "Cartão"
      }
  }
}
</script>

<style>
    .side-menu{
        float: left;
    }
</style>

