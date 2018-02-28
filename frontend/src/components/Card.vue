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
                <tr class="center aligned" v-for="card in cards">
                    <td><i class="edit large icon row-edit"></i></td>
                    <td>{{card.n_order}}</td>
                    <td>{{card.n_transacao}}</td>
                    <td>{{card.nome_cartao}}</td>
                    <td>{{card.n_cartao}}</td>
                    <td>{{card.tipo_cartao}}</td>
                    <td>{{card.valor_brl}}</td>
                    <td>{{card.valor_moeda}}</td>
                    <td>{{card.moeda}}</td>
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
import SideMenu from './SideMenu'

export default {
    components: {
        'side-menu': SideMenu
    },
    data () {
        return {
            username: this.$store.state.username,
            cards: {
                0: {
                    n_order: "1",
                    nome_cartao: "card 1",
                    data: "2018-10-05",
                    tipo_cartao: "credito",
                    n_cartao: "7895432154",
                    n_transacao: "A321H32D84R5132",
                    valor_brl: "500",
                    valor_moeda: "500",
                    moeda: "BRL",
                    status: "1",
                    empresa: "6",
                    ip: "192.168.1.2",
                },
                1: {
                    n_order: "2",
                    nome_cartao: "TEST CARD 2",
                    data: "2018-10-09",
                    tipo_cartao: "debito",
                    n_cartao: "9874200645",
                    n_transacao: "5SG751225C8S7",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                }
            }
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
