<template>
  <section id="news" v-show="true">
      <h1>{{ news.title }}</h1>
      <div class="news_content" v-for="(item, index) in news.contents" :key="index">
        <img v-if="item.picture.length" width="300" height="300" :src="item.picture"/>
        <p>{{ item.content }}</p>
      </div>
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
        newsJson.forEach((item, index) => {
          news.contents[index].content = item.content
          news.contents[index].picture = item.picture
        })
      } else news.contents[0].content = response.data().content
    })
})()
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/news.scss";
</style>
