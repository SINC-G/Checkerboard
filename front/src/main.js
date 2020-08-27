import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import './plugins/element.js'
import router from './router'
import cookie from './plugins/cookie'

Vue.config.productionTip = false

new Vue({
  router,
  cookie,
  render: h => h(App)
}).$mount('#app')
