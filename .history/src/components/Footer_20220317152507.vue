<template>
  <div class="footer">
    < class="footer_text" col=4 v-for="(text, index) in textItems" :key="index">
        {{text.content}}
    </v-col>
  </div>
</template>

<script>
export default {
 name:'Footer',
 data:()=>({
   text_Item:[{
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
}
.footer_text{
  text-align: center;
  font-size: 20px;
}
</style>