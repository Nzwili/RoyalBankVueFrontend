<template>
  <div class="loan-calculator">
    <h1>Loan Calculator</h1>

    <!-- Input Card -->
    <div class="calculator-card">
      <div class="form-group">
        <label>Loan Type</label>
        <select v-model="selectedLoan">
          <option disabled value="">-- Select Loan Type --</option>
          <option v-for="loan in loanTypes" :key="loan.type" :value="loan">
            {{ loan.type }} ({{ loan.rate }}% APR)
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>Loan Amount</label>
        <input type="number" v-model.number="amount" placeholder="Enter amount" />
      </div>

      <div class="form-group">
        <label>Repayment Months</label>
        <input type="number" v-model.number="months" placeholder="e.g. 24" />
      </div>
    </div>

    <!-- Results + Charts -->
    <div v-if="isValid" class="results-and-charts">
      <div class="results-card">
        <h2>Results</h2>
        <p><strong>Monthly Payment:</strong> (KES){{ monthlyPayment.toFixed(2) }}</p>
        <p><strong>Total Repayment:</strong> (KES){{ totalRepayment.toFixed(2) }}</p>
        <p><strong>Total Interest:</strong> (KES){{ totalInterest.toFixed(2) }}</p>
      </div>

      <div class="charts-area">
        <div class="chart-card small">
          <h3>Principal vs Interest</h3>
          <canvas ref="chartBreakdown"></canvas>
        </div>

        <div class="chart-card large">
          <h3>Monthly Repayments (stacked)</h3>
          <canvas ref="chartMonthly"></canvas>
        </div>
      </div>
    </div>

    <!-- helpful note for huge month counts -->
    <p v-if="isValid && months > 240" class="note">
      Note: very large month counts may create many bars and affect performance.
    </p>
  </div>
</template>

<script setup>
import { ref, computed, watch, nextTick } from "vue";
import Chart from "chart.js/auto"; // make sure `npm i chart.js` was run

// Inputs
const amount = ref(null);
const months = ref(null);
const selectedLoan = ref("");

// Loan types (you can change rates)
const loanTypes = [
  { type: "Personal Loan", rate: 10 },
  { type: "Car Loan", rate: 8 },
  { type: "Home Loan", rate: 6 },
  { type: "Business Loan", rate: 12 }
];

// derived state
const monthlyRate = computed(() =>
  selectedLoan.value && typeof selectedLoan.value.rate === "number"
    ? selectedLoan.value.rate / 100 / 12
    : 0
);

