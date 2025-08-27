<script setup>
import { ref } from "vue";

const name = ref("");
const email = ref("");
const password = ref("");

async function handleSignup() {
  try {
    const res = await fetch("http://127.0.0.1:8000/auth/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: name.value,
        email: email.value,
        password: password.value,
      }),
    });

    if (!res.ok) {
      const errorText = await res.text();
      throw new Error(`Signup failed: ${errorText}`);
    }

    const data = await res.json();
    console.log("✅ Signup success", data);
    alert("🎉 Account created successfully! Please Log in");
    router.push("/login");
  } catch (err) {
    console.error(err);
    alert(err.message);
  }
}
</script>


<template>
  <div class="auth-page">
    <div class="auth-card">
      <h1>Create Account</h1>
      <p class="subtitle">Join us today</p>

      <form @submit.prevent="handleSignup">
        <div class="form-group">
          <label>Full Name</label>
          <input type="text" v-model="name" required placeholder="Enter your name" />
        </div>

        <div class="form-group">
          <label>Email</label>
          <input type="email" v-model="email" required placeholder="Enter your email" />
        </div>

        <div class="form-group">
          <label>Password</label>
          <input type="password" v-model="password" required placeholder="Enter your password" />
        </div>

        <button type="submit" class="btn" :disabled="loading">
          {{ loading ? "Signing up..." : "Sign Up" }}
        </button>
      </form>

      <p v-if="error" class="msg error">{{ error }}</p>
      <p v-if="success" class="msg success">{{ success }}</p>

      <p class="switch">
        Already have an account?
        <router-link to="/login">Login</router-link>
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
