<template>
  <section id="comment" data-aos="fade-up">
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
    <!-- swiper -->
    <div class="swiper-area">
      <swiper
        :slidesPerView="!mobile ? 2 : 1"
        :spaceBetween="!mobile ? 20 : 30"
        :pagination="{ clickable: true, dynamicBullets: false }"
        :navigation="true"
        :loop="true"
      >
        <swiper-slide v-for="(comment, index) in comments" :key="index">
          <div class="comment-card">
            <StarRating
              :rating="toNumber(comment.star)"
              :read-only="true"
              :increment="0.5"
              :show-rating="false"
            ></StarRating>
            <div class="comment-content">{{ comment.content }}</div>
            <div class="headIcon"><img :src="comment.icon" /></div>
            <div class="name">{{ comment.name }}</div>
          </div>
        </swiper-slide>
      </swiper>
    </div>
  </section>
</template>

<script setup>
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import SwiperCore, { Navigation, Pagination } from "swiper"
import "swiper/swiper-bundle.css"
import { ref, onMounted, onUpdated } from "vue"

import axios from "axios"
import Popup from "../components/Popup.vue"
import StarRating from "vue-star-rating"

SwiperCore.use([Pagination, Navigation])
const comments = ref([])
const mobile = ref(null)
const toNumber = star => {
  return parseInt(star)
}
onMounted(() => {
  axios.get("http://localhost:8100/comments")
    .then((res) => {
      comments.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

onUpdated(() => {
  window.addEventListener("resize", checkScreen)
  checkScreen()
})

const checkScreen = () => {
  const windowWidth = window.innerWidth
  if (windowWidth <= 992) {
    mobile.value = true
    return
  }
  mobile.value = false
}
</script>

<script>
export default {
  components: { Swiper, SwiperSlide, Popup, StarRating }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/comment.scss";
@import url("https://cdn-uicons.flaticon.com/uicons-solid-straight/css/uicons-solid-straight.css");
@import url("https://cdn-uicons.flaticon.com/uicons-solid-rounded/css/uicons-solid-rounded.css");
@import url("https://cdn-uicons.flaticon.com/uicons-regular-rounded/css/uicons-regular-rounded.css");
</style>
