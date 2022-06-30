<template>
  <header :class="{ 'scrolled-nav': scrollNav }">
    <!-- 寬版navbar -->
    <ul v-show="!mobile">
      <li v-for="(tab, index) in tabs.slice(0, 4)" :key="index">
        <router-link :to="{ name: tab.name, hash: tab.hash }">
          {{ tab.show }}
        </router-link>
      </li>
      <li>
        <router-link :to="`/${tabs[4].hash}`">{{ tabs[4].show }}</router-link>
      </li>
    </ul>
    <!-- 窄版navbar -->
    <div class="logo" v-show="mobile">
      <img :src="iconImg" />
    </div>
    <ul v-show="mobile">
      <li v-for="(tab, index) in tabs.slice(0, 4)" :key="index">
        <router-link :to="{ name: tab.name, hash: tab.hash }">
          <i :class="`${tab.icon}`"></i>
          <p class="iconText">{{ tab.show }}</p>
        </router-link>
      </li>
      <li>
        <router-link :to="`/${tabs[4].hash}`">
          <i :class="`${tabs[4].icon}`"></i>
          <p class="iconText">{{ tabs[4].show }}</p>
        </router-link>
      </li>
    </ul>
  </header>
</template>

<script>
export default {
  data: () => ({
    tabs: [
      {
        name: "Home",
        show: "首頁",
        hash: "#time",
        icon: "fi fi-sr-calendar"
      },
      {
        name: "Merchandise",
        show: "水煎包",
        hash: "#merchandise",
        icon: "fi fi-rr-restaurant"
      },
      {
        name: "Photos",
        show: "相簿",
        hash: "#photos",
        icon: "fi fi-br-picture"
      },
      {
        name: "Comment",
        show: "評論",
        hash: "#comment",
        icon: "fi fi-sr-comment-alt"
      },
      {
        name: "Contact",
        show: "聯絡我們",
        hash: "#contact",
        icon: "fi fi-sr-call-incoming"
      }
    ],
    iconImg: require("@/assets/picture/guanghui.png"),
    mobileNav: null,
    scrollNav: null,
    windowWidth: null,
    mobile: null
  }),

  created () {
    window.addEventListener("resize", this.checkScreen)
    this.checkScreen()
  },
  mounted () {
    window.addEventListener("scroll", this.updateScroll)
  },
  methods: {
    toggleMobileNav () {
      this.mobileNav = !this.mobileNav
    },
    updateScroll () {
      const scrollPosition = window.scrollY
      if (scrollPosition > 20) {
        this.scrollNav = true
        return
      }
      this.scrollNav = false
    },
    checkScreen () {
      this.windowWidth = window.innerWidth
      if (this.windowWidth <= 850) {
        this.mobile = true
        return
      }
      this.mobile = false
      this.mobileNav = false
    }
  }
}
</script>

<style scoped lang="scss">
@import "@/assets/scss/navbar.scss";
@import url("https://cdn-uicons.flaticon.com/uicons-bold-rounded/css/uicons-bold-rounded.css");
@import url("https://cdn-uicons.flaticon.com/uicons-solid-rounded/css/uicons-solid-rounded.css");
@import url("https://cdn-uicons.flaticon.com/uicons-bold-rounded/css/uicons-bold-rounded.css");
@import url("https://cdn-uicons.flaticon.com/uicons-solid-rounded/css/uicons-solid-rounded.css");
@import url("https://cdn-uicons.flaticon.com/uicons-solid-rounded/css/uicons-solid-rounded.css");
@import url("https://cdn-uicons.flaticon.com/uicons-regular-rounded/css/uicons-regular-rounded.css");
</style>
