<template>

  <header :class="{'scrolled-nav': scrollNav}">
        <ul>
            <li><router-link :to="{name:'Home', hash:'#time'}">首頁</router-link> </li>
            <li><router-link :to="{name:'Photos', hash:'#photos'}">相簿</router-link> </li>
            <li><router-link :to="{name:'Comment', hash:'#comment'}">評價</router-link> </li>
            <li><router-link to="/#contact">聯絡我們</router-link> </li>
        </ul>
  </header>

</template>

<script>
export default {
  name: 'Navbar',
  data(){
    return{
      mobileNav: null,
      scrollNav: null,
      };
  },

  mounted(){
    window.addEventListener('scroll',this.updateScroll);
  },
  methods:{
    updateScroll(){
      const scrollPosition = window.scrollY;
      if(scrollPosition > 20){
        this.scrollNav = true;
        return;
      }
      this.scrollNav = false;
    },
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "@/assets/scss/navbar.scss";
</style>