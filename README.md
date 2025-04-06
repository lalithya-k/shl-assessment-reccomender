# shl-assessment-reccomender
# SHL Assessment Recommender System

This project is a take-home assignment for SHL's Generative AI Internship. It is a lightweight, scalable Streamlit-based recommender system that helps match SHL assessments to job descriptions or hiring queries.

---

## Live Demo

🔗 [Try the app](https://shl-assessment-reccomender-uvjfghdocyyyawawq3zp8k.streamlit.app/)

---

##  Features

- Accepts free-text queries or job descriptions
- Recommends the top-k SHL assessments based on semantic similarity
- Displays metadata like:
  - Remote Testing Support
  - Adaptive/IRT Support
  - Duration and Test Type
- Fully responsive UI built with Streamlit

---

## How It Works

- Uses **TF-IDF Vectorizer** to embed assessment descriptions
- Computes **cosine similarity** between user query and dataset
- Returns top 5–10 relevant matches in a clean table

---

## Files

| File | Description |
|------|-------------|
| `streamlit_app.py` | Main Streamlit app |
| `shl_assessments.csv` | Pre-scraped dataset of SHL assessments |
| `requirements.txt` | Python dependencies for deployment |
| `Lalithya_SHL_Assessment_Recommender.pdf` | 1-page summary PDF submitted to SHL |

---

## Libraries Used

- `streamlit`
- `pandas`
- `scikit-learn`

---


## Notes

- The original implementation used `sentence-transformers`, but was adapted to `TF-IDF` for Streamlit Cloud compatibility.
- No external API calls or downloads are required — works offline.

---


