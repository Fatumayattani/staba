# 📦 StorachaIntegration.md

## 🎯 Objective
This document provides a detailed guide for integrating **Storacha**, a decentralized storage solution built on IPFS, with an AI agent framework (in this case, **Fetch.ai's uAgents**). The integration enables the storage and retrieval of data (e.g., health symptoms and AI-generated diagnoses) in a way that ensures security, decentralization, and reproducibility.

---

## 🔧 Prerequisites

- Python 3.8+
- [uAgents framework](https://github.com/fetchai/uAgents)
- Storacha Python SDK
- IPFS daemon (optional if using remote gateway)
- Environment variables or config file for API keys and CIDs

---

## 🧠 Use Case Context
In our project **Staba**, Storacha is used to:

- Store user-reported symptoms as `symptoms.json`
- Store AI-generated diagnosis reports as `diagnosis_output.json`
- Enable both storage and retrieval by different autonomous agents in the pipeline

---

## 🧱 Integration Steps

### 1. Install Storacha SDK

```bash
pip install storacha
```

### 2. Initialize Storacha Client

Create a `storacha_config.py` to handle the connection:

```python
from storacha import StorachaClient

storacha = StorachaClient(api_key="YOUR_STORACHA_API_KEY")
```

### 3. Uploading a File to Storacha

Used by **Symptom Collector Agent**:

```python
import json
from storacha_config import storacha

symptom_data = {
    "user_id": "anon-123",
    "symptoms": "persistent cough, fatigue, shortness of breath"
}

with open("symptoms.json", "w") as f:
    json.dump(symptom_data, f)

cid = storacha.upload("symptoms.json")
print(f"Uploaded to Storacha with CID: {cid}")
```

### 4. Downloading a File from Storacha

Used by **Diagnosis Generator Agent**:

```python
from storacha_config import storacha

cid = "Qm..."  # CID from previous upload
file_path = storacha.download(cid, output_file="symptoms.json")

print(f"Downloaded file saved to: {file_path}")
```

---

## 🔁 Agent Interaction Workflow with Storacha

1. **Symptom Collector Agent**
   - Receives user input via Streamlit.
   - Saves symptoms as JSON.
   - Uploads file to Storacha → receives CID.

2. **Diagnosis Generator Agent**
   - Reads CID.
   - Downloads file via Storacha.
   - Uses Gemini API to generate a diagnosis.
   - Uploads diagnosis JSON to Storacha → generates new CID.

3. **Frontend**
   - Fetches diagnosis CID.
   - Downloads and displays results to user.

---

## 🔐 Security & Privacy

- Store only anonymized data.
- Use encryption before uploading if necessary.
- Always validate and sanitize data post-download.

---

## ♻️ Reproducibility Tips

- Store each CID in a log file or metadata DB.
- Include timestamps and agent metadata in every JSON.
- Ensure consistent file naming conventions (`symptoms_<uid>.json`, `diagnosis_<uid>.json`).

---

## 📚 References

- [Storacha Docs](https://docs.storacha.network)
- [Fetch.ai uAgents](https://github.com/fetchai/uAgents)
- [Google Gemini API](https://ai.google.dev/gemini-api/docs)

---


