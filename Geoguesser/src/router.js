// router.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './components/homepage.vue'
import Menu from './components/menu.vue'
import Login from './components/login.vue'
import Register from './components/register.vue'
import Multiplayer from './components/multiplayer.vue'
import Guest from './components/guest.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/menu', component: Menu },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
 { path: '/multiplayer', component: Multiplayer },
  { path: '/guest', component: Guest }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router