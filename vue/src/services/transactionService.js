import api from './api'

export default {
    boleto (){
        return api().get('boleto/')
    }
}