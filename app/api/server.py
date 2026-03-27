from collections import Counter
from pathlib import Path
import json

from fastapi import FastAPI


app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
QUOTES_FILE = BASE_DIR / "data" / "quotes_ai.json"


def load_quotes():
    with open(QUOTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def build_analysis_report(quotes: list[dict]) -> dict:
    author_counter = Counter()
    tag_counter = Counter()
    theme_counter = Counter()
    sentiment_counter = Counter()
    quotes_per_page = Counter()

    for item in quotes:
        author = item.get("author", "").strip()
        if author:
            author_counter[author] += 1

        for tag in item.get("tags", []):
            if tag:
                tag_counter[tag] += 1

        theme = item.get("ai_theme", "").strip()
        if theme:
            theme_counter[theme] += 1

        sentiment = item.get("ai_sentiment", "").strip().lower()
        if sentiment:
            sentiment_counter[sentiment] += 1

        page = item.get("page")
        if page is not None:
            quotes_per_page[str(page)] += 1

    return {
        "total_quotes": len(quotes),
        "top_10_authors": author_counter.most_common(10),
        "top_10_tags": tag_counter.most_common(10),
        "top_10_ai_themes": theme_counter.most_common(10),
        "sentiment_distribution": dict(sentiment_counter),
        "quotes_per_page": dict(sorted(quotes_per_page.items(), key=lambda x: int(x[0]))),
    }


@app.get("/")
def root():
    return {"message": "AI Browser Agent API running"}


@app.get("/quotes")
def get_quotes():
    return load_quotes()


@app.get("/analysis")
def get_analysis():
    quotes = load_quotes()
    return build_analysis_report(quotes)