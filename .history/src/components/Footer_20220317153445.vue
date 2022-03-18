<template>
  <div class="footer">
    <div class="footer_text" v-for="(text, index) in textItems" :key="index">
      div.
        {{text.content}}
    </div>
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
   },{
     content: "Facebook"
   }]
 })
}
</script>

<style>
.footer{
    background:#9E261B;
    height:20vh;
    width: 100%;
    align-items: center;
    justify-content: center;
}
.footer_text{
  text-align: center;
  font-size: 20px;
}
</style>