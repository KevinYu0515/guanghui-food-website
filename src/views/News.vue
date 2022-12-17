<template>
  <section id="news" v-show="true">
      <h1>{{ title }}</h1>
      <p v-for="(content, index) in contents" :key="index">
        {{ content }}
      </p>
    </section>
</template>

<script>
import { news } from "../firebase"
import { getDoc } from "firebase/firestore"
import newsJson from "../../python/news.json"
import { getCurrentInstance } from "vue"
export default {
  data () {
    return {
      title: "",
      contents: ""
    }
  }
}
</script>

<script setup>
const Instance = getCurrentInstance()
;(function () {
  getDoc(news)
    .then((response) => {
      Instance.data.title = response.data().title
      if (newsJson.length) {
        Instance.data.contents[0] = newsJson[0].content
      } else Instance.data.contents = response.data().content
    })
})()
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/news.scss";
</style>
