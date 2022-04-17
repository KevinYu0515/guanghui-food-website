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
                <div class="image" v-for="(img, index) in images" :key="index">
                    <span @click="imgClick(index)"><img class="initial_img" :src="img.src" alt=""></span>
                </div>
                <Popup :open="isOpen_1" @close="isOpen_1 = !isOpen_1">
                    <template #imageName>{{images[0].name}}</template>
                    <template #img><img :src="images[0].src"/></template>
                </Popup>
                <Popup :open="isOpen_2" @close="isOpen_2 = !isOpen_2">
                    <template #imageName>{{images[1].name}}</template>
                    <template #img><img :src="images[1].src"/></template>
                </Popup>
                <Popup :open="isOpen_3" @close="isOpen_3 = !isOpen_3">
                     <template #imageName>{{images[2].name}}</template>
                    <template #img><img :src="images[2].src"/></template>
                </Popup>
                <Popup :open="isOpen_4" @close="isOpen_4 = !isOpen_4">
                    <template #imageName>{{images[3].name}}</template>
                    <template #img><img :src="images[3].src"/></template>
                </Popup>
                <Popup :open="isOpen_5" @close="isOpen_5 = !isOpen_5">
                    <template #imageName>{{images[4].name}}</template>
                    <template #img><img :src="images[4].src"/></template>
                </Popup>
                <Popup :open="isOpen_6" @close="isOpen_6 = !isOpen_6">
                    <template #imageName>{{images[5].name}}</template>
                    <template #img><img :src="images[5].src"/></template>
                </Popup>
                <Popup :open="isOpen_7" @close="isOpen_7 = !isOpen_7">
                    <template #imageName>{{images[6].name}}</template>
                    <template #img><img :src="images[6].src"/></template>
                </Popup>
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
                    <img :src="img.src"/>
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
        return {isOpen_1, isOpen_2, isOpen_3, isOpen_4, isOpen_5, isOpen_6, isOpen_7}
    },

    data() {
        return{
            images:[
                {
                    src:require("@/assets/picture/001.jpg"),
                    name:"高麗菜水煎包",
                },{
                    src:require("@/assets/picture/002.jpg"),
                    name:"竹筍水煎包",
                },{
                    src:require("@/assets/picture/003.jpg"),
                    name:"冬粉水煎包",
                },{
                    src:require("@/assets/picture/004.jpg"),
                    name:"水煎包下鍋瞜~",
                },{
                    src:require("@/assets/picture/005.jpg"),
                    name:"水煎包快起鍋瞜~",
                },{
                    src:require("@/assets/picture/006.jpg"),
                    name:"店面右斜側拍",
                },{
                    src:require("@/assets/picture/007.jpg"),
                    name:"店面左斜側拍",
                }],
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
        closeAllisOpen(){
            this.isOpen_1 = false;
            this.isOpen_2 = false;
            this.isOpen_3 = false;
            this.isOpen_4 = false;
            this.isOpen_5 = false;
            this.isOpen_6 = false;
            this.isOpen_7 = false;
        },
        imgClick(index){
            this.closeAllisOpen();
            switch(index){
                case 0: this.isOpen_1 = true; break
                case 1: this.isOpen_2 = true; break
                case 2: this.isOpen_3 = true; break
                case 3: this.isOpen_4 = true; break
                case 4: this.isOpen_5 = true; break
                case 5: this.isOpen_6 = true; break
                case 6: this.isOpen_7 = true; break
            }
        },
    }
}
</script>

<style lang='scss' scoped>
@import "@/assets/scss/Home/gallery.scss";
@import url('https://cdn-uicons.flaticon.com/uicons-bold-rounded/css/uicons-bold-rounded.css');
</style>