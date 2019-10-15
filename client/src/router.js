import Vue from 'vue';
import Router from 'vue-router';
import Status from './components/Status.vue';
import Users from './components/Users.vue';
import Landing from './components/Landing.vue';
import Menu from './components/Menu.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/status',
      name: 'Status',
      component: Status,
    },
    {
      path: '/users',
      name: 'Users',
      component: Users,
    },
    {
      path: '',
      name: 'Landing',
      component: Landing,
    },
    {
      path: '/menu',
      name: 'Menu',
      component: Menu,
    },

  ],
});
