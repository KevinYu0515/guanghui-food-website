<template>
  <div class='home'>

    <section id="time">
      <p class="store-name" >{{store_name}}</p>
      <p class="store-subname">{{store_subname}}</p>
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

      <section v-show="mobileNews" id="about">
        <h1>{{news_title}}</h1>
        <p>{{news_content}}</p>
      </section>

    <Merchandise></Merchandise>
    <Photos></Photos>
    <!-- <Comment></Comment> -->
    
  </div>
</template>

<script>
import Merchandise from "./Merchandise.vue";
import Photos from "./Photos_test.vue"
import Comment from "./Comment.vue";

export default {
  name: 'Home',
  components:{
    Merchandise,Comment,Photos
  },
  data(){
    return{
      mobileNews: null,
      store_name: "光慧水煎包",
      store_subname:"(梧棲店)",
      timetable_title:"營業時間",
      news_title:"最新公告",
      news_content:"清明連假公休",
      days:['週一','週二','週三','週四','週五'],
      weekends:['週六','週日'],
      times:["0600~0900","1500~1700","公休"],
    }
  },
  
  mounted(){
    window.addEventListener('scroll',this.updateScroll);
  },

  methods:{
    updateScroll(){
      const scrollPosition = window.scrollY;
      if(scrollPosition > 100){
        this.mobileNews = true;
        return;
      }
    },
  },
}
</script>

<style lang="scss" scoped>
  @import "@/assets/scss/Home/home.scss";
  @import "@/assets/scss/Home/time.scss";
  @import "@/assets/scss/Home/about.scss";
  @import "@/assets/scss/Home/comment.scss";
</style>