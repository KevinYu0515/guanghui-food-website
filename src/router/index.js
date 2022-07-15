import { createRouter, createWebHistory } from "vue-router"
import Home from "../views/Home.vue"

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/time",
    name: "time",
    component: Home
  },
  {
    path: "/merchandise",
    name: "merchandise",
    component: Home
  },
  {
    path: "/photos",
    name: "photos",
    component: Home
  },
  {
    path: "/comment",
    name: "comment",
    component: Home
  },
  {
    path: "/contact",
    name: "contact",
    component: Home,
    meta: { scrollToBottom: true }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  hashchange () {
    const local = location.hash
    console.log(local)
  },
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else if (to.name) {
      if (to.matched.some(m => m.meta.scrollToBottom)) {
        return {
          top: 3000,
          behavior: "smooth"
        }
      }
      return {
        el: `#${to.name}`,
        top: 200,
        behavior: "smooth"
      }
    }
  }
})

export default router
