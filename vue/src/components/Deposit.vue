<template>
    <div class="transaction">
      <div class="menu-holder">
          <side-menu :menu="3"></side-menu>
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
                    <th class="">Valor BRL</th>
                    <th class="">Valor Convertido</th>
                    <th class="">Moeda</th>
                    <th class="">Comprovante</th>
                    <th class="">Ip</th>
                </tr>
            </thead>
            <tbody>
                <tr class="center aligned" v-for="(dep, idx) in deposits" :key="idx">
                    <td><i class="edit large icon row-edit"></i></td>
                    <td>{{dep.n_deposito}}</td>
                    <td>{{dep.data}}</td>
                    <td>{{dep.empresa}}</td>
                    <td>{{dep.nome}}</td>
                    <td>{{dep.valor_brl}}</td>
                    <td>{{dep.valor_usd}}</td>
                    <td>{{dep.moeda}}</td>
                    <td><a v-bind:href="'https://gpmsolutions.com.br/_imagens/imagemdepositos/'+dep.imglink" target="_blank"><i class="file image outline icon"></i></a></td>
                    <td>{{dep.ip}}</td>
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
            deposits: null
        }
    },
    methods: {
        async getDeposits() {
            await transactionService.deposit()
            .then(response => {
                this.deposits = response.data.return
            }).catch(err => {
                console.log('Error: ', err.response.data)
            })
        }
    },
    beforeCreate () {
        if (this.$store.state.logged == false) {
            this.$router.push({path: '/login'})
        }
    },
    created () {
        this.getDeposits()
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
        width: 245px;
    }

    .dash-content{
        padding: 20px;
        /* padding-left: 50px; */
        width: 100%;
        margin: 0;
    }

    .row-edit{

    }

    .row-edit:hover{
        cursor: pointer;
    }
</style>
