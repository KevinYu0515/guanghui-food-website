<template>
  <section id="photos" data-aos="fade-up" data-aos-duration="1000">
      <!-- 主標 -->
        <div class="content-titlewrapper">
          <i class="decoration"></i>
          <p class="content-title">{{title}}</p>
          <i class="decoration"></i>
        </div>
        <!-- 寬版架構-相片藝廊 -->
          <div class="wrapper" v-show="!mobile">
              <div class="gallery">
                  <div class="image" v-for="(img, index) in images" :key="index">
                    <span><img :src="require(`@/assets/picture/${img}.jpg`)" alt=""></span>
                </div>
              </div>
          </div>
          <!-- 相片彈出檢視窗 -->
          <div class="preview-box" v-show="!mobile">
            <div class="details">
                <span class="title">Image <p class="current-img"></p> of <p class="total-img"></p></span>
                <span class="icon fas fa-times"></span>
            </div>
            <div class="image-box" v-show="!mobile">
                <div class="slide prev"><i class="fas fa-angle-left"></i></div>
                <div class="slide next"><i class="fas fa-angle-right"></i></div>
                <img src="" alt="">
            </div>
        </div>
        <div class="shadow"></div>

        <!-- 窄版架構-swiper -->
        <div class="swiper-area">
            <swiper
                v-show="mobile"
                :slides-per-view="1"
                :space-between="50"
                :modules="modules"
                :pagination="{ clickable: true, dynamicBullets: true }"
                @swiper="onSwiper"
                @slideChange="onSlideChange"
            >
                <swiper-slide v-for="(img, index) in images" :key="index">
                    <img :src="require(`@/assets/picture/${img}.jpg`)"/>
                </swiper-slide>

            </swiper>
        </div>

    </section>
</template>


<script>
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Navigation, Pagination } from 'swiper'
import 'swiper/swiper-bundle.css'

export default {
    components: {
        Swiper,
        SwiperSlide,
    },
    setup() {
        const onSwiper = (swiper) => {
        console.log(swiper);
      };
      const onSlideChange = () => {
        console.log('slide change');
      };
        return {
            onSwiper,
            onSlideChange,
            modules: [Navigation, Pagination],
        };
    },


    data(){

        return{
            mobile:null,
            images:['001','002','003','004','005','006','007'],
            title:"相關照片",
        }
    },

    created(){
      window.addEventListener('resize', this.checkScreen);
      this.checkScreen();
    },
    methods:{
        checkScreen(){
            this.windowWidth = window.innerWidth;
            if(this.windowWidth <= 850){
                this.mobile = true;
                return
                }
            this.mobile = false;
            return;
        },
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/gallery.scss";
</style>