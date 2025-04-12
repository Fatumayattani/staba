# 🧠 Staba Architecture

## 📐 Overview

This architecture outlines the flow of data and agent interactions within the Staba system. It visually represents how the system processes user-reported symptoms and generates a diagnosis using autonomous agents, IPFS storage, and the Gemini API.

---

## 🔄 Flowchart Diagram (Mermaid)

```mermaid
flowchart TD
    %% Styling
    classDef pink fill:#fff0f5,color:#ff69b4,stroke:#ff69b4

    %% Nodes
    A["User inputs symptoms<br/>(via Streamlit frontend)"]:::pink
    B["Symptom Collector Agent<br/>(uAgents)"]:::pink
    C["Upload symptoms.json<br/>to Storacha (IPFS)"]:::pink
    D["Diagnosis Generator Agent<br/>(uAgents)"]:::pink
    E["Gemini API generates<br/>diagnosis"]:::pink
    F["Upload diagnosis_output.json<br/>to Storacha"]:::pink
    G["Streamlit frontend<br/>fetches and displays diagnosis"]:::pink

    %% Flow
    A --> B --> C --> D --> E --> F --> G
```

---

## 🧩 Component Breakdown

### 🧍 Streamlit Frontend
- Accepts user input (symptoms).
- Displays AI-generated diagnosis report.

### 🤖 Symptom Collector Agent (uAgents)
- Collects user symptoms.
- Uploads structured data (`symptoms.json`) to Storacha (IPFS).

### 📦 Storacha (IPFS)
- Decentralized file storage.
- Enables data access between agents.

### 🤖 Diagnosis Generator Agent (uAgents)
- Retrieves symptom data from Storacha.
- Calls Gemini API to generate diagnosis.
- Stores `diagnosis_output.json` back to Storacha.

### 🔮 Gemini API
- Large Language Model API (by Google).
- Processes input data and produces possible diagnoses and recommendations.

---

## ⚙️ Future Expansion

This architecture is modular and extensible:
- More agents can be added (e.g., nutrition analysis, lifestyle recommender).
- Diagnosis accuracy can improve with localized LLM tuning.
- New frontend interfaces can connect to the same agent pipeline.

---

