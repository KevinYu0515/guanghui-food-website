<template>
  <div class="footer">
    <div class="footer_text" v-for="(text, index) in textItems" :key="index">
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
data:()=>({
      media_icons:[{
          icon: require("@/assets/icon/facebook1.png"),
          path: "https://www.facebook.com/profile.php?id=100009946749327",
      },
      {
          icon: require("@/assets/icon/email1.png"),
          path: "",
      },
      {
          icon: require("@/assets/icon/phone1.png"),
          path: "",
      },
      {
          icon: require("@/assets/icon/github1.png"),
          path: "https://github.com/",
      }
      ]
  }),
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