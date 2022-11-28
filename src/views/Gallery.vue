<template>
  <section id="photos" data-aos="fade-up">
    <!-- 主標 -->
    <div class="content-titleWrapper">
      <i class="strips-red"></i>
      <p class="content-title">
        <slot name="sectionTitle"></slot>
      </p>
      <i class="strips-red"></i>
    </div>
    <p class="content-description">
      <slot name="sectionTitleContent"></slot>
    </p>
    <!-- 寬版架構-相片藝廊 -->
    <div class="wrapper" v-show="!mobile">
      <div class="gallery">
        <div class="image" v-for="(img, index) in images" :key="index">
          <span @click="imgClick(index)">
            <img class="initial_img" :src="require('@/assets/picture/' + img.src + '.jpg')" alt="picture"/>
          </span>
        </div>
        <teleport to="body">
          <Popup :open="isOpen" @close="isOpen = !isOpen">
            <template #imageName>{{ images[imgIndex].name }}</template>
            <template #img><img height="400" width="400" :src="require('@/assets/picture/' + images[imgIndex].src + '.jpg')" /></template>
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
        :loop="true"
        :autoplay="{ delay: 1000, disableOnInteraction: false}"
      >
        <swiper-slide v-for="(img, index) in images" :key="index">
          <img :src="require('@/assets/picture/' + img.src + '.jpg')"  />
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
import json from "../../python/text.json"

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
      images: json[3].images
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/gallery.scss";
</style>
