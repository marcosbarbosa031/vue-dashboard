import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import DashHome from '@/components/DashHome'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login,
      props: true
    },
    {
      path: '/home',
      name: 'DashHome',
      component: DashHome,
      props: true
    }
  ]
})
