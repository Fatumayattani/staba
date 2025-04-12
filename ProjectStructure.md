## 🗂️ Project Structure

```
staba/
├── streamlit_frontend/
│   ├── app.py
│   ├── components/
│   │   └── diagnosis_display.py
│   ├── utils/
│   │   └── cid_fetcher.py
│   └── symptoms_input_form.py
│
├── agents/
│   ├── symptom_collector/
│   │   ├── main.py
│   │   ├── uploader.py
│   │   └── agent_config.json
│   │
│   └── diagnosis_generator/
│       ├── main.py
│       ├── gemini_interface.py
│       └── agent_config.json
│
├── storage/
│   ├── storacha_interface.py
│   └── ipfs_helpers.py
│
├── data/
│   ├── symptoms.json
│   └── diagnosis_output.json
│
├── cli/
│   └── run_pipeline.py
│
├── tests/
│   ├── test_symptom_collector.py
│   ├── test_diagnosis_generator.py
│   └── test_storage.py
│
├── .env
├── requirements.txt
├── README.md
└── Architecture.md
├── ProjectStructure.md
└── StorachaIntegration.md
```

---

### 🧠 Breakdown of What's What

#### `streamlit_frontend/`
This is where the user interface lives. Built with Streamlit, of course.

- `app.py`: The main entry point of the frontend.
- `components/`: Holds reusable UI components like the diagnosis display.
- `utils/`: Helper functions (like fetching CID data from Storacha).
- `symptoms_input_form.py`: The form where users enter symptoms.

#### `agents/`
Contains both uAgents — the engine room of the project.

- `symptom_collector/`: Handles user input and pushes it to Storacha.
- `diagnosis_generator/`: Pulls from Storacha, sends data to Gemini, and returns results.

Each agent folder has:
- `main.py`: Core agent logic.
- Helper files like `uploader.py` and `gemini_interface.py`.
- `agent_config.json`: Configs for each agent.

#### `storage/`
Handles all interactions with Storacha/IPFS.

- `storacha_interface.py`: Abstraction over Storacha APIs.
- `ipfs_helpers.py`: Utility functions for CID, file handling, etc.

#### `data/`
Sample files to show the pipeline in action.

- `symptoms.json`: Sample symptom input.
- `diagnosis_output.json`: Sample diagnosis from Gemini.

#### `cli/`
If someone prefers command-line to UI, this script simulates the full process.

- `run_pipeline.py`: Manually runs both agents and the full flow.

#### `tests/`
Just keeping things in check. Unit tests for agents, storage, etc.

#### Root-Level Files

- `.env`: API keys and secrets (not to be shared, obviously).
- `requirements.txt`: Python dependencies.
- `README.md`: You're reading it.
- `architecture.md`: Mermaid diagram and a bit more technical deep-dive.

---

### 🛠 Dev Convenience (Optional)

If needed, I can include a `Makefile` or some bash scripts to make life easier during development. Something like:

```makefile
run-ui:
	python streamlit_frontend/app.py

start-agents:
	python agents/symptom_collector/main.py &
	python agents/diagnosis_generator/main.py

test:
	pytest tests/

simulate:
	python cli/run_pipeline.py
```
