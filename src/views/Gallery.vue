<template>
  <section id="photos">
    <div class="content-titleWrapper">
      <i class="strips-red"></i>
      <h2 class="content-title">{{ title }}</h2>
      <i class="strips-red"></i>
    </div>
    <p class="content-description">{{ content }}</p>
    <!-- 寬版架構-相片藝廊 -->
    <div class="wrapper" v-show="!mobile">
      <div class="gallery">
        <div class="image" v-for="(img, index) in images" :key="index">
          <span @click="imgClick(index)">
            <img class="initial_img" :src="img.picture" alt="picture"/>
          </span>
        </div>
        <teleport to="body">
          <Popup :open="isOpen" @close="isOpen = !isOpen">
            <template #imageName>{{ images[imgIndex].name }}</template>
            <template #img><img height="400" width="400" :src="images[imgIndex].picture" /></template>
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
          <img :src="images[index].picture"  />
        </swiper-slide>
      </swiper>
    </div>
  </section>
</template>

<script>
import Popup from "../components/Popup.vue"
import { gallery } from "../firebase"
import { getDoc } from "firebase/firestore"
import { ref, onMounted, getCurrentInstance } from "vue"
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import SwiperCore, { Navigation, Pagination } from "swiper"
import "swiper/swiper-bundle.css"

SwiperCore.use([Pagination, Navigation])
export default {
  components: { Swiper, SwiperSlide, Popup },
  data () {
    return {
      title: "",
      content: "",
      images: [{ name: "", picture: "" }]
    }
  }
}
</script>

<script setup>
const Instance = getCurrentInstance()
const isOpen = ref(false)
const imgIndex = ref(0)
const imgClick = i => {
  isOpen.value = true
  imgIndex.value = i
}

;(function () {
  getDoc(gallery)
    .then((response) => {
      Instance.data.title = response.data().title
      Instance.data.content = response.data().content
      Instance.data.images = response.data().types
    })
})()

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

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/gallery.scss";
</style>
