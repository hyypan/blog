import Vue from 'vue'
import Router from 'vue-router'
import VueRouter from 'vue-router'
// import Content from '@/components/Content'

Vue.use(Router)

export default new VueRouter({
  mode: 'history',
  hashbang: false,
  routes: [
    {
      path: '/',
      name: 'hello',
      component: require('../components/Hello.vue')
    },
    {
      path: '/content',
      component: require('../components/Content.vue'),
      name: 'content',
    },
    {
      path: '/content/Articles',
      component: require('../components/Articles.vue'),
      name:'articles',
    },
        {
      path: '/content/Hotest',
      component: require('../components/Hotest.vue'),
      name:'hotest',
    },
        {
      path: '/content/Newest',
      component: require('../components/Newest.vue'),
      name:'newest',
    },
        {
      path: '/content/Others',
      component: require('../components/Others.vue'),
      name:'others',
    },
    {
      path: '*',
      component: require('../components/common/404.vue'),
      name:'404',
    }
  ]
})
