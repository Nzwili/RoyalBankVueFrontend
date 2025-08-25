<template>
  <div id="app">
    <Navbar />
    <main class="content">
      <router-view /> <!-- Page content renders here -->
    </main>
    <HelpBot />
    <Footer />
  </div>
</template>

<script setup>
import Footer from './components/Footer.vue';
import HelpBot from './components/HelpBot.vue';
import Navbar from './components/Navbar.vue'
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
.content {
  min-height: calc(100vh - 60px); /* adjust for navbar height */
  padding: 2rem;
}
</style>
