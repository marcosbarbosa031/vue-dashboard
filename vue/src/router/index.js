import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import DashHome from '@/components/DashHome'
import Modal from '@/components/transactions/Modal'
import Card from '@/components/transactions/Card'
import Boleto from '@/components/transactions/Boleto'
import Transfer from '@/components/transactions/Transfer'
import Deposit from '@/components/transactions/Deposit'
import NotFound from '@/components/404'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'DashHome',
      component: DashHome
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/modal',
      name: 'Modal',
      component: Modal
    },
    {
      path: '/boleto',
      name: 'Boleto',
      component: Boleto
    },
    {
      path: '/card',
      name: 'Card',
      component: Card
    },
    {
      path: '/transfer',
      name: 'Transfer',
      component: Transfer
    },
    {
      path: '/deposit',
      name: 'Deposit',
      component: Deposit
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
