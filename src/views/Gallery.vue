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
          <span @click="imgClick(index)"
            ><img class="initial_img" :src="img.src" alt=""
          /></span>
        </div>
        <Popup :open="isOpen" @close="isOpen = !isOpen">
          <template #imageName>{{ images[imgIndex].name }}</template>
          <template #img><img :src="images[imgIndex].src" /></template>
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
          <img :src="img.src" />
        </swiper-slide>
      </swiper>
    </div>
  </section>
</template>

<script>
import Popup from "../components/Popup.vue";
import { ref } from "vue";
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import SwiperCore, { Navigation, Pagination } from "swiper";
import "swiper/swiper-bundle.css";

SwiperCore.use([Pagination, Navigation]);

export default {
  components: {
    Swiper,
    SwiperSlide,
    Popup,
  },
  setup() {
    const isOpen = ref(false);
    return { isOpen };
  },

  data() {
    return {
      images: [
        {
          src: require("@/assets/picture/001.jpg"),
          name: "高麗菜水煎包",
        },
        {
          src: require("@/assets/picture/002.jpg"),
          name: "竹筍水煎包",
        },
        {
          src: require("@/assets/picture/003.jpg"),
          name: "冬粉水煎包",
        },
        {
          src: require("@/assets/picture/004.jpg"),
          name: "水煎包下鍋瞜~",
        },
        {
          src: require("@/assets/picture/005.jpg"),
          name: "水煎包快起鍋瞜~",
        },
        {
          src: require("@/assets/picture/006.jpg"),
          name: "店面右斜側拍",
        },
        {
          src: require("@/assets/picture/007.jpg"),
          name: "店面左斜側拍",
        },
      ],
      mobile: null,
      imgIndex: 0,
    };
  },

  created() {
    window.addEventListener("resize", this.checkScreen);
    this.checkScreen();
  },
  methods: {
    checkScreen() {
      this.windowWidth = window.innerWidth;
      if (this.windowWidth <= 850) {
        this.mobile = true;
        return;
      }
      this.mobile = false;
      return;
    },
    imgClick(index) {
      this.isOpen = true;
      this.imgIndex = index;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/gallery.scss";
@import url("https://cdn-uicons.flaticon.com/uicons-bold-rounded/css/uicons-bold-rounded.css");
</style>
