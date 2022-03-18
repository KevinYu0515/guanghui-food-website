<template>
  <div class=app
  <Navbar></Navbar>
  <router-view></router-view>
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

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@800&family=Quicksand&family=Ubuntu&display=swap');
* {
  font-family: 'Assistant', Helvetica, Arial, sans-serif;
  background-color: #FEDB8E;
  justify-content: center;
  align-items: center;
}
</style>
