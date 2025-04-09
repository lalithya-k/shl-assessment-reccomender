from flask import Flask, request, render_template, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load data
df = pd.read_csv("shl_assessments.csv")
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Description"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    query = data.get("query", "")
    top_k = int(data.get("top_k", 5))
    
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    df["score"] = similarities
    top_matches = df.sort_values(by="score", ascending=False).head(top_k)

    results = top_matches[[
        "Assessment Name", "URL", "Remote Testing Support",
        "Adaptive/IRT Support", "Duration", "Test Type", "score"
    ]].to_dict(orient="records")

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
