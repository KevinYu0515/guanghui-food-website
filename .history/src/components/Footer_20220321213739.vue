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
        <h1>聯絡我們</h1>
        <p>電話：0952404078</p>
        <p style="margin-bottom: 20px;">地址：臺中市梧棲區民和路一段37號</p>
        <!-- <a src=" -->
        <i style="font-size: 5vmin;" class="fi fi-brands-facebook"></i>
        <i style="font-size: 5vmin;" class="fi fi-rs-marker"></i>
      </div>
    </section>
    <!--<div v-for="(text, index) in textItems" :key="index">
      <div class="footer_text">
        {{text.content}}
      </div>
    </div>-->
  </div>
</template>

<script>
export default {
 name:'Footer',
 data:()=>({
   textItem:[{
     content: "電話：0952404078"
   },
   {
     content: "地址：臺中市梧棲區民和路一段37號"
   },
   {
     content: "Facebook"
   }]
 })
}
</script>

<style lang='scss'>

@import "@/assets/scss/footer.scss";
</style>

<style lang="scss" scoped>
@import url('https://cdn-uicons.flaticon.com/uicons-regular-straight/css/uicons-regular-straight.css');
@import url('https://cdn-uicons.flaticon.com/uicons-brands/css/uicons-brands.css');
</style>