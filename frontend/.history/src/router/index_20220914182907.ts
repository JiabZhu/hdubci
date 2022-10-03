import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/rsvponline/adddevice',
    name: 'adddevice',
    component: () => import('../views/AddDeviceView.vue')
  },
  {
    path: '/rsvpoffline/setstudy',
    name: 'setstudy',
    component: () => import('../views/SetStudyView.vue')
  },
  {
    path: '/rsvpoffline/setstudy',
    name: 'setstudy',
    component: () => import('../views/SetStudyView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
