<template>
    <div class="side-menu-content">
        <!-- <div class="ui secondary vertical pointing large menu">
            <a class="item active"><i class="barcode icon"></i> Boleto</a>
            <a class="item"><i class="credit card alternative icon"></i> Cartão</a>
            <a class="item"><i class="money icon"></i> Depósito</a>
            <a class="item"><i class="exchange icon"></i> Transferência</a>
        </div> -->
        <div class="ui sidebar visible inverted vertical menu">
            <div class="ui divider"></div>
            <div class="side-menu-user">
               Usuário: <span class="username"> {{ username }} </span>
            </div>
            <div class="user-menu-container">
                <a class="user-link"><i class="configure large icon user-icon"></i></a>
                <a class="user-link" @click="logout"><i class="sign out large icon user-icon"></i></a>
            </div>
            <div class="ui divider"></div>
            <a id="boleto" class="item" @click="boleto"><i class="barcode icon"></i> Boleto</a>
            <a id="cartao" class="item" @click="card" ><i  class="credit card alternative icon"></i> Cartão</a>
            <a id="deposito" class="item"><i class="money icon"></i> Depósito</a>
            <a id="transferencia" class="item"><i class="exchange icon"></i> Transferência</a>
        </div>
    </div>
</template>

<script>
export default {
    props: ['menu'],
    data () {
        return {
            username: this.$store.state.username,
        }
    },
    mounted () {
        switch (this.menu) {
            case 1:
                document.getElementById("boleto").classList.add("active")
                document.getElementById("cartao").classList.remove("active")
                document.getElementById("deposito").classList.remove("active")
                document.getElementById("transferencia").classList.remove("active")
                break;
            case 2:
                document.getElementById("boleto").classList.remove("active")
                document.getElementById("cartao").classList.add("active")
                document.getElementById("deposito").classList.remove("active")
                document.getElementById("transferencia").classList.remove("active")
                break;
            case 3:
                document.getElementById("boleto").classList.remove("active")
                document.getElementById("cartao").classList.remove("active")
                document.getElementById("deposito").classList.add("active")
                document.getElementById("transferencia").classList.remove("active")
                break;
            case 4:
                document.getElementById("boleto").classList.remove("active")
                document.getElementById("cartao").classList.remove("active")
                document.getElementById("deposito").classList.remove("active")
                document.getElementById("transferencia").classList.add("active")
                break;
            default:
                break;
        }
    },
    methods: {
        boleto () {
            this.$router.push({path: '/'});
        },
        card () {
            this.$router.push({path: '/card'});
        },
        deposit () {
            this.$router.push({path: '/card'});
        },
        transfer () {
            this.$router.push({path: '/card'});
        },
        logout () {
            this.$store.dispatch('setLogged', false);
            this.$router.push({path: '/login'});
        }
    }
}
</script>

<style>
    .user-menu-container{
        text-align: center;
    }

    .side-menu-content{
        float: left;
    }

    .side-menu-user{
        padding: 20px;
        color: white;
    }

    span.username{
        margin-left: 5px;
    }

    .user-menu{
        text-align: center;
    }

    .user-link{
        padding-left: 20px;
        padding-right: 20px;
    }

    .user-link:hover{
        cursor: pointer;
        
    }

    .user-icon{
        transition: transform .2s;
    }

    .user-icon:hover{
        cursor: pointer;
        -ms-transform: scale(1.2); /* IE 9 */
        -webkit-transform: scale(1.2); /* Safari 3-8 */
        transform: scale(1.2);
    }
</style>

