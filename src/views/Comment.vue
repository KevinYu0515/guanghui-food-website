<template>
  <section id="comment" data-aos="fade-up">
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
    <!-- swiper -->
    <div class="swiper-area" v-if="!mobile">
      <swiper
        :slidesPerView="!mobile ? 2 : 0"
        :spaceBetween="10"
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
            <div class="comment-content" @click="popup(index)">{{ commentFilter(comment.content) }}</div>
            <div class="headIcon"><img :src="comment.icon" /></div>
            <div class="name">{{ comment.name }}</div>
          </div>
        </swiper-slide>
      </swiper>
      <teleport to="body">
        <Popup :open="isOpen" @close="isOpen = !isOpen">
          <template #imageName><img :src="comments[commentIndex].icon" />{{ comments[commentIndex].name }}</template>
          <template #img><p style="padding: 50px; white-space: pre-wrap; word-wrap: break-word;">{{ comments[commentIndex].content }}</p></template>
        </Popup>
      </teleport>
    </div>
    <div class="commentList" :class="{'active': isMore}" v-if="mobile">
      <div class="comment-card" v-for="(comment, index) in comments" :key="index">
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
    </div>
    <div class="btnGroup" v-if="mobile">
      <i v-show="isMore" class="fi fi-br-angle-double-small-up icon"></i>
      <div :class="{'btn-active' : isMore , 'btn': !isMore}" @click="readmore">{{ buttonContent }}</div>
      <i v-show="!isMore" class="fi fi-br-angle-double-small-down icon"></i>
    </div>
  </section>
</template>

<script>
import json from "../../python/comment.json"
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import SwiperCore, { Navigation, Pagination } from "swiper"
import "swiper/swiper-bundle.css"
import { ref, onMounted, onUpdated } from "vue"

import Popup from "../components/Popup.vue"
import StarRating from "vue-star-rating"
SwiperCore.use([Pagination, Navigation])

export default {
  components: { Swiper, SwiperSlide, Popup, StarRating },
  data () {
    return {
      comments: json
    }
  }
}

</script>

<script setup>
const mobile = ref(null)
const toNumber = star => parseInt(star)
const isOpen = ref(false)
const commentIndex = ref(0)
const isMore = ref(false)
const buttonContent = ref("Read More")

onMounted(() => {
  checkScreen()
})

onUpdated(() => {
  window.addEventListener("resize", checkScreen)
})

const checkScreen = () => {
  const windowWidth = window.innerWidth
  if (windowWidth <= 992) {
    mobile.value = true
    return
  }
  mobile.value = false
}

const commentFilter = content => {
  if (content.length > 40) {
    return content.slice(0, 40) + "...閱讀更多"
  } else return content
}

const popup = i => {
  isOpen.value = true
  commentIndex.value = i
}

const readmore = () => {
  isMore.value = !isMore.value
  buttonContent.value = isMore.value ? "Read Less" : "Read More"
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/comment.scss";
@import "../assets/scss/index.scss";
</style>
