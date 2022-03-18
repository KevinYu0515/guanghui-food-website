<template>
  <div class='home'>
    <Navbar></Navbar>
    <section class="sec1">
      <ul>
        <li>週一 0600~0900 1500~1700</li>
        <li>週二 0600~0900 1500~1700</li>
        <li>週三 0600~0900 1500~1700</li>
        <li>週四 0600~0900 1500~1700</li>
        <li>週四 0600~0900 1500~1700</li>
        <li>週四 0600~0900 1500~1700</li>
        <li>週四 0600~0900 1500~1700</li>
      </ul四
    </secti四n>
    <section class="sec2"></section>
    <section class="sec3"></section>
    <section class="sec4"></section>
    <section class="sec5"></section>
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
    height:55vh;
    background: url("../assets/store.jpg");
    background-size: cover;
  }
}
.home_picture{
  height:80%;
  width:80%;
}
</style>
