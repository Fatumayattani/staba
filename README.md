# Staba – AI Health Assistant Bot  

Staba is an **AI-powered Telegram bot** built with **ElizaOS** and **Storacha decentralized storage**.  
It collects user-reported health symptoms, generates AI-driven diagnosis reports, and securely stores anonymized data for medical research.  

---

## 📌 Overview  
Staba bridges the gap between self-reported symptoms and actionable health insights.  
Through a simple Telegram chat, users can:  

- Report their symptoms  
- Receive personalized AI-generated feedback  
- Contribute anonymized data to healthcare research  

---

## 🤖 Bot Agents  
- **Symptom Collector (Telegram + ElizaOS)**: Interacts with the user in Telegram, collects symptoms, and uploads to **Storacha**.  
- **Diagnosis Generator (ElizaOS Agent)**: Fetches stored symptoms, generates a diagnosis report using LLM APIs, and delivers results back to the user.  

---

## 🚀 Key Technologies  
- **ElizaOS** – conversational AI agent framework with Telegram integration  
- **Storacha** – decentralized IPFS-backed storage for secure health data  
- **LLM APIs (Gemini / OpenAI / others)** – for generating health insights  

---

## 🧩 Architecture  

### System Overview  
```mermaid
graph TD
    User[👩 User on Telegram] -->|Reports Symptoms| Bot[🤖 Staba Bot (ElizaOS)]
    Bot -->|Uploads Data| Storacha[📦 Storacha (IPFS)]
    Storacha -->|Provides IPFS Link| DiagnosisAgent[🧠 Diagnosis Generator]
    DiagnosisAgent -->|Uses LLM API| LLM[🔮 Gemini / OpenAI API]
    LLM -->|Generates Report| DiagnosisAgent
    DiagnosisAgent -->|Stores Report| Storacha
    DiagnosisAgent -->|Sends Results| Bot
    Bot -->|Delivers Feedback| User
````

---

### Interaction Flow (Sequence Diagram)

```mermaid
sequenceDiagram
    participant U as User
    participant B as Staba Bot
    participant S as Storacha
    participant D as Diagnosis Agent
    participant L as LLM API

    U->>B: Report symptoms
    B->>S: Upload symptoms (IPFS)
    S-->>B: Return IPFS link
    B->>D: Send IPFS link
    D->>S: Fetch symptoms
    D->>L: Analyze symptoms
    L-->>D: Return diagnosis
    D->>S: Store diagnosis report
    D-->>B: Send diagnosis summary
    B-->>U: Deliver feedback
```

---

## 💡 Features

* **Conversational Symptom Collection** – users simply chat with the bot
* **AI Diagnosis Reports** – personalized insights generated instantly
* **Decentralized Storage** – files stored securely on Storacha (IPFS)
* **Privacy First** – anonymized before research use
* **Extensible** – additional agents (nutrition, lifestyle, treatment suggester) can be added

---

## 🧑‍⚕️ Use Cases

* Personal health self-checks
* Virtual health assistants in clinics
* Telehealth platforms
* Research into aggregated, anonymized health patterns

---

## 💸 Business Model

* **Freemium**: Free for individuals, premium for advanced features (PDF reports, history tracking).
* **B2B Licensing**: Clinics & startups can integrate the diagnosis agent or license anonymized datasets.

---

## 💬 Sample Bot Interaction

Here’s an example of how a user interacts with **Staba** on Telegram:

```
👩 User: Hi Staba, I’ve been having headaches and fatigue for 3 days.  

🤖 Staba: Thanks for sharing. Do you also have any of these symptoms: fever, cough, or nausea?  

👩 User: Mild fever and body aches.  

🤖 Staba: Got it. Please wait while I analyze your symptoms...  

📦 [Symptoms securely uploaded to Storacha]  

🤖 Staba: Based on your reported symptoms, here are some possible causes:  
- Viral infection (such as flu)  
- Dehydration or sleep-related issues  

⚠️ This is **not a medical diagnosis**. Please consult a healthcare professional for confirmation.  

Would you like me to save this anonymously for medical research?  

👩 User: Yes.  

🤖 Staba: ✅ Your report has been securely stored (IPFS hash: `bafy...xyz`).  
Thank you for contributing to better healthcare research!  
```

---

## ⚙️ Setup & Running the Bot

### 1. Clone & Install Dependencies

```bash
git clone https://github.com/yourusername/staba.git
cd staba
poetry install
```

### 2. Install Storacha CLI

```bash
npm install -g @web3-storage/w3cli
w3 login
```

### 3. Configure Environment

Create a `.env` file:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the Bot

```bash
poetry run python bot.py
```

Your Telegram bot should now be live 🎉

---

## ❗ Troubleshooting

| Issue             | Fix                                            |
| ----------------- | ---------------------------------------------- |
| Bot not replying  | Check if `TELEGRAM_BOT_TOKEN` is valid         |
| IPFS upload fails | Ensure Storacha CLI (`w3`) is logged in        |
| No diagnosis      | Verify LLM API key (Gemini/OpenAI/etc.) is set |

---

## 📣 Collaboration

This project was built for the **Hot AI Integrations, Hotter Storage Hackathon**.
Contributions, ideas, and collaborations are always welcome!

📧 **[fyattani@gmail.com](mailto:fyattani@gmail.com)**
🐦 **@fatumayattani**

---


