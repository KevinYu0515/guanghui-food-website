import { createApp } from "vue"
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import App from "./App.vue"
import AOS from "aos"
import router from "./router"
import Button from "primevue/button"
import PrimeVue from "primevue/config"
import VueLoading from "vue-loading-overlay"
import StarRating from "vue-star-rating"
import "swiper/swiper-bundle.css"
import "aos/dist/aos.css"
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"

AOS.init({
  offset: 10,
  duration: 1000,
  delay: 2,
  once: true
})
AOS.refreshHard()

const app = createApp(App)
app.component("loading", VueLoading)
  .component("Button", Button)
  .component("StarRating", StarRating)
  .component("Swiper", Swiper)
  .component("SwiperSlide", SwiperSlide)
  .use(router, AOS, PrimeVue)
  .mount("#app")
