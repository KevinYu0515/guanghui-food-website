<template>
  <header>
      <router-link to="/" class="logo">Logo</router-link>
      <ul>
          <li><router-link to="/home">主頁</router-link> </li>
          <li><router-link to="/about">關於</router-link> </li>
          <li><router-link to="/picture">相簿</router-link> </li>
          <li><router-link to="/contact">聯絡我們</router-link> </li>
      </ul>
    <transition name="mobile-nav">
      <ul v-show="mobileNav" :class="{'scrolled-nav': scrollNav}">
          <li><router-link to="/home">主頁</router-link> </li>
          <li><router-link to="/about">關於</router-link> </li>
          <li><router-link to="/picture">相簿</router-link> </li>
          <li><router-link to="/contact">聯絡我們</router-link> </li>
      </ul>
    </transition>
  </header>

</template>

<script>
export default {
  name: 'Navbar',
  data(){
    return{
      // mobile: null,
      mobileNav: null,
      // windowWidth: null,
      scrollNav : null,
      };
  },
  // created(){
  //       window.addEventListener('resize', this.checkScreen);
  //       this.checkScreen();
  //   },
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
    // checkScreen(){
    //         this.windowWidth = window.innerWidth;
    //         if(this.windowWidth <= 850){
    //             this.mobile = true;
    //             return
    //         }
    //         this.mobile = false;
    //         this.mobileNav = false;
    //         return;
    //     },
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "@/assets/scss/navbar.scss";
</style>