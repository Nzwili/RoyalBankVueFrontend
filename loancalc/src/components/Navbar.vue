<template>
  <nav class="navbar">
    <div class="navbar-container">
      <!-- Logo -->
      <router-link to="/" class="logo">
        <img src="@/assets/logo.png" alt="Royal Bank Logo" />
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
        <!-- Welcome message if logged in -->
        <span v-if="user && user.name" class="welcome">Hello, {{ user.name }}</span>

        <!-- Login/Signup if not logged in -->
        <router-link v-if="!user || !user.name" to="/login" class="btn login">Login</router-link>
        <router-link v-if="!user || !user.name" to="/signup" class="btn signup">Sign Up</router-link>

        <!-- Logout button if logged in -->
        <button v-if="user && user.name" @click="handleLogout" class="btn logout">Logout</button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import { useAuth } from "../composables/useAuth.js";

const router = useRouter();
const { user, loadUser, logout } = useAuth();

// Load user from localStorage when Navbar mounts
onMounted(() => {
  loadUser();
});

function handleLogout() {
  logout(); // Clear user state and localStorage
  router.push("/login"); // Redirect to login
}
</script>

<style scoped>
.navbar {
  background-color: #1a237e;
  color: white;
  padding: 0.8rem 2rem;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.navbar-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.logo { 
  display: flex; 
  align-items: center; 
  gap: 0.5rem; 
  text-decoration: none; 
  color: white; 
  font-weight: bold; 
  font-size: 1.2rem; 
}
.logo img { height: 35px; }
.nav-links { display: flex; gap: 1.5rem; list-style: none; margin: 0; padding: 0; }
.nav-links a { text-decoration: none; color: white; font-size: 0.95rem; transition: color 0.3s; }
.nav-links a:hover, .router-link-active { color: #ffca28; }
.auth-buttons { display: flex; gap: 1rem; align-items: center; }
.btn { padding: 0.4rem 1rem; border-radius: 20px; text-decoration: none; font-size: 0.9rem; font-weight: 600; transition: all 0.3s ease; cursor: pointer; }
.btn.login { background: transparent; border: 1px solid #fff; color: white; }
.btn.login:hover { background: white; color: #1a237e; }
.btn.signup { background: #ffca28; color: #1a237e; border: none; }
.btn.signup:hover { background: #ffc107; }
.btn.logout { background: #ff5252; color: white; border: none; }
.btn.logout:hover { background: #ff1744; }
.welcome { font-weight: 500; }
</style>
