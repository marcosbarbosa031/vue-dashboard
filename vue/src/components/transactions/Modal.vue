<template>
    <div class="background">
        <div class="modal-tran ui centered card ">
            <div class="content" v-show="type == 3">
                <div class="ui divided items" v-for="(trans, idx) in transaction" :key="idx">
                    <input type="text" v-bind:value="trans">
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
        margin-top: 20%!important;
    }

    .background{
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background: #00000050;
    }
</style>
