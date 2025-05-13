<template>
  <section id="news" v-show="showNews">
    <img class="cloud-left" width="400" :src="require('@/assets/cloud2.png')"/>
    <img class="cloud-right" width="400" :src="require('@/assets/cloud2.png')"/>
    <div class="news-title">
      <img class="cloud-title" width="100" :src="require('@/assets/cloud1.png')"/>
      <h1>{{ news.title }}</h1>
      <img class="cloud-title" width="100" :src="require('@/assets/cloud1.png')" :style="{ transform: 'rotateY(180deg)' }"/>
    </div>
    <div class="news_content" v-for="(item, index) in news.contents" :key="index">
      <p class="date">{{ item.date }}</p>
      <p class="content">❝ {{ item.content }} ❞</p>
    </div>
    <a href="https://www.facebook.com/profile.php?id=100075103166257">詳細資訊</a>
  </section>
</template>

<script setup>
import { newsBlock } from "@/firebase"
import { getDoc } from "firebase/firestore"
import { reactive, ref } from "vue"
const news = reactive({
  title: "",
  contents: []
})
const showNews = ref(false)

;(function () {
  getDoc(newsBlock)
    .then((response) => {
      news.title = response.data().title
      news.contents = response.data().data
      if (response.data().count === 0) showNews.value = false
      else showNews.value = true
    })
})()
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/news.scss";
</style>
