<template>
  <section id="about" data-aos="fade-up">
    <h2 class="title">{{ title }}</h2>
    <p class="content">{{ content }}</p>
  </section>
</template>

<script>
import json from "../../python/text.json"
export default {
  data () {
    return {
      title: json[1].title,
      content: json[1].content
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/about.scss";
</style>
