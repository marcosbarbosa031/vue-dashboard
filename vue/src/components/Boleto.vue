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
                <tr class="center aligned" v-for="boleto in boletos">
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

export default {
    components: {
        'side-menu': SideMenu
    },
    data () {
        return {
            username: this.$store.state.username,
            boletos: {
                0: {
                    num_pedido: "1",
                    nome: "teste 1",
                    data: "2018-10-05",
                    d_vencimento: "2018-10-09",
                    documento: "7895432154",
                    email: "aasd@ajsdh.com",
                    valor_brl: "500",
                    valor_moeda: "500",
                    moeda: "BRL",
                    status: "1",
                    empresa: "6",
                    ip: "192.168.1.2",
                },
                2: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                3: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                4: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                5: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                6: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                7: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                8: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                9: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                10: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                11: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                12: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                13: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                14: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                15: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                16: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                17: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                18: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                19: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                20: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                21: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                21: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                23: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                24: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                25: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
                    valor_brl: "100",
                    valor_moeda: "100",
                    moeda: "BRL",
                    status: "2",
                    empresa: "6",
                    ip: "192.168.1.4",
                },
                26: {
                    num_pedido: "2",
                    nome: "teste 2",
                    data: "2018-10-25",
                    d_vencimento: "2018-10-29",
                    documento: "98804975",
                    email: "emabsdi@ajsdh.com",
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
