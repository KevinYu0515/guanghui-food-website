<template>
  <section id="about" data-aos="fade-up">
    <h2 class="title">{{ title }}</h2>
    <p class="content">{{ content }}</p>
  </section>
</template>

<script>
export default {
  data () {
    return {
      title: "關於",
      content:
        "光慧水煎包梧棲分店開幕於2021年10月初，傳承自於50年的老店--草屯光慧水煎包，口味有竹筍、高麗菜、冬粉三種(素食可食)，每一顆都是新鮮出爐，給客人最溫暖的點心\n(梧棲小吃店，路邊取餐，可預約預定，不接受外送)"
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/about.scss";
</style>
