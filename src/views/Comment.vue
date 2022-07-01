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
            <StarRating
              :rating="comment.star"
              :read-only="true"
              :increment="0.5"
              :show-rating="false"
            ></StarRating>
            <div class="comment-content">{{ comment.content }}</div>
            <div class="headIcon"><i class="icon fi fi-sr-user"></i></div>
            <div class="name">{{ comment.name }}</div>
          </div>
        </swiper-slide>
        <swiper-slide v-show="false">
          <div class="addNewComment">
            <i class="addComment fi fi-rr-add" @click="addComment = true"></i>
          </div>
        </swiper-slide>
      </swiper>
    </div>
    <Popup :open="addComment" @close="addComment = !addComment">
      <template #imageName>評論表單</template>
      <template #img>
        <div class="input">
          <label class="nameLabel">Name 評論者名稱</label>
          <input
            type="text"
            class="name"
            placeholder="評論者名稱"
            v-model.trim="commentInput.name"
          />
          <StarRating
            :increment="0.5"
            :max-rating="5"
            inactive-color="#000"
            active-color="#f0f19c"
            :star-size="30"
            :rating="commentInput.star"
          ></StarRating>
          <label class="commentLabel">Comment 評論內容</label>
          <textarea
            rows="2"
            cols="23"
            class="content"
            placeholder="評論內容"
            v-model.trim="commentInput.content"
          ></textarea>
          <div class="buttonBox">
            <button
              type="button"
              class="btn btn-outline-primary delete"
              @click="cancelHandler()"
            >
              Delete
            </button>
            <button
              type="button"
              class="btn btn-outline-warning send"
              @click="submitHandler()"
            >
              Send
            </button>
          </div>
        </div>
      </template>
    </Popup>
  </section>
</template>

<script setup>
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import SwiperCore, { Navigation, Pagination } from "swiper"
import "swiper/swiper-bundle.css"

import axios from "axios"
import Popup from "../components/Popup.vue"
import StarRating from "vue-star-rating"
import { ref } from "vue"

SwiperCore.use([Pagination, Navigation])

const commentInput = {
  name: "",
  content: "",
  star: 0
}
const comments = ref([])
const mobile = ref(null)
const addComment = ref(false)
</script>

<script>
export default {
  components: {
    Swiper,
    SwiperSlide,
    Popup,
    StarRating
  },
  created () {
    window.addEventListener("resize", this.checkScreen)
    this.checkScreen()
  },
  mounted () {
    axios.get("http://localhost:8020/comments")
      .then((res) => {
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  },
  methods: {
    checkScreen () {
      this.windowWidth = window.innerWidth
      if (this.windowWidth <= 992) {
        this.mobile = true
        return
      }
      this.mobile = false
    },
    submitHandler () {
      const { name, content, star } = this.commentInput
      if (!name || !content || !star) return
      axios.post("http://localhost:8020/comments", this.commentInput)
        .then((res) => {
          this.comments.push(res.data)
          this.cancelHandler()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    cancelHandler () {
      this.commentInput.name = ""
      this.commentInput.content = ""
      this.commentInput.star = ""
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/Home/comment.scss";
@import url("https://cdn-uicons.flaticon.com/uicons-solid-straight/css/uicons-solid-straight.css");
@import url("https://cdn-uicons.flaticon.com/uicons-solid-rounded/css/uicons-solid-rounded.css");
@import url("https://cdn-uicons.flaticon.com/uicons-regular-rounded/css/uicons-regular-rounded.css");
</style>
