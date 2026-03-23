# Smart-Snort 🛡️

### ⚠️ Project Status: In Development
This project is currently in the active development phase as part of our final year B.Tech CSAI program. Architecture and tech stack are subject to change.

---

## 🎯 Project Overview
Smart-Snort is an AI-enhanced Network Intrusion Detection System (NIDS). Our goal is to sit on top of standard Snort/Suricata installations to:
1. **Reduce Noise**: Use Machine Learning to filter out known false positives.
2. **Explain Threats**: Use Large Language Models (LLM) to translate complex hex/binary logs into plain English summaries.
3. **Speed up Triage**: Provide a dashboard for SOC analysts to see high-priority threats immediately.

---

## 🏗️ Proposed Tech Stack (Subject to Change)
- **Backend:** Python (FastAPI / Flask)
- **AI/ML:** Scikit-learn / TensorFlow, Meta Llama 3.2 1B (Local)
- **Frontend:** HTML / Tailwind CSS
- **Traffic Analysis:** Snort / Suricata
- **Database/Logging:** Splunk or ELK Stack

---

## 👥 The Team & Roles
- **Hemant Sharma (@hemantsharma-cell)**: Project Lead & Backend Integration.
- **Anshu (@itskr-Anshu)**: Machine Learning Model Development.
- **Husain (@zk3344804-lgtm)**: Frontend UI & Dashboard Design.
- **Vidit (@yvidit)**: Frontend Data Visualization & API Integration.

---

## 🛠️ Current Instructions for the Team
1. **Git LFS**: Ensure `git-lfs` is installed on your local machine before pushing any `.pkl` or `.h5` files.
2. **Branching**: Always create a new branch for your work (e.g., `feat-ml-model`). **Do not push directly to `main`.**
3. **Daily Sync**: Please push your progress to your respective branches daily so we can track the evolution of the code.

---

## 📂 Current Directory Structure
- `/backend`: API and logic (In Progress)
- `/ml-model`: Model training and LFS assets (In Progress)
- `/frontend`: UI components (In Progress)
