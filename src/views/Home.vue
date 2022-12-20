<template>
  <div class="home">
    <button class="btn-to-top" v-show="scroll" @click="toTop"> <i class="fi fi-br-angle-double-small-up icon-150" style="color: #ee7748"></i></button>
    <section id="time">
      <p class="store-name">{{ store.name }}</p>
      <p class="store-subName">{{ store.subName }}</p>
      <div class="timetable">
        <p class="timetable-title">{{ timeTable.title }}</p>
        <ul>
          <li v-for="(day, index) in timeTable.content.days.slice(0, 5)" :key="index">
            {{ day }} &nbsp;&nbsp;
            <p>{{ timeTable.content.time[0] }}、{{ timeTable.content.time[1] }} </p>
          </li>
          <li>
            {{ timeTable.content.days[5] }} &nbsp;&nbsp;
            <p>{{ timeTable.content.time[0] }}</p>
          </li>
          <li>{{ timeTable.content.days[6] }} &nbsp; {{ timeTable.content.time[2] }}</li>
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
    <news></news>
    <about data-aos-anchor-placement="center-bottom" data-aos="fade-up"></about>
    <merchandise data-aos-anchor-placement="center-bottom" data-aos="fade-up"></merchandise>
    <gallery data-aos-anchor-placement="center-bottom" data-aos="fade-up"></gallery>
    <comment data-aos-anchor-placement="center-bottom" data-aos="fade-up"></comment>
  </div>
</template>

<script setup>
import { storeNames, timeTableBlock } from "../firebase"
import { getDoc } from "firebase/firestore"
import { ref, reactive, onMounted, onBeforeMount, defineExpose } from "vue"
import news from "./News.vue"
import about from "./About.vue"
import merchandise from "./Merchandise.vue"
import gallery from "./Gallery.vue"
import comment from "./Comment.vue"

const loading = ref(true)
const mobile = ref(null)
const mobileIcon = ref(null)
const scrollTop = ref(0)
const scroll = ref(false)
const store = reactive({
  name: "",
  subName: ""
})
const timeTable = reactive({
  title: "",
  content: {
    days: [],
    time: []
  }
})
const facebookSrc = "https://reurl.cc/9pbQ2O"
const mapSrc = "https://reurl.cc/yMKlzD"

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

const toTop = () => {
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

onBeforeMount(() => {
  checkScreen()
  console.log("beforeMount")
  getDoc(storeNames)
    .then(response => {
      store.name = response.data().name
      store.subName = response.data().subName
    })
  getDoc(timeTableBlock)
    .then(response => {
      timeTable.title = response.data().title
      timeTable.content = response.data().content
      console.log("getData")
      loading.value = false
    })
})

onMounted(() => {
  console.log("onMounted")
  window.addEventListener("resize", checkScreen)
  window.addEventListener("scroll", showbtn, true)
  checkScreen()
})

defineExpose({ loading })
</script>

<style lang="scss" scoped>
@import "../assets/scss/index.scss";
@import "@/assets/scss/Home/time.scss";
</style>
