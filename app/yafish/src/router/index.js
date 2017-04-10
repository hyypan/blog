import Vue from 'vue'
import Router from 'vue-router'
// import Hello from '@/components/Hello'
// import Content from '@/components/Content'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'Hello',
    //   component: Hello
    // },
    // {
    //   path: '/content',
    //   name: 'content',
    //   component: Content
    // }
    {
      path: '/content', name: 'Content', component: require('../components/Content.vue')
    }
  ]
})
