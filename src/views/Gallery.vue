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
                  <div class="image" 
                   v-for="(img, i) in images" :key="i"
                   >
                   <!-- @click="popup=true" 可開啟相片彈出檢視窗功能 -->
                    <span @click="popup=false"><img :src="require(`@/assets/picture/${img}.jpg`)" alt=""></span>
                </div>
              </div>
          </div>

          <!-- 相片彈出檢視窗 -->
            <div class="preview-box" v-if="popup">
                <div class="details">
                    <span class="title">Image</span>
                    <span v-if="popup" @click="popup=false" class="icon fi fi-br-cross" ></span>
                </div>
                <div class="image-box">
                    <img :src="require('@/assets/picture/001.jpg')" alt="">
                </div>
            </div>
            <div class="shadow"></div>

        <!-- 窄版架構-swiper -->
         <div class="swiper-area">
            <swiper
                v-show="mobile"
                :slidesPerView="1"
                :spaceBetween="30"
                :pagination="{ clickable: true, dynamicBullets: false }"
                :navigation="true"
                :loop="true"
            >
                <swiper-slide v-for="(img, index) in images" :key="index">
                    <img :src="require(`@/assets/picture/${img}.jpg`)"/>
                </swiper-slide>
            </swiper>
        </div>

    </section>
</template>


<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import SwiperCore, { Navigation, Pagination } from 'swiper'
import 'swiper/swiper-bundle.css'

SwiperCore.use([Pagination,Navigation])


export default {
    components: {
        Swiper,
        SwiperSlide,
    },

    data() {
        return{
            images:['001','002','003','004','005','006','007'],
            title:"相關照片",
            mobile:null,
            popup:null,
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

<style lang='scss' scoped>
@import "@/assets/scss/Home/gallery.scss";
@import url('https://cdn-uicons.flaticon.com/uicons-bold-rounded/css/uicons-bold-rounded.css');
</style>