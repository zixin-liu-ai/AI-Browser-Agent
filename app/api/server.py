from __future__ import annotations

import traceback
from typing import Any, Dict, List, Literal, Optional

from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.task.task_manager import task_manager


app = FastAPI(
    title="AI Browser Agent Workflow Platform API",
    description="""
A task-driven AI browser workflow backend for structured crawling,
semantic enrichment, task lifecycle orchestration, and dashboard monitoring.
""".strip(),
    version="2.0.0",
    contact={
        "name": "Catherine",
    },
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TaskRunRequest(BaseModel):
    pages: int = Field(default=3, ge=1, le=20, description="Number of pages to crawl")
    mode: Literal["llm", "local"] = Field(default="llm", description="Analysis mode")


class TaskRunResponse(BaseModel):
    task_id: str
    status: str
    message: str


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


@app.get(
    "/health",
    tags=["System"],
    summary="Health check",
    response_model=HealthResponse,
)
def health() -> Dict[str, str]:
    return {
        "status": "ok",
        "service": "AI Browser Agent Workflow Platform API",
        "version": "2.0.0",
    }


@app.get(
    "/tasks",
    tags=["Tasks"],
    summary="List all tasks",
)
def list_tasks() -> List[Dict[str, Any]]:
    return task_manager.list_tasks()


@app.get(
    "/tasks/metrics/summary",
    tags=["Tasks"],
    summary="Get dashboard summary metrics",
)
def get_task_metrics_summary() -> Dict[str, Any]:
    return task_manager.get_metrics_summary()


@app.get(
    "/tasks/{task_id}",
    tags=["Tasks"],
    summary="Get task detail by task_id",
)
def get_task_detail(task_id: str) -> Dict[str, Any]:
    task = task_manager.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task not found: {task_id}")
    return task


@app.post(
    "/tasks/run",
    tags=["Tasks"],
    summary="Create and run a new task",
    response_model=TaskRunResponse,
)
def run_task(payload: TaskRunRequest, background_tasks: BackgroundTasks) -> Dict[str, Any]:
    task = task_manager.create_task(pages=payload.pages, mode=payload.mode)
    task_id = task["task_id"]

    background_tasks.add_task(execute_pipeline_task, task_id, payload.pages, payload.mode)

    return {
        "task_id": task_id,
        "status": "pending",
        "message": "Task created successfully and scheduled for background execution.",
    }


def execute_pipeline_task(task_id: str, pages: int, mode: str) -> None:
    """
    Replace the mock implementation below with your real pipeline call.

    Later you can switch this section to:
    - Playwright crawler
    - parser
    - analyzer
    - report builder

    For now it already supports the dashboard end-to-end.
    """
    try:
        task_manager.mark_running(task_id)

        # ===== Mock pipeline start =====
        # You can replace this block with your real business logic.
        quotes = build_mock_quotes(pages=pages, mode=mode)
        report = build_mock_report(quotes=quotes, pages=pages, mode=mode)
        # ===== Mock pipeline end =====

        task_manager.mark_success(task_id, quotes=quotes, report=report)

    except Exception as e:
        error_message = f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
        task_manager.mark_failed(task_id, error=error_message)


def build_mock_quotes(pages: int, mode: str) -> List[Dict[str, Any]]:
    sample_quotes = [
        {
            "text": "The world as we have created it is a process of our thinking.",
            "author": "Albert Einstein",
            "tags": ["change", "thinking"],
            "ai_theme": "deep-thoughts, change",
            "ai_sentiment": "neutral",
            "ai_tone": "philosophical",
            "ai_summary": "A reflective quote about how human thinking shapes reality.",
        },
        {
            "text": "It is never too late to be what you might have been.",
            "author": "George Eliot",
            "tags": ["inspirational"],
            "ai_theme": "self-growth",
            "ai_sentiment": "positive",
            "ai_tone": "motivational",
            "ai_summary": "Encourages personal transformation and late starts.",
        },
        {
            "text": "Do what you can, with what you have, where you are.",
            "author": "Theodore Roosevelt",
            "tags": ["action", "motivation"],
            "ai_theme": "action-oriented",
            "ai_sentiment": "positive",
            "ai_tone": "practical",
            "ai_summary": "Highlights immediate action under limited conditions.",
        },
        {
            "text": "Life is really simple, but we insist on making it complicated.",
            "author": "Confucius",
            "tags": ["life", "simplicity"],
            "ai_theme": "life-philosophy",
            "ai_sentiment": "neutral",
            "ai_tone": "reflective",
            "ai_summary": "A reminder that complexity is often self-imposed.",
        },
    ]

    output: List[Dict[str, Any]] = []
    total = max(pages * 8, 8)

    for i in range(total):
        item = sample_quotes[i % len(sample_quotes)].copy()
        item["source_page"] = (i // 8) + 1
        item["mode"] = mode
        output.append(item)

    return output


def build_mock_report(quotes: List[Dict[str, Any]], pages: int, mode: str) -> Dict[str, Any]:
    quote_count = len(quotes)
    authors = [q.get("author", "Unknown") for q in quotes]
    unique_authors = len(set(authors))
    all_tags = []
    for q in quotes:
        all_tags.extend(q.get("tags", []))

    return {
        "summary": f"Successfully crawled and AI-enriched {quote_count} quotes.",
        "quote_count": quote_count,
        "unique_authors": unique_authors,
        "total_tags": len(all_tags),
        "mode": mode,
        "pages": pages,
        "highlights": [
            "Task lifecycle persisted to disk",
            "Quotes enriched with AI metadata",
            "Dashboard-ready summary metrics generated",
        ],
    }