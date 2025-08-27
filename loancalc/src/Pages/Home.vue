<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1>Welcome to Royal Bank</h1>
        <p>Smart. Secure. Modern banking at your fingertips.</p>
        <router-link to="/signup" class="cta-btn">Open an Account</router-link>
      </div>
      <div class="hero-image">
        <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/512/external-banking-banking-flaticons-lineal-color-flat-icons.png" alt="Banking Illustration">
      </div>
    </section>

    <!-- Services -->
    <section class="services">
      <h2>Our Services</h2>
      <div class="services-grid">
        <div class="service-card">
          <h3>💳 Digital Banking</h3>
          <p>24/7 secure access to your accounts from anywhere.</p>
        </div>
        <div class="service-card">
          <h3>🏦 Loans</h3>
          <p>Flexible loans designed to support your goals.</p>
        </div>
        <div class="service-card">
          <h3>📈 Investments</h3>
          <p>Grow your wealth with our safe investment options.</p>
        </div>
        <div class="service-card">
          <h3>🌍 Global Transfers</h3>
          <p>Send money worldwide instantly and securely.</p>
        </div>
      </div>
    </section>
    <router-link to="/services" class="see-all">See All Services →</router-link>


    <!-- Stats -->
    <section class="stats">
      <div class="stat">
        <h2>2M+</h2>
        <p>Happy Customers</p>
      </div>
      <div class="stat">
        <h2>50+</h2>
        <p>Branches Worldwide</p>
      </div>
      <div class="stat">
        <h2>$5B+</h2>
        <p>Assets Managed</p>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="testimonials">
      <h2>What Our Customers Say</h2>
      <div class="testimonial-grid">
        <div class="testimonial">
          <p>"Royal Bank made it so easy to get my first loan. Fast and transparent!"</p>
          <span>- James K.</span>
        </div>
        <div class="testimonial">
          <p>"I love the mobile banking app. Managing money has never been this smooth."</p>
          <span>- Aisha M.</span>
        </div>
        <div class="testimonial">
          <p>"Their investment plans helped me grow my savings securely."</p>
          <span>- Brian O.</span>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="cta">
      <h2>Ready to start banking smarter?</h2>
      <router-link to="/signup" class="cta-btn">Join Royal Bank Today</router-link>
    </section>
  </div>
</template>

<script setup></script>

<style scoped>
/* HERO */
.hero {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 3rem 2rem;
  background: linear-gradient(to right, #1a237e, #3949ab);
  color: white;
  border-radius: 12px;
  margin-bottom: 3rem;
}
.hero-content {
  max-width: 50%;
}
.hero-content h1 {
  font-size: 2.8rem;
  margin-bottom: 1rem;
}
.hero-content p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
}
.hero-image img {
  max-width: 280px;
}
.cta-btn {
  padding: 0.8rem 1.5rem;
  background: #ffca28;
  color: #1a237e;
  font-weight: bold;
  border-radius: 30px;
  text-decoration: none;
  transition: 0.3s;
}
.cta-btn:hover {
  background: #ffc107;
}

/* SERVICES */
.services {
  text-align: center;
  margin: 3rem 0;
}
.services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-top: 2rem;
}
.service-card {
  background: #f9f9f9;
  padding: 1.5rem;
  border-radius: 10px;
  transition: 0.3s;
}
.service-card:hover {
  background: #e8eaf6;
  transform: translateY(-5px);
}
.see-all {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.6rem 1.2rem;
  background: #1976d2;
  color: #fff;
  border-radius: 8px;
  text-decoration: none;
  transition: background 0.3s ease;
}
.see-all:hover {
  background: #0d47a1;
}


/* STATS */
.stats {
  display: flex;
  justify-content: space-around;
  background: #1a237e;
  color: white;
  padding: 2rem 1rem;
  margin: 3rem 0;
  border-radius: 10px;
}
.stat h2 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

/* TESTIMONIALS */
.testimonials {
  text-align: center;
  margin: 3rem 0;
}
.testimonial-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-top: 2rem;
}
.testimonial {
  background: #f4f4f4;
  padding: 1.5rem;
  border-radius: 10px;
  font-style: italic;
}

/* CTA Footer */
.cta {
  text-align: center;
  padding: 3rem 2rem;
  background: linear-gradient(to right, #3949ab, #5c6bc0);
  color: white;
  border-radius: 12px;
  margin-top: 3rem;
}
</style>
