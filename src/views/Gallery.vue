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
                   v-for="(img, i) in images" :key="i"
                   >
                    <span><img :src="require(`@/assets/picture/${img}.jpg`)" alt=""></span>
                </div>
              </div>
          </div>

          <!-- 相片彈出檢視窗 -->
            <div class="preview-box">
                <div class="details">
                    <span class="title">Image</span>
                    <span class="icon fi fi-br-cross" ></span>
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
// import { onMounted } from 'vue'

SwiperCore.use([Pagination,Navigation])


export default {
    components: {
        Swiper,
        SwiperSlide,
    },

    data() {
        return{
            images:['001','002','003','004','005','006','007'],
            mobile:null,
        }
    },

    // setup(){
    //     onMounted(()=>{
    //         popup_image = document.querySelectorAll('.image span').forEach(image =>{
    //             image.onclick = () =>{
    //                 document.querySelector('perview-box').style.display = 'block';
    //                 document.querySelector('.image-box img').src = image.getAttribute('src');
    //             }
    //         });
    //         document.querySelector('.details icon').onclick = () =>{
    //         document.querySelector('preview-box').style.display = 'none';
    //         }
    //     });
    // },

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