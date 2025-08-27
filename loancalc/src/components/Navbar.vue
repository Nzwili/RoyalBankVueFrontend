<template>
  <nav class="navbar">
    <div class="navbar-container">
      <!-- Logo -->
      <router-link to="/" class="logo">
        <img src="D:\WEB DVPMT\Vue LoanCalc\loancalc\src\assets\logo.png" alt="Royal Bank Logo" />
        <span>Royal Bank</span>
      </router-link>

      <!-- Navigation Links -->
      <ul class="nav-links">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/loan-calculator">Loan Calculator</router-link></li>
        <li><router-link to="/about">About Us</router-link></li>
        <li><router-link to="/services">Services</router-link></li>
        <li><router-link to="/blog">Blog</router-link></li>
        <li><router-link to="/support">Support</router-link></li>
      </ul>

      <!-- Auth Buttons -->
      <div class="auth-buttons">
        <router-link to="/login" class="btn login">Login</router-link>
        <router-link to="/signup" class="btn signup">Sign Up</router-link>
      </div>
    </div>
  </nav>
</template>

<script setup>
</script>

<style scoped>
/* Navbar wrapper */
.navbar {
  background-color: #1a237e; /* Deep Royal Blue */
  color: white;
  padding: 0.8rem 2rem;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

/* Flex container */
.navbar-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Logo */
.logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  color: white;
  font-weight: bold;
  font-size: 1.2rem;
}

.logo img {
  height: 35px;
}

/* Links */
.nav-links {
  display: flex;
  gap: 1.5rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-links a {
  text-decoration: none;
  color: white;
  font-size: 0.95rem;
  transition: color 0.3s;
}

.nav-links a:hover,
.router-link-active {
  color: #ffca28; /* Gold accent */
}

/* Auth buttons */
.auth-buttons {
  display: flex;
  gap: 1rem;
}

.btn {
  padding: 0.4rem 1rem;
  border-radius: 20px;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn.login {
  background: transparent;
  border: 1px solid #fff;
  color: white;
}

.btn.login:hover {
  background: white;
  color: #1a237e;
}

.btn.signup {
  background: #ffca28;
  color: #1a237e;
  border: none;
}

.btn.signup:hover {
  background: #ffc107;
}
</style>
