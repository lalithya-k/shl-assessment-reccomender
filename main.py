
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Load the dataset
df = pd.read_csv("shl_assessments.csv")

# Create TF-IDF matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Description"])

class RecommendRequest(BaseModel):
    query: str
    top_k: int = 5

@app.post("/recommend")
def recommend(req: RecommendRequest):
    query_vec = vectorizer.transform([req.query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    df["score"] = similarities
    top_matches = df.sort_values(by="score", ascending=False).head(req.top_k)

    results = top_matches[[
        "Assessment Name", "URL", "Remote Testing Support",
        "Adaptive/IRT Support", "Duration", "Test Type", "score"
    ]].to_dict(orient="records")

    return results
