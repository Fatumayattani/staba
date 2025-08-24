# 🩺 Staba – AI Symptom & Diagnosis Bot

[![Made with ElizaOS](https://img.shields.io/badge/Made%20with-ElizaOS-blueviolet?style=for-the-badge&logo=protocols)](https://github.com/elizaos/eliza)
[![Powered by Storacha](https://img.shields.io/badge/Powered%20by-Storacha-orange?style=for-the-badge&logo=ipfs)](https://storacha.network)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram)](https://t.me/)
[![LLM Powered](https://img.shields.io/badge/LLM-OpenAI%2FGemini-green?style=for-the-badge&logo=OpenAI)](https://openai.com)

---

## 📌 Overview

**Staba** is an intelligent AI-powered Telegram bot that helps users **report symptoms** and receive **preliminary diagnostic insights**.  
It integrates with **ElizaOS** for conversational flow and **Storacha** for secure, decentralized storage of anonymized medical data.

> ⚠️ **Disclaimer**: Staba is for **educational and research purposes only**.  
> It is **not a substitute for professional medical advice**. Always consult a qualified healthcare provider.

---

## ✨ Features

- 🤖 **Telegram Bot** interface for easy symptom reporting  
- 🧠 **Diagnosis Agent** powered by LLMs (OpenAI / Gemini via OpenRouter)  
- 🔐 **Decentralized Storage** with **Storacha** (built on IPFS/Filecoin)  
- 📊 **Anonymized Data Storage** for research & analytics  
- 🛠️ **Built with ElizaOS** for modular multi-agent orchestration  

---

## 🗂️ Architecture

### 📊 System Overview
```mermaid
graph TD
    User[👩 User on Telegram] -->|Reports Symptoms| Bot[🤖 Staba Bot (ElizaOS)]
    Bot -->|Sends Symptoms| DiagnosisAgent[🧠 Diagnosis Generator]
    DiagnosisAgent -->|Uses LLM API| LLM[🔮 Gemini / OpenAI API]
    LLM -->|Returns Insights| DiagnosisAgent
    DiagnosisAgent -->|Sends Report| Bot
    Bot -->|Delivers Feedback| User
    Bot -->|Stores Data (symptoms + diagnosis)| Storacha[📦 Storacha]
````

### 📊 Interaction Flow

```mermaid
sequenceDiagram
    participant U as User
    participant B as Staba Bot
    participant D as Diagnosis Agent
    participant L as LLM API
    participant S as Storacha

    U->>B: Report symptoms
    B->>D: Forward symptoms
    D->>L: Analyze with LLM
    L-->>D: Return diagnosis
    D-->>B: Send diagnosis summary
    B-->>U: Deliver feedback
    B->>S: Store symptoms + diagnosis (anonymized)
```

---

## 💬 Example Bot Interaction

Here’s how Staba feels in action:

```
👩 User: I have a sore throat, mild fever, and fatigue.

🤖 Staba: Thanks for sharing. Based on your symptoms, here are some possible conditions:
- Viral pharyngitis
- Seasonal flu
- Mild bacterial infection

⚠️ Recommendation: Stay hydrated, rest, and monitor your fever. If symptoms worsen, consult a doctor.

📦 (Data stored securely on Storacha for anonymized research)
```

---

## ⚡ Prerequisites

* [Node.js](https://nodejs.org/) v22 or higher
* [pnpm](https://pnpm.io/) package manager
* [Git](https://git-scm.com/)
* [Telegram account](https://t.me/) (for bot creation)
* [OpenRouter API key](https://openrouter.ai/)
* [Storacha account](https://storacha.network) and `w3cli` tools

---

## 🚀 Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/Fatumayattani/staba
cd staba
```

### 2. Install Dependencies

```bash
pnpm install
```

### 3. Set Up Storacha Integration

a. Install w3cli tool:

```bash
npm install -g @web3-storage/w3cli
```

b. Generate a DID (Decentralized Identifier):

```bash
w3 key create
```

Save both the **private key** (`Mg...`) and **public key** (`did:key:`).

c. Create a Space:

```bash
w3 space create [YOUR_SPACE_NAME]
```

Save the **space DID**.

d. Create Delegation:

```bash
w3 delegation create -c space/blob/add -c space/index/add -c filecoin/offer -c upload/add <YOUR_AGENT_DID> --base64
```

Save the delegation output for your `.env`.
---

### 4. Set Up Telegram Bot

1. Open [@BotFather](https://t.me/BotFather) on Telegram
2. Create a new bot with `/newbot`
3. Save the bot token

---

### 5. Configure Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

Fill in:

```env
# Required API Keys
OPENROUTER_API_KEY="your-openrouter-api-key"
TELEGRAM_BOT_TOKEN="your-telegram-bot-token"

# Storacha Configuration
STORACHA__AGENT_PRIVATE_KEY="your-private-key"
STORACHA__AGENT_DELEGATION="your-delegation"

# WebSocket Configuration (if integrating with other agents)
WS_URL="ws://localhost:8765"
```

---

### 6. Start the Bot

```bash
pnpm start
```

For custom character configs:

```bash
pnpm start --characters="path/to/your/character.json"
```

---

## 🔗 Integration

Staba can be extended into a **multi-agent system** with:

* **Other ElizaOS agents** (doctors, pharmacies, etc.)
* **Storacha-powered research pipelines**

---

## 📜 License

MIT License © 2025 Fatumayattani

---

## 🤝 Contributing

Pull requests are welcome!
If you’d like to contribute new features (new agents, analytics, or storage flows), open an issue first to discuss.

---

## 🙏 Inspiration

This project was inspired by [Tripmate-Planner](https://github.com/Dhruv-Varshney-developer/Tripmate-Planner) by **Dhruv Varshney**, which demonstrated how to build a modular AI agent system with ElizaOS.

```


