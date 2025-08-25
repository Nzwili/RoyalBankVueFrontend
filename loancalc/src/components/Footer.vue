<template>
  <footer class="footer">
    <div class="footer-content">
      <p>&copy; 2025 Royal Bank. All rights reserved.</p>
      <nav class="footer-links">
        <a href="#">Privacy Policy</a>
        <a href="#">Terms</a>
        <a href="#">Contact</a>
      </nav>
    </div>
  </footer>
</template>

<script setup>
// no props for now, but we can add dynamic content later
</script>

<style scoped>
.footer {
  background: #2c3e50;
  color: #fff;
  padding: 1rem 2rem;
  margin-top: 2rem;
  text-align: center;
}
.footer-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.footer-links {
  margin-top: 0.5rem;
}
.footer-links a {
  color: #42b883;
  margin: 0 0.5rem;
  text-decoration: none;
  font-size: 0.9rem;
}
.footer-links a:hover {
  text-decoration: underline;
}
</style>
