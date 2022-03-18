<template>
  <section id='home'>
    <img id="home_picture" src="@/assets\store.jpg">
  </section>
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
  background: #FEDB8E;
  width: 100;
}
</style>
