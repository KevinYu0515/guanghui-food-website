<template>
  <div class="footer">
    <div style="display:flex">
      <p class="footer_text">電話：0952404078</p>
      <p class="footer_text">地址：台中市梧棲區民和路一段37號</p>
      <p class="footer_text">Facebook</p>
    </div>
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
     content: "地址：台中市梧棲區民和路一段37號"
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