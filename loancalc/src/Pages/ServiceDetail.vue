<template>
  <div class="service-detail">
    <header class="detail-header">
      <h1>{{ service.title }}</h1>
      <p>{{ service.tagline }}</p>
    </header>

    <section class="detail-body">
      <img :src="service.icon" :alt="service.title" class="detail-icon" />

      <p class="detail-description">{{ service.description }}</p>

      <ul class="detail-benefits">
        <li v-for="(benefit, index) in service.benefits" :key="index">
          ✅ {{ benefit }}
        </li>
      </ul>

      <div class="detail-nav">
        <router-link
          v-if="prevService"
          :to="`/services/${prevService.id}`"
          class="nav-btn"
        >
          ← {{ prevService.title }}
        </router-link>

        <router-link
          v-if="nextService"
          :to="`/services/${nextService.id}`"
          class="nav-btn"
        >
          {{ nextService.title }} →
        </router-link>
      </div>

      <router-link to="/services" class="back-btn">← Back to Services</router-link>
    </section>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()

// ✅ Service Data
const services = [
  {
    id: "digital-banking",
    title: "Digital Banking",
    tagline: "Your bank in your pocket, 24/7.",
    description: "Manage accounts, transfer money, pay bills, and track spending with our secure and user-friendly mobile and online banking platforms.",
    benefits: ["Instant transfers", "Secure mobile app", "Real-time alerts", "Access anywhere"],
    icon: "https://img.icons8.com/ios/100/4a90e2/bank-building.png"
  },
  {
    id: "loans",
    title: "Loans",
    tagline: "Flexible loans tailored for you.",
    description: "From personal loans to auto and home financing, we provide customized solutions with competitive interest rates.",
    benefits: ["Low interest rates", "Flexible repayment terms", "Quick approval", "Dedicated loan officers"],
    icon: "https://img.icons8.com/ios/100/4a90e2/money-bag.png"
  },
  {
    id: "investments",
    title: "Investments",
    tagline: "Grow your wealth with us.",
    description: "Choose from a wide range of investment products backed by expert advisors to secure your financial future.",
    benefits: ["Portfolio management", "Diverse options", "Risk analysis", "Competitive returns"],
    icon: "https://img.icons8.com/ios/100/4a90e2/stocks.png"
  },
  {
    id: "transfers",
    title: "Global Transfers",
    tagline: "Send and receive money worldwide.",
    description: "Fast and secure transfers ensuring money reaches your loved ones and partners globally.",
    benefits: ["Low fees", "Instant transfers", "Secure network", "Multi-currency support"],
    icon: "https://img.icons8.com/ios/100/4a90e2/money-transfer.png"
  },
  {
    id: "credit-cards",
    title: "Credit Cards",
    tagline: "Smart spending with exclusive rewards.",
    description: "Our credit cards come with cashback, travel rewards, and premium lifestyle benefits.",
    benefits: ["Cashback & rewards", "Global acceptance", "Travel insurance", "Flexible payments"],
    icon: "https://img.icons8.com/ios/100/4a90e2/credit-card.png"
  },
  {
    id: "savings",
    title: "Savings Accounts",
    tagline: "Secure your future, grow your savings.",
    description: "Open high-interest savings accounts or fixed deposits with flexible withdrawal options.",
    benefits: ["High interest", "Easy management", "Flexible saving plans", "Safe & reliable"],
    icon: "https://img.icons8.com/ios/100/4a90e2/safe.png"
  }
]

// ✅ Current service
const currentService = computed(() =>
  services.find(s => s.id === route.params.id)
)

// ✅ Index
const currentIndex = computed(() =>
  services.findIndex(s => s.id === route.params.id)
)

// ✅ Next & Previous
const prevService = computed(() =>
  currentIndex.value > 0 ? services[currentIndex.value - 1] : null
)

const nextService = computed(() =>
  currentIndex.value < services.length - 1 ? services[currentIndex.value + 1] : null
)

const service = currentService.value || {
  title: "Service Not Found",
  tagline: "",
  description: "This service doesn’t exist.",
  benefits: [],
  icon: ""
}
</script>

<style scoped>
.service-detail {
  max-width: 900px;
  margin: auto;
  padding: 2rem;
}

.detail-header {
  text-align: center;
  margin-bottom: 2rem;
}

.detail-header h1 {
  font-size: 2.5rem;
  color: #1a237e;
}

.detail-header p {
  color: #555;
  margin-top: 0.5rem;
}

.detail-icon {
  width: 90px;
  display: block;
  margin: 1rem auto;
}

.detail-description {
  text-align: center;
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
  color: #444;
}

.detail-benefits {
  list-style: none;
  padding: 0;
  margin-bottom: 2rem;
}

.detail-benefits li {
  margin: 0.5rem 0;
}

.detail-nav {
  display: flex;
  justify-content: space-between;
  margin-bottom: 2rem;
}

.nav-btn {
  padding: 0.6rem 1.2rem;
  background: #eeeeee;
  color: #333;
  border-radius: 6px;
  text-decoration: none;
  transition: background 0.3s ease;
}

.nav-btn:hover {
  background: #d1d1d1;
}

.back-btn {
  display: block;
  text-align: center;
  padding: 0.7rem 1.2rem;
  background: #1976d2;
  color: #fff;
  border-radius: 8px;
  text-decoration: none;
}

.back-btn:hover {
  background: #0d47a1;
}
</style>
