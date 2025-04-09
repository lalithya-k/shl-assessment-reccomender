# SHL Assessment Recommender

This project is a smart recommendation system that suggests SHL assessments based on a job description or user query using Natural Language Processing (NLP) techniques.

It includes:
- A **Flask backend** serving an assessment recommendation API.
- A lightweight **HTML UI** (served from Flask) for interacting with the recommender.
- A dataset of SHL assessments with metadata used for similarity matching.

---

## Live Demo

🌐 [Streamlit UI Version](https://shl-assessment-reccomender-uvjfghdocyyyawawq3zp8k.streamlit.app/)  
⚙️ [Flask API Hosted on Render](https://shl-assessment-reccomender.onrender.com)

---

## How it Works

1. A user enters a job description or desired skills.
2. The query is transformed using **TF-IDF Vectorization**.
3. Cosine similarity is computed between the query and assessment descriptions.
4. The top-k most relevant SHL assessments are returned.

---

## Tech Stack

- **Python 3.10+**
- **Flask** – backend server and UI templating
- **Pandas, Scikit-learn** – data handling and NLP
- **Jinja2** – HTML templating for UI
- **gunicorn** – production WSGI server (for deployment)

---


## Installation (Run Locally)

```bash
git clone https://github.com/lalithya-k/shl-assessment-reccomender.git
cd shl-assessment-reccomender
pip install -r requirements.txt
python main.py
```

Then go to `http://localhost:5000` to use the app.

---

## API Usage

**POST** `/recommend`  
**Body:**
```json
{
  "query": "python data analyst",
  "top_k": 3
}
```

**Response:**
Returns top matching SHL assessments with name, URL, and match score.

---

##  Report & Submission Links

-  **GitHub Repo:** [https://github.com/lalithya-k/shl-assessment-reccomender](https://github.com/lalithya-k/shl-assessment-reccomender)
-  **1-page Report (PDF):** _[https://drive.google.com/file/d/1vwjHg0heplvdoB7ostftEUS48mkHRumC/view?usp=sharing]
-  **API Endpoint:** [https://shl-assessment-reccomender.onrender.com/recommend](https://shl-assessment-reccomender.onrender.com/recommend)

---

##  License

This project is built for SHL assignment evaluation purposes and may include publicly available assessment descriptions only for academic/research demonstration.

