<template>
  <div class="transaction">
      <div class="menu-holder">
          <side-menu :menu="1"></side-menu>
      </div>
      <div class="dash-content">

        <table class="ui sortable celled definition table">
            <thead>
                <tr>
                    <th></th>
                    <th class="sorted ascending">No.</th>
                    <th class="">Nome</th>
                    <th class="">Data Emissão</th>
                    <th class="">Data Vencimento</th>
                    <th class="">CPF</th>
                    <th class="">Email</th>
                    <th class="">Valor BRL</th>
                    <th class="">Valor Conv.</th>
                    <th class="">Moeda</th>
                    <th class="">Status</th>
                    <th class="">No. Empresa</th>
                    <th class="">IP</th>
                </tr>
            </thead>
            <tbody>
                <tr class="center aligned" v-for="(boleto, idx) in boletos" :key="idx">
                    <td><i class="edit large icon row-edit"></i></td>
                    <td>{{boleto.num_pedido}}</td>
                    <td>{{boleto.nome}}</td>
                    <td>{{boleto.data}}</td>
                    <td>{{boleto.d_vencimento}}</td>
                    <td>{{boleto.documento}}</td>
                    <td>{{boleto.email}}</td>
                    <td>{{boleto.valor_brl}}</td>
                    <td>{{boleto.valor_moeda}}</td>
                    <td>{{boleto.moeda}}</td>
                    <td>{{boleto.status}}</td>
                    <td>{{boleto.empresa}}</td>
                    <td>{{boleto.ip}}</td>
                </tr>
            </tbody>
        </table>
      </div>
  </div>
</template>

<script>
import SideMenu from './SideMenu'
import transactionService from "../services/transactionService"

export default {
    components: {
        'side-menu': SideMenu
    },
    data () {
        return {
            username: this.$store.state.username,
            boletos: null
        }
    },
    methods: {
        async getBoletos () {
            await transactionService.boleto()
            .then(response => {
                // console.log('funfou ', response.data.return)
                this.boletos = response.data.return
            }).catch(err => {
                console.log('Error: ', err.response.data)
            })
        }
    },
    beforeCreate () {
        if (this.$store.state.logged == false) {
            this.$router.push({path: '/login'});
        }
    },
    created () {
        this.getBoletos()
    },
    mounted () {
        $('table').tablesort()
        // $('.ui.sticky').sticky()
    }
}
</script>

<style>
    .transaction{
        display: flex;
    }

    .menu-holder{
        float: left;
        width: 247px;
    }

    .dash-content{
        padding: 20px;
        width: 100%;
    }

    .row-edit{

    }

    .row-edit:hover{
        cursor: pointer;
    }
</style>
