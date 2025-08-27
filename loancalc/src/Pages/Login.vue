<script setup>
import { ref } from "vue";

const email = ref("");
const password = ref("");

async function handleLogin() {
  try {
    const res = await fetch("http://127.0.0.1:8000/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: email.value,
        password: password.value,
      }),
    });

    if (!res.ok) {
      const errorText = await res.text();
      throw new Error(`Login failed: ${errorText}`);
    }

    const data = await res.json();
    console.log("✅ Login success:", data);
    alert("🎉 Welcome back!");

    router.push("/dashboard");
  } catch (err) {
    console.error(err);
    alert(err.message);
  }
}
</script>


<template>
  <div class="auth-page">
    <div class="auth-card">
      <h1>Welcome Back</h1>
      <p class="subtitle">Login to continue</p>

      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label>Email</label>
          <input type="email" v-model="email" required placeholder="Enter your email" />
        </div>

        <div class="form-group">
          <label>Password</label>
          <input type="password" v-model="password" required placeholder="Enter your password" />
        </div>

        <button type="submit" class="btn" :disabled="loading">
          {{ loading ? "Logging in..." : "Login" }}
        </button>
      </form>

      <p v-if="error" class="msg error">{{ error }}</p>
      <p v-if="success" class="msg success">{{ success }}</p>

      <p class="switch">
        Don’t have an account?
        <router-link to="/signup">Sign up</router-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
.auth-page {
  display: flex; justify-content: center; align-items: center;
  min-height: 100vh; background: #f8fafc;
}
.auth-card {
  background: white; padding: 2rem; border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  width: 100%; max-width: 400px; text-align: center;
}
h1 { font-size: 1.75rem; margin-bottom: 0.5rem; }
.subtitle { color: #64748b; margin-bottom: 1.5rem; }
.form-group { text-align: left; margin-bottom: 1rem; }
label { display: block; margin-bottom: 0.25rem; font-weight: 500; }
input {
  width: 100%; padding: 0.75rem; border: 1px solid #cbd5e1;
  border-radius: 0.5rem; outline: none;
}
input:focus { border-color: #3b82f6; }
.btn {
  width: 100%; padding: 0.75rem; background: #3b82f6; color: white;
  border: none; border-radius: 0.5rem; cursor: pointer; font-weight: 600;
}
.btn:disabled { background: #94a3b8; cursor: not-allowed; }
.switch { margin-top: 1rem; color: #64748b; }
.msg { margin-top: 1rem; font-size: 0.9rem; }
.error { color: red; }
.success { color: green; }
</style>
