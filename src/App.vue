<template>
  <div id="app">
    <div v-if="isLoading">
      <loading :active="isLoading" class="loading"><img :src="require('@/assets/loading.gif')"/></loading>
    </div>
    <div v-else>
      <Navbar></Navbar>
      <router-view/>
      <Footer></Footer>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue"
import Footer from "./components/Footer.vue"
import { onMounted, ref } from "vue"
export default {
  name: "App",
  components: {
    Navbar,
    Footer
  }
}
</script>

<script setup>
const isLoading = ref(true)

onMounted(() => {
  setTimeout(() => {
    isLoading.value = false
  }, 1000)
})
</script>

<style lang="scss" scoped>
#app{
  min-width: 100vw;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-content: center;
  .loading{
    width: 10vw;
    height: auto;
  }
}
</style>
