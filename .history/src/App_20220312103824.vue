<template>
  <v-container class="container">
    <Navbar></Navbar>
    <router-view/>
  </v-container>
</template>

<script>
import Navbar from './components/Navbar.vue';
export default {
  name:"App",
  components:{
    Navbar
  }
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@800&family=Quicksand&family=Ubuntu&display=swap');
* {
  font-family: 'Assistant', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin: 0;
}
</style>

<style lang="scss">
@import "@/assets/scss/index.scss";
</style>
