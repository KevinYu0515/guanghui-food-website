<template>
  <section id="comment" data-aos="fade-up">
    <!-- 主標 -->
    <div class="content-titleWrapper">
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
            <div class="headIcon"><i class="icon fi fi-sr-user"></i></div>
            <div class="name">{{ comment.name }}</div>
            <div class="record-time">{{ comment.record_time }}</div>
          </div>
        </swiper-slide>
        <!-- <swiper-slide>
          <div class="addNewComment">
            <i class="addComment fi fi-rr-add" @click="addComment = true"></i>
          </div>
        </swiper-slide> -->
      </swiper>
    </div>
    <Popup :open="addComment" @close="addComment = !addComment">
      <template #imageName>評論表單</template>
      <template #img>
        <input type="text" class="name" v-model.trim="commentInput.name" />
        <input
          type="text"
          class="comment"
          v-model.trim="commentInput.content"
        />
        <input type="text" class="star" v-model.trim="commentInput.star" />
      </template>
    </Popup>
  </section>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import SwiperCore, { Navigation, Pagination } from "swiper";
import "swiper/swiper-bundle.css";
import Popup from "../components/Popup.vue";
import { ref } from "vue";

SwiperCore.use([Pagination, Navigation]);

export default {
  components: {
    Swiper,
    SwiperSlide,
    Popup,
  },
  setup() {
    const addComment = ref(false);
    return { addComment };
  },
  data: () => ({
    commentInput: {
      name: "",
      content: "",
      star: "",
    },
    comments: [],
    mobile: null,
  }),
  created() {
    window.addEventListener("resize", this.checkScreen);
    this.checkScreen();
  },
  mounted() {
    this.axios
      .get("http://localhost:8020/comments")
      .then((res) => {
        this.comments = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
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
@import url("https://cdn-uicons.flaticon.com/uicons-regular-rounded/css/uicons-regular-rounded.css");
</style>
