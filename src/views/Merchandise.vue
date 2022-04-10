<template>
  <section id="merchandise" data-aos="fade-up">
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
        <div class="cardwrapper" v-show="!mobile2">
          <div class="card" v-for="(item, index) in cardItems" :key="index">
            <img :src="item.imgPath">
            <div class="info">
              <h1>{{item.name}}<br><span>{{item.name2}}</span></h1>
              <p>{{cardcontent}}</p>
            </div>
          </div>
        </div>
      <!-- 窄版架構 -->
        <div class="card_mobile" 
        v-show="mobile2" 
        v-for="(item, index) in cardItems" :key="index"
        data-aos="fade-up"
        >
          <img :src="item.imgPath"> 
          <div class="description">
            <p class="item-name"><span>{{item.name}}</span><br>{{item.name2}}</p>
            <p class="item-content">{{cardcontent}}</p>
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
          name2: "Fried bun stuffed with cabbage",
      },
      {
          imgPath: require('@/assets/picture/002.jpg'),
          name: "竹筍水煎包",
          name2: "Fried bun stuffed with bamboo shoots",
      },
      {
          imgPath: require('@/assets/picture/003.jpg'),
          name: "冬粉水煎包",
          name2: "Fried bun stuffed with bean thread",
      }],
      title:"水煎包",
      title_content:"主要賣三種水煎包，內餡分別為高麗菜、竹筍、冬粉，每個售價15元，飲料有 紅茶、奶茶 另售10元",
      cardcontent:"一個15元",
      mobile2:null,
  }),
  created(){
      window.addEventListener('resize', this.checkScreen);
      this.checkScreen();
    },
    methods:{
        checkScreen(){
            this.windowWidth = window.innerWidth;
            if(this.windowWidth<= 850){
                  this.mobile2 = true;
                  return
                }
            this.mobile2 = false;
            return;
        },
    }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/merchandise.scss";
</style>>
