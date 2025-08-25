<template>
  <div class="home">
    <section class="hero">
        <img src=""></img>
      <h1>Welcome to Royal Bank</h1>
      <p>Your trusted partner in personal and business finance.</p>
    </section>
  </div>
</template>

<style scoped>
.hero {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 70vh;
  text-align: center;
}
.hero h1 { font-size: 2.5rem; margin-bottom: 1rem; }
.hero p { font-size: 1.2rem; margin-bottom: 2rem; color: #555; }
.btn {
  background: #42b883;
  color: white;
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
}
.btn:hover { background: #36a36d; }
</style>
