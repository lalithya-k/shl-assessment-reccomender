
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
st.title("🔍 SHL Assessment Recommender")

@st.cache_resource
def load_model():
    return SentenceTransformer("paraphrase-MiniLM-L6-v2")

@st.cache_data
def load_data():
    df = pd.read_csv("shl_assessments.csv")
    model = load_model()
    df["embedding"] = df["Description"].apply(lambda x: model.encode(x, convert_to_numpy=True))
    return df

df = load_data()
model = load_model()

query = st.text_area("Enter a job description or query:", height=150)

if st.button("🔎 Recommend"):
    if query.strip():
        query_embedding = model.encode(query, convert_to_numpy=True)
        df["score"] = df["embedding"].apply(lambda emb: cosine_similarity([query_embedding], [emb])[0][0])
        top_matches = df.sort_values(by="score", ascending=False).head(10)
        
        st.markdown("### 📝 Recommended Assessments:")
        st.dataframe(top_matches[[
            "Assessment Name", "URL", "Remote Testing Support",
            "Adaptive/IRT Support", "Duration", "Test Type"
        ]], use_container_width=True)
    else:
        st.warning("Please enter a query above.")
