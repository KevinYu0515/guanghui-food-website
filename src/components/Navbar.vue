<template>

  <header :class="{'scrolled-nav': scrollNav}">
        <ul>
            <li><router-link to="/#time">首頁</router-link> </li>
            <li><router-link to="/#photos">相簿</router-link> </li>
            <li><router-link to="/#comment">評價</router-link> </li>
            <li><router-link to="/#time">聯絡我們</router-link> </li>
        </ul>
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