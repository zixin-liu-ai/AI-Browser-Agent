import argparse

from app.crawler.quotes_spider import crawl_quotes, save_quotes_to_json
from app.analyzer.quotes_analyzer import analyze_quotes
from app.analyzer.llm_analyzer import analyze_quotes_with_llm


def main():
    # ===== CLI参数 =====
    parser = argparse.ArgumentParser(description="AI Browser Agent Pipeline")

    parser.add_argument(
        "--pages",
        type=int,
        default=10,
        help="Number of pages to crawl"
    )

    parser.add_argument(
        "--mode",
        type=str,
        default="llm",
        choices=["llm", "local"],
        help="Analysis mode: llm or local"
    )

    args = parser.parse_args()

    pages = args.pages
    mode = args.mode

    print(f"\n🚀 Starting pipeline | pages={pages}, mode={mode}\n")

    # ===== 1. 抓取数据 =====
    quotes = crawl_quotes(pages)

    # ===== 2. 保存原始数据 =====
    save_quotes_to_json(quotes, "data/quotes_all.json")

    # ===== 3. 本地统计分析 =====
    stats_result = analyze_quotes(quotes)

    print("\n📊 Statistical Analysis Result:")
    print(stats_result)

    # ===== 4. AI分析 =====
    if mode == "llm":
        print("\n🤖 Running LLM analysis...")
        ai_result = analyze_quotes_with_llm(quotes)
    else:
        print("\n🤖 Using local analysis mode...")
        ai_result = "Local mode: LLM skipped. Using statistical insights only."

    print("\n🤖 AI Analysis Result:")
    print(ai_result)

    # ===== 5. 保存AI分析结果 =====
    with open("data/llm_report.txt", "w", encoding="utf-8") as f:
        f.write(ai_result)

    print("\n✅ LLM analysis saved to data/llm_report.txt")


if __name__ == "__main__":
    main()