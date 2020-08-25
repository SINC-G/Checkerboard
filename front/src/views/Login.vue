<template>
  <div>
    <el-form :model="loginForm" :rules="loginRules">
      <div>
        <h3 class="title">Login</h3>
      </div>

      <el-form-item prop="username">
        <el-input
          v-model="loginForm.username"
          placeholder="Username"
          name="username"
          type="text"
          tabindex="1"
        />
      </el-form-item>

      <el-form-item prop="password">
        <el-input
          :key="passwordType"
          v-model="loginForm.password"
          :type="passwordType"
          placeholder="Password"
          name="password"
          tabindex="2"
          auto-complete="on"
          @keyup.enter.native="handleLogin"
        />
      </el-form-item>

      <el-button
        :loading="loading"
        type="primary"
        style="width:100%;margin-bottom:30px;"
        @click.native.prevent="handleLogin"
      >Login</el-button>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
      },
      loginRules: {
        username: [{ required: true, trigger: "blur" }],
        password: [{ required: true, trigger: "blur" }],
      },
      loading: false,
      passwordType: "password",
      redirect: undefined,
    };
  },
  methods: {
    handleLogin() {
      this.axios
        .post("/login", {
          username: this.loginForm.username,
          password: this.loginForm.password,
        })
        .then(function (response) {
          console.log(response.status);
          // 其实是应该走后台路由
        })
        .catch(function (error) {
          console.log(error.response);
        });
    },
  },
};
</script>

<style>
</style>

<style scoped>
</style>
