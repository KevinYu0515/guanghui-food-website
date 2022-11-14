import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"
import axios from "axios"
import PrimeVue from "primevue/config"
import Button from "primevue/button"
import VueLoading from "vue-loading-overlay"

import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"

createApp(App)
  .component("loading", VueLoading)
  .component("Button", Button)
  .use(router, axios)
  .use(PrimeVue)
  .mount("#app")
