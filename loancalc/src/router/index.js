import { createRouter, createWebHistory } from 'vue-router'
import Home from '../Pages/Home.vue'
import LoanCalculator from '../Pages/LoanCalculator.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/loan', component: LoanCalculator }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
