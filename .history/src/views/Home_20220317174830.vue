<template>
  <div class='home'>
    <Navbar></Navbar>
    <section class="sec1"></section>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
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
  .sec1{
    width:100%;
    height:100vh;
    background:url("./assets/store.jpg");
    background-size: cover;
  }
}
.home_picture{
  height:80%;
  width:80%;
}
</style>
