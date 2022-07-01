<template>
  <div id="app">
    <Navbar></Navbar>
    <router-view/>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue"
import Footer from "./components/Footer.vue"
export default {
  name: "App",
  components: {
    Navbar,
    Footer
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/earlyaccess/notosanstc.css');
@import url('https://fonts.googleapis.com/css2?family=Secular+One&display=swap');
* {
  font-family: "Noto Sans TC", 'Secular One', Arial, sans-serif;
  height: auto;
  max-width: 100%;
  margin:0;
  justify-content: center;
  align-items: center;
  text-decoration: none;

}
#app{
    background-color: #FDF2D8;
}
</style>
