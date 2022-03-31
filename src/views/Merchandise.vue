<template>
  <section id="merchandise" data-aos="fade-up" data-aos-duration="1000">
    <!-- 主標 -->
      <div class="content-titlewrapper">
        <i class="decoration"></i>
        <p class="content-title">{{title}}</p>
        <i class="decoration"></i>
      </div>
      <p class="content-description">
        {{title_content}}
      </p>
      <!-- 各產品卡片內容 -->
      <!-- 寬版架構 -->
        <div class="cardwrapper">
          <div class="card" v-for="(item, index) in cardItems" :key="index">
            <img :src="item.imgPath">
            <div class="info">
              <h1>{{item.name}}</h1>
              <p>{{cardcontent}}</p>
            </div>
          <!-- 窄版架構 -->
            <div v-show="mobile" class="description">
                <p>{{item.name}}</p>
            </div>          
          </div> 
        </div>
    </section>
</template>

<script>
export default {
    data:()=>({
        cardItems:[
        {
            imgPath: require('@/assets/picture/001.jpg'),
            name: "高麗菜水煎包",
            
        },
        {
            imgPath: require('@/assets/picture/002.jpg'),
            name: "筍子水煎包",
        },
        {
            imgPath: require('@/assets/picture/003.jpg'),
            name: "冬粉水煎包",
        }],
        title:"水煎包",
        title_content:"主要賣三種水煎包，內餡分別為高麗菜、筍子、冬粉，每個售價15元，飲料有 紅茶、奶茶 另售10元",
        cardcontent:"一個15元",
    })
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/merchandise.scss";
</style>>
