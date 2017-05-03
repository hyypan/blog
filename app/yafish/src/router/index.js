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
      name: 'content',
      component: require('../components/Content.vue'),
    },
    {
      path: '/content/Articles',
      name:'articles',
      component: require('../components/Articles.vue'),
    },
        {
      path: '/content/Hotest',
          name:'hotest',
      component: require('../components/Hotest.vue'),
    },
        {
      path: '/content/Newest',
          name:'newest',
      component: require('../components/Newest.vue'),
    },
        {
      path: '/content/Others',
          name:'others',
      component: require('../components/Others.vue'),
    },
    {
      path: '*',
      component: require('../components/common/404.vue'),
      name:'404',
    }
  ]
})
