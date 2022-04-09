<template>
  <section id="comment">
      <!-- 主標 -->
    <div class="content-titlewrapper">
        <i class="decoration"></i>
        <p class="content-title">{{title}}</p>
        <i class="decoration"></i>
    </div>
    <div class="swiper-area">
        <swiper
            :slidesPerView="1"
            :spaceBetween="30"
            :pagination="{ clickable: true, dynamicBullets: false }"
            :navigation="true"
            :loop="true"
        >
            <swiper-slide v-for="(comment, index) in comments" :key="index">
                <div class="comment-card">
                    <div class="stars">
                        <i class="fi fi-ss-star"></i>
                        <i class="fi fi-ss-star"></i>
                        <i class="fi fi-ss-star"></i>
                        <i class="fi fi-ss-star"></i>
                        <i class="fi fi-ss-star"></i>
                    </div>
                    <div class="comment-content">{{comment.content}}</div>
                    <div class="headicon"><i class="fi fi-sr-user"></i></div>
                    <div class="name">{{comment.name}}</div>
                    <div class="record-time">{{comment.record_time}}</div>
                </div>
            </swiper-slide>
        </swiper>
    </div>
    </section> 
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import SwiperCore, { Navigation, Pagination } from 'swiper'
import 'swiper/swiper-bundle.css'

SwiperCore.use([Pagination,Navigation])

export default {
    components: {
        Swiper,
        SwiperSlide,
    },
    data:()=>({
            title:"相關評論",
            comments:[
            {
                content: '"光慧素食水煎包在梧棲也吃得到啦！只是品項只有三種，不過沒關係，三種都很好吃噢😋，下午茶時段不怕肚子餓沒素食點心可以吃了，大力地給它點下去吧！"',
                record_time:'兩個月前',
                name:'小鬆餅',
            },{
                content: '"水煎包新鮮現作皮薄餡多好吃，再來一杯老闆特調的奶茶更是絕配！"',
                record_time:'一個月前',
                name:'joanna c',
            },{
                content: '"用料實在，皮薄餡多，好吃😋～店家服務親切～有經過一定要進去買～超推"',
                record_time:'一個月前',
                name:'謝慧珍',
            }],

    })
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/comment.scss";
@import url('https://cdn-uicons.flaticon.com/uicons-solid-straight/css/uicons-solid-straight.css');
@import url('https://cdn-uicons.flaticon.com/uicons-solid-rounded/css/uicons-solid-rounded.css');
</style>