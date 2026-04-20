# 🚀 AI Browser Agent Workflow Platform

> Turning browser automation into a scalable AI workflow system.

A portfolio-grade **AI-powered browser workflow platform** built with **FastAPI, Playwright, and Streamlit**.

This project transforms traditional one-off crawler scripts into a **modular, workflow-driven AI system** capable of structured data extraction, lifecycle orchestration, and trend analytics.

---

## 🎬 Demo Video

> Watch the 58s end-to-end workflow demo

[https://www.bilibili.com/video/BV1uYdrBMEM4](https://www.bilibili.com/video/BV1uYdrBMEM4)

---

## ✨ What This Project Demonstrates

This project showcases a **full-stack AI workflow system**, including:

* Browser automation at scale (Playwright)
* Task lifecycle orchestration (creation → execution → persistence)
* Structured data extraction from real web sources
* LLM-based trend analysis and summarization
* Historical snapshot tracking and aggregation
* Interactive dashboard for monitoring and insights
* Production-style API services with FastAPI

Designed to demonstrate **real-world AI application engineering**, not just isolated scripts.

---

## 🎯 Project Positioning

Unlike traditional crawler scripts, this project is designed as a:

* workflow-driven automation platform
* modular AI application system
* reusable engineering architecture

It reflects how browser automation can evolve into a **scalable AI-powered workflow system**.

---

## 💡 Example Use Case

This platform can be used to:

* analyze global hiring trends from job platforms
* extract structured data from dynamic websites
* monitor keyword evolution in tech roles
* build automated research pipelines

---

## 🖥️ Dashboard Overview

A polished visual dashboard for browser workflow monitoring and trend intelligence.

![Dashboard Overview](./assets/01-dashboard-overview.png)

---

## 📈 Trend Analytics Panel

The analytics panel highlights:

* total tasks
* latest trend metrics
* top locations
* recurring keywords
* role category distribution

![Trend Analysis](./assets/02-trend-analysis-panel.png)

---

## 🕒 Category & History Panel

Supports:

* category breakdown
* trend history
* keyword accumulation
* snapshot timeline

![Category History](./assets/03-category-history-panel.png)

---

## 📋 Task Lifecycle Table

All tasks are persisted and visualized through a lifecycle table.

Tracked fields include:

* task_id
* source
* status
* updated_at
* lifecycle history

![Task Lifecycle](./assets/04-task-lifecycle-table.png)

---

## 🧠 System Architecture

Pipeline:

Browser Source → Parser → Task Store → Analyzer → Summary → History → Dashboard

![System Architecture](./assets/05-system-architecture.png)

### Modules

* Browser Source
* Playwright Parser
* Task Storage
* Workflow Manager
* Trend Analyzer
* Snapshot Summary
* History Accumulator
* Streamlit Dashboard

---

## 🔌 API Workflow

### Swagger Overview

![Swagger API](./assets/06-api-swagger-overview.png)

### Run Task Request

![Task Run Request](./assets/07-api-task-run-request.png)

### Run Task Response

![Task Run Response](./assets/08-api-task-run-response.png)

---

## ⚙️ Tech Stack

### Backend

* FastAPI
* Uvicorn
* Playwright
* Python 3.11

### Frontend

* Streamlit
* Metrics panels
* Task lifecycle table
* Trend analytics blocks

### Workflow

* task orchestration
* async scheduling
* historical snapshots
* structured trend analytics

---

## 🚀 Quick Start

### 1. Backend

```bash
uvicorn app.api.main:app --reload
```

### 2. Dashboard

```bash
streamlit run ui/dashboard.py
```

### 3. Swagger

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 Roadmap

* PostgreSQL persistence
* Docker Compose deployment
* multi-source browser workflows
* task retry queue
* daily scheduled automation
* AI-generated workflow reports
* cloud deployment pipeline

---

## ⭐ Technical Blog

Juejin Write-up:
[https://juejin.cn/post/7627400127372935214](https://juejin.cn/post/7627400127372935214)
