# Apply feedparser patch BEFORE importing anything else
import feedparser_patch # Add this at the very top

# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.graph import router as graph_router

# Import necessary modules for the pipeline
import os
import json
from datetime import datetime
from modules.scraping import fetch_articles
from modules.translation import translate_article
from modules.summarization import summarize

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In dev. Lock it down in prod.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router mounted at /api/graph
app.include_router(graph_router, prefix="/api/graph")

# Serve static files (e.g. your graph.html page)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/graph")
def serve_graph_page():
    return FileResponse("static/graph.html")

@app.get("/api/run_pipeline")
def run_pipeline():
    print("🚀 Starting news pipeline...")

    try:
        # Step 1: Scrape
        print("📰 Scraping articles...")
        articles = fetch_articles(max_articles=10) # Use the updated max_articles

        # Step 2: Process each article
        results = []
        for article in articles:
            print(f"🔍 Processing: {article['title']}")

            # Translate if needed
            article['translated_text'] = translate_article(article)

            # Summarize
            article['summary'] = summarize(article['translated_text'])

            results.append({
                'title': article['title'],
                'source': article['source'],
                'summary': article['summary'],
                'url': article['url'],
                'published': article['published']
            })

        # Step 3: Output
        timestamp = datetime.now().strftime("%Y-%m-%d")
        output_file = os.path.join('output', f'news_digest_{timestamp}.json') # Correct path

        print("📝 Final results before saving:") # Add logging
        print(json.dumps(results, indent=2)) # Print the results

        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)

        print(f"✅ Pipeline complete! Output saved to {output_file}")
        print(f"📊 Processed {len(results)} articles")

        return {"status": "success", "message": "Pipeline executed successfully."}

    except Exception as e:
        print(f"❌ Pipeline failed: {str(e)}")
        return {"status": "error", "message": str(e)}
