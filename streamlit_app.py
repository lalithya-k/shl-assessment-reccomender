
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
st.title("🔍 SHL Assessment Recommender (TF-IDF Version)")

@st.cache_data
def load_data():
    df = pd.read_csv("shl_assessments.csv")
    return df

@st.cache_resource
def get_vectorizer_and_matrix(docs):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(docs)
    return vectorizer, matrix

df = load_data()
vectorizer, matrix = get_vectorizer_and_matrix(df["Description"])

query = st.text_area("Enter a job description or query:", height=150)

if st.button("🔎 Recommend"):
    if query.strip():
        query_vec = vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, matrix).flatten()
        df["score"] = similarities
        top_matches = df.sort_values(by="score", ascending=False).head(10)
        
        st.markdown("### 📝 Recommended Assessments:")
        st.dataframe(top_matches[[
            "Assessment Name", "URL", "Remote Testing Support",
            "Adaptive/IRT Support", "Duration", "Test Type"
        ]], use_container_width=True)
    else:
        st.warning("Please enter a query above.")
