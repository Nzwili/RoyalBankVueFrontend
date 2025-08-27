<template>
  <div class="support-page">
    <!-- Header -->
    <header class="support-header">
      <h1>Contact Royal Bank Support</h1>
      <p>Need help? Our team is here 24/7 to assist you.</p>
    </header>

    <!-- Contact Form -->
    <section class="support-form">
      <div class="form-card">
        <h2>Send us a Message</h2>
        <form @submit.prevent="handleSubmit">
          <div class="form-group">
            <label for="name">Full Name</label>
            <input v-model="form.name" type="text" id="name" placeholder="Enter your full name" required />
          </div>

          <div class="form-group">
            <label for="email">Email</label>
            <input v-model="form.email" type="email" id="email" placeholder="Enter your email" required />
          </div>

          <div class="form-group">
            <label for="subject">Subject</label>
            <input v-model="form.subject" type="text" id="subject" placeholder="Subject" required />
          </div>

          <div class="form-group">
            <label for="message">Message</label>
            <textarea v-model="form.message" id="message" rows="5" placeholder="Write your message here..." required></textarea>
          </div>

          <button type="submit" class="btn-submit">Send Message</button>
        </form>

        <!-- Success message -->
        <p v-if="successMessage" class="success">{{ successMessage }}</p>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq">
      <h2>Frequently Asked Questions</h2>
      <ul>
        <li>
          <strong>How can I reset my password?</strong><br />
          You can reset your password from the login page by clicking "Forgot Password".
        </li>
        <li>
          <strong>Where can I view my loan details?</strong><br />
          After logging in, navigate to "My Loans" under your account dashboard.
        </li>
        <li>
          <strong>How do I contact customer care directly?</strong><br />
          Call our 24/7 hotline at <b>+254 700 123 456</b>.
        </li>
      </ul>
    </section>

    <!-- Map Section -->
    <section class="map">
      <h2>Our Headquarters</h2>
      <iframe
        class="map-frame"
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1994.8223830429282!2d36.82194631577211!3d-1.2920659990480303!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x182f10e7a1e76f15%3A0x9f8a87d431f9c!2sNairobi!5e0!3m2!1sen!2ske!4v1700000000000"
        width="100%"
        height="300"
        style="border:0;"
        allowfullscreen=""
        loading="lazy">
      </iframe>
    </section>
  </div>
</template>

<script setup>
import { ref } from "vue"

const form = ref({
  name: "",
  email: "",
  subject: "",
  message: "",
})

const successMessage = ref("")

function handleSubmit() {
  // Simple validation
  if (!form.value.name || !form.value.email || !form.value.subject || !form.value.message) {
    successMessage.value = "⚠️ Please fill out all fields."
    return
  }

  // Save to localStorage
  let storedMessages = JSON.parse(localStorage.getItem("supportMessages")) || []
  storedMessages.push({ ...form.value, date: new Date().toISOString() })
  localStorage.setItem("supportMessages", JSON.stringify(storedMessages))

  // Show success
  successMessage.value = "✅ Your message has been sent! We'll get back to you shortly."

  // Reset form
  form.value = { name: "", email: "", subject: "", message: "" }
}
</script>

<style scoped>
.support-page {
  padding: 2rem;
  max-width: 1000px;
  margin: auto;
}

.support-header {
  text-align: center;
  margin-bottom: 2rem;
}

.form-card {
  background: #fff;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 1rem;
}

label {
  font-weight: 600;
  display: block;
  margin-bottom: 0.5rem;
}

input, textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  outline: none;
}

input:focus, textarea:focus {
  border-color: #007bff;
}

.btn-submit {
  background: #007bff;
  color: white;
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  width: 100%;
  transition: background 0.3s;
}

.btn-submit:hover {
  background: #0056b3;
}

.success {
  margin-top: 1rem;
  color: green;
  font-weight: bold;
}

.faq {
  margin-top: 3rem;
}

.faq h2 {
  margin-bottom: 1rem;
}

.faq ul {
  list-style: none;
  padding: 0;
}

.faq li {
  background: #f9f9f9;
  margin-bottom: 1rem;
  padding: 1rem;
  border-radius: 8px;
}

.map {
  margin-top: 3rem;
}

.map-frame {
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
</style>
