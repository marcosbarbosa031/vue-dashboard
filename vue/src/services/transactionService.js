import api from './api.js'

export default {
    boleto () {
        return api().get('getboleto')
    },
    card () {
        return api().get('getcard')
    }
}