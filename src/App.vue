<template>
  <div id="app">
      <!-- <v-container class="container"> -->
        <Navbar></Navbar>
          <router-view/>
        <Footer></Footer>
      <!-- </v-container> -->
  </div>
</template>

<script>
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
export default {
  name:"App",
  components:{
    Footer,
    Navbar
  }
}
</script>

<style lang="scss">
// @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@800&family=Quicksand&family=Ubuntu&display=swap');
@import url(https://fonts.googleapis.com/earlyaccess/notosanstc.css);
@import url('https://fonts.googleapis.com/css2?family=Secular+One&display=swap');
* {
  font-family: "Noto Sans TC", 'Secular One', Arial, sans-serif;
  justify-content: center;
  align-items: center;
  margin:0;
  text-decoration: none;
}
#app{
    background-color: #FDF2D8;
}
</style>
