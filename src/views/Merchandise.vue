<template>
  <section id="merchandise" data-aos="fade-up">
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
    <!-- 各產品卡片內容 -->
    <!-- 寬版架構 -->
    <div class="cardWrapper" v-show="!mobile">
      <div class="card" v-for="(item, index) in cardItems" :key="index">
        <img :src="require('@/assets/picture/' + item.src + '.jpg')" />
        <div class="info">
          <h2>
            {{ item.name }}<br />
            <span>{{ item.name2 }}</span>
            <p>{{ cardContent }}</p>
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
          <img :src="require('@/assets/picture/' + item.src + '.jpg')" />
          <div class="description">
            <p class="item-content">
              <span>{{ item.name }}</span
              ><br />
              {{ item.name2 }}<br />
              {{ cardContent }}
            </p>
          </div>
        </swiper-slide>
      </swiper>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import "swiper/swiper-bundle.css"
import json from "../../python/text.json"

const mobile = ref(null)
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

<script>
export default {
  components: { Swiper, SwiperSlide },
  data () {
    return {
      cardItems: json[2].cardItems,
      cardContent: json[2].cardContent
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/merchandise.scss";
</style>
