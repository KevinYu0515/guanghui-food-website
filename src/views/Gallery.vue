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
                  <div class="image">
                    <span @click="isOpen_1 = true"><img class="initial_img" :src="require(`@/assets/picture/001.jpg`)" alt=""></span>
                    <Popup :open="isOpen_1" @close="isOpen_1 = !isOpen_1">
                        <img :src="require('@/assets/picture/001.jpg')"/>
                    </Popup>
                </div>
                <div class="image">
                    <span @click="isOpen_2 = true"><img class="initial_img" :src="require(`@/assets/picture/002.jpg`)" alt=""></span>
                    <Popup :open="isOpen_2" @close="isOpen_2 = !isOpen_2">
                        <img :src="require('@/assets/picture/002.jpg')"/>
                    </Popup>
                </div>
                <div class="image">
                    <span @click="isOpen_3 = true"><img class="initial_img" :src="require(`@/assets/picture/003.jpg`)" alt=""></span>
                    <Popup :open="isOpen_3" @close="isOpen_3 = !isOpen_3">
                        <img :src="require('@/assets/picture/003.jpg')"/>
                    </Popup>
                </div>
                <div class="image">
                    <span @click="isOpen_4 = true"><img class="initial_img" :src="require(`@/assets/picture/004.jpg`)" alt=""></span>
                    <Popup :open="isOpen_4" @close="isOpen_4 = !isOpen_4">
                        <img :src="require('@/assets/picture/004.jpg')"/>
                    </Popup>
                </div>
                <div class="image">
                    <span @click="isOpen_5 = true"><img class="initial_img" :src="require(`@/assets/picture/005.jpg`)" alt=""></span>
                    <Popup :open="isOpen_5" @close="isOpen_5 = !isOpen_5">
                        <img :src="require('@/assets/picture/005.jpg')"/>
                    </Popup>
                </div>
                <div class="image">
                    <span @click="isOpen_6 = true"><img class="initial_img" :src="require(`@/assets/picture/006.jpg`)" alt=""></span>
                    <Popup :open="isOpen_6" @close="isOpen_6 = !isOpen_6">
                        <img :src="require('@/assets/picture/006.jpg')"/>
                    </Popup>
                </div>
                <div class="image">
                    <span @click="isOpen_7 = true"><img class="initial_img" :src="require(`@/assets/picture/007.jpg`)" alt=""></span>
                    <Popup :open="isOpen_7" @close="isOpen_7 = !isOpen_7">
                        <img :src="require('@/assets/picture/007.jpg')"/>
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
        const isOpen_1 = ref(false);
        const isOpen_2 = ref(false);
        const isOpen_3 = ref(false);
        const isOpen_4 = ref(false);
        const isOpen_5 = ref(false);
        const isOpen_6 = ref(false);
        const isOpen_7 = ref(false);
        return {isOpen_1, isOpen_2, isOpen_3, isOpen_4, isOpen_5, isOpen_6, isOpen_7};
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