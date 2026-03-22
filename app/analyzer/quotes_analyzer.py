from collections import Counter
import json
import os


def analyze_quotes(data):
    total_quotes = len(data)

    author_counter = Counter()
    tag_counter = Counter()
    page_counter = Counter()

    for item in data:
        author_counter[item["author"]] += 1
        page_counter[item["page"]] += 1

        for tag in item.get("tags", []):
            tag_counter[tag] += 1

    report = {
        "total_quotes": total_quotes,
        "top_10_authors": author_counter.most_common(10),
        "top_10_tags": tag_counter.most_common(10),
        "quotes_per_page": dict(sorted(page_counter.items()))
    }

    return report


def save_analysis_report(report, output_path="data/analysis_report.json"):
    os.makedirs("data", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"✅ 成功保存分析报告到 {output_path}")