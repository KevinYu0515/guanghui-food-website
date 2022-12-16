<template>
  <section id="about" data-aos="fade-up">
    <h2 class="title">{{ title }}</h2>
    <p class="content" style="white-space:pre-wrap; word-break:break-all">{{ content }}</p>
  </section>
</template>

<script>
import { about } from "../firebase"
import { getDoc } from "firebase/firestore"
import { onMounted, getCurrentInstance } from "@vue/runtime-core"
export default {
  data () {
    return {
      title: "",
      content: ""
    }
  }
}
</script>

<script setup>
const Instance = getCurrentInstance()
onMounted(() => {
  getDoc(about)
    .then((response) => {
      Instance.data.title = response.data().title
      Instance.data.content = response.data().content.replace(" ", "\n")
    })
})
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/about.scss";
</style>
