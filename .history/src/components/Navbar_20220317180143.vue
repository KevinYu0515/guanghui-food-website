<template>
  <header :class="{'scrolled-nav':scollNav}">
      <router-link to="/" class="logo">Logo</router-link>
      <ul>
          <li><router-link to="/home">主頁</router-link> </li>
          <li><router-link to="/about">關於</router-link> </li>
          <li><router-link to="/picture">相簿</router-link> </li>
          <li><router-link to="/contact">聯絡我們</router-link> </li>
      </ul>
  </header>
</template>

<script>
export default {
  name: 'Navbar',
  data(){
    return{
      scrollNav = null
      };
  },
  mounted(){
    window.addEventListener('scroll',this.updateScroll);
  },
  methods:{
    updateScroll(){
      const scrollPosition = window.scrollY;
      if(scrollPosition>50){
        this.scrollNav = true;
        return;
      }
      this.scrollNav = false;
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "@/assets/scss/navbar.scss";
</style>