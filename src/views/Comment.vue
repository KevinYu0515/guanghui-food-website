<template>
  <section id="comment" data-aos="fade-up">
    <!-- 主標 -->
    <div class="content-titlewrapper">
      <i class="decoration"></i>
      <p class="content-title">
        <slot name="sectionTitle"></slot>
      </p>
      <i class="decoration"></i>
    </div>
    <p class="content-description">
      <slot name="sectionTitleContent"></slot>
    </p>
    <!-- swiper -->
    <div class="swiper-area">
      <swiper
        :slidesPerView="!mobile ? 2 : 1"
        :spaceBetween="!mobile ? 20 : 30"
        :pagination="{ clickable: true, dynamicBullets: false }"
        :navigation="true"
        :loop="true"
      >
        <swiper-slide v-for="(comment, index) in comments" :key="index">
          <div class="comment-card">
            <div class="stars">
              <i class="icon fi fi-ss-star"></i>
              <i class="icon fi fi-ss-star"></i>
              <i class="icon fi fi-ss-star"></i>
              <i class="icon fi fi-ss-star"></i>
              <i class="icon fi fi-ss-star"></i>
            </div>
            <div class="comment-content">{{ comment.content }}</div>
            <div class="headicon"><i class="icon fi fi-sr-user"></i></div>
            <div class="name">{{ comment.name }}</div>
            <div class="record-time">{{ comment.record_time }}</div>
          </div>
        </swiper-slide>
      </swiper>
    </div>
  </section>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import SwiperCore, { Navigation, Pagination } from "swiper";
import "swiper/swiper-bundle.css";

SwiperCore.use([Pagination, Navigation]);

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  data: () => ({
    comments: [
      {
        content:
          '"光慧素食水煎包在梧棲也吃得到啦！只是品項只有三種，不過沒關係，三種都很好吃噢😋，下午茶時段不怕肚子餓沒素食點心可以吃了，大力地給它點下去吧！"',
        record_time: "兩個月前",
        name: "小鬆餅",
      },
      {
        content:
          '"水煎包新鮮現作皮薄餡多好吃，再來一杯老闆特調的奶茶更是絕配！"',
        record_time: "八週前",
        name: "joanna chang",
      },
      {
        content:
          '"用料實在，皮薄餡多，好吃😋～店家服務親切～有經過一定要進去買～超推"',
        record_time: "一個月前",
        name: "謝慧珍",
      },
      {
        content: '"皮薄餡多，服務佳，是早餐.下午茶的最佳首選餐點"',
        record_time: "八週前",
        name: "李雅萍",
      },
      {
        content: '"老闆親切水煎包好吃😋"',
        record_time: "八週前",
        name: "吳玫茱",
      },
      {
        content:
          '"親切的老闆。闆娘👍加上好吃 的皮 餡水煎包🥰是全素食的幸福好選擇👍"',
        record_time: "八週前",
        name: "廖偵雅",
      },
      {
        content: '"很好吃，梧棲難得看到素食水煎包"',
        record_time: "八週前",
        name: "王瓊惠",
      },
      {
        content: '"好吃.料多皮薄😋口感不輸葷食.👍"',
        record_time: "八週前",
        name: "高麗娜",
      },
      {
        content: '"料多皮薄實在，好吃喔，超推~"',
        record_time: "八週前",
        name: "李春美",
      },
      {
        content: '"料好實在，超推！熱熱吃更好吃喔！"',
        record_time: "八週前",
        name: "蘇紫晴",
      },
      {
        content: '"真的好吃，強力推薦喔！"',
        record_time: "八週前",
        name: "許翠盈",
      },
    ],
    mobile: null,
  }),
  created() {
    window.addEventListener("resize", this.checkScreen);
    this.checkScreen();
  },
  methods: {
    checkScreen() {
      this.windowWidth = window.innerWidth;
      if (this.windowWidth <= 992) {
        this.mobile = true;
        return;
      }
      this.mobile = false;
      return;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/comment.scss";
@import url("https://cdn-uicons.flaticon.com/uicons-solid-straight/css/uicons-solid-straight.css");
@import url("https://cdn-uicons.flaticon.com/uicons-solid-rounded/css/uicons-solid-rounded.css");
</style>
