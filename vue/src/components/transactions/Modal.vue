<template>
    <div class="background">
        <div class="modal-tran ui centered card">
            <div class="content" v-show="type == 3">
                <div class="ui divided items" >
                    <div class="item">
                        <div class="ui labeled input i-left">
                            <div class="ui right pointing label">
                                Nº Depósito
                            </div>
                            <input type="text" v-bind:value="transaction.n_deposito" readonly>
                        </div>
                        <div class="ui labeled input i-right">
                            <div class="ui right pointing label">
                                Empresa
                            </div>
                            <input type="text" v-bind:value="transaction.empresa" readonly>
                        </div>
                    </div>
                    <div class="item">
                        <div class="ui labeled input i-left">
                            <div class="ui right pointing label">
                                Nome
                            </div>
                            <input type="text" v-bind:value="transaction.nome" readonly>
                        </div>
                        <div class="ui labeled input i-right">
                            <div class="ui right pointing label">
                                Data
                            </div>
                            <input type="text" v-bind:value="transaction.data" readonly>
                        </div>
                    </div>
                    <div class="item">
                        <div class="ui labeled input i-left">
                            <div class="ui right pointing label">
                                Valor BRL
                            </div>
                            <input type="text" v-bind:value="transaction.valor_brl" readonly>
                        </div>
                        <div class="ui labeled input i-right">
                            <div class="ui right pointing label">
                                Valor Moeda
                            </div>
                            <input type="text" v-bind:value="transaction.valor_usd" readonly>
                        </div>
                    </div>
                    <div class="item">
                        <div class="ui labeled input i-left">
                            <div class="ui right pointing label">
                                Moeda
                            </div>
                            <input type="text" v-bind:value="transaction.moeda" readonly>
                        </div>
                        <div class="ui labeled input i-right">
                            <div class="ui right pointing label">
                                IP
                            </div>
                            <input type="text" v-bind:value="transaction.ip" readonly>
                        </div>
                    </div>
                </div>
                <button @click="test">Test</button>
                <button @click="close">Cancelar</button>
            </div>
        </div>
    </div>
</template>


<script>
    export default {
        props: {
            transaction: 'transaction',
            type: 'type'
        },
        data () {
            return {
            }
        },
        methods: {
            test () {
                console.log("Transactions: ", this.transaction)
                console.log("type: ", this.type)
            },
            close () {
                this.$emit('input', false)
            }
        }
    }
</script>

<style>
    .modal-tran{
        margin-top: 10%!important;
        width: 630px!important;
    }

    .background{
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background: #00000050;
    }

    .i-left{
        margin: 10px 5px!important;
    }

    .i-right{
        margin: 10px 5px!important;
    }
</style>
