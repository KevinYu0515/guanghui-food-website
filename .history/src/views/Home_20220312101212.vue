<template>
  <section id='home'>
    <v-img aspect-ratio="2"
            src="@/assets\store.jpg"
            class="d-flex align-end">
            </v-img>
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
  background: #F5A02A;
  width: 100%;
  height: 100%;
  #home_picture{
  }
}
</style>
