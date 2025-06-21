from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from azure_search import semantic_rank_resumes
from resume_optimizer import optimize_resume_bullets
from utils import parse_resume_text
import shutil, os

app = FastAPI(title="AI Resume Ranker with Microsoft Integration")

UPLOAD_DIR = "./uploaded_resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_resume(file: UploadFile = File(...), job_description: str = Form(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    resume_text = parse_resume_text(file_path)
    optimized_resume = optimize_resume_bullets(resume_text)

    ranking_score = semantic_rank_resumes(job_description, optimized_resume)

    return JSONResponse({
        "filename": file.filename,
        "optimized_resume": optimized_resume,
        "score": ranking_score
    })

# resume_optimizer.py
from openai import AzureOpenAI
import os

openai_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-06-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def optimize_resume_bullets(resume_text: str) -> str:
    prompt = f"""
    Improve the following resume bullet points by making them more action-oriented,
    measurable, and tailored for professional impact:

    {resume_text}
    """
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
