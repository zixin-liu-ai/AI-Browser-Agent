from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional


STATUS_COLOR_MAP = {
    "success": "#22c55e",
    "failed": "#ef4444",
    "running": "#3b82f6",
    "pending": "#f59e0b",
    "unknown": "#6b7280",
}


STATUS_LABEL_MAP = {
    "success": "SUCCESS",
    "failed": "FAILED",
    "running": "RUNNING",
    "pending": "PENDING",
    "unknown": "UNKNOWN",
}


def safe_get(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    if not isinstance(data, dict):
        return default
    return data.get(key, default)


def format_datetime(iso_str: Optional[str]) -> str:
    if not iso_str:
        return "-"
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", ""))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return str(iso_str)


def format_duration(seconds: Optional[float]) -> str:
    if seconds is None:
        return "-"
    try:
        seconds = float(seconds)
    except Exception:
        return "-"
    if seconds < 60:
        return f"{seconds:.2f}s"
    minutes = int(seconds // 60)
    remain = seconds % 60
    return f"{minutes}m {remain:.1f}s"


def get_status_color(status: Optional[str]) -> str:
    if not status:
        return STATUS_COLOR_MAP["unknown"]
    return STATUS_COLOR_MAP.get(status.lower(), STATUS_COLOR_MAP["unknown"])


def get_status_label(status: Optional[str]) -> str:
    if not status:
        return STATUS_LABEL_MAP["unknown"]
    return STATUS_LABEL_MAP.get(status.lower(), STATUS_LABEL_MAP["unknown"])


def calc_success_rate(tasks: List[Dict[str, Any]]) -> float:
    if not tasks:
        return 0.0
    success_count = sum(1 for t in tasks if t.get("status") == "success")
    return round(success_count / len(tasks) * 100, 2)


def build_status_badge_html(status: Optional[str]) -> str:
    color = get_status_color(status)
    label = get_status_label(status)
    return f"""
    <span style="
        display:inline-block;
        padding:4px 10px;
        border-radius:999px;
        font-size:12px;
        font-weight:700;
        color:white;
        background:{color};
        letter-spacing:0.4px;
    ">
        {label}
    </span>
    """.strip()


def normalize_task_rows(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows = []
    for task in tasks:
        rows.append(
            {
                "task_id": task.get("task_id", "-"),
                "status": task.get("status", "unknown"),
                "pages": task.get("pages", "-"),
                "mode": task.get("mode", "-"),
                "created_at": format_datetime(task.get("created_at")),
                "duration": format_duration(task.get("duration_seconds")),
                "quote_count": task.get("quote_count", 0),
                "unique_authors": task.get("unique_authors", 0),
                "total_tags": task.get("total_tags", 0),
                "summary": task.get("summary", ""),
            }
        )
    return rows


def truncate_text(text: Optional[str], max_len: int = 100) -> str:
    if not text:
        return ""
    text = str(text).strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def flatten_top_items(items: Optional[List[Dict[str, Any]]]) -> str:
    if not items:
        return "-"
    parts = []
    for item in items:
        name = item.get("name", "")
        count = item.get("count", 0)
        parts.append(f"{name} ({count})")
    return ", ".join(parts) if parts else "-"