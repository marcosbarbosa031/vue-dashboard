import api from './api'

export default {
    login (data) {
        return api().post('user/login', data)
    },
    register (data) {
        return api().post('user/register', data)
    }
}