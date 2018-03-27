import api from './api.js'

export default {
    boleto () {
        return api().get('getboleto')
    },
    updateBoleto (dados) {
        return api().post('updateboleto', dados)
    },
    cancelBoleto (dados) {
        return api().post('cancelboleto', dados)
    },
    deleteBoleto (dados) {
        return api().post('deleteboleto', dados)
    },
    card () {
        return api().get('getcard')
    },
    updateCard (dados) {
        return api().post('updatecard', dados)
    },
    cancelCard (dados) {
        return api().post('cancelcard', dados)
    },
    deleteCard (dados) {
        return api().post('deletecard', dados)
    },
    transfer () {
        return api().get('gettransfer')
    },
    updateTransfer (dados) {
        return api().post('updatetransfer', dados)
    },
    cancelTransfer (dados) {
        return api().post('canceltransfer', dados)
    },
    deleteTransfer (dados) {
        return api().post('deletetransfer', dados)
    },
    deposit () {
        return api().get('getdeposit')
    },
    updateDeposit (dados) {
        return api().post('updatedeposit', dados)
    },
    cancelDeposit (dados) {
        return api().post('canceldeposit', dados)
    },
    deleteDeposit (dados) {
        return api().post('deletedeposit', dados)
    }
}