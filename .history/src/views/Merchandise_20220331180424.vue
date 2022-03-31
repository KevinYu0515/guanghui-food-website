<template>
  <section id="merchandise">
      <div class="content-titlewrapper" data-0-top="opacity:1;bottom:100px;" data-200-top="opacity:1;bottom:0px>
        <i class="decoration"></i>
        <p class="content-title">水煎包</p>
        <i class="decoration"></i>
      </div>
      <p class="content-description">
        {{content}}
      </p>
        <!-- <div class="card" v-for="(item,index) in goods" :key="index">
          <img :src="item.imgpath">
          <div class="info">
            <h1>{{item.name}}</h1>
            <p>一個15元</p>
          </div>
        </div> -->
        <div class="cardwrapper">
          <div class="card" v-for="(item, index) in items" :key="index">
            <img :src="item.imgPath">
            <div class="info">
              <h1>{{item.name}}</h1>
              <p>一個15元</p>
            </div>
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
        items:[
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
        content:"主要賣三種水煎包，內餡分別為高麗菜、筍子、冬粉，每個售價15元，飲料有 紅茶、奶茶 另售10元"
    }),
    // data(){
    //     return{
    //         cardcontent:"一個15元",
    //     }
    // }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/merchandise.scss";
</style>>
