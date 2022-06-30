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
            <star-rating
              :rating="comment.star"
              :read-only="true"
              :increment="0.5"
              :show-rating="false"
            ></star-rating>
            <div class="comment-content">{{ comment.content }}</div>
            <div class="headIcon"><i class="icon fi fi-sr-user"></i></div>
            <div class="name">{{ comment.name }}</div>
          </div>
        </swiper-slide>
        <swiper-slide>
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
            placeholder="評論者姓名"
            v-model.trim="commentInput.name"
          />
          <star-rating
            :increment="0.5"
            :max-rating="5"
            inactive-color="#000"
            active-color="#f0f19c"
            :star-size="30"
            :rating="commentInput.star"
          ></star-rating>
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

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import SwiperCore, { Navigation, Pagination } from "swiper"
import "swiper/swiper-bundle.css"
import Popup from "../components/Popup.vue"
import StarRating from "vue-star-rating"
import { ref } from "vue"

SwiperCore.use([Pagination, Navigation])

export default {
  components: {
    Swiper,
    SwiperSlide,
    Popup,
    StarRating
  },
  setup () {
    const addComment = ref(false)
    return { addComment }
  },
  data () {
    return {
      commentInput: {
        name: "",
        content: "",
        star: ""
      },
      comments: [],
      mobile: null
    }
  },
  created () {
    window.addEventListener("resize", this.checkScreen)
    this.checkScreen()
  },
  mounted () {
    this.axios
      .get("http://localhost:8020/comments")
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
      this.axios
        .post("http://localhost:8020/comments", this.commentInput)
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
