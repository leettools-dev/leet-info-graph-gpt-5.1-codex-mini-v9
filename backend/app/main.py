from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/infographic")
def infographic():
    # Minimal placeholder response for infographic
    return {
        "title": "Research Snapshot",
        "date": "2026-02-19",
        "summary": "Infographic preview"
    }

@app.get("/article")
def article():
    return {
        "title": "Sample Article",
        "sections": [
            {"heading": "Overview", "content": "This is an overview."}
        ],
        "citations": ["https://example.com"]
    }

@app.get("/sources")
def sources():
    return [
        {
            "title": "Source Example",
            "url": "https://example.com",
            "publisher": "Example Pub",
            "published_at": "2026-02-19"
        }
    ]
