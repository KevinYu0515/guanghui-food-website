<template>

  <div class='home'>
    <section id="time">
      <!-- 主標 -->
      <p class="store-name" >{{store_name}}</p>
      <p class="store-subname">{{store_subname}}</p>
      <!-- 時間表 -->
      <div class="timetable">
          <p class="timetable-subtitle">{{timetable_title}}</p>
          <ul>
            <li v-for="(day,index) in days" :key="index">
              {{day}} &nbsp;&nbsp;<p>{{times[0]}} &nbsp;{{times[1]}}</p>
            </li>
            <li>{{weekends[0]}} &nbsp;&nbsp;<p>{{times[0]}}</p></li>
            <li>{{weekends[1]}} &nbsp; {{times[2]}}</li>
          </ul>
      </div>
    </section>
    <div class="socialMedia3" v-show="!mobileIcon" data-aos="fade-up">
      <a href="https://www.facebook.com/people/%E5%85%89%E6%85%A7%E6%B0%B4%E7%85%8E%E5%8C%85-%E6%A2%A7%E6%A3%B2%E5%BA%97/100075103166257/">
        <i class="icon fi fi-brands-facebook"><span style="font-weight:bolder">{{facebook}}</span></i>
      </a>
    </div>
    <div class="socialMedia2" v-show="!mobileIcon" data-aos="fade-up">
      <a href="https://www.google.com.tw/maps/place/%E5%85%89%E6%85%A7%E6%B0%B4%E7%85%8E%E5%8C%85%EF%BC%88%E6%A2%A7%E6%A3%B2%E5%BA%97%EF%BC%89/@24.2467507,120.5456227,17z/data=!3m1!4b1!4m5!3m4!1s0x346915859dc0b4dd:0x37ba3c60d4fc0ca8!8m2!3d24.2467287!4d120.5478919?hl=zh-TW&authuser=0">
        <i class="icon fi fi-rs-marker"><span>{{place}}</span></i>
      </a>
    </div>
    <div class="socialMedia" v-show="!mobileIcon" data-aos="fade-up">
      <i class="icon fi fi-rr-call-incoming"><span>{{phone}}</span></i>
    </div>
    <!-- 新公告說明版面 -->
    <section id="news" v-show="true" data-aos="fade-up">
      <h1>{{news_title}}</h1>
      <p>{{news_content}}</p>
    </section>
    <!-- 其他版面 -->
    <about></about>
    <merchandise>
      <template #sectionTitle>
        {{sectionTitle[0]}}
      </template>
      <template #sectionTitleContent>
        {{sectionTitleContent[0]}}
      </template>
    </merchandise>
    <gallery>
      <template #sectionTitle>
        {{sectionTitle[1]}}
      </template>
      <template #sectionTitleContent>
        {{sectionTitleContent[1]}}
      </template>
    </gallery>
    <comment>
      <template #sectionTitle>
        {{sectionTitle[2]}}
      </template>
      <template #sectionTitleContent>
        {{sectionTitleContent[2]}}
      </template>
    </comment>
    
  </div>
</template>

<script>
import about from "./About.vue";
import merchandise from "./Merchandise.vue";
import gallery from "./Gallery.vue"
import comment from "./Comment.vue";

export default {
  name: 'Home',
  components:{
    about,merchandise,comment,gallery
  },
  data(){
    return{
      store_name: "光慧水煎包",
      store_subname:"(梧棲店)",
      timetable_title:"營業時間",
      news_title:"最新公告",
      news_content:"暫無新公告",
      days:['週一','週二','週三','週四','週五'],
      weekends:['週六','週日'],
      times:["0600~0900","1500~1700","公休"],
      sectionTitle:["水煎包","相片集","評論區"],
      sectionTitleContent:[
        "主要賣三種水煎包，內餡分別為高麗菜、竹筍、冬粉，每個售價15元，飲料有 紅茶、奶茶 另售10元",
        "由商家提供的照片，其中包含最新實體店面、三種水煎包、水煎包烹煮過程，拍攝技術拙劣還請見諒",
        "評論皆於Google評論索取，五星好評謝謝大家的支持"
      ],
      mobileIcon: null,
    }
  },
  created(){
    window.addEventListener('resize', this.checkScreen);
    this.checkScreen();
  },
  mounted(){
    window.addEventListener('scroll',this.updateScroll);
  },
  methods:{
    checkScreen(){
            this.windowWidth = window.innerWidth;
            if(this.windowWidth <= 850){
                this.mobileIcon = true;
                return
                }
            this.mobileIcon = false;
            return;
        },
  }
}
</script>

<style lang="scss" scoped>
  @import "@/assets/scss/Home/index.scss";
  @import "@/assets/scss/Home/time.scss";
  @import "@/assets/scss/Home/news.scss";
</style>