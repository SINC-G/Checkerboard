<template>
  <div>
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
    >
      <el-menu-item index="1">主页</el-menu-item>
      <el-menu-item index="2" @click="getCB">保险箱</el-menu-item>
    </el-menu>
    <div>管理员的保险箱，里面保存了最重要的东西</div>
    <Checkerboard :cb="cb" v-if="flag"></Checkerboard>
  </div>
</template>

<script>
import Checkerboard from "@/components/Checkerboard";
export default {
  data() {
    return {
      flag: false,
    };
  },
  methods: {
    getCB() {
      this.axios
        .get("/checkerboard")
        .then((res) => {
          /* 返回的是硬币翻转（64个） */
          this.cb = res.data;
          this.flag = true;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  components: {
    Checkerboard,
  },
};
</script>