import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/rsvpoffline/adddevice',
    name: 'adddOffevice',
    component: () => import('../views/AddDeviceView.vue')
  },
  {
    path: '/rsvponline/adddevice',
    name: 'adddOnevice',
    component: () => import('../views/AddDeviceView.vue'),
  },
  {
    path: '/rsvpoffline/setstudy',
    name: 'setOffstudy',
    component: () => import('../views/SetOffStudyView.vue')
  },
  {
    path: '/rsvponline/setstudy',
    name: 'setOnstudy',
    component: () => import('../views/SetOnStudyView.vue')
  },
  {
    path: '/admin',
    name: 'AdminOnstudy',
    component: () => import('../views/AdminView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
