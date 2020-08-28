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
    <div>
      Welcom admin!
      <br />Admin的保险箱，里面保存了最重要的东西
    </div>
    <div>
      1. 保险箱是个前后端分离的项目，前端使用Vue，后端使用flask。
      <br />2. 保险箱是基于一个棋盘谜题。黑白块是随机生成的，
      <br />
      <!-- 3.可以再浏览器控制台看到翻转的是哪一块  -->
    </div>
    <div style="text-align:center">
      <Checkerboard :cb="cb" v-if="flag"></Checkerboard>
    </div>
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
          this.cb = res.data.cb;
          console.log("flip:" + res.data.flip);
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