# AI Resume Ranker — Microsoft-Enhanced 🧠📄

An AI-powered tool to rank resumes against job descriptions using Microsoft Azure AI tools:
- ✅ GPT-4 via Azure OpenAI Service for resume optimization
- ✅ Azure Cognitive Search for semantic scoring
- ✅ FastAPI backend with PDF parsing

## 🔧 Setup
```bash
git clone https://github.com/suryanshsugara/Microsoft-AI/tree/main/Resume-Ranker
cd resume-ranker-microsoft-enhanced
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# add your Azure keys in .env
uvicorn main:app --reload
```

## 🧪 Features
- Upload PDF resumes and a job description
- Automatically rewrite resume bullets
- Get semantic score of fit using Azure Cognitive Search

## 💼 Microsoft Tech Used
- Azure OpenAI GPT-4
- Azure Cognitive Search
- Azure Blob (optional for large scale resume ingestion)

## 📬 Contact
Built with ❤️ by [Suryansh Sugara](https://github.com/suryanshsugara).
