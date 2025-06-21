import requests
import os

AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")

headers = {
    'Content-Type': 'application/json',
    'api-key': AZURE_SEARCH_KEY
}

def semantic_rank_resumes(job_description: str, resume_text: str) -> float:
    payload = {
        "query": job_description,
        "documents": [resume_text],
        "semanticConfiguration": "default",
        "queryType": "semantic"
    }
    r = requests.post(f"{AZURE_SEARCH_ENDPOINT}/indexes/{AZURE_SEARCH_INDEX}/docs/search?api-version=2023-07-01-preview",
                      headers=headers, json=payload)
    results = r.json()
    return results.get("value", [{}])[0].get("@search.score", 0.0)