// handle zero-rate (r===0) case
const monthlyPayment = computed(() => {
  const P = Number(amount.value) || 0;
  const n = Number(months.value) || 0;
  const r = monthlyRate.value;
  if (!P || !n) return 0;
  if (r === 0) return P / n;
  return (P * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
});

const totalRepayment = computed(() => monthlyPayment.value * (Number(months.value) || 0));
const totalInterest = computed(() => totalRepayment.value - (Number(amount.value) || 0));
const isValid = computed(() => selectedLoan.value && amount.value > 0 && months.value > 0);

// chart refs + instances
const chartBreakdown = ref(null);
const chartMonthly = ref(null);
let chartBreakdownInstance = null;
let chartMonthlyInstance = null;

// amortization schedule generator
function generateAmortizationSchedule(P, r, n, monthlyPaymentVal) {
  const schedule = [];
  let balance = P;
  for (let i = 0; i < n; i++) {
    const interest = balance * r;
    // guard negative due to rounding on last step:
    let principal = monthlyPaymentVal - interest;
    // if we're at the last payment, make principal = remaining balance (avoid tiny negative)
    if (i === n - 1) principal = balance;
    // ensure neither is NaN
    schedule.push({
      interest: Math.max(0, interest),
      principal: Math.max(0, principal)
    });
    balance -= principal;
    if (balance < 0.0001) balance = 0;
  }
  return schedule;
}

// render/update charts
async function renderCharts() {
  if (!isValid.value) return;

  await nextTick(); // ensure canvas elements exist

  // --- Principal vs Interest (compact bar) ---
  try {
    if (!chartBreakdown.value || !chartMonthly.value) return;

    if (chartBreakdownInstance) {
      chartBreakdownInstance.destroy();
      chartBreakdownInstance = null;
    }

    const ctx1 = chartBreakdown.value.getContext("2d");
    chartBreakdownInstance = new Chart(ctx1, {
      type: "bar",
      data: {
        labels: ["Principal", "Interest"],
        datasets: [{
          data: [Number(amount.value), Number(totalInterest.value)],
          backgroundColor: ["#4CAF50", "#FF5722"],
          borderRadius: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: { y: { beginAtZero: true, title: { display: false } } }
      }
    });
  } catch (err) {
    console.error("Chart (breakdown) error:", err);
  }

  // --- Monthly stacked amortization chart ---
  try {
    if (chartMonthlyInstance) {
      chartMonthlyInstance.destroy();
      chartMonthlyInstance = null;
    }

    const ctx2 = chartMonthly.value.getContext("2d");

    const P = Number(amount.value);
    const n = Number(months.value);
    const r = monthlyRate.value;
    const monthlyPaymentVal = Number(monthlyPayment.value);

    // generate schedule (principal + interest portion for each month)
    const schedule = generateAmortizationSchedule(P, r, n, monthlyPaymentVal);
    const labels = schedule.map((_, i) => `M${i + 1}`);
    const interestData = schedule.map((s) => Number(s.interest.toFixed(2)));
    const principalData = schedule.map((s) => Number(s.principal.toFixed(2)));

    chartMonthlyInstance = new Chart(ctx2, {
      type: "bar",
      data: {
        labels,
        datasets: [
          { label: "Interest", data: interestData, backgroundColor: "#FF5722", stack: "stack1" },
          { label: "Principal", data: principalData, backgroundColor: "#4CAF50", stack: "stack1" }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { position: "bottom" } },
        scales: {
          x: { stacked: true, ticks: { maxRotation: 0, autoSkip: true, maxTicksLimit: 12 } },
          y: { stacked: true, beginAtZero: true, title: { display: true, text: "Amount (KES)" } }
        }
      }
    });
  } catch (err) {
    console.error("Chart (monthly) error:", err);
  }
}

// watch input changes and update charts (debounce not strictly needed)
watch([amount, months, selectedLoan], () => {
  if (isValid.value) renderCharts();
});
</script>

<style scoped>
.loan-calculator {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
}

/* input card */
.calculator-card {
  background: white;
  padding: 1.25rem;
  width: 420px;
  max-width: 95%;
  border-radius: 10px;
  box-shadow: 0 6px 18px rgba(12, 17, 20, 0.06);
  margin-bottom: 1.25rem;
}

.form-group { margin-bottom: 1rem; }
label { font-weight: 600; display: block; margin-bottom: .35rem; }
input, select {
  width: 100%;
  padding: .55rem;
  border-radius: 6px;
  border: 1px solid #ddd;
  font-size: .95rem;
}

/* layout for results + charts */
.results-and-charts {
  width: 100%;
  max-width: 1000px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* results */
.results-card {
  background: white;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 6px 18px rgba(12, 17, 20, 0.04);
}

/* charts area */
.charts-area {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: space-between;
}

/* chart cards smaller */
.chart-card {
  background: white;
  padding: 0.8rem;
  border-radius: 10px;
  box-shadow: 0 6px 18px rgba(12, 17, 20, 0.04);
  display: flex;
  flex-direction: column;
  gap: .5rem;
}

/* small vs large sizing */
.chart-card.small { width: 320px; height: 220px; }
.chart-card.large { flex: 1 1 620px; min-width: 320px; height: 220px; }

/* ensure canvas fills card */
.chart-card canvas { width: 100% !important; height: 100% !important; display: block; }

/* note */
.note { margin-top: .8rem; color: #666; font-size: .9rem; text-align: center; }
</style>
