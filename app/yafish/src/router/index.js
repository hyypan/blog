import Vue from 'vue'
import Router from 'vue-router'
import VueRouter from 'vue-router'
// import Content from '@/components/Content'

Vue.use(Router)

export default new VueRouter({
  hashbang: false,
  routes: [
    {
      path: '/',
      name: 'hello',
      // component: require('../components/Hello.vue')
      component:function (resolve) {
            require(['../components/hello.vue'], resolve)
          }
    },
    {
      path:'/index',
      name: 'index',
      component: require('../components/index.vue'),
    },
    {
      path: '/content',
      name: 'content',
      component:function (resolve) {
            require(['../components/content.vue'], resolve)
          }
    },
    {
      path: '/content/Articles',
      name:'articles',
      component: require('../components/articles.vue'),
    },
        {
      path: '/content/Hotest',
          name:'hotest',
      component: require('../components/hotest.vue'),
    },
        {
      path: '/content/Newest',
          name:'newest',
      component: require('../components/newest.vue'),
    },
        {
      path: '/content/Others',
          name:'others',
      component: require('../components/others.vue'),
    },
    {
      path: '/content/Detail',
      name: 'Detail',
      component: require('../components/detail.vue')
    },
    {
      path: '*',
      component: require('../components/common/404.vue'),
      name:'404',
    }
  ]
})
