---

# 🤖 AI-Browser-Agent

✨ A browser automation data collection and analysis project built with Playwright and Python.

---

## 🚀 Project Overview

This project uses Playwright to automate browser interactions, crawl paginated quote data from a website, extract structured fields, and generate analysis reports.

### 🔥 Currently implemented features:

* 🌐 Automated browser control with Playwright
* 📄 Multi-page crawling
* 🧩 Structured quote extraction
* 💾 JSON data persistence
* 📊 Author/tag frequency analysis
* 🧱 Modular project structure

---

## 🛠️ Tech Stack

* 🐍 Python
* 🎭 Playwright
* 📦 JSON
* 🔢 collections.Counter

---

## 📂 Project Structure

```
AI-Browser-Agent/
├── app/
│   ├── crawler/
│   │   └── quotes_spider.py
│   ├── analyzer/
│   │   └── quotes_analyzer.py
│   └── main.py
├── data/
│   ├── quotes_all.json
│   └── analysis_report.json
├── README.md
└── requirements.txt
```

---

## ⚙️ Features

### 1️⃣ Browser Automation 🌐

The project launches a browser automatically and navigates through multiple pages.

### 2️⃣ Data Crawling 📥

It extracts the following fields for each quote:

* 📄 page
* 💬 text
* 👤 author
* 🏷️ tags

### 3️⃣ Data Storage 💾

The crawled data is saved into `data/quotes_all.json`.

### 4️⃣ Data Analysis 📊

The analysis module generates:

* 🔢 total number of quotes
* 🏆 top 10 authors
* 🏷️ top 10 tags
* 📑 quote count per page

The result is saved into `data/analysis_report.json`.

---

## 📌 Sample Output

### 💬 Quote Data Example

```json
{
  "page": 1,
  "text": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
  "author": "Albert Einstein",
  "tags": ["change", "deep-thoughts", "thinking", "world"]
}
```

### 📊 Analysis Report Example

```json
{
  "total_quotes": 100,
  "top_10_authors": [
    ["Albert Einstein", 10],
    ["J.K. Rowling", 9]
  ],
  "top_10_tags": [
    ["love", 14],
    ["inspirational", 13]
  ]
}
```

---

## ▶️ How to Run

### 1️⃣ Create virtual environment 🧪

```
python -m venv venv
```

### 2️⃣ Activate virtual environment ⚡

```
venv\Scripts\activate
```

### 3️⃣ Install dependencies 📦

```
pip install -r requirements.txt
playwright install
```

### 4️⃣ Run the project 🚀

```
python app/main.py
```

---

## 🔮 Future Improvements

* 🗄️ Add database storage with PostgreSQL
* 🤖 Add LLM-based text classification and summarization
* 🌍 Support more websites
* 🛡️ Add anti-bot / login handling
* 🐳 Containerize with Docker
* ⚡ Build API service with FastAPI

---

## 👩‍💻 Author

Catherine 💅

---
