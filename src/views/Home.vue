<template>
  <div class="home">
    <section id="time">
      <!-- 主標 -->
      <p class="store-name">{{ store[index].name }}</p>
      <p class="store-subName">{{ store[index].subName }}</p>
      <!-- 時間表 -->
      <div class="timetable">
        <p class="timetable-title">{{ timetableTitle }}</p>
        <ul>
          <li v-for="(day, i) in days.slice(0, 5)" :key="i">
            {{ day }} &nbsp;&nbsp;
            <p>{{ times[index] }}、{{ times[index+1] }} </p>
          </li>
          <li>
            {{ days[index + 5] }} &nbsp;&nbsp;
            <p>{{ times[index] }}</p>
          </li>
          <li>{{ days[index + 6] }} &nbsp; {{ times[index + 2] }}</li>
        </ul>
      </div>
    </section>
    <div class="facebook" v-show="!mobileIcon" data-aos="fade-up">
      <a :href="facebookSrc">
        <i class="icon fi fi-brands-facebook"></i>
      </a>
    </div>
    <div class="map" v-show="!mobileIcon" data-aos="fade-up">
      <a :href="mapSrc">
        <i class="icon fi fi-rs-marker"></i>
      </a>
    </div>
    <div class="calling" v-show="!mobileIcon" data-aos="fade-up">
      <i class="icon fi fi-rr-call-incoming"></i>
    </div>
    <!-- 新公告說明版面 -->
    <section id="news" v-show="true" data-aos="fade-up">
      <h1>{{ newsTitle }}</h1>
      <p v-for="(content, i) in newsContents" :key="i">
        {{ content }}
      </p>
    </section>
    <!-- 其他版面 -->
    <about></about>
    <merchandise>
      <template #sectionTitle>
        {{ sections[index].title }}
      </template>
      <template #sectionTitleContent>
        {{ sections[index].content }}
      </template>
    </merchandise>
    <gallery>
      <template #sectionTitle>
        {{ sections[index + 1].title }}
      </template>
      <template #sectionTitleContent>
        {{ sections[index + 1].content }}
      </template>
    </gallery>
    <comment>
      <template #sectionTitle>
        {{ sections[index + 2].title }}
      </template>
      <template #sectionTitleContent>
        {{ sections[index + 2].content }}
      </template>
    </comment>
  </div>
</template>

<script setup>
import about from "./About.vue"
import merchandise from "./Merchandise.vue"
import gallery from "./Gallery.vue"
import comment from "./Comment.vue"
import { ref, onMounted } from "vue"

const store = ref([{ name: "光慧水煎包", subName: "(梧棲店)" }])
const timetableTitle = ref("正常營業時間")
const newsTitle = ref("近期公告")
const newsContents = ref(["暫無新公告"])
const days = ref(["週一", "週二", "週三", "週四", "週五", "週六", "週日"])
const times = ref(["06:00~09:00", "15:00~17:00", "公休"])
const sections = ref([
  {
    title: "水煎包",
    content:
      "主要賣三種水煎包，內餡分別為高麗菜、竹筍、冬粉，每個售價18元\n飲料有 紅茶10元、奶茶15元"
  },
  {
    title: "相片集",
    content:
      "由商家提供的照片，其中包含最新實體店面、三種水煎包、水煎包烹煮過程，拍攝技術拙劣還請見諒"
  },
  {
    title: "評論區",
    content: "評論皆於Google評論索取，五星好評謝謝大家的支持"
  }
])
const index = ref(0)
const mobile = ref(null)
const mobileIcon = ref(null)

onMounted(() => {
  window.addEventListener("resize", checkScreen)
  checkScreen()
})
const checkScreen = () => {
  const windowWidth = window.innerWidth
  if (windowWidth <= 992) {
    mobileIcon.value = true
    mobile.value = true
    return
  }
  mobileIcon.value = false
  mobile.value = false
}
</script>

<script>
export default {
  data () {
    return {
      facebookSrc: "https://reurl.cc/9pbQ2O",
      mapSrc: "https://reurl.cc/yMKlzD"
    }
  },
  components: { about, merchandise, comment, gallery }
}
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/time.scss";
@import "@/assets/scss/Home/news.scss";
</style>
