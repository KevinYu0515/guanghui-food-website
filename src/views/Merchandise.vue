<template>
  <section id="merchandise" data-aos="fade-up">
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
    <!-- 各產品卡片內容 -->
    <!-- 寬版架構 -->
    <div class="cardWrapper" v-show="!mobile">
      <div class="card" v-for="(item, index) in cardItems" :key="index">
        <img :src="item.src" />
        <div class="info">
          <h1>
            {{ item.name }}<br />
            <span>{{ item.name2 }}</span>
            <p>{{ cardContent }}</p>
          </h1>
        </div>
      </div>
    </div>
    <!-- 窄版架構 -->
    <div
      class="card_mobile"
      v-show="mobile"
      v-for="(item, index) in cardItems"
      :key="index"
      data-aos="fade-left"
    >
      <img :src="item.src" />
      <div class="description">
        <p class="item-content">
          <span>{{ item.name }}</span
          ><br />
          {{ item.name2 }}<br />
          {{ cardContent }}
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue"

const cardItems = ref([
  {
    src: require("@/assets/picture/001.jpg"),
    name: "高麗菜水煎包",
    name2: "Fried bun stuffed with cabbage"
  },
  {
    src: require("@/assets/picture/002.jpg"),
    name: "竹筍水煎包",
    name2: "Fried bun stuffed with bamboo shoots"
  },
  {
    src: require("@/assets/picture/003.jpg"),
    name: "冬粉水煎包",
    name2: "Fried bun stuffed with bean thread"
  }])
const cardContent = ref("一個18元")

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

<style lang="scss" scoped>
@import "@/assets/scss/Home/merchandise.scss";
</style>
>
