<template>
  <div id="app">
    <Navbar />

    <main class="content">
      <router-view /> <!-- Page content renders here -->
    </main>

    <Footer />
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
</script>

<style>
/* Reset margins/paddings */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background: #f9f9f9;
  color: #333;
}

/* Main area should not push navbar/footer weirdly */
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.content {
  flex: 1;
  padding: 2rem;
}
</style>
