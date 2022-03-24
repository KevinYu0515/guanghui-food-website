<template>

  <header :class="{'scrolled-nav': scrollNav}">
        <ul v-show="!mobile">
            <li><router-link :to="{name:'Home', hash:'#time'}">首頁</router-link> </li>
            <li><router-link :to="{name:'Photos', hash:'#photos'}">相簿</router-link> </li>
            <li><router-link :to="{name:'Comment', hash:'#comment'}">評價</router-link> </li>
            <li><router-link to="/#contact">聯絡我們</router-link> </li>
        </ul>
        <div class="navbar_icon">
          <i @click="toggleMobileNav" v-show="mobile" class="fi fi-br-menu-burger" :class="{'icon-active':mobileNav}" ></i>
        </div>
        <transition name='mobile-nav'>
            <ul v-show="mobileNav" class="dropdown-nav">
              <li><router-link :to="{name:'Home', hash:'#time'}">首頁</router-link> </li>
              <li><router-link :to="{name:'Photos', hash:'#photos'}">相簿</router-link> </li>
              <li><router-link :to="{name:'Comment', hash:'#comment'}">評價</router-link> </li>
              <li><router-link to="/#contact">聯絡我們</router-link> </li>
            </ul>
        </transition>
  </header>

</template>

<script>
export default {
  name: 'Navbar',
  data(){
    return{
      mobileNav: null,
      scrollNav: null,
      windowWidth: null,
      mobile:null,
      };
  },
  created(){
      window.addEventListener('resize', this.checkScreen);
      this.checkScreen();
  },
  mounted(){
    window.addEventListener('scroll',this.updateScroll);
  },
  methods:{
    toggleMobileNav(){
      this.mobileNav = !this.mobileNav;
    },
    updateScroll(){
      const scrollPosition = window.scrollY;
      if(scrollPosition > 20){
        this.scrollNav = true;
        return;
      }
      this.scrollNav = false;
    },
    checkScreen(){
        this.windowWidth = window.innerWidth;
        if(this.windowWidth <= 850){
            this.mobile = true;
            return
        }
        this.mobile = false;
        this.mobileNav = false;
        return;
    },
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "@/assets/scss/navbar.scss";
@import url('https://cdn-uicons.flaticon.com/uicons-bold-rounded/css/uicons-bold-rounded.css');
</style>