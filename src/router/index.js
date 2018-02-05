import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import DashHome from '@/components/DashHome'
import SideMenu from '@/components/SideMenu'
import Card from '@/components/Card'

Vue.use(Router)

export default new Router({
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
      path: '/card',
      name: 'Card',
      component: Card
    }
  ]
})
