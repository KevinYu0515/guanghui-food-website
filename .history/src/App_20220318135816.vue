<template>
  <div class="app">
    <
      <router-view/>
    <Footer></Footer>
  </div>
</template>

<script>
import Footer from './components/Footer.vue';
export default {
  name:"App",
  components:{
    Footer
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@800&family=Quicksand&family=Ubuntu&display=swap');
* {
  font-family: 'Assistant', Helvetica, Arial, sans-serif;
  justify-content: center;
  align-items: center;
  margin:0;
}
.app{
  background-color: #FEDB8E;
}
</style>
