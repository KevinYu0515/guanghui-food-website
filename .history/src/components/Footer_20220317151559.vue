<template>
  <div class="footer">
    <v-col col=4 v-for="(media_icon, index) in media_icons" :key="index">
        <a :href="media_icon.path">
            <img :src="media_icon.icon" class="media_icon">
        </a>
    </v-col>
  </div>
</template>

<script>
export default {
 name:'Footer',
}
</script>

<style>
.footer{
    background:#9E261B;
    height:20vh;
    width: 100%;
}
</style>