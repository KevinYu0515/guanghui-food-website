<template>
  <div class='home'>
    <!-- <Navbar></Navbar> -->
    <section class="sec1">
      <div class="timetable">
          <p>營業時間</p>
          <ul>
            <li>週一 &nbsp;0600~0900 &nbsp;1500~1700</li>
            <li>週二 &nbsp;0600~0900 &nbsp;1500~1700</li>
            <li>週三 &nbsp;0600~0900 &nbsp;1500~1700</li>
            <li>週四 &nbsp;0600~0900 &nbsp;1500~1700</li>
            <li>週五 &nbsp;0600~0900 &nbsp;1500~1700</li>
            <li>週六 &nbsp;0600~0900 </li>
            <li>週日 公休</li>
          </ul>
      </div>
    </section>
    <section class="sec2">
      <div class="decoration"></div>
      <p>最新消息</p>
    </section>
    <section class="sec3">
        <div class="card">
          <img :src="require('@/assets/picture/001.jpg')">
          <div class="info">
            <h1>高麗菜水煎包</h1>
            <p>一個15元</p>
          </div>
        </div>
        <div class="card">
          <img :src="require('@/assets/picture/002.jpg')">
          <div class="info">
            <h1>筍子水煎包</h1>
            <p>一個15元</p>
          </div>
        </div>
        <div class="card">
          <img :src="require('@/assets/picture/003.jpg')">
          <div class="info">
            <h1>冬粉水煎包</h1>
            <p>一個15元</p>
          </div>
        </div>
    </section>
    <section class="sec4">
      div.decoratio
    </section>
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
@import "@/assets/scss/Home/home.scss";
@import "@/assets/scss/Home/section1.scss";
@import "@/assets/scss/Home/section2.scss";
@import "@/assets/scss/Home/section3.scss";
</style>
