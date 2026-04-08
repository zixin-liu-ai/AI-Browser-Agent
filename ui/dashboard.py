from __future__ import annotations

from typing import Any

import pandas as pd
import streamlit as st

from styles import inject_global_styles
from components import (
    analysis_summary_panel,
    browser_shell_header,
    build_demo_table,
    build_demo_tasks,
    earnings_chart,
    heatmap_chart,
    line_performance_chart,
    metric_card,
    render_ai_workspace_panel,
    render_manage_projects_panel,
    render_priority_tasks_panel,
    side_nav,
)


st.set_page_config(
    page_title="AI Browser Agent Dashboard",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def safe_get_real_data() -> dict[str, Any]:
    data: dict[str, Any] = {
        "metrics": {
            "clients": "14",
            "revenue": "$3.52",
            "projects": "22",
            "priority": "03",
        },
        "task_queue": build_demo_tasks(),
        "table": build_demo_table(),
    }

    try:
        from api_client import list_tasks, get_dashboard_data  # type: ignore

        try:
            dashboard_payload = get_dashboard_data()
            if isinstance(dashboard_payload, dict):
                metrics = dashboard_payload.get("metrics", {})
                data["metrics"] = {
                    "clients": str(metrics.get("clients", data["metrics"]["clients"])),
                    "revenue": str(metrics.get("revenue", data["metrics"]["revenue"])),
                    "projects": str(metrics.get("projects", data["metrics"]["projects"])),
                    "priority": str(metrics.get("priority", data["metrics"]["priority"])),
                }
        except Exception:
            pass

        try:
            tasks_payload = list_tasks()
            if isinstance(tasks_payload, list) and tasks_payload:
                rows: list[dict[str, Any]] = []
                queue: list[dict[str, Any]] = []

                for idx, item in enumerate(tasks_payload[:10]):
                    task_id = item.get("task_id", f"T-{idx + 1:03d}")
                    status = str(item.get("status", "pending"))
                    updated = item.get("updated_at") or item.get("created_at") or "--"
                    task_type = item.get("task_type") or item.get("mode") or "workflow"
                    source = item.get("source") or "browser"

                    rows.append(
                        {
                            "task_name": task_id,
                            "task_type": task_type,
                            "source": source,
                            "updated_at": str(updated)[:10],
                            "price": "$--",
                            "status": status,
                        }
                    )

                    queue.append(
                        {
                            "name": task_id,
                            "date": str(updated)[:10],
                            "progress": f"{idx + 1}/{len(tasks_payload)} Active",
                            "desc": f"{task_type} / {status}",
                        }
                    )

                if rows:
                    data["table"] = pd.DataFrame(rows)
                if queue:
                    data["task_queue"] = queue[:3]

                data["metrics"]["projects"] = str(len(tasks_payload))
        except Exception:
            pass

    except Exception:
        pass

    return data


def top_metrics(metrics: dict[str, str]) -> None:
    c1, c2, c3, c4 = st.columns(4, gap="small")

    with c1:
        metric_card("Clients", metrics.get("clients", "14"), "Compare 10 last month", featured=True)
    with c2:
        metric_card("Revenue", metrics.get("revenue", "$3.52"), "$3720.00 last month")
    with c3:
        metric_card("Projects", metrics.get("projects", "22"), "Compare 16 last month")
    with c4:
        metric_card("Priority Tasks", metrics.get("priority", "03"), "Queue synced")


def simple_panel_title(title: str, subtitle: str = "", badge: str = "") -> None:
    if badge:
        st.markdown(
            f"""
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
                <div>
                    <div class="panel-title">{title}</div>
                    <div class="panel-subtitle">{subtitle}</div>
                </div>
                <div class="badge-glow">{badge}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        subtitle_html = f'<div class="panel-subtitle">{subtitle}</div>' if subtitle else ""
        st.markdown(
            f"""
            <div style="margin-bottom:10px;">
                <div class="panel-title">{title}</div>
                {subtitle_html}
            </div>
            """,
            unsafe_allow_html=True,
        )


def main() -> None:
    inject_global_styles()
    payload = safe_get_real_data()

    st.markdown('<div class="app-shell">', unsafe_allow_html=True)
    browser_shell_header()

    nav_col, main_col, right_col = st.columns([0.7, 6.2, 3.0], gap="small")

    with nav_col:
        side_nav()

    with main_col:
        top_metrics(payload["metrics"])

        left_sub, right_sub = st.columns([1.0, 1.15], gap="small")

        with left_sub:
            simple_panel_title("Revenue Analytics")
            analysis_summary_panel()

        with right_sub:
            simple_panel_title("Earnings Last 30 Days", badge="Live")
            earnings_chart()
            st.markdown(
                """
                <div style="display:flex;justify-content:space-between;color:#c8d3f4;font-size:13px;margin-top:-8px;margin-bottom:16px;">
                    <div>
                        <span style="color:#8ea0ca;">Earned</span><br>
                        <span style="font-size:28px;font-weight:800;color:white;">$220</span>
                    </div>
                    <div style="text-align:right;">
                        <span style="color:#8ea0ca;">Projected</span><br>
                        <span style="font-size:28px;font-weight:800;color:white;">$245</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        render_manage_projects_panel(payload["table"])

    with right_col:
        render_priority_tasks_panel(payload["task_queue"])
        render_ai_workspace_panel()

        simple_panel_title("Orders by Time", "Execution intensity heatmap")
        heatmap_chart()

        simple_panel_title("Sales Performance", "Projected vs actual")
        line_performance_chart()

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()