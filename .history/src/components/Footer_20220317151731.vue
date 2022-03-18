<template>
  <div class="footer">
    <v-col col=4 v-for="(media_icon, index) in media_icons" :key="index">
        
    </v-col>
  </div>
</template>

<script>
export default {
 name:'Footer',
 data:()=>({
   text_group:[{
     
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