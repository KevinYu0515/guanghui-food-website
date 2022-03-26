<template>

  <header :class="{'scrolled-nav': scrollNav}">
        <ul v-show="!mobile">
            <li v-for="(tab, index) in tabs" :key="index">
              <router-link :to="{name:tab.name, hash:tab.hash}">
                {{tab.show}}
              </router-link> 
            </li>
            <li><router-link to='/#contact'>{{ex_tab}}</router-link> </li>
        </ul>
        <ul v-show="mobile">
            <li v-for="(tab, index) in tabs" :key="index">
              <router-link :to="{name:tab.name, hash:tab.hash}">
                <i class=`${{tab.icon}`></i>
              </router-link> 
            </li>
            <li>
              <router-link to='/#contact'>
                <i class="fi fi-sr-call-incoming"></i>
              </router-link> 
            </li>
        </ul>
  </header>

</template>

<script>
export default {
  name: 'Navbar',
  data:()=>({
    ex_tab:'聯絡我們',
    tabs:[
      {
        name:'Home' ,show:'首頁' ,hash:'#time', icon:"fi fi-sr-calendar"
    },{
        name:'Photos' ,show:'相簿' ,hash:'#photos', icon:"fi fi-br-picture"
    },{
        name:'Comment' ,show:'評價' ,hash:'#comment', icon:"fi fi-sr-comment-alt"
    }],

    mobileNav: null,
    scrollNav: null,
    windowWidth: null,
    mobile:null,

    }),

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
@import url('https://cdn-uicons.flaticon.com/uicons-solid-rounded/css/uicons-solid-rounded.css');
@import url('https://cdn-uicons.flaticon.com/uicons-bold-rounded/css/uicons-bold-rounded.css');
@import url('https://cdn-uicons.flaticon.com/uicons-solid-rounded/css/uicons-solid-rounded.css')
@import url('https://cdn-uicons.flaticon.com/uicons-solid-rounded/css/uicons-solid-rounded.css');
</style>