<template>
  <main class="calc-container">
    <h1>Loan Calculator</h1>

    <div class="card">
      <form class="calc-form">
        <!-- Loan type -->
        <label>Loan Type</label>
        <select v-model="loanType" :class="{ invalid: loanTypeError }">
          <option disabled value="">-- Select Loan Type --</option>
          <option v-for="(rate, type) in loanTypes" :key="type" :value="type">
            {{ type }} ({{ rate }}%)
          </option>
        </select>
        <span v-if="loanTypeError" class="error">{{ loanTypeError }}</span>

        <!-- Loan amount -->
        <label>Loan Amount</label>
        <input
          v-model.number="amount"
          type="number"
          placeholder="Enter loan amount"
          :class="{ invalid: amountError }"
        />
        <span v-if="amountError" class="error">{{ amountError }}</span>

        <!-- Duration -->
        <label>Duration (months)</label>
        <input
          v-model.number="months"
          type="number"
          placeholder="Enter number of months"
          :class="{ invalid: monthsError }"
        />
        <span v-if="monthsError" class="error">{{ monthsError }}</span>
      </form>

      <!-- Results -->
      <div v-if="showResults" class="results">
        <h2>Results</h2>
        <p><strong>Monthly Payment:(KES)</strong> {{ monthlyPayment.toFixed(2) }}</p>
        <p><strong>Total Repayment:(KES)</strong> {{ totalRepayment.toFixed(2) }}</p>
        <p><strong>Total Interest:(KES)</strong> {{ totalInterest.toFixed(2) }}</p>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, computed } from "vue"

// Loan options with interest rates
const loanTypes = {
  "Personal Loan": 10,
  "Car Loan": 7,
  "Mortgage": 5,
  "Student Loan": 3,
}

const loanType = ref("")
const amount = ref(null)
const months = ref(null)

// --- Validation ---
const loanTypeError = computed(() => {
  if (!loanType.value) return "Please select a loan type"
  return null
})

const amountError = computed(() => {
  if (amount.value === null) return null
  if (amount.value <= 0) return "Loan amount must be greater than 0"
  return null
})

const monthsError = computed(() => {
  if (months.value === null) return null
  if (months.value <= 0) return "Months must be greater than 0"
  return null
})

// --- Calculations ---
const monthlyRate = computed(() =>
  loanType.value ? loanTypes[loanType.value] / 100 / 12 : 0
)

const monthlyPayment = computed(() => {
  if (!loanType.value || !amount.value || !months.value) return null
  if (loanTypeError.value || amountError.value || monthsError.value) return null

  const r = monthlyRate.value
  const n = months.value
  const P = amount.value

  if (r === 0) return P / n

  return (P * r) / (1 - Math.pow(1 + r, -n))
})

const totalRepayment = computed(() =>
  monthlyPayment.value ? monthlyPayment.value * months.value : null
)

const totalInterest = computed(() =>
  totalRepayment.value ? totalRepayment.value - amount.value : null
)

const showResults = computed(
  () =>
    monthlyPayment.value &&
    !loanTypeError.value &&
    !amountError.value &&
    !monthsError.value
)
</script>

<style scoped>
/* Layout */
.calc-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #f8f9fa;
  padding: 2rem;
}

.card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
}

h1 {
  margin-bottom: 1.5rem;
  color: #333;
  text-align: center;
}

.calc-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

label {
  font-weight: 600;
  margin-bottom: 0.3rem;
}

input,
select {
  padding: 0.6rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
}

input:focus,
select:focus {
  outline: none;
  border-color: #42b883;
}

.invalid {
  border-color: red;
}

.error {
  color: red;
  font-size: 0.85rem;
}

.results {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid #eee;
}

.results h2 {
  margin-bottom: 1rem;
  color: #42b883;
}
</style>
