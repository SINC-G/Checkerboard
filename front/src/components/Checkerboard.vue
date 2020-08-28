<template>
  <div id="view">
    <table cellpadding="0" cellspacing="0">
      <tr v-for="(row,i) in cb" :key="i">
        <td :class="singleClass(single)" v-for="(single,k) in row" :key="k">
          <button @click="postKey(i,k)" class="selectBut"></button>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    cb: Array,
  },
  methods: {
    singleClass(number) {
      if (number) {
        return { td01: true };
      } else {
        return { td00: true };
      }
    },
    postKey(i, k) {
      let key = i * 8 + k;
      this.axios
        .post("/chekerboard", { key: key })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>

<style scoped>
table {
  border: 1px solid #000;
}

td {
  width: 50px;
  height: 50px;
  background: #ff0;
  border-right: #cccccc solid 1px;
  border-left: #cccccc solid 1px;
  border-top: #cccccc solid 1px;
  border-bottom: #cccccc solid 1px;
}

.td00 {
  background: #fff;
}

.td01 {
  background: #000;
}

.selectBut {
  width: 100%;
  height: 100%;
  background-color: transparent;
  border-style: none;
}
</style>