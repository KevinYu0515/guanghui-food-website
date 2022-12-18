<template>
  <section id="about">
    <h2 class="title">{{ about.title }}</h2>
    <p class="content" style="white-space:pre-wrap; word-break:break-all">{{ about.content }}</p>
  </section>
</template>

<script setup>
import { aboutBlock } from "../firebase"
import { getDoc } from "firebase/firestore"
import { reactive } from "vue"
const about = reactive({
  title: "",
  content: ""
})

;(function () {
  getDoc(aboutBlock)
    .then((response) => {
      about.title = response.data().title
      about.content = response.data().content.replace(" ", "\n")
    })
})()
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/about.scss";
</style>
