<template>
  <section id="photos" data-aos="fade-up">
      <!-- 主標 -->
        <div class="content-titlewrapper">
            <i class="decoration"></i>
            <p class="content-title">
                <slot name="sectionTitle"></slot>
            </p>
            <i class="decoration"></i>
        </div>
        <p class="content-description">
            <slot name="sectionTitleContent"></slot>
        </p>
        <!-- 寬版架構-相片藝廊 -->
          <div class="wrapper" v-show="!mobile">
              <div class="gallery">
                  <div class="image" 
                   v-for="(img, index) in images" :key="index"
                   >
                    <span @click="isOpen = true"><img :src="require(`@/assets/picture/${img}.jpg`)" alt=""></span>
                    <Popup :open="isOpen" @close="isOpen = !isOpen">
                        <img :src="require(`@/assets/picture/${img}.jpg`)"/>
                    </Popup>
                </div>
              </div>
          </div>

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
import Popup from "../components/Popup.vue"
import {ref} from "vue"
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import SwiperCore, { Navigation, Pagination } from 'swiper'
import 'swiper/swiper-bundle.css'

SwiperCore.use([Pagination,Navigation])


export default {
    components: {
        Swiper,
        SwiperSlide,
        Popup,
    },
    setup(){
        const isOpen = ref(false);
        return {isOpen};
    
    },

    data() {
        return{
            images:['001','002','003','004','005','006','007'],
            mobile:null,
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