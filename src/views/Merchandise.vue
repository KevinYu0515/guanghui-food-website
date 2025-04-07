<template>
  <section id="merchandise">
    <!-- 主標 -->
    <div class="content-titleWrapper">
      <i class="strips-red"></i>
      <h2 class="content-title">{{ merchandise.title }}</h2>
      <i class="strips-red"></i>
    </div>
    <div class="content-description">
      <p class="item" v-for="(item, index) in merchandise.content" :key="index">
        <span>{{ item.name }}</span>
        <span class="cost">{{ item.cost }} 元</span>
      </p>
    </div>
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
        :observer="true"
        :observeParents="true"
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

<script setup>
import { merchandiseBlock } from "@/firebase"
import { getDoc } from "firebase/firestore"
import { ref, onMounted, reactive } from "vue"

const merchandise = reactive({
  title: "",
  content: ""
})
const cardItems = ref([])
const mobile = ref(null)

const checkScreen = () => {
  const windowWidth = window.innerWidth
  if (windowWidth <= 992) {
    mobile.value = true
    return
  }
  mobile.value = false
}

;(function () {
  getDoc(merchandiseBlock)
    .then((response) => {
      merchandise.title = response.data().title
      merchandise.content = response.data().content.map((item) => {
        return {
          name: item.name,
          cost: item.cost
        }
      })
      cardItems.value = response.data().cards
    })
})()

onMounted(() => {
  window.addEventListener("resize", checkScreen)
  checkScreen()
})
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/merchandise.scss";
</style>
