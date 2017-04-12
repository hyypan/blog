import Vue from 'vue'
import Router from 'vue-router'
// import Content from '@/components/Content'

Vue.use(Router)

export default new Router({
  mode: 'history',
  hashbang: false,
  routes: [
    {
      path: '/',
      name: 'hello',
      component: require('../components/Hello.vue')
    },
    {
      path: '/content', component: require('../components/Content.vue')
    }
  ]
})
