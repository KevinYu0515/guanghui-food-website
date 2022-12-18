<template>
  <section id="news" v-show="true">
      <h1>{{ news.title }}</h1>
      <p v-for="(content, index) in news.contents" :key="index">
        {{ content }}
      </p>
    </section>
</template>

<script setup>
import { newsBlock } from "../firebase"
import { getDoc } from "firebase/firestore"
import newsJson from "../../python/news.json"
import { reactive } from "vue"
const news = reactive({
  title: "",
  contents: []
})

;(function () {
  getDoc(newsBlock)
    .then((response) => {
      news.title = response.data().title
      if (newsJson.length) {
        news.contents[0] = newsJson[0].content
      } else news.contents = response.data().content
    })
})()
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/news.scss";
</style>
