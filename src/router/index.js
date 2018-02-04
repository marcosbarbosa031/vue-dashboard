import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import DashHome from '@/components/DashHome'
import SideMenu from '@/components/SideMenu'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/home',
      name: 'DashHome',
      component: DashHome
    },
    {
      path: '/menu',
      name: 'SideMenu',
      component: SideMenu
    }
  ]
})
