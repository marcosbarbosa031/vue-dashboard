import api from './api.js'

export default {
    boleto () {
        return api().get('getboleto')
    },
    card () {
        return api().get('getcard')
    },
    transfer () {
        return api().get('gettransfer')
    },
    updateTransfer (dados) {
        return api().post('updatetransfer', dados)
    },
    cancelTransfer (dados) {
        return api().post('canceldeposit', dados)
    },
    deposit () {
        return api().get('getdeposit')
    }
}