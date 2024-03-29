import Vue from "vue";
import "./plugins/axios";
import App from "./App.vue";
import "./plugins/element.js";
import router from "./router";

// cookies
Vue.use(require("vue-cookies"));

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
