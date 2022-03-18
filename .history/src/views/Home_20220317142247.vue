<template>
  <div id='home'>
    <img src="./assets\store.jpg">
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'Home',
  components: {
    Navbar
  }
}
</script>

<style lang="scss" scoped>
#home{
  background: #F5A02A;
  width: 100%;
  height: 100%;
}
</style>
