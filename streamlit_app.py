import streamlit as st
import requests

# Page config
st.set_page_config(page_title="SHL Assessment Recommender", page_icon="🔍")

# App title
st.title("🔍 SHL Assessment Recommender\n(API UI)")

# Input fields
query = st.text_area("Enter a job description or skills you’re looking for:")
top_k = st.slider("Number of recommendations", 1, 5, 3)

# Call the API
if st.button("🔍 Recommend") and query:
    with st.spinner("Fetching recommendations..."):
        try:
            response = requests.post(
                "https://shl-assessment-reccomender.onrender.com/recommend",
                headers={"Content-Type": "application/json"},
                json={"query": query, "top_k": top_k}
            )

            if response.status_code == 200:
                results = response.json()
                if results:
                    st.success("Here are your recommendations:")
                    for res in results:
                        st.markdown(f"### ✅ {res['Assessment Name']}")
                        st.write(f"🔗 [Link]({res['URL']})")
                        st.write(f"🧪 **Type:** {res['Test Type']} &nbsp;&nbsp;&nbsp; ⏱️ **Duration:** {res['Duration']}")
                        st.write(f"📡 **Remote:** {res['Remote Testing Support']} &nbsp;&nbsp;&nbsp; 🧠 **Adaptive:** {res['Adaptive/IRT Support']}")
                        st.markdown("---")
                else:
                    st.warning("No matches found for your query.")
            else:
                st.error(f"❌ Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"🚨 Request failed: {e}")
