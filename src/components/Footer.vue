<template>
  <div class="footer">
    <i class="decoration"></i>
     <section id="contact">
       <img class="logo" :src="logo">
      <div class="mapBox" v-show="!mobile">
        <iframe :src="mapsrc" 
          style="border:0;" 
          allowfullscreen="" 
          loading="lazy"
          >
        </iframe>
      </div>
      <div class="contact-box">
        <div class="decoration2"></div>
        <h1>{{title}}</h1>
        <a :href="contacts[0].src">
          <i class="icon fi fi-brands-facebook">
            <span style="font-weight:bolder">{{contacts[0].name}}</span>
          </i>
        </a>
        <a :href="contacts[2].src">
          <i class="icon fi fi-rs-marker">
            <span>{{contacts[2].name}}</span>
          </i>
        </a>
        <i class="icon fi fi-rr-call-incoming">
          <span>{{contacts[1].name}}</span>
        </i>
      </div>
    </section>
  </div>
</template>

<script>
export default {
 name:'Footer',
 data(){
   return{
     title:"聯絡我們",
     logo:require('@/assets/logo.jpg'),
     contacts:[{
       src:"https://reurl.cc/g2vY6V",
       name:"facebook",
     },{
       src:"",
       name:"0952404078 | 0935368684"
     },{
       src:"https://reurl.cc/9Gzn6a",
       name:"臺中市梧棲區民和路一段37號"
     }],
     mapsrc:"https://reurl.cc/Lm1nnX",
     mobile:null,
   }
 },
 created(){
      window.addEventListener('resize', this.checkScreen);
      this.checkScreen();
  },
  methods:{
    checkScreen(){
        this.windowWidth = window.innerWidth;
        if(this.windowWidth <= 1120){
            this.mobile = true;
            return
        }
        this.mobile = false;
        this.mobileNav = false;
        return;
    },
  }
 
}
</script>

<style lang='scss'>
@import "@/assets/scss/footer.scss";
</style>

<style lang="scss" scoped>
@import url('https://cdn-uicons.flaticon.com/uicons-regular-straight/css/uicons-regular-straight.css');
@import url('https://cdn-uicons.flaticon.com/uicons-brands/css/uicons-brands.css');
@import url('https://cdn-uicons.flaticon.com/uicons-regular-rounded/css/uicons-regular-rounded.css');
</style>