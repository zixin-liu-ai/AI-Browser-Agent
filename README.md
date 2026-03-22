# 🤖 AI-Browser-Agent

✨ A browser automation + AI-powered data analysis agent built with Playwright and Python.

---

## 🚀 Project Overview

This project implements an **AI-enhanced browser data agent** that automates web interaction, collects structured data across paginated pages, performs statistical analysis, and generates AI-driven insights with graceful fallback handling.

> ⚡ Not just a crawler — this is a mini AI data pipeline.

---

## 🔥 Key Features

- 🌐 **Browser Automation** — Playwright-based dynamic page control
- 📄 **Paginated Crawling** — automatic navigation across multiple pages
- 🧩 **Structured Extraction** — quote text / author / tags parsing
- 💾 **Data Persistence** — JSON storage for downstream processing
- 📊 **Statistical Analysis** — frequency analysis (authors, tags, distribution)
- 🤖 **LLM Integration** — AI-generated insights from collected data
- 🛡️ **Fallback Mechanism** — prevents system failure when API quota is exceeded
- 🧱 **Modular Design** — crawler / analyzer / LLM separated cleanly

---

## 🛠️ Tech Stack

- 🐍 Python
- 🎭 Playwright
- 📦 JSON
- 🔢 collections.Counter
- 🤖 OpenAI API (LLM analysis)

---

## 📂 Project Structure

```
AI-Browser-Agent/
├── app/
│   ├── crawler/
│   │   └── quotes_spider.py
│   ├── analyzer/
│   │   ├── quotes_analyzer.py
│   │   └── llm_analyzer.py
│   └── main.py
├── data/
│   ├── quotes_all.json
│   ├── analysis_report.json
│   └── llm_report.txt
├── README.md
└── requirements.txt
```

---

## ⚙️ Pipeline Architecture

```
Web → Playwright → Structured Data → Statistical Analysis → LLM Insight → Output
```

---

## 📊 Outputs

### 💬 Quote Dataset

- 100 quotes
- Structured fields: page / text / author / tags

### 📈 Analysis Report

- Top authors
- Top tags
- Distribution across pages

### 🤖 AI Insight

- Natural language summary of dataset
- Saved to `llm_report.txt`
- Fallback enabled if API fails

---

## 📌 Sample Output

### JSON Data

```json
{
  "page": 1,
  "text": "...",
  "author": "Albert Einstein",
  "tags": ["thinking", "world"]
}
```

### Analysis Report

```json
{
  "total_quotes": 100,
  "top_10_authors": [["Albert Einstein", 10]]
}
```

---

## ▶️ How to Run

```bash
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
playwright install

python app/main.py
```

---

## 🔮 Future Improvements

- 🗄️ PostgreSQL storage
- 🤖 Structured LLM output (JSON instead of text)
- 🌍 Multi-site crawling
- 🛡️ Anti-bot handling
- ⚡ FastAPI service
- 🐳 Docker deployment

---

## 👩‍💻 Author

Catherine 💅
