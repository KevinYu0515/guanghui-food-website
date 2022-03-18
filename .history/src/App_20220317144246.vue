<template>
  <div class="app">
    <Navbar></Navbar>
    <div class="content">
    <router-view/>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';
export default {
  name:"App",
  components:{
    Navbar,
    Footer
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@800&family=Quicksand&family=Ubuntu&display=swap');
* {
  font-family: 'Assistant', Helvetica, Arial, sans-serif;
  background-color: #FEDB8E;
  justify-content: center;
  align-items: center;
  margin:0;
}
</style>
