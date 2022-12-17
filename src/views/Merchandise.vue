<template>
  <section id="merchandise">
    <!-- 主標 -->
    <div class="content-titleWrapper">
      <i class="strips-red"></i>
      <h2 class="content-title">{{ title }}</h2>
      <i class="strips-red"></i>
    </div>
    <p class="content-description">{{ content }}</p>
    <!-- 各產品卡片內容 -->
    <!-- 寬版架構 -->
    <div class="cardWrapper" v-show="!mobile">
      <div class="card" v-for="(item, index) in cardItems" :key="index">
        <img :src="item.picture" />
        <div class="info">
          <h2>
            {{ item.name_ch }}<br />
            <span>{{ item.name_en }}</span>
            <p>{{ item.content }}</p>
          </h2>
        </div>
      </div>
    </div>
    <!-- 窄版架構 -->
    <div class="swiper-area">
      <swiper
        v-show="mobile"
        :slidesPerView="1"
        :spaceBetween="30"
        :centered-slides="true"
        :loop="true"
      >
        <swiper-slide v-for="(item, index) in cardItems" :key="index">
          <img :src="item.picture" />
          <div class="description">
            <p class="item-content">
              <span>{{ item.name_ch }}</span
              ><br />
              {{ item.name_en }}<br />
              {{ item.content }}
            </p>
          </div>
        </swiper-slide>
      </swiper>
    </div>
  </section>
</template>

<script>
import { merchandise } from "../firebase"
import { getDoc } from "firebase/firestore"
import { ref, onMounted, getCurrentInstance } from "vue"
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import "swiper/swiper-bundle.css"

export default {
  components: { Swiper, SwiperSlide },
  data () {
    return {
      title: "",
      content: "",
      cardItems: []
    }
  }
}
</script>

<script setup>
const Instance = getCurrentInstance()
const mobile = ref(null)

;(function () {
  getDoc(merchandise)
    .then((response) => {
      Instance.data.title = response.data().title
      Instance.data.content = response.data().content.replace(" ", "\n")
      Instance.data.cardItems = response.data().cards
    })
})()

onMounted(() => {
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

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/merchandise.scss";
</style>
