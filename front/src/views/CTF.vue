<template>
  <div>{{message}}</div>
</template>

<script>
export default {
  data() {
    return {
      message: "Tips",
    };
  },
  mounted() {
    this.axios
      .get("/ctf")
      .then((res) => {
        this.message = res.data;
      })
      .catch((err) => {
        console.error(err);
      });
  },
};
</script>