<template>
  <header :class="{ 'scrolled-nav': scrollNav }">
    <!-- 寬版navbar -->
    <ul v-show="!mobile">
      <li v-for="(tab, index) in tabs" :key="index">
          <router-link :to="`/${tab.name}`">
            {{ tab.show }}
          </router-link>
        </li>
    </ul>
    <!-- 窄版navbar -->
    <div class="logo" v-show="mobile">
      <img :src="iconImg" />
    </div>
    <ul v-show="mobile">
      <li v-for="(tab, index) in tabs.slice(0,4)" :key="index">
        <router-link :to="`/${tab.name}`">
          <i :class="`${tab.icon}`"></i>
        </router-link>
      </li>
      <li>
        <router-link to="/contact">
          <i class="fi fi-sr-call-incoming"></i>
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
        name: "time",
        show: "首頁",
        icon: "fi fi-sr-calendar"
      },
      {
        name: "merchandise",
        show: "水煎包",
        icon: "fi fi-sr-hat-chef"
      },
      {
        name: "photos",
        show: "相簿",
        icon: "fi fi-br-picture"
      },
      {
        name: "comment",
        show: "評論",
        icon: "fi fi-sr-comment-alt"
      },
      {
        name: "contact",
        show: "聯絡我們",
        icon: "fi fi-ss-phone-call"
      }
    ],
    iconImg: require("@/assets/picture/guanghui.png"),
    mobileNav: null,
    scrollNav: null,
    windowWidth: null,
    mobile: null,
    userId: ""
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
      if (this.windowWidth <= 840) {
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
</style>
