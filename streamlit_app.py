!pip install sentence-transformers


import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# Load the CSV
df = pd.read_csv("/kaggle/input/shl-assessments/shl_assessments.csv")

# Initialize model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings from descriptions
df['embedding'] = df['Description'].apply(lambda desc: model.encode(desc, convert_to_numpy=True))


from sklearn.metrics.pairwise import cosine_similarity

def get_top_assessments(query, top_k=5):
    query_embedding = model.encode(query, convert_to_numpy=True)

    # Calculate cosine similarity
    similarities = df['embedding'].apply(lambda emb: cosine_similarity([query_embedding], [emb])[0][0])
    df['score'] = similarities

    # Return top matches
    top_matches = df.sort_values(by='score', ascending=False).head(top_k)
    return top_matches[['Assessment Name', 'URL', 'Remote Testing Support', 'Adaptive/IRT Support', 'Duration', 'Test Type', 'score']]


query = "I want to test Python coding skills for developers"
results = get_top_assessments(query)
results


!pip install streamlit sentence-transformers pandas scikit-learn


import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
st.title("SHL Assessment Recommender")

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_data
def load_data():
    df = pd.read_csv("/kaggle/input/shl-assessments/shl_assessments.csv")
    model = load_model()
    df["embedding"] = df["Description"].apply(lambda x: model.encode(x, convert_to_numpy=True))
    return df

df = load_data()
model = load_model()

query = st.text_area("Enter a job description or query:", height=150)

if st.button("Recommend"):
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


streamlit_code = """
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
st.title("SHL Assessment Recommender")

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_data
def load_data():
    df = pd.read_csv("shl_assessments.csv")
    model = load_model()
    df["embedding"] = df["Description"].apply(lambda x: model.encode(x, convert_to_numpy=True))
    return df

df = load_data()
model = load_model()

query = st.text_area("Enter a job description or query:", height=150)

if st.button("Recommend"):
    if query.strip():
        query_embedding = model.encode(query, convert_to_numpy=True)
        df["score"] = df["embedding"].apply(lambda emb: cosine_similarity([query_embedding], [emb])[0][0])
        top_matches = df.sort_values(by="score", ascending=False).head(10)
        
        st.markdown("###  Recommended Assessments:")
        st.dataframe(top_matches[[
            "Assessment Name", "URL", "Remote Testing Support",
            "Adaptive/IRT Support", "Duration", "Test Type"
        ]], use_container_width=True)
    else:
        st.warning("Please enter a query above.")
"""

with open("streamlit_app.py", "w") as f:
    f.write(streamlit_code)

print(" streamlit_app.py saved.")


!streamlit run streamlit_app.py
