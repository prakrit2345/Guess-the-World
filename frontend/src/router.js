// router.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './components/homepage.vue'
import Menu from './components/menu.vue'
import Login from './components/login.vue'
import Register from './components/register.vue'
import Multiplayer from './components/multiplayer.vue'
import Guest from './components/guest.vue'
import Home from './components/home.vue'
import Cookies from 'js-cookie'

const routes = [
  { path: '/', component: HomePage },
  { path: '/menu', component: Menu },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/multiplayer', component: Multiplayer },
  { path: '/guest', component: Guest },
  { path: '/home', component: Home, meta: { requiresAuth: true }}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
router.beforeEach((to) => {
  const token = Cookies.get('access_token')

  if (to.meta.requiresAuth && !token) {
    return '/login'
  }

  if (to.path === '/login' && token) {
    return '/home'
  }
})


export default router