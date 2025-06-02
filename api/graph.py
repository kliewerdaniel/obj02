# obj01/api/graph.py

from fastapi import APIRouter, HTTPException
from nlp.entity_extractor import extract_entity_relationships, build_networkx_graph
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import json
import yaml
from datetime import datetime # Import datetime

current_dir = os.path.dirname(__file__)
# Dynamically generate news digest filepath based on current date
timestamp = datetime.now().strftime("%Y-%m-%d")
news_digest_filepath = os.path.join(current_dir, '..', 'output', f'news_digest_{timestamp}.json')
feeds_config_filepath = os.path.join(current_dir, '..', 'configs', 'feeds.yaml')

# news_digest_json is no longer needed as data is reloaded in get_articles

router = APIRouter()

# Pydantic model for a feed source
class FeedSource(BaseModel):
    name: str
    type: str
    url: str
    lang: str
    diversity_score: float
    perspective: str
    region: str

# Helper function to read feeds.yaml
def read_feeds_config():
    try:
        with open(feeds_config_filepath, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return {"sources": []} # Return empty structure if file not found
    except yaml.YAMLError as e:
        print(f"Error reading feeds.yaml: {e}")
        raise HTTPException(status_code=500, detail="Error reading feeds configuration")

# Helper function to write feeds.yaml
def write_feeds_config(config_data):
    try:
        with open(feeds_config_filepath, 'w') as f:
            yaml.dump(config_data, f, indent=2)
    except Exception as e:
        print(f"Error writing feeds.yaml: {e}")
        raise HTTPException(status_code=500, detail="Error writing feeds configuration")

@router.get("/graph.json")
def get_graph():
    # Use the dynamically generated news digest filepath
    try:
        with open(news_digest_filepath, 'r') as f:
            summaries = json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="News digest file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding news digest JSON")


    if not summaries:
         raise HTTPException(status_code=404, detail="No summaries found in news digest")

    # Assuming the first summary is representative for graph generation
    text = summaries[0]['summary']
    triples = extract_entity_relationships(text)

    G = build_networkx_graph(triples)

    # Convert to D3-friendly JSON
    nodes = [{"id": n} for n in G.nodes]
    links = [{"source": u, "target": v, "label": d["label"]} for u, v, d in G.edges(data=True)]

    return JSONResponse(content={"nodes": nodes, "links": links})


@router.get("/")
def get_articles():
    # Reload news digest data to ensure latest stories are fetched
    try:
        with open(news_digest_filepath, 'r') as f:
            reloaded_news_digest = json.load(f)
    except FileNotFoundError:
        reloaded_news_digest = [] # Handle case where file doesn't exist

    # Return actual news digest data
    return {
        "data": reloaded_news_digest
    }

@router.get("/feeds")
def get_feeds():
    config = read_feeds_config()
    return {"sources": config.get("sources", [])}

@router.post("/feeds")
def add_feed(source: FeedSource):
    config = read_feeds_config()
    # Check if a source with the same name or URL already exists
    for existing_source in config.get("sources", []):
        if existing_source.get("name") == source.name or existing_source.get("url") == source.url:
            raise HTTPException(status_code=400, detail="Feed source with this name or URL already exists")

    if "sources" not in config:
        config["sources"] = []
    config["sources"].append(source.dict()) # Use dict() for broader compatibility
    write_feeds_config(config)
    return {"message": "Feed source added successfully", "source": source}

@router.delete("/feeds/{name}")
def delete_feed(name: str):
    config = read_feeds_config()
    initial_count = len(config.get("sources", []))
    config["sources"] = [s for s in config.get("sources", []) if s.get("name") != name]

    if len(config.get("sources", [])) == initial_count:
        raise HTTPException(status_code=404, detail=f"Feed source with name '{name}' not found")

    write_feeds_config(config)
    return {"message": f"Feed source '{name}' deleted successfully"}
