<template>
  <div>
    <!-- Floating button -->
    <button class="chat-toggle" @click="isOpen = !isOpen">
      💬
    </button>

    <!-- Chat window -->
    <div v-if="isOpen" class="chat-window">
      <header>
        <h3>Loan Help Bot</h3>
        <button @click="isOpen = false">✖</button>
      </header>

      <div class="messages">
        <div v-for="(msg, index) in messages" :key="index" :class="msg.sender">
          <p>{{ msg.text }}</p>
        </div>
      </div>

      <div class="input-bar">
        <input v-model="userInput" @keyup.enter="sendMessage" placeholder="Ask something..." />
        <button @click="sendMessage">➤</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"

const isOpen = ref(false)
const userInput = ref("")
const messages = ref([{ sender: "bot", text: "Hi! Ask me about loans 👋" }])

// Simple FAQ knowledge base
const faqs = {
  "how is interest calculated": "We use the amortization formula with your loan type’s interest rate.",
  "what do i need": "Select a loan type, enter amount & months. We’ll calculate instantly.",
  "monthly payment": "It’s based on the formula: (P*r) / (1 - (1+r)^-n).",
}

function sendMessage() {
  if (!userInput.value.trim()) return
  const question = userInput.value.trim()
  messages.value.push({ sender: "user", text: question })

  // Check FAQ
  const key = Object.keys(faqs).find(q =>
    question.toLowerCase().includes(q)
  )
  if (key) {
    messages.value.push({ sender: "bot", text: faqs[key] })
  } else {
    messages.value.push({ sender: "bot", text: "I’m not sure 🤔, but I can help with loan basics!" })
  }

  userInput.value = ""
}
</script>

<style scoped>
.chat-toggle {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #42b883;
  color: white;
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  font-size: 24px;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

.chat-window {
  position: fixed;
  bottom: 90px;
  right: 20px;
  width: 300px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
  max-height: 400px;
}

header {
  background: #42b883;
  color: white;
  padding: 10px;
  border-radius: 12px 12px 0 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
}

.messages .user {
  text-align: right;
  color: #333;
}

.messages .bot {
  text-align: left;
  color: #42b883;
}

.input-bar {
  display: flex;
  border-top: 1px solid #eee;
}

.input-bar input {
  flex: 1;
  border: none;
  padding: 10px;
}

.input-bar button {
  background: #42b883;
  border: none;
  color: white;
  padding: 10px 15px;
  cursor: pointer;
}
</style>
