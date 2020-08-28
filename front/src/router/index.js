import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import CTF from "../views/CTF.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      requireAuth: true,
    },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/ctf",
    name: "CTF",
    component: CTF,
    meta: {
      requireAuth: true,
    },
  },
];

const router = new VueRouter({
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((r) => r.meta.requireAuth)) {
    /* 验证是否有session，有则next，没有则跳转至登录界面，或者后端返回401也跳转到登录界面 */
    if (Vue.$cookies.isKey("session")) {
      next();
    } else {
      console.log(Vue.$cookies.isKey("session"));
      next({
        path: "/login",
      });
    }
  } else {
    next();
  }
});

export default router;
