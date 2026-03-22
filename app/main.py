from crawler.quotes_spider import crawl_quotes, save_quotes_to_json
from analyzer.quotes_analyzer import analyze_quotes, save_analysis_report


def run():
    data = crawl_quotes()
    save_quotes_to_json(data)

    report = analyze_quotes(data)
    save_analysis_report(report)

    print("分析结果：")
    print(report)


if __name__ == "__main__":
    run()