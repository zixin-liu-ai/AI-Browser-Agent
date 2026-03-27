import json
from pathlib import Path

from app.analyzer.llm_analyzer import analyze_quote_with_llm


BASE_DIR = Path(__file__).resolve().parent.parent.parent
INPUT_FILE = BASE_DIR / "data" / "quotes_all.json"
OUTPUT_FILE = BASE_DIR / "data" / "quotes_ai.json"


def enrich_quotes():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        quotes = json.load(f)

    enriched = []

    for i, item in enumerate(quotes, 1):
        print(f"[{i}/{len(quotes)}] analyzing...")

        quote_text = item.get("text", "").strip()
        author = item.get("author", "").strip()
        tags = item.get("tags", [])

        llm_result = analyze_quote_with_llm(
            quote=quote_text,
            author=author,
            tags=tags
        )

        new_item = {**item, **llm_result}
        enriched.append(new_item)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(enriched, f, ensure_ascii=False, indent=2)

    print(f"Done. Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    enrich_quotes()