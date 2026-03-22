import json
import os
from playwright.sync_api import sync_playwright


def crawl_quotes():
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://quotes.toscrape.com/")
        page.wait_for_timeout(2000)

        page_num = 1

        while True:
            print(f"正在抓取第 {page_num} 页...")

            quotes = page.locator(".quote")
            count = quotes.count()

            for i in range(count):
                quote = quotes.nth(i)

                text = quote.locator(".text").text_content()
                author = quote.locator(".author").text_content()
                tags = quote.locator(".tags .tag").all_text_contents()

                results.append({
                    "page": page_num,
                    "text": text,
                    "author": author,
                    "tags": tags
                })

            next_btn = page.locator(".next a")

            if next_btn.count() > 0:
                next_btn.click()
                page.wait_for_timeout(2000)
                page_num += 1
            else:
                break

        browser.close()

    return results


def save_quotes_to_json(data, output_path="data/quotes_all.json"):
    os.makedirs("data", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 成功保存 {len(data)} 条数据到 {output_path}")