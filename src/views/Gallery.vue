<template>
  <section id="photos" data-aos="fade-up">
    <!-- 主標 -->
    <div class="content-titleWrapper">
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
            ><img class="initial_img" :src="img.src" alt="picture"
          /></span>
        </div>
        <teleport to="body">
          <Popup :open="isOpen" @close="isOpen = !isOpen">
            <template #imageName>{{ images[imgIndex].name }}</template>
            <template #img><img height="400" width="400" :src="images[imgIndex].src" /></template>
          </Popup>
        </teleport>
      </div>
    </div>

    <!-- 窄版架構-swiper -->
    <div class="swiper-area">
      <swiper
        v-show="mobile"
        :slidesPerView="1.5"
        :spaceBetween="30"
        :centered-slides="true"
        :pagination="{ clickable: true, dynamicBullets: false }"
        :navigation="false"
        :loop="false"
      >
        <swiper-slide v-for="(img, index) in images" :key="index">
          <img :src="img.src" />
        </swiper-slide>
      </swiper>
    </div>
  </section>
</template>

<script setup>
import Popup from "../components/Popup.vue"
import { ref, onMounted } from "vue"
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import SwiperCore, { Navigation, Pagination } from "swiper"
import "swiper/swiper-bundle.css"

SwiperCore.use([Pagination, Navigation])

const isOpen = ref(false)
const imgIndex = ref(0)
const imgClick = i => {
  isOpen.value = true
  imgIndex.value = i
}

const mobile = ref(null)
onMounted(() => {
  window.addEventListener("resize", checkScreen)
  checkScreen()
})

const checkScreen = () => {
  const windowWidth = window.innerWidth
  if (windowWidth <= 550) {
    mobile.value = true
    return
  }
  mobile.value = false
}

</script>

<script>
export default {
  components: { Swiper, SwiperSlide, Popup },
  data () {
    return {
      images: [
        {
          src: require("@/assets/picture/001.jpg"),
          name: "高麗菜水煎包"
        },
        {
          src: require("@/assets/picture/002.jpg"),
          name: "竹筍水煎包"
        },
        {
          src: require("@/assets/picture/003.jpg"),
          name: "冬粉水煎包"
        },
        {
          src: require("@/assets/picture/004.jpg"),
          name: "水煎包下鍋瞜~"
        },
        {
          src: require("@/assets/picture/005.jpg"),
          name: "水煎包快起鍋瞜~"
        },
        {
          src: require("@/assets/picture/006.jpg"),
          name: "店面右斜側拍"
        },
        {
          src: require("@/assets/picture/007.jpg"),
          name: "店面左斜側拍"
        },
        {
          src: require("@/assets/picture/008.jpg"),
          name: "在 Uber Eats 上的總覽圖"
        },
        {
          src: require("@/assets/picture/009.jpg"),
          name: "竹筍水煎包"
        },
        {
          src: require("@/assets/picture/010.jpg"),
          name: "高麗菜水煎包"
        },
        {
          src: require("@/assets/picture/011.jpg"),
          name: "好吃的水煎包"
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/gallery.scss";

</style>
