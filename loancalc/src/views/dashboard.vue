<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useAuth } from "../composables/useAuth.js";

const router = useRouter();
const user = ref(null);

onMounted(() => {
  const storedUser = localStorage.getItem("user");
  if (storedUser) {
    user.value = JSON.parse(storedUser);
    requireAuth(); 
  }
});

function handleLogout() {
  localStorage.removeItem("user");
  user.value = null; // update state
  alert("You have been logged out.");
  router.push("/login");
}
</script>


<template>
  <div class="dashboard-page">
    <div class="dashboard-card">
      <h1>Welcome, {{ user?.name || "User" }} 🎉</h1>
      <p class="subtitle">You are logged in successfully</p>

      <div class="links">
        <router-link to="/calculator" class="btn">Go to Calculator</router-link>
        <router-link v-if="!user" to="/login" class="btn-outline">Login</router-link>
        <router-link v-if="!user" to="/signup" class="btn-outline">Signup</router-link>
        <button v-if="user" @click="handleLogout" class="btn-logout">Logout</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #f8fafc;
}

.dashboard-card {
  background: white;
  max-width: 480px;
  width: 100%;
  padding: 2rem;
  border-radius: 1rem;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

h1 { font-size: 2rem; margin-bottom: 0.5rem; }
.subtitle { color: #64748b; margin-bottom: 1.5rem; }

.links {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.btn, .btn-outline, .btn-logout {
  display: block;
  padding: 0.75rem;
  border-radius: 0.5rem;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  text-align: center;
}

.btn {
  background: #3b82f6;
  color: white;
  border: none;
}
.btn:hover { background: #2563eb; }

.btn-outline {
  border: 2px solid #3b82f6;
  color: #3b82f6;
  background: transparent;
}
.btn-outline:hover { background: #e0f2fe; }

.btn-logout {
  background: #ef4444;
  color: white;
  border: none;
}
.btn-logout:hover { background: #dc2626; }
</style>
