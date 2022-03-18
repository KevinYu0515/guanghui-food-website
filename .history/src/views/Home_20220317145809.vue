<template>
  <div class='home'>
  </div>
</template>

<script>
import Navbar from '../Navbar.vue';
export default {
  name: 'Home',
  components:{
    Navbar
  }
}
</script>

<style lang="scss" scoped>
.home{
  margin: 0 auto 0 auto;
  background: #F5A02A;
  width: 65%;
  height: 100vh;
}
.home_picture{
  height:80%;
  width:80%;
}
</style>
