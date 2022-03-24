<template>
  <section id="photos">
        <div class="content-titlewrapper">
          <i class="decoration"></i>
          <p class="content-title">相關照片</p>
          <i class="decoration"></i>
        </div>
      <!-- <i class="btn">更多照片</i> -->
          <div class="wrapper">
              <div class="gallery">
                  <div class="image" v-for="(img, index) in images" :key="index">
                    <span><img :src="require(`@/assets/picture/${img}.jpg`)" alt=""></span>
                </div>
              </div>
          </div>
          <div class="preview-box">
            <div class="details">
                <span class="title">Image <p class="current-img"></p> of <p class="total-img"></p></span>
                <span class="icon fas fa-times"></span>
            </div>
            <div class="image-box">
                <div class="slide prev"><i class="fas fa-angle-left"></i></div>
                <div class="slide next"><i class="fas fa-angle-right"></i></div>
                <img src="" alt="">
            </div>
        </div>
        <div class="shadow"></div>
    </section>
</template>

<script>

export default {
    data(){
        return{
            images:["001","002","003","004","005","006","007"],
        }
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/gallery.scss";
</style>