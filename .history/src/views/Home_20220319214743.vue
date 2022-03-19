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
    <section id="about">
      <i class="decoration1">
        <h>最新消息</h>
      </i>
      <div class="content">

      </div>
    </section>
    <section class="sec3">
        <v-col class="card" v-for="(item,index) in goods" :key="index">
          <img :src="item.imgpath">
          <div class="info">
            <h1>{{item.name}}</h1>
            <p>一個15元</p>
          </div>
        </v-col>
        <!-- <div class="card">
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
        </div> -->
    </section>
    <section id="photos">
      <div class="decoration2"></div>
      <div class="swipper-wrapper">
        <div class="swiper-side">
          <img :src="require('@/assets/picture/004.jpg')">
        </div>
        <div class="swiper-side">
          <img :src="require('@/assets/picture/005.jpg')">
        </div>
        <div class="swiper-side">
          <img :src="require('@/assets/picture/001.jpg')">
        </div>
        <div class="swiper-side">
          <img :src="require('@/assets/picture/002.jpg')">
        </div>
        <div class="swiper-side">
          <img :src="require('@/assets/picture/003.jpg')">
        </div>
      </div>
      <div class="decoration3"></div>
    </section>
    <section id="contact">
      <div class="mapBox">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3637.857831780853!2d120.54562271494271!3d24.246750684347145!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x346915859dc0b4dd%3A0x37ba3c60d4fc0ca8!2z5YWJ5oWn5rC054WO5YyF77yI5qKn5qOy5bqX77yJ!5e0!3m2!1szh-TW!2stw!4v1647614092352!5m2!1szh-TW!2stw" 
         style="border:0;" allowfullscreen="" loading="lazy"></iframe>
      </div>
      <div class="contact-box">
        <div class="decoration4"></div>
        <h1>聯絡我們</h1>
        <p>電話：0952404078</p>
        <p style="margin-bottom: 20px;">地址：臺中市梧棲區民和路一段37號</p>
        <!-- <a src=" -->
        <i style="font-size: 5vmin;" class="fi fi-brands-facebook"></i>
      </div>
    </section>
  </div>
</template>

<script>
// import Navbar from '@/components/Navbar.vue';
export default {
  name: 'Home',
  // components:{
  //   Navbar
  // },
  data:()=>({
    good:[{
      name:"高麗菜水煎包",
      imgpath:'@/assets/picture/001.jpg'
    },
    {
      name:"筍子水煎包",
      imgpath:'@/assets/picture/002.jpg'
    },
    {
      name:"冬粉水煎包",
      imgpath:'@/assets/picture/003.jpg'
    }]
  })
}
</script>

<style scoped>
@import url('https://cdn-uicons.flaticon.com/uicons-brands/css/uicons-brands.css');
</style>

<style lang="scss" scoped>
@import "@/assets/scss/Home/home.scss";
@import "@/assets/scss/Home/section1.scss";
@import "@/assets/scss/Home/section2.scss";
@import "@/assets/scss/Home/section3.scss";
@import "@/assets/scss/Home/section4.scss";
@import "@/assets/scss/Home/section5.scss";
</style>
