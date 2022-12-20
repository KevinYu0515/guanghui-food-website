import { createRouter, createWebHistory } from "vue-router"
const routes = [
  {
    path: "/",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home.vue")
  },
  {
    path: "/time",
    name: "time",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home.vue")
  },
  {
    path: "/merchandise",
    name: "merchandise",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home.vue")
  },
  {
    path: "/photos",
    name: "photos",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home.vue")
  },
  {
    path: "/comment",
    name: "comment",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home.vue")
  },
  {
    path: "/contact",
    name: "contact",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home.vue"),
    meta: { scrollToBottom: true }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else if (to.name) {
      if (to.matched.some(m => m.meta.scrollToBottom)) {
        return {
          top: 1000000,
          behavior: "smooth"
        }
      }
      return {
        el: `#${to.name}`,
        top: 100,
        behavior: "smooth"
      }
    }
  }
})

export default router
