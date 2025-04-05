<template>
  <section id="news" v-show="true">
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
    <a href="">詳細資訊</a>
  </section>
</template>

<script setup>
import { newsBlock } from "../firebase"
import { getDoc } from "firebase/firestore"
import newsJson from "../../python/news.json"
import { reactive } from "vue"
const news = reactive({
  title: "",
  contents: [{ content: "", picture: "" }]
})

;(function () {
  getDoc(newsBlock)
    .then((response) => {
      news.title = response.data().title
      if (newsJson.length) {
        console.log(newsJson)
        newsJson.forEach((item, index) => {
          news.contents[index].date = item.date
          news.contents[index].content = item.content
        })
      } else news.contents[0].content = response.data().content
    })
})()
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/news.scss";
</style>
