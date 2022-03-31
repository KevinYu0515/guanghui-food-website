import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/',
    name: 'Merchandise',
    component: Home
  },
  {
    path: '/',
    name: 'Photos',
    component: Home
  },
  {
    path: '/',
    name: 'Comment',
    component: Home
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to,from,savedPosition){
    if(savedPosition){
      return savedPosition;
    }else if(to.hash){
      if(to.hash=="/#contact"){
          return {
            bottom:0,
            behavior: 'smooth',
          } 
      }else{
        return {
          el: to.hash,
          top:-100,
          behavior: 'smooth',
          }
      }
    }
  }
})

export default router
