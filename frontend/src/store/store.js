import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        logged: false,
        username: ''
    },
    mutations: {
        setLogged (state, log) {
            state.logged = log;
        },
        setUsername (state, user) {
            state.username = user;
        }
    },
    actions: {
        setLogged ({ commit }, log) {
            commit('setLogged', log)
        },
        setUsername ({ commit }, user){
            commit('setUsername', user)
        }
    }
})