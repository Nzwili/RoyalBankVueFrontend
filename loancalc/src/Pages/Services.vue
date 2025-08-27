<template>
  <div class="services-page">
    <header class="services-header">
      <h1>Our Services</h1>
      <p>Discover the full range of financial services designed to empower you.</p>
    </header>

    <section class="services-grid">
      <div v-for="service in services" :key="service.title" class="service-card">
        <img :src="service.icon" :alt="service.title" class="service-icon" />
        <h2>{{ service.title }}</h2>
        <p>{{ service.description }}</p>
        <router-link :to="`/services/${service.id}`" class="learn-more">Learn More →</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
const services = [
  {
    id: "digital-banking",
    title: "Digital Banking",
    description: "Bank anytime, anywhere with our secure mobile and online banking.",
    icon: "https://img.icons8.com/ios/100/4a90e2/bank-building.png",
    link: "/services/digital-banking"
  },
  {
    id: "loans",
    title: "Loans",
    description: "Flexible personal, auto, and home loans tailored to your needs.",
    icon: "https://img.icons8.com/ios/100/4a90e2/money-bag.png",
    link: "/services/loans"
  },
  {
    id: "investments",
    title: "Investments",
    description: "Grow your wealth with expert-guided investment options.",
    icon: "https://img.icons8.com/ios/100/4a90e2/stocks.png",
    link: "/services/investments"
  },
  { 
    id: "global-transfers",
    title: "Global Transfers",
    description: "Send and receive money worldwide with ease and security.",
    icon: "https://img.icons8.com/ios/100/4a90e2/money-transfer.png",
    link: "/services/transfers"
  },
  {
    id: "credit-cards",
    title: "Credit Cards",
    description: "Get credit cards with cashback, travel rewards, and more.",
    icon: "https://img.icons8.com/ios/100/4a90e2/credit-card.png",
    link: "/services/credit-cards"
  },
  {
    id: " savings-accounts",
    title: "Savings Accounts",
    description: "Save smart with high interest savings and fixed deposit plans.",
    icon: "https://img.icons8.com/ios/100/4a90e2/safe.png",
    link: "/services/savings"
  }
]
</script>

<style scoped>
.services-page {
  max-width: 1200px;
  margin: auto;
  padding: 2rem;
}

.services-header {
  text-align: center;
  margin-bottom: 2rem;
}

.services-header h1 {
  font-size: 2.5rem;
  color: #1a237e;
}

.services-header p {
  color: #555;
  margin-top: 0.5rem;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5rem;
}

.service-card {
  background: #fff;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  text-align: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.service-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
}

.service-icon {
  width: 60px;
  margin-bottom: 1rem;
}

h2 {
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
  color: #1a237e;
}

p {
  font-size: 0.95rem;
  color: #666;
  margin-bottom: 1rem;
}

.learn-more {
  text-decoration: none;
  color: #1976d2;
  font-weight: bold;
  transition: color 0.2s;
}

.learn-more:hover {
  color: #0d47a1;
}
</style>
