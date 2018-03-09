<template>
    <div class="transaction">
      <div class="menu-holder">
          <side-menu :menu="4"></side-menu>
      </div>
      <div class="dash-content">

        <table class="ui sortable celled definition table">
            <thead>
                <tr>
                    <th></th>
                    <th class="sorted ascending">No.</th>
                    <th class="">Data</th>
                    <th class="">No. Empresa</th>
                    <th class="">Nome</th>
                    <th class="">Valor da Compra</th>
                    <th class="">Valor Transferido</th>
                    <th class="">Valor Convertido</th>
                    <th class="">Moeda</th>
                    <!-- <th class=""></th> -->
                    <th class="">Banco</th>
                    <th class="">Status</th>
                    <th class="">Ip</th>
                </tr>
            </thead>
            <tbody>
                <tr class="center aligned" v-for="(trans, idx) in transfers" :key="idx">
                    <td><i class="edit large icon row-edit"></i></td>
                    <td>{{trans.n_transferencia}}</td>
                    <td>{{trans.data}}</td>
                    <td>{{trans.empresa}}</td>
                    <td>{{trans.nome}}</td>
                    <td>{{trans.valor_compra}}</td>
                    <td>{{trans.valor_deposit}}</td>
                    <td>{{trans.valor_currency}}</td>
                    <td>{{trans.currency}}</td>
                    <!-- <td><img v-bind:src="trans.banco_img" height="40"></td> -->
                    <td>{{trans.banco}} - {{trans.banco_name}}</td>
                    <td>{{trans.status}}</td>
                    <td>{{trans.ip}}</td>
                </tr>
            </tbody>
        </table>
      </div>
    </div>
</template>

<script>
import transactionService from '../services/transactionService'
import SideMenu from './SideMenu'

export default {
    components: {
        'side-menu': SideMenu
    },
    data () {
        return {
            transfers : null
        }
    },
    methods: {
        async getTransfer () {
            await transactionService.transfer()
            .then(response => {
                this.transfers = response.data.return
            }).catch(err => {
                console.log("Error: ", err.response.data)
            })
        }
    },
    beforeCreate () {
        if (this.$store.state.logged == false) {
            this.$router.push({path: '/login'})
        }
    },
    created () {
        this.getTransfer()
    },
    mounted () {
        $('table').tablesort()
    }
}
</script>

<style>
    .transaction{
        display: flex;
    }

    .menu-holder{
        float: left;
        width: 210px;
    }

    .dash-content{
        padding: 20px;
        width: 70%;
        margin: 0 auto;
    }

    .row-edit{

    }

    .row-edit:hover{
        cursor: pointer;
    }
</style>
