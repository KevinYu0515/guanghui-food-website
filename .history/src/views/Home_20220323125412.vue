<template>
  <div class='home'>
    <!-- <Navbar></Navbar> -->
    <section id="time">
      <p class="store-name">光慧水煎包</p>
      <p class="store-subname">(梧棲店)</p>
      <div class="timetable">
          <p class="timetable-subtitle">營業時間</p>
          <ul>
            <li>週一 &nbsp;&nbsp;<p>0600~0900 &nbsp;1500~1700</p></li>
            <li>週二 &nbsp;&nbsp;<p>0600~0900 &nbsp;1500~1700</p></li>
            <li>週三 &nbsp;&nbsp;<p>0600~0900 &nbsp;1500~1700</p></li>
            <li>週四 &nbsp;&nbsp;<p>0600~0900 &nbsp;1500~1700</p></li>
            <li>週五 &nbsp;&nbsp;<p>0600~0900 &nbsp;1500~1700</p></li>
            <li>週六 &nbsp;&nbsp;<p>0600~0900</p></li>
            <li>週日 &nbsp; 公休</li>
          </ul>
      </div>
    </section>
    <transition name="about">
      <section v-show="mobileNews" id="about">
        <h1>最新公告</h1>
        <p>清明連假公休</p>
      </section>
    </transition>
    <section id="merchandise">
      <div class="content-titlewrapper">
        <i class="decoration"></i>
        <p class="content-title">水煎包</p>
        <i class="decoration"></i>
      </div>
      <p class="content-description">
        主要賣三種水煎包，內餡分別為高麗菜、筍子、冬粉，每個售價15元<br>
        飲料有 紅茶、奶茶 另售10元
      </p>
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
        <div class="content-titlewrapper">
          <i class="decoration"></i>
          <p class="content-title">相關照片</p>
          <i class="decoration"></i>
        </div>
      <i class="btn">更多照片</i>
        <swiper
          :slides-per-view="3"
          :space-between="50"
          @swiper="onSwiper"
          @slideChange="onSlideChange"
          :pagination="pagination" :modules="modules" class="mySwiper"
        >
          <swiper-slide>
            <img :src="require('@/assets/picture/001.jpg')"/>
          </swiper-slide>
          <swiper-slide> <img :src="require('@/assets/picture/001.jpg')"/>
          </swiper-slide>
          <swiper-slide>Slide 3</swiper-slide>

        </swiper>
    </section>
    <section id="comment">
      <div class="content-titlewrapper">
          <i class="decoration"></i>
          <p class="content-title">相關評論</p>
          <i class="decoration"></i>
        </div>
        <img :src="require('@/assets/waiting.png')"/>
    </section>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import { Pagination } from 'swiper';

import 'swiper/swiper-bundle.css'
// import "swiper/css";
// import "swiper/css/pagination";
// import "./style.css";

export default {
  name: 'Home',
  components:{
    Swiper, SwiperSlide 
  },
  setup() {
    // const carouselSlides = ["001", "002", "003","004","005"];
    // return { carouselSlides };

    return {
      pagination: {
        clickable: true,
        renderBullet: function (index, className) {
          return '<span class="' + className + '">' + (index + 1) + "</span>";
      },
      modules: [Pagination],
      },
    }
  },
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

</style>

<style lang="scss" scoped>
@import "@/assets/scss/Home/home.scss";
@import "@/assets/scss/Home/time.scss";
@import "@/assets/scss/Home/about.scss";
@import "@/assets/scss/Home/merchandise.scss";
@import "@/assets/scss/Home/photos.scss";
@import "@/assets/scss/Home/comment.scss";
</style>