<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>

   </div>
</template>

<script>

 import Navbar from './components/Navbar.vue';

export default {
  name: 'App',
  data() {
    return {
      msg: 'Hello!',
    };
  },
   components: {
    navbar: Navbar,
  },
};

</script>