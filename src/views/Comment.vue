<template>
  <section id="comment">
      <!-- 主標 -->
    <div class="content-titlewrapper">
        <i class="decoration"></i>
        <p class="content-title">{{title}}</p>
        <i class="decoration"></i>
    </div>
        <img :src="require('@/assets/waiting.png')">
    </section> 
</template>

<script>
export default {
    data(){
        return{
            title:"相關評論",
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/comment.scss";
</style>