<template>
  <section id="comment">
    <!-- 主標 -->
    <div class="content-titleWrapper">
      <i class="strips-red"></i>
      <h2 class="content-title">{{ comment.title }}</h2>
      <i class="strips-red"></i>
    </div>
    <p class="content-description">{{ comment.content }}</p>
    <!-- swiper -->
    <div class="swiper-area" v-if="!mobile">
      <swiper
        :observer="true"
        :observeParents="true"
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
          <template #img><p style="font-size: .8rem; padding: 50px; white-space: pre-wrap; word-wrap: break-word;">{{ comments[commentIndex].content }}</p></template>
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
        <div class="comment-content" @click="commentClick(index)" style="white-space: pre-wrap; word-wrap: break-word;">{{ commentFilter2(comment.content, index) }}</div>
        <div class="headIcon"><img :src="comment.icon" /></div>
        <div class="name">{{ comment.name }}</div>
      </div>
    </div>
    <div class="btnGroup" v-if="mobile">
      <button :class="{'btn-active' : isMore , 'btn': !isMore}" class="more-btn" @click="readmore">
        <span>{{ buttonContent }}</span>
      </button>
    </div>
  </section>
</template>

<script setup>
import { commentBlock } from "../firebase"
import { getDoc } from "firebase/firestore"
import json from "../../python/comment.json"
import SwiperCore, { Navigation, Pagination } from "swiper"
import { ref, onUpdated, reactive, onMounted } from "vue"
import Popup from "../components/Popup.vue"
SwiperCore.use([Pagination, Navigation])

const mobile = ref(null)
const toNumber = star => parseInt(star)
const isOpen = ref(false)
const commentIndex = ref(0)
const isMore = ref(false)
const buttonContent = ref("更多評論")
const op = ref([true])
const comment = reactive({
  title: "",
  content: ""
})
const comments = json

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

const commentFilter2 = (content, index) => {
  if (content.length > 40 && op.value[index] === undefined) {
    return content.slice(0, 40) + "...閱讀更多"
  } else return content
}

const popup = i => {
  isOpen.value = true
  commentIndex.value = i
}

const commentClick = index => {
  op.value[index] = !op.value[index]
}

const readmore = () => {
  isMore.value = !isMore.value
  buttonContent.value = isMore.value ? "收起評論" : "更多評論"
}

;(function () {
  getDoc(commentBlock)
    .then((response) => {
      comment.title = response.data().title
      comment.content = response.data().content.replace(" ", "\n")
    })
})()

onMounted(() => {
  checkScreen()
})
onUpdated(() => {
  window.addEventListener("resize", checkScreen)
})
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/comment.scss";
@import "../assets/scss/index.scss";
</style>
