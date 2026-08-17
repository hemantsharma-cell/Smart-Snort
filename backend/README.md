# Smart-Snort: AI Cybersecurity Backend (v1.0)

This is the backend microservice for the Smart-Snort AI Cybersecurity system. This module is responsible for real-time monitoring of Snort Intrusion Detection System (IDS) fast-logs, parsing the outputs, enriching them with external Threat Intelligence feeds, and utilizing a local Large Language Model to auto-generate security analyses.

## 🏗️ Architecture Stack
* **Framework:** FastAPI (Python)
* **Real-time Engine:** Watchdog & WebSockets
* **Database:** SQLite & SQLAlchemy ORM
* **Local ML/AI:** Ollama (Llama 3.2 3B Parameters)
* **Remote Threat Intel:** AbuseIPDB & VirusTotal APIs

## 🚀 Setup Instructions

### 1. Environment Setup
Create a virtual environment to isolate the dependencies:
```bash
python -m venv venv

# On Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# On macOS and Linux (Bash/Zsh)
source venv/bin/activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Configure Threat Intelligence (`.env`)
You must configure the external API keys. Create a `.env` file in this directory with the following structure:
```env
ABUSEIPDB_API_KEY=your_abuseipdb_key_here
VIRUSTOTAL_API_KEY=your_virustotal_key_here
```

### 3. Local AI Setup
This backend uses locally-hosted LLMs to maintain total data privacy. 
1. Install [Ollama](https://ollama.com/).
2. Run `ollama pull llama3.2` to download the specific model into your local system constraint.

## 🔧 Running the Backend

The backend utilizes an asynchronous two-pronged architecture. You must run both the API server and the Watchdog listener simultaneously.

**Terminal 1 (The Server):**
Start the FastAPI server. This handles the REST APIs, Database ingestion, WebSockets, and AI prompting.
```powershell
uvicorn main:app --reload
```
*Access the Swagger UI documentation at `http://127.0.0.1:8000/docs`*

**Terminal 2 (The Ingestion Engine):**
Start the Watchdog listener. This continuously monitors `mock_snort.log` for changes and pipes the data into the server.
```powershell
python file_watcher.py
```

## 📡 API Endpoints
- `GET /alerts/`: Fetch all historical parsed alerts.
- `POST /alerts/`: Internal ingestion pipeline triggered by the file watcher.
- `WS /ws`: Open a persistent WebSocket tunnel for real-time UI streaming.
