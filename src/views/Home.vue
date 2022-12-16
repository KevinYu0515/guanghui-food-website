<template>
  <div class="home">
    <button class="btn-to-top" v-show="scroll" @click="toTop"> <i class="fi fi-br-angle-double-small-up icon-150" style="color: #ee7748"></i></button>
    <section id="time">
      <p class="store-name">{{ storeName }}</p>
      <p class="store-subName">{{ storeSubName }}</p>
      <div class="timetable">
        <p class="timetable-title">{{ timeTableTitle }}</p>
        <ul>
          <li v-for="(day, index) in timeTableContent.days.slice(0, 5)" :key="index">
            {{ day }} &nbsp;&nbsp;
            <p>{{ timeTableContent.time[0] }}、{{ timeTableContent.time[1] }} </p>
          </li>
          <li>
            {{ timeTableContent.days[5] }} &nbsp;&nbsp;
            <p>{{ timeTableContent.time[0] }}</p>
          </li>
          <li>{{ timeTableContent.days[6] }} &nbsp; {{ timeTableContent.time[2] }}</li>
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
    <merchandise></merchandise>
    <gallery></gallery>
    <comment></comment>
  </div>
</template>

<script>
import { storeNames, timeTable, news } from "../firebase"
import { getDoc } from "firebase/firestore"
import about from "./About.vue"
import merchandise from "./Merchandise.vue"
import gallery from "./Gallery.vue"
import comment from "./Comment.vue"
import { ref, onMounted, getCurrentInstance } from "vue"

export default {
  data () {
    return {
      storeName: "",
      storeSubName: "",
      newsTitle: "",
      newsContents: [],
      timeTableTitle: "",
      timeTableContent: { days: [], time: [] },
      facebookSrc: "https://reurl.cc/9pbQ2O",
      mapSrc: "https://reurl.cc/yMKlzD"
    }
  },
  components: { about, merchandise, comment, gallery },
  methods: {
    toTop () {
      const timer = setInterval(function () {
        const osTop = document.documentElement.scrollTop || document.body.scrollTop
        const ispeed = Math.floor(-osTop / 5)
        document.documentElement.scrollTop = document.body.scrollTop = osTop + ispeed
        this.isTop = true
        if (osTop === 0) {
          clearInterval(timer)
        }
      }, 30)
    }
  }
}
</script>

<script setup>
const Instance = getCurrentInstance()
const mobile = ref(null)
const mobileIcon = ref(null)
const scrollTop = ref(0)
const scroll = ref(false)

onMounted(() => {
  window.addEventListener("resize", checkScreen)
  window.addEventListener("scroll", showbtn, true)
  checkScreen()
  getTimeTableData()
  getStoreNameData()
  getNewsData()
})

const getStoreNameData = () => {
  getDoc(storeNames)
    .then((response) => {
      console.log(response.data())
      Instance.data.storeName = response.data().name
      Instance.data.storeSubName = response.data().subName
    })
}

const getTimeTableData = () => {
  getDoc(timeTable)
    .then((response) => {
      Instance.data.timeTableTitle = response.data().title
      Instance.data.timeTableContent = response.data().content
    })
}

const getNewsData = () => {
  getDoc(news)
    .then((response) => {
      Instance.data.newsTitle = response.data().title
      Instance.data.newsContents = response.data().content
    })
}

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
const showbtn = () => {
  scrollTop.value = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
  if (scrollTop.value !== 0) {
    scroll.value = true
  } else scroll.value = false
}
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/time.scss";
@import "@/assets/scss/Home/news.scss";
</style>
