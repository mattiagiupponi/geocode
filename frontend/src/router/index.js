import Vue from 'vue'
import Router from 'vue-router'
import GetCoordinate from '@/components/GetCoordinate'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'GetCoordinate',
      component: GetCoordinate
    }
  ]
})
