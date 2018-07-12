import Vue from 'vue'
import Router from 'vue-router'
import UserAuth from '@/components/UserAuth'
import Channels from '@/components/Channels'
import BaseChat from '@/components/BaseChat'
Vue.use(Router);


const router = new Router({
  routes: [
    {
      path: '/auth',
      name: 'UserAuth',
      component: UserAuth
    },
    {
      path: '/channels',
      name: 'Channels',
      component: Channels
    },

    {
      path: '/chat/:id?',
      name: 'BaseChat',
      component: BaseChat
    }
  ]
});

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
    next()
  } else {
    next('/auth')
  }
});

export default router
