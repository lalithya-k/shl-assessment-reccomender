import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="SHL Recommender", layout="centered")

st.title("🔍 SHL Assessment Recommender (API UI)")

query = st.text_area("Enter a job description or skills you’re looking for:")
top_k = st.slider("Number of recommendations", 1, 10, 3)

if st.button("Recommend"):
    if not query.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Getting recommendations..."):
            try:
                response = requests.post(
                    "https://shl-assessment-reccomender.onrender.com/recommend",
                    json={"query": query, "top_k": top_k},
                    headers={"Content-Type": "application/json"},
                    timeout=20
                )

                if response.status_code == 200:
                    data = response.json()
                    if not data:
                        st.info("No assessments matched your query.")
                    else:
                        df = pd.DataFrame(data)
                        st.success("Top Recommendations:")
                        st.dataframe(df)
                else:
                    st.error(f"Error: {response.status_code} - {response.json().get('detail')}")
            except Exception as e:
                st.error(f"Request failed: {e}")
