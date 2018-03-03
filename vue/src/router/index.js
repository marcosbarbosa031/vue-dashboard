import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import DashHome from '@/components/DashHome'
import SideMenu from '@/components/SideMenu'
import Card from '@/components/Card'
import Boleto from '@/components/Boleto'
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
      path: '/menu',
      name: 'SideMenu',
      component: SideMenu
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
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})