<template>
  <div class="footer">
    <v-col col=4 v-for="(textGroup, index) in textGroups" :key="index">
        
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
</style>