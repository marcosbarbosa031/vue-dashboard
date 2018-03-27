<template>
    <div class="transaction">
      <div class="menu-holder">
          <side-menu :menu="2"></side-menu>
      </div>
      <div class="dash-content">

        <table class="ui sortable celled definition table">
            <thead>
                <tr>
                    <th></th>
                    <th class="sorted ascending">No.</th>
                    <th class="">TID</th>
                    <th class="">Nome Cartão</th>
                    <th class="">No. Cartão</th>
                    <th class="">Tipo</th>
                    <th class="">Valor BRL</th>
                    <th class="">Valor Conv.</th>
                    <th class="">Moeda</th>
                    <th class="">Data</th>
                    <th class="">Status</th>
                    <th class="">No. Empresa</th>
                    <th class="">IP</th>
                </tr>
            </thead>
            <tbody>
                <tr class="center aligned" v-for="(card, idx) in cards" :key="idx">
                    <td><i class="edit large icon row-edit"></i></td>
                    <td>{{card.n_order}}</td>
                    <td>{{card.n_transacao}}</td>
                    <td>{{card.nome_cartao}}</td>
                    <td>{{card.n_cartao}}</td>
                    <td>{{card.tipo_cartao}}</td>
                    <td>{{card.valor_brl}}</td>
                    <td>{{card.valor_usd}}</td>
                    <td>{{card.currency}}</td>
                    <td>{{card.data}}</td>
                    <td>{{card.status}}</td>
                    <td>{{card.empresa}}</td>
                    <td>{{card.ip}}</td>
                </tr>
            </tbody>
        </table>
      </div>
    </div>
</template>


<script>
import SideMenu from '../SideMenu'
import transactionService from '../../services/transactionService'

export default {
    components: {
        'side-menu': SideMenu
    },
    data () {
        return {
            username: this.$store.state.username,
            cards: null
        }
    },
    methods: {
        async getCards() {
            await transactionService.card()
            .then(response => {
                // console.log('funfou ', response.data.return)
                this.cards = response.data.return
            }).catch(err => {
                console.log("Error: ", err.response.data)
            })
        },
        async cancel() {
            await transactionService.cancelCard({
                id: this.cards.id
            }).then(response => {
                // TODO mensagem de resposta
            })
        },
        async delete() {
            await transactionService.deleteCard({
                id: this.cards.id
            }).then(response => {
                // TODO mensagem de resposta
            })
        },
        async update() {
            await transactionService.updateCard({
                id: this.cards.id,
                nome_cartao: this.cards.nome_cartao,
                n_transacao: this.cards.n_transacao,
                tipo_cartao: this.cards.tipo_cartao,
                n_cartao: this.cards.n_cartao,
                n_order: this.cards.n_order,
                valor_brl: this.cards.valor_brl,
                valor_usd: this.cards.valor_usd,
                hora: this.cards.hora,
                data: this.cards.data,
                status_id: this.cards.status_id,
                status: this.cards.status,
                motivo: this.cards.motivo,
                currency: this.cards.currency,
                email: this.cards.email,
                data_inicio: this.cards.data_inicio,
                data_fim: this.cards.data_fim,
                tipo_pag: this.cards.tipo_pag
            }).then(response => {
                // TODO mensagem de resposta
            })
        }
    },
    created () {
        this.getCards()
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
