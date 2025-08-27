import { createRouter, createWebHistory } from 'vue-router'

// Import pages
import Home from '../Pages/Home.vue'
import LoanCalculator from '../Pages/LoanCalculator.vue'
import Login from '../Pages/Login.vue'
import Signup from '../Pages/SignUp.vue'
import About from '../Pages/About.vue'
import Blog from '../Pages/Blog.vue'
import Support from '../Pages/Support.vue'
import Services from '../Pages/Services.vue'
import ServiceDetail from '../Pages/ServiceDetail.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/loan-calculator', component: LoanCalculator },
  { path: '/login', component: Login },
  { path: '/signup', component: Signup },
  { path: '/about', component: About },
  { path: '/services', component: Services },
  { path: '/services/:id', component: ServiceDetail },
  { path: '/blog', component: Blog },
  { path: '/support', component: Support },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: () => import("../views/dashboard.vue")
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
