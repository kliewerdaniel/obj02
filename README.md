Certainly! Based on the actual structure and contents of the kliewerdaniel/obj01 repository, here is a revised README.md that accurately reflects the project’s setup and functionality:

⸻

Objective Newsfeed — A Tool for Truth

🧭 Mission Statement

Objective Newsfeed is an open-source initiative aimed at reclaiming truth in journalism through technology. Our mission is to empower individuals with tools to parse, translate, compare, and summarize global news coverage from multiple sources—free from commercial, political, or algorithmic bias.

⸻

📁 Project Structure

The repository is organized as follows:
	•	api/: Contains FastAPI route definitions.
	•	configs/: YAML configuration files for feeds and pipeline settings.
	•	frontend/: Frontend assets and templates.
	•	modules/: Core modules for scraping, translation, embedding, etc.
	•	nlp/: Natural Language Processing utilities.
	•	output/: Generated outputs such as summaries and graphs.
	•	static/: Static files for the web interface.
	•	main.py: Entry point for the FastAPI application.
	•	pipeline.py: Script to run the data processing pipeline.
	•	requirements.txt: Python dependencies.

⸻

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/kliewerdaniel/obj01.git
cd obj01

2. Create and Activate a Virtual Environment (Optional but Recommended)

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Download SpaCy Language Model

python -m spacy download en_core_web_sm

5. Start the FastAPI Application

uvicorn main:app --reload

Access the API at http://127.0.0.1:8000.

6. Frontend

Navigate to the frontend directory and start the development server:
cd frontend
npm install
npm run dev
Access the web interface at http://localhost:5173.

⸻

🔧 Configuration
	•	configs/newsfeeds.yaml: Define RSS feed URLs and categories.
	

⸻

🛠️ Extending the Project
	•	Translation Models: Swap translation models by updating the TRANSLATION_MODEL environment variable.
	•	Embedding Models: Change embedding models via the EMBEDDING_MODEL environment variable.
	•	Summarization: Modify or add summarization techniques in the nlp/ directory.
	•	Frontend: Customize the web interface in the frontend/ directory.

⸻

📜 License

MIT License — Open source for truth seekers, researchers, and builders of transparent media tools.

⸻
