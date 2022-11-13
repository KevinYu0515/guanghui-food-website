<template>
  <div class="footer">
    <i class="decoration"></i>
     <section id="contact">
       <img class="logo" :src="logo">
      <div class="mapBox" v-show="!mobile">
        <iframe :src="mapSrc"
          style="border: 0"
          allowfullscreen=""
          loading="lazy"
          >
        </iframe>
      </div>
      <div class="contact-box">
        <div class="decoration2"></div>
        <h1>{{title}}</h1>
        <div v-for="(item, index) in contacts" :key="index" class="contact">
          <a :href="item.src">
            <img :src="item.icon" class="icon">
          </a>
          <span>{{item.name}}</span>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: "聯絡我們",
      logo: require("@/assets/logo.jpg"),
      contacts: [{
        src: "https://reurl.cc/g2vY6V",
        icon: require("@/assets/icon/facebook.png"),
        name: "facebook"
      }, {
        src: "",
        icon: require("@/assets/icon/calling.png"),
        name: "0952404078 | 0935368684"
      }, {
        src: "https://reurl.cc/9Gzn6a",
        icon: require("@/assets/icon/mapMark.png"),
        name: "臺中市梧棲區民和路一段37號"
      }],
      mapSrc: "https://reurl.cc/Lm1nnX",
      mobile: null
    }
  },
  created () {
    window.addEventListener("resize", this.checkScreen)
    this.checkScreen()
  },
  methods: {
    checkScreen () {
      this.windowWidth = window.innerWidth
      if (this.windowWidth <= 1120) {
        this.mobile = true
        return
      }
      this.mobile = false
      this.mobileNav = false
    }
  }

}
</script>

<style lang='scss'>
@import "@/assets/scss/footer.scss";
</style>

<style lang="scss" scoped>
@import url('https://cdn-uicons.flaticon.com/uicons-regular-straight/css/uicons-regular-straight.css');
@import url('https://cdn-uicons.flaticon.com/uicons-brands/css/uicons-brands.css');
@import url('https://cdn-uicons.flaticon.com/uicons-regular-rounded/css/uicons-regular-rounded.css');
</style>
