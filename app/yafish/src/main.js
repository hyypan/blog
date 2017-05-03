// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import configrouter from './router/index'

Vue.config.productionTip = false
/* eslint-disable no-new */
const routes=configrouter.options.routes
const router = new VueRouter({
  mode:'history',
  routes // short for routes: routes
})
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
window.router=router;



