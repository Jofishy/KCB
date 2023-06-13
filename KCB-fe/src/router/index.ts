import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: LandingView
    },
    {
      path: '/about',
      // lazy-loaded when the route is visited
      component: () => import('../views/AboutView.vue')
    }, {
      path: '/recipe/:id',
      component: () => import('../views/RecipeView.vue')
    }
  ]
})

export default router
