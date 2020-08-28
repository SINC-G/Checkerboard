<template>
  <div>
    <div>提示:{{message}}</div>
    <el-button @click="back">回到登录界面</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Tips",
    };
  },
  methods: {
    back() {
      this.$cookies.remove("session");
      this.$router.push({
        path: "/login",
      });
    },
  },
  mounted() {
    this.axios
      .get("/ctf")
      .then((res) => {
        this.message = res.data.tip;
      })
      .catch((err) => {
        console.error(err);
      });
  },
};
</script>