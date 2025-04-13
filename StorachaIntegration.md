# Storacha Integration with AI Agent Framework

This document provides a comprehensive overview of how we integrated [Storacha (Web3.Storage)](https://web3.storage/) with our AI Agent framework using the [UAgents](https://github.com/uAgents/uAgents) micro-agent protocol. The goal is to ensure reproducibility of results and decentralized storage of agent outputs.

---

## 🧠 Overview
We implemented a multi-agent system consisting of two key agents:

1. **SymptomCollectorAgent**: Collects symptoms from a user.
2. **DiagnosisGeneratorAgent**: Generates a diagnosis based on those symptoms using Gemini API.

These agents interact asynchronously and use Storacha for logging and reproducible storage of collected symptoms and generated diagnoses.

---

## 🧩 Architecture Recap
Each agent has its own unique address, handles specific responsibilities, and communicates using structured messages.

---

## 📦 Storacha Integration

### Why Storacha?
We chose Storacha to:
- Store agent outputs (symptoms, diagnoses) immutably.
- Make the data shareable and publicly reproducible.
- Support decentralized data flows aligned with Web3.

---

## 🔧 Setup Instructions

### 1. Install CLI Tool
Ensure you have Node.js 18+ and npm 7+:

```bash
node --version && npm --version
```

Install the Storacha CLI:

```bash
npm install -g @web3-storage/w3cli
```

Verify:

```bash
w3 --help
```

---

### 2. Create Spaces for Each Agent

Each agent gets its own "space" (namespace) to manage uploads.

#### SymptomCollectorAgent
```bash
w3 space create CollectorSpace
```

#### DiagnosisGeneratorAgent
```bash
w3 space create DiagnosisSpace
```

To list all spaces:
```bash
w3 space ls
```

Switch between them:
```bash
w3 space use CollectorSpace
```

---

### 3. Upload Files
After agent tasks complete:

#### For SymptomCollectorAgent:
```bash
w3 space use CollectorSpace
w3 up symptoms.json
```

#### For DiagnosisGeneratorAgent:
```bash
w3 space use DiagnosisSpace
w3 up diagnosis_output.json
```

This uploads the files to IPFS and provides a link like:
```
https://w3s.link/ipfs/bafy.../symptoms.json
```

---

## 🛠 Automating CLI Uploads (Optional)
In Python, we can shell out to automate uploads:

```python
import subprocess

def upload_to_space(space, file):
    subprocess.run(["w3", "space", "use", space])
    subprocess.run(["w3", "up", file])

# Example
upload_to_space("CollectorSpace", "symptoms.json")
```

---

## ✅ Benefits for Reproducibility
- Agent results are persistently stored
- Easy to share diagnosis outputs via IPFS
- Ensures the same results can be validated and used again later

---

## 📎 Final Notes
Make sure both agents are run locally before uploading results. Use their assigned spaces consistently for clean, traceable datasets.

> With this setup, anyone replicating the agent flow will have access to the exact data the agents generated — backed by the power of decentralized storage.

