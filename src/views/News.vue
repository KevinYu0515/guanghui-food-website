<template>
  <section id="news" v-show="true">
      <h1>{{ news.title }}</h1>
      <div class="news_content" v-for="(item, index) in news.contents" :key="index">
        <img v-show="item.picture.length" width="300" height="300" :src="item.picture"/>
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
        news.contents[0].content = newsJson[0].content
        news.contents[0].picture = newsJson[0].picture
      } else news.contents = response.data().content
    })
})()
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/news.scss";
</style>
