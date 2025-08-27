<template>
  <section class="about">
    <!-- Hero -->
    <div class="about-hero">
      <h1>About Royal Bank</h1>
      <p>Building trust, innovation, and growth in modern banking.</p>
    </div>

    <!-- Mission & Vision -->
    <div class="about-cards">
      <div class="card">
        <h2>🎯 Our Mission</h2>
        <p>
          To empower individuals and businesses through accessible, reliable, 
          and modern banking solutions.
        </p>
      </div>
      <div class="card">
        <h2>🌍 Our Vision</h2>
        <p>
          To be the most customer-centric financial institution in Africa, 
          redefining how people interact with their money.
        </p>
      </div>
    </div>

    <!-- Values -->
    <div class="about-values">
      <h2>Our Core Values</h2>
      <ul>
        <li>✔ Trust & Transparency</li>
        <li>✔ Innovation</li>
        <li>✔ Customer First</li>
        <li>✔ Sustainability</li>
      </ul>
    </div>

    <!-- History Timeline -->
    <div class="about-history">
      <h2>Our Journey</h2>
      <div class="timeline">
        <div class="timeline-item">
          <span class="year">2005</span>
          <p>Royal Bank was founded with a mission to provide secure banking solutions.</p>
        </div>
        <div class="timeline-item">
          <span class="year">2015</span>
          <p>Launched digital banking, making accounts accessible on mobile devices.</p>
        </div>
        <div class="timeline-item">
          <span class="year">2025</span>
          <p>Royal Bank leads in innovation with AI-driven financial services.</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup></script>

<style scoped>
.about-hero {
  text-align: center;
  padding: 3rem 2rem;
  background: linear-gradient(to right, #1a237e, #3949ab);
  color: white;
  border-radius: 10px;
}
.about-cards {
  display: flex;
  justify-content: space-around;
  margin: 3rem 0;
  gap: 1.5rem;
}
.card {
  flex: 1;
  padding: 2rem;
  background: #f9f9f9;
  border-radius: 10px;
  text-align: center;
}
.about-values {
  text-align: center;
  margin: 3rem 0;
}
.about-values ul {
  list-style: none;
  padding: 0;
}
.about-values li {
  margin: 0.5rem 0;
  font-size: 1.1rem;
}
.about-history {
  margin: 3rem 0;
}
.timeline {
  border-left: 3px solid #3949ab;
  padding-left: 1.5rem;
}
.timeline-item {
  margin-bottom: 1.5rem;
  position: relative;
}
.timeline-item .year {
  font-weight: bold;
  color: #1a237e;
  margin-right: 0.5rem;
}
</style>
