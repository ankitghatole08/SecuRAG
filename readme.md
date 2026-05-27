# 🔐 SecuRAG – AI-Powered Security Governance Platform

SecuRAG is an AI-powered security governance platform that analyzes application security posture, calculates risk scores, and generates AI-based security insights using a local LLM (Ollama + Llama3).

It simulates real-world security assessment workflows with automated risk scoring and AI-generated explanations.

---

# 🚀 Features

- 📊 Application security risk scoring engine
- ⚠️ Risk level classification (Low / Medium / High / Critical)
- 🤖 AI-generated security summary using local LLM (Ollama + Llama3)
- 🌐 FastAPI backend with REST APIs
- 🗄️ PostgreSQL database integration
- 🖥️ Streamlit interactive dashboard UI
- 🔍 Real-time backend + AI status monitoring
- 🧠 Fully local AI processing (no cloud dependency)
- 📦 Clean CRUD-based architecture

---

# 🏗️ System Architecture
Streamlit UI
↓
FastAPI Backend
↓
Risk Engine + AI Engine
↓
PostgreSQL Database
↓
Ollama (Llama3 Local LLM)


---

# 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- PostgreSQL
- SQLAlchemy
- Pydantic
- Requests
- Ollama
- Llama3

---

securag-platform/
│
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── crud.py             # Business logic + AI integration
│   │   ├── models.py           # SQLAlchemy models
│   │   ├── database.py         # DB connection
│   │   ├── schemas.py          # Pydantic schemas
│   │   ├── ai_engine.py        # Ollama AI integration
│   │
│   ├── requirements.txt
│   └── .env (optional)
│
├── streamlit_app/
│   ├── app.py                  # Streamlit UI dashboard
│
├── README.md
└── venv/


---

# ⚙️ Setup Instructions

## 1. Clone Repository
git clone <YOUR_GITHUB_REPO_URL>
cd securag-platform


---

## 2. Create Virtual Environment

### Windows
python -m venv venv
venv\Scripts\activate

### Mac/Linux
python3 -m venv venv
source venv/bin/activate


---

## 3. Install Dependencies
pip install -r requirements.txt


---

# 🗄️ Database Setup (PostgreSQL)

Create a database:
securag_db

Update database connection in:
backend/app/database.py

Example:
DATABASE_URL = "postgresql://postgres:password@localhost/securag_db"


---

# 🤖 AI Setup (Ollama + Llama3)

Install Ollama:
https://ollama.com

Pull Llama3 model:

Check AI service:
curl http://localhost:11434/api/tags


---

# ▶️ Run the Project

## Start Backend (FastAPI)
cd backend
uvicorn app.main:app --reload

Backend runs at:http://127.0.0.1:8000


---

## Start Frontend (Streamlit)
cd streamlit_app
streamlit run app.py


Frontend runs at:http://localhost:8501

---
---

# 📸 Screenshots

Add your screenshots here in the `screenshots/` folder.

## 🖥️ Dashboard View
![Dashboard](Screenshots/dashboard.png)

## 🤖 AI Assesment Output
![AI Result](Screenshots/assesment_result.png)

## 📡 Backend Logs
![Backend Logs](Screenshots/backend_logs.png)

---

# 📊 Risk Scoring Logic

| Condition | Score |
|----------|------|
| Internet exposed | +25 |
| Sensitive data | +30 |
| Password-only authentication | +20 |
| Encryption disabled | +25 |

---

# 🚨 Risk Levels

| Score Range | Risk Level |
|------------|------------|
| 70+ | Critical |
| 50–69 | High |
| 30–49 | Medium |
| <30 | Low |

---

# 🤖 AI Behavior

The AI (Llama3 via Ollama) generates:

- Security risk explanation
- Attack surface insights
- Simple remediation suggestions

Example output:
High risk due to internet exposure and weak authentication.
Enable MFA and encryption to reduce attack surface.

---

# 🔍 UI Features

- Submit application form
- Live risk calculation
- AI-generated security summary
- Latest application view
- Backend + AI status indicators
- Recent applications list

---

# 🧪 Example Workflow

1. User submits application details
2. FastAPI receives request
3. Risk engine calculates score
4. Ollama generates AI summary
5. Data saved in PostgreSQL
6. Streamlit UI displays results

---

# 🔮 Future Improvements

- RAG-based security knowledge base
- PDF security reports export
- Docker containerization
- Cloud deployment (AWS / Azure)
- Authentication system
- CVE vulnerability integration
- Advanced analytics dashboard
- Multi-agent AI workflow

---
