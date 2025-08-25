<template>
  <nav class="navbar">
    <div class="nav-left">
      <a href="/"> <img src="@/assets/logo.png" alt="Logo" class="logo"  /></a>
      <span class="brand">Royal Bank</span>
    </div>
    <ul class="nav-links">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/">About Us</router-link></li>
      <li><router-link to="/loan">Loan Calculator</router-link></li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #004080;
  padding: 0.8rem 2rem;
  color: white;
}
.nav-left {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.logo {
  height: 32px;
  width: 32px;
}
.brand {
  font-size: 1.2rem;
  font-weight: bold;
}
.nav-links {
  list-style: none;
  display: flex;
  gap: 1rem;
  margin: 0;
  padding: 0;
}
.nav-links a {
  color: white;
  text-decoration: none;
}
.nav-links a.router-link-active {
  border-bottom: 2px solid white;
  padding-bottom: 2px;
}
</style>
