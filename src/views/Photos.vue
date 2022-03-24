<template>
  <section id="photos">
        <div class="content-titlewrapper">
          <i class="decoration"></i>
          <p class="content-title">相關照片</p>
          <i class="decoration"></i>
        </div>
      <i class="btn">更多照片</i>
      <swiper
        :slides-per-view="3"
        :space-between="10"
        :pagination='{"el": ".swiper-pagination"}'
        :modules="modules"
        @swiper="onSwiper"
        @slideChange="onSlideChange"
        data-observer="true"
      >
            <swiper-slide>
              <img :src="require('@/assets/picture/001.jpg')"/>
            </swiper-slide>
            <swiper-slide>
              <img :src="require('@/assets/picture/002.jpg')"/>
            </swiper-slide>
            <swiper-slide>
              <img :src="require('@/assets/picture/003.jpg')"/>
            </swiper-slide>
            <swiper-slide>
              <img :src="require('@/assets/picture/004.jpg')"/>
            </swiper-slide>
            <swiper-slide>
              <img :src="require('@/assets/picture/005.jpg')"/>
            </swiper-slide>
      </swiper>
          
      </section>
</template>

<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import { Pagination } from 'swiper';

import 'swiper/swiper-bundle.css'

export default {
    components:{
        Swiper,SwiperSlide
    },
    setup(){
        return{
        modules:[Pagination],
        }
    },

}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/photos.scss";
</style>