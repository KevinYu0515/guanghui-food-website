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
        <i class="icon-500 fi fi-brands-facebook"/>
      </a>
    </div>
    <div class="map" v-show="!mobileIcon" data-aos="fade-up">
      <a :href="mapSrc">
        <i class="icon-500 fi fi-bs-marker"/>
      </a>
    </div>
    <div class="calling" v-show="!mobileIcon" data-aos="fade-up">
      <i class="icon-500 fi fi-ss-phone-call"/>
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
import json from "../../python/text.json"

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
      store: json[0].store,
      timetableTitle: json[0].timetableTitle,
      newsTitle: json[0].newsTitle,
      newsContents: json[0].newsContents,
      days: json[0].days,
      times: json[0].times,
      sections: json[0].sections,
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
