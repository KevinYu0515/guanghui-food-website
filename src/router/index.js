import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   component: Home
  // },
  // {
  //   path: '/picture',
  //   name: 'Picture',
  //   component: Home
  // },
  // {
  //   path: '/contact',
  //   name: 'Contact',
  //   component: Home
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to,from,savedPosition){
    if(savedPosition){
      return savedPosition;
    }else if(to.hash){
        return {
            el: to.hash,
            behavior: 'smooth',
        }
    }
}
})

export default router
