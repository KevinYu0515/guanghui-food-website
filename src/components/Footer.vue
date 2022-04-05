<template>
  <div class="footer">
    <i class="decoration"></i>
     <section id="contact">
       <img class="logo" :src="require('@/assets/logo.jpg')">
      <div class="mapBox">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3637.857831780853!2d120.54562271494271!3d24.246750684347145!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x346915859dc0b4dd%3A0x37ba3c60d4fc0ca8!2z5YWJ5oWn5rC054WO5YyF77yI5qKn5qOy5bqX77yJ!5e0!3m2!1szh-TW!2stw!4v1647614092352!5m2!1szh-TW!2stw" 
         style="border:0;" allowfullscreen="" loading="lazy"></iframe>
      </div>
      <div class="contact-box">
        <div class="decoration4"></div>
        <h1>{{title}}</h1>
        <a href="https://www.facebook.com/people/%E5%85%89%E6%85%A7%E6%B0%B4%E7%85%8E%E5%8C%85-%E6%A2%A7%E6%A3%B2%E5%BA%97/100075103166257/">
          <i class="icon fi fi-brands-facebook"><span style="font-weight:bolder">{{facebook}}</span></i>
        </a>
        <a href="https://www.google.com.tw/maps/place/%E5%85%89%E6%85%A7%E6%B0%B4%E7%85%8E%E5%8C%85%EF%BC%88%E6%A2%A7%E6%A3%B2%E5%BA%97%EF%BC%89/@24.2467507,120.5456227,17z/data=!3m1!4b1!4m5!3m4!1s0x346915859dc0b4dd:0x37ba3c60d4fc0ca8!8m2!3d24.2467287!4d120.5478919?hl=zh-TW&authuser=0">
          <i class="icon fi fi-rs-marker"><span>{{place}}</span></i>
        </a>
        <i class="icon fi fi-rr-call-incoming"><span>{{phone}}</span></i>
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
     facebook:"facebook",
     phone:"0952404078 | 0935368684",
     place:"臺中市梧棲區民和路一段37號",
   }
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