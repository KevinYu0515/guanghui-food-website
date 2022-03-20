<template>
  <div class='home'>
    <!-- <Navbar></Navbar> -->
    <section id="time">
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
      <img :src="require('@/assets/logo.jpg')">
    </section>
    <transition name="about">
      <section v-show="mobileNews" id="about">
        <i class="decoration1">
          <h>最新公告</h>
        </i>
      </section>
    </transition>
    <section id="merchandise">
      <div class="content-title">
      </div>
        <!-- <div class="card" v-for="(item,index) in goods" :key="index">
          <img :src="item.imgpath">
          <div class="info">
            <h1>{{item.name}}</h1>
            <p>一個15元</p>
          </div>
        </div> -->
        <div class="cardwrapper">
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
        </div>
      </section>
      <section id="photos">
        <i class="decoration2"></i>
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
  data(){
    return{
      mobileNews: null,
    }
  },
  mounted(){
    window.addEventListener('scroll',this.updateScroll);
  },
  methods:{
    updateScroll(){
      const scrollPosition = window.scrollY;
      if(scrollPosition > 100){
        this.mobileNews = true;
        return;
      }
      // this.mobileNews = false;
    },
  },
  // data:()=>({
  //   good:[{
  //     name:"高麗菜水煎包",
  //     imgpath:require('@/assets/picture/001.jpg')
  //   },
  //   {
  //     name:"筍子水煎包",
  //     imgpath:require('@/assets/picture/002.jpg')
  //   },
  //   {
  //     name:"冬粉水煎包",
  //     imgpath:require('@/assets/picture/003.jpg')
  //   }]
  // })
}
</script>

<style scoped>
@import url('https://cdn-uicons.flaticon.com/uicons-brands/css/uicons-brands.css');
</style>

<style lang="scss" scoped>
@import "@/assets/scss/Home/home.scss";
@import "@/assets/scss/Home/time.scss";
@import "@/assets/scss/Home/about.scss";
@import "@/assets/scss/Home/merchandise.scss";
@import "@/assets/scss/Home/photos.scss";
</style>