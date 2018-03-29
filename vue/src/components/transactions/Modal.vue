<template>
    <div class="background">
        <div class="modal-tran ui centered card ">
            <div class="content">
                <button @click="test">Test</button>
                <button @click="close">Cancelar</button>
            </div>
        </div>
    </div>
</template>


<script>
    export default {
        props: ['transaction'],
        data () {
            return {
            }
        },
        methods: {
            test () {
                console.log("Transactions: ", this.transaction)
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
