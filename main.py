from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Load and prepare data
df = pd.read_csv("shl_assessments.csv")
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Description"])

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": None})

@app.post("/recommend", response_class=HTMLResponse)
def recommend(request: Request, query: str = Form(...), top_k: int = Form(...)):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    df["score"] = similarities
    top_matches = df.sort_values(by="score", ascending=False).head(top_k)
    results = top_matches[["Assessment Name", "URL", "Duration", "Test Type", "score"]].to_dict(orient="records")
    return templates.TemplateResponse("index.html", {"request": request, "results": results, "query": query})
