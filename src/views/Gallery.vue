<template>
  <section id="photos">
    <div class="content-titleWrapper">
      <i class="strips-red"></i>
      <h2 class="content-title">{{ gallery.title }}</h2>
      <i class="strips-red"></i>
    </div>
    <p class="content-description">{{ gallery.content }}</p>
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

<script setup>
import SwiperCore, { Navigation, Pagination } from "swiper"
import { galleryBlock } from "../firebase"
import { getDoc } from "firebase/firestore"
import { ref, onMounted, reactive } from "vue"
import Popup from "../components/Popup.vue"

SwiperCore.use([Pagination, Navigation])

const isOpen = ref(false)
const imgIndex = ref(0)
const gallery = reactive({
  title: "",
  content: ""
})
const images = ref([{ name: "", picture: "" }])

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

;(function () {
  getDoc(galleryBlock)
    .then((response) => {
      gallery.title = response.data().title
      gallery.content = response.data().content
      images.value = response.data().types
    })
})()

</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/gallery.scss";
</style>
