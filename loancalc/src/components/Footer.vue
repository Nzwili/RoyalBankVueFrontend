<template>
  <footer class="footer">
    <div class="footer-container">
      <!-- Left side: Logo & Name -->
      <div class="footer-logo">
        <img src="@/assets/logo.png" alt="Royal Bank Logo" />
        <span>Royal Bank</span>
      </div>

      <!-- Center: Links -->
      <ul class="footer-links">
        <li><router-link to="/about">About Us</router-link></li>
        <li><router-link to="/blog">Blog</router-link></li>
        <li><router-link to="/support">Support</router-link></li>
        <li><router-link to="/loan-calculator">Loan Calculator</router-link></li>
      </ul>

      <!-- Right side: Socials -->
      <div class="footer-socials">
        <a href="#" target="_blank">🌐</a>
        <a href="#" target="_blank">🐦</a>
        <a href="#" target="_blank">📘</a>
      </div>
    </div>

    <!-- Bottom small text -->
    <div class="footer-bottom">
      <p>© 2025 Royal Bank. All Rights Reserved.</p>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: #002b5c;
  color: white;
  padding: 1.5rem 2rem;
  margin-top: 2rem;
}

.footer-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.footer-logo img {
  height: 35px;
}

.footer-links {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  padding: 0;
  margin: 0;
}

.footer-links a {
  color: white;
  text-decoration: none;
  font-size: 0.95rem;
  transition: 0.2s;
}

.footer-links a:hover {
  text-decoration: underline;
}

.footer-socials a {
  margin-left: 0.8rem;
  font-size: 1.2rem;
  text-decoration: none;
  color: white;
}

.footer-socials a:hover {
  opacity: 0.7;
}

.footer-bottom {
  text-align: center;
  margin-top: 1rem;
  font-size: 0.85rem;
  opacity: 0.8;
}

/* Mobile view */
@media (max-width: 768px) {
  .footer-container {
    flex-direction: column;
    text-align: center;
  }

  .footer-links {
    flex-direction: column;
    gap: 0.8rem;
  }

  .footer-socials {
    margin-top: 0.5rem;
  }
}
</style>
