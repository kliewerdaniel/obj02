Here’s your rewritten and Markdown-formatted version of the document:

⸻

📰 Objective Newsfeed — A Tool for Truth

🧭 Mission Statement

Objective Newsfeed is an open-source initiative committed to reclaiming truth in journalism through technology. Our mission is to equip individuals with tools to parse, translate, compare, and summarize global news coverage across diverse sources—free from commercial, political, or algorithmic bias.

⸻

📁 Project Structure

The repository is organized as follows:

obj01/
├── api/           # FastAPI route definitions
├── configs/       # YAML configs for feeds and pipeline settings
├── frontend/      # Frontend assets and templates
├── modules/       # Core modules: scraping, translation, embeddings, etc.
├── nlp/           # Natural Language Processing utilities
├── output/        # Generated summaries, graphs, and outputs
├── static/        # Static files for the web UI
├── main.py        # Entry point for FastAPI app
├── pipeline.py    # Script to run the data processing pipeline
└── requirements.txt  # Python dependencies


⸻

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/kliewerdaniel/obj01.git
cd obj01

2. Create and Activate a Virtual Environment (Recommended)

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Download the SpaCy Language Model

python -m spacy download en_core_web_sm

5. Start the FastAPI Backend

uvicorn main:app --reload

Access the API at: http://127.0.0.1:8000

6. Launch the Frontend

cd frontend
npm install
npm run dev

Access the web interface at: http://localhost:5173

⸻

🔧 Configuration
	•	configs/newsfeeds.yaml: Define your RSS feed sources and categories here.

⸻

🛠️ Extending the Project
	•	Translation Models: Swap models by setting the TRANSLATION_MODEL environment variable.
	•	Embedding Models: Update the EMBEDDING_MODEL variable to change vector embeddings.
	•	Summarization Techniques: Add or modify methods inside the nlp/ directory.
	•	Frontend Customization: Update components and styles in the frontend/ folder.

⸻

📜 License

MIT License — Built for truth seekers, researchers, and developers committed to transparent media tools.

⸻
