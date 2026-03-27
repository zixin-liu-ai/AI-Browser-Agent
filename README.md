# 🤖 AI Browser Agent

🚀 An end-to-end AI-powered browser automation system for structured data extraction, analysis, and interactive visualization.

---

## 🌟 Overview

This project builds a complete data pipeline that:

* Automates browser interaction using Playwright
* Extracts structured quote data from web pages
* Performs statistical and AI-enhanced analysis
* Exposes data through FastAPI APIs
* Visualizes insights via an interactive Streamlit dashboard

> 🧠 Pipeline:
> **Playwright → Data Processing → AI Enrichment → FastAPI → Streamlit**

---

## 🔥 Key Features

### 🌐 Browser Automation (Playwright)

* Automated crawling of multi-page websites
* Handles pagination dynamically
* Extracts structured content reliably

---

### 📥 Structured Data Extraction

Each quote contains:

* 📄 Page number
* 💬 Quote text
* 👤 Author
* 🏷️ Tags

---

### 🧠 AI Enrichment

* Automatic theme extraction (AI Theme)
* Sentiment classification (positive / neutral / negative)
* Tone detection (e.g. philosophical, humorous, inspirational)

---

### 📊 Statistical Analysis

* Total number of quotes
* Top 10 authors
* Top 10 tags
* Quotes per page distribution
* AI theme distribution
* Sentiment distribution

---

### 🔌 FastAPI Backend

* RESTful API service
* Auto-generated Swagger docs

Endpoints:

* `/quotes` → raw + enriched data
* `/analysis` → aggregated statistics

---

### 🎨 Interactive Dashboard (Streamlit)

#### 📊 Overview

* Total quotes
* Total pages
* Top author
* Top tag
* Top AI theme

#### 📈 Visualization

* Top authors bar chart
* Top tags bar chart
* AI theme distribution
* Sentiment distribution
* Quotes per page line chart

#### 🔎 Data Exploration

* Filter by author
* Search quote text
* Search tags / AI themes

---

## 🛠️ Tech Stack

* Python
* Playwright
* FastAPI
* Streamlit
* JSON
* collections.Counter
* LLM (optional, with fallback)

---

## 📂 Project Structure

AI-Browser-Agent/
├── app/
│   ├── crawler/
│   │   └── quotes_spider.py
│   ├── analyzer/
│   │   ├── quotes_analyzer.py
│   │   ├── enrich_quotes.py
│   │   └── llm_analyzer.py
│   ├── api/
│   │   └── server.py
│   └── main.py
├── ui/
│   └── dashboard.py
├── data/
│   ├── quotes_all.json
│   ├── analysis_report.json
│   └── enriched_quotes.json
├── requirements.txt
├── docker-compose.yml
└── README.md
---

## ▶️ Getting Started

### 1️⃣ Create virtual environment

python -m venv venv

### 2️⃣ Activate

venv\Scripts\activate

### 3️⃣ Install dependencies

pip install -r requirements.txt
playwright install

---

## 🚀 Run the Project

### 🧠 Step 1: Crawl + Analyze + Enrich

python app/main.py

---

### 🔌 Step 2: Start FastAPI

python -m uvicorn app.api.server:app --reload

Swagger UI:
http://127.0.0.1:8000/docs

---

### 🎨 Step 3: Start Dashboard

streamlit run ui/dashboard.py

---

## 📡 API Endpoints

/quotes   → Get all enriched quotes
/analysis → Get analysis results

---

## 📊 Example Output

### 💬 Quote (Enriched)

{
  "page": 1,
  "author": "Albert Einstein",
  "text": "The world as we have created it is a process of our thinking.",
  "tags": ["thinking", "world"],
  "ai_theme": "deep-thoughts",
  "sentiment": "neutral",
  "tone": "philosophical"
}

---

### 📈 Analysis

{
  "total_quotes": 100,
  "top_10_authors": [["Albert Einstein", 10]],
  "top_10_tags": [["love", 14]],
  "sentiment_distribution": {
    "positive": 50,
    "neutral": 43,
    "negative": 7
  }
}

---

## 📸 Demo

Dashboard includes:

* Overview metrics
* Top authors & tags
* AI themes & sentiment charts
* Search & filtering system

---

## 🚧 Future Improvements

* Replace JSON with PostgreSQL
* Add vector search (RAG)
* Build conversational AI interface
* Support multi-site crawling
* Full Docker deployment
* Async + production optimization

---

## 👩‍💻 Author

Catherine ✨

---

## 💡 Notes

This project demonstrates:

* End-to-end system design (crawler → backend → frontend)
* AI integration into data pipelines
* Real-world data engineering workflow
* Full-stack engineering capability

Not just a crawler — but a mini AI data platform.
