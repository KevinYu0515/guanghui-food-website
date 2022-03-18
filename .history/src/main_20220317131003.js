import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false
Vue.use(Carousel3d)
Vue.use(vuePositionSticky)
new Vue({
  router,
  vuetify,
  render: function (h) { return h(App) },
  mounted: () => document.dispatchEvent(new Event("x-app-rendered")),
}).$mount('#app'

createApp(App).use(router).mount('#app')
