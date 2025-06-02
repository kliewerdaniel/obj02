# Objective Newsfeed — A Tool for Truth

---

## 🧭 Mission Statement

**Objective Newsfeed** is an open-source initiative dedicated to reclaiming truth in journalism through technology.  
Our mission is to empower individuals with tools to parse, translate, compare, and summarize global news coverage from multiple sources—free from commercial, political, or algorithmic bias.

---

## 📁 Project Structure

The repository is organized as follows:

- `api/` — FastAPI route definitions  
- `configs/` — YAML configuration files for feeds and pipeline settings  
- `frontend/` — Frontend assets and templates  
- `modules/` — Core modules for scraping, translation, embedding, etc.  
- `nlp/` — Natural Language Processing utilities  
- `output/` — Generated outputs such as summaries and graphs  
- `static/` — Static files for the web interface  
- `main.py` — Entry point for the FastAPI application  
- `pipeline.py` — Script to run the data processing pipeline  
- `requirements.txt` — Python dependencies  

---

## 🚀 Getting Started

1. **Clone the Repository**

```bash
   git clone https://github.com/kliewerdaniel/obj02.git
   cd obj02
```

2.	Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3.	Install Dependencies

```bash
pip install -r requirements.txt
```

4.	Download SpaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

5.	Start the FastAPI Application

```bash
uvicorn main:app --reload
```

Access the API at: http://127.0.0.1:8000

6.	Frontend

```bash
cd frontend
npm install
npm run dev
```

Access the web interface at: http://localhost:5173

⸻

🔧 Configuration
	•	configs/newsfeeds.yaml — Define RSS feed URLs and categories

⸻

📜 License

MIT License — Open source for truth seekers, researchers, and builders of transparent media tools.

⸻
