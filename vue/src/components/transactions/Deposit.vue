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
                    <td><a>
                        <i class="edit large icon row-edit"></i>
                        </a></td>
                    <td>{{dep.id}}</td>
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
import transactionService from '../../services/transactionService'
import SideMenu from '../SideMenu'

export default {
    components: {
        'side-menu': SideMenu
    },
    data () {
        return {
            deposits: null,
            modal: false
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
        },
        async cancel() {
            await transactionService.cancelDeposit({
                id: this.deposits.id
            }).then(response => {
                // TODO mensagem de resposta
            })
        },
        async delete() {
            await transactionService.deleteDeposit({
                id: this.deposits.id
            }).then(response => {
                // TODO mensagem de resposta
            })
        },
        async update() {
            await transactionService.updateDeposit({
                id: this.deposits.id,
                empresa: this.deposits.empresa,
                nome: this.deposits.nome,
                valor_brl: this.deposits.valor_brl,
                valor_usd: this.deposits.valor_usd,
                moeda: this.deposits.moeda,
                data: this.deposits.data,
                n_deposito: this.deposits.n_deposito,
                imglink: this.deposits.imglink,
                status: this.deposits.status,
                ip: this.deposits.ip
            }).then(response => {
                // TODO mensagem de resposta
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
        width: 100vw;
        margin: 0;
        overflow: auto;
    }

    .row-edit{

    }

    .row-edit:hover{
        cursor: pointer;
    }
</style>
