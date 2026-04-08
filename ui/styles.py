from __future__ import annotations


def inject_global_styles() -> None:
    import streamlit as st

    st.markdown(
        """
        <style>
        :root {
            --bg: #070b14;
            --panel: linear-gradient(180deg, rgba(11,16,30,0.96) 0%, rgba(8,12,24,0.98) 100%);
            --panel-2: linear-gradient(180deg, rgba(18,24,42,0.92) 0%, rgba(10,14,26,0.95) 100%);
            --line: rgba(127, 90, 240, 0.20);
            --line-strong: rgba(166, 114, 255, 0.42);
            --text: #f4f7ff;
            --muted: #9da7c2;
            --muted-2: #6f7a98;
            --purple: #8b5cf6;
            --purple-2: #a855f7;
            --purple-3: #c084fc;
            --blue: #38bdf8;
            --cyan: #22d3ee;
            --green: #22c55e;
            --danger: #fb7185;
            --warning: #f59e0b;
            --shadow: 0 0 0 1px rgba(139,92,246,0.14), 0 10px 30px rgba(0,0,0,0.35), 0 0 40px rgba(139,92,246,0.12);
            --radius-xl: 22px;
            --radius-lg: 18px;
            --radius-md: 14px;
        }

        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background:
                radial-gradient(circle at 15% 20%, rgba(56,189,248,0.10), transparent 20%),
                radial-gradient(circle at 85% 15%, rgba(168,85,247,0.16), transparent 22%),
                radial-gradient(circle at 80% 80%, rgba(34,211,238,0.10), transparent 18%),
                linear-gradient(135deg, #03060d 0%, #070b14 45%, #050814 100%);
            color: var(--text);
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stSidebar"] {
            display: none;
        }

        .block-container {
            padding-top: 1.1rem;
            padding-bottom: 1.25rem;
            max-width: 1500px;
        }

        .app-shell {
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 28px;
            background: rgba(5, 9, 18, 0.78);
            box-shadow: 0 20px 60px rgba(0,0,0,0.38), 0 0 0 1px rgba(168,85,247,0.10);
            padding: 14px;
            backdrop-filter: blur(10px);
        }

        .top-browser {
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 20px;
            background: linear-gradient(180deg, rgba(18,22,32,0.96), rgba(9,12,21,0.96));
            padding: 10px 14px;
            margin-bottom: 14px;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
        }

        .browser-row {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .traffic {
            display: flex;
            gap: 7px;
            min-width: 60px;
        }

        .dot {
            width: 11px;
            height: 11px;
            border-radius: 50%;
            opacity: 0.95;
        }

        .dot.red { background: #ff5f57; }
        .dot.yellow { background: #febc2e; }
        .dot.green { background: #28c840; }

        .browser-bar {
            flex: 1;
            height: 36px;
            border-radius: 999px;
            background: linear-gradient(180deg, rgba(16,20,30,0.98), rgba(9,12,20,0.98));
            border: 1px solid rgba(255,255,255,0.05);
            display: flex;
            align-items: center;
            padding: 0 16px;
            color: var(--muted);
            font-size: 13px;
            letter-spacing: 0.2px;
        }

        .browser-actions {
            display: flex;
            gap: 8px;
        }

        .mini-btn {
            width: 28px;
            height: 28px;
            border-radius: 10px;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
        }

        .main-grid {
            display: grid;
            grid-template-columns: 82px minmax(0, 1fr) 360px;
            gap: 14px;
            align-items: start;
        }

        .side-nav {
            min-height: 840px;
            border-radius: 24px;
            background: var(--panel);
            border: 1px solid rgba(255,255,255,0.05);
            box-shadow: var(--shadow);
            padding: 12px 10px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .brand {
            width: 52px;
            height: 52px;
            margin: 0 auto 10px auto;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 23px;
            font-weight: 800;
            color: white;
            background: linear-gradient(135deg, rgba(29,36,62,1) 0%, rgba(76,29,149,1) 50%, rgba(139,92,246,1) 100%);
            box-shadow: 0 0 24px rgba(139,92,246,0.32);
        }

        .nav-stack {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-top: 10px;
        }

        .nav-item {
            width: 48px;
            height: 48px;
            margin: 0 auto;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #d7def3;
            background: rgba(255,255,255,0.025);
            border: 1px solid rgba(255,255,255,0.045);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.025);
            font-size: 20px;
        }

        .nav-item.active {
            background: linear-gradient(135deg, rgba(85,44,202,0.92), rgba(180,83,255,0.94));
            border: 1px solid rgba(210,170,255,0.26);
            box-shadow: 0 0 28px rgba(168,85,247,0.30);
        }

        .content-col {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .panel {
            background: var(--panel);
            border: 1px solid rgba(255,255,255,0.05);
            box-shadow: var(--shadow);
            border-radius: var(--radius-xl);
            padding: 18px 18px 16px 18px;
            position: relative;
            overflow: hidden;
        }

        .panel::before {
            content: "";
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at top right, rgba(168,85,247,0.10), transparent 28%);
            pointer-events: none;
        }

        .panel-soft {
            background: var(--panel-2);
        }

        .panel-title-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            margin-bottom: 10px;
        }

        .panel-title {
            font-size: 18px;
            font-weight: 700;
            color: var(--text);
            letter-spacing: 0.2px;
        }

        .panel-subtitle {
            color: var(--muted);
            font-size: 12px;
        }

        .badge-glow {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 10px;
            border-radius: 999px;
            border: 1px solid rgba(168,85,247,0.22);
            background: rgba(168,85,247,0.10);
            color: #efe7ff;
            font-size: 12px;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 14px;
        }

        .metric-card {
            background: linear-gradient(180deg, rgba(12,17,31,0.98), rgba(9,12,23,0.98));
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 22px;
            padding: 16px;
            position: relative;
            min-height: 130px;
            box-shadow: var(--shadow);
            overflow: hidden;
        }

        .metric-card.featured {
            background:
                radial-gradient(circle at 85% 20%, rgba(192,132,252,0.26), transparent 18%),
                linear-gradient(135deg, rgba(76,29,149,0.92), rgba(23,37,84,0.92));
            border: 1px solid rgba(216,180,254,0.18);
        }

        .metric-card::after {
            content: "";
            position: absolute;
            right: -20px;
            top: -20px;
            width: 110px;
            height: 110px;
            background: radial-gradient(circle, rgba(168,85,247,0.13), transparent 60%);
            pointer-events: none;
        }

        .metric-label {
            color: #cdd6ee;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 12px;
        }

        .metric-value {
            font-size: 40px;
            line-height: 1;
            font-weight: 800;
            letter-spacing: -1px;
            color: white;
            margin-bottom: 8px;
        }

        .metric-foot {
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: var(--muted);
            font-size: 12px;
        }

        .status-dots {
            display: flex;
            gap: 6px;
        }

        .status-dots span {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--green);
            box-shadow: 0 0 12px rgba(34,197,94,0.5);
            display: inline-block;
        }

        .two-col {
            display: grid;
            grid-template-columns: 1.05fr 1.15fr;
            gap: 14px;
        }

        .right-col {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .task-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .task-item {
            padding: 12px 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .task-item:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }

        .task-top {
            display: flex;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 6px;
            font-size: 14px;
            font-weight: 600;
        }

        .task-meta {
            color: var(--muted);
            font-size: 12px;
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .tiny-dot {
            display: inline-block;
            width: 9px;
            height: 9px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7c3aed, #a855f7);
            box-shadow: 0 0 10px rgba(168,85,247,0.45);
            margin-right: 8px;
        }

        .cta-btn {
            width: 100%;
            padding: 13px 16px;
            border-radius: 999px;
            background: linear-gradient(90deg, #6d28d9 0%, #a855f7 100%);
            color: white;
            text-align: center;
            font-weight: 700;
            margin-top: 16px;
            border: 1px solid rgba(255,255,255,0.06);
            box-shadow: 0 10px 30px rgba(109,40,217,0.28);
        }

        .ai-hero {
            background:
                radial-gradient(circle at 50% 0%, rgba(216,180,254,0.18), transparent 30%),
                linear-gradient(180deg, rgba(121,58,237,0.26), rgba(52,18,102,0.22)),
                linear-gradient(180deg, rgba(19,24,42,0.95), rgba(11,14,28,0.98));
            border: 1px solid rgba(216,180,254,0.14);
        }

        .ai-title {
            font-size: 32px;
            line-height: 1.1;
            font-weight: 800;
            margin: 8px 0 10px 0;
            text-align: center;
        }

        .ai-caption {
            text-align: center;
            color: var(--muted);
            font-size: 13px;
            margin-bottom: 14px;
        }

        .pill-row {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            justify-content: center;
            margin-bottom: 14px;
        }

        .pill {
            padding: 7px 10px;
            border-radius: 999px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.07);
            color: #ebe8ff;
            font-size: 12px;
        }

        .ai-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 12px;
            margin-top: 10px;
        }

        .ai-box {
            min-height: 120px;
            border-radius: 20px;
            background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
            border: 1px solid rgba(255,255,255,0.07);
            padding: 16px;
            display: flex;
            flex-direction: column;
            justify-content: end;
            color: #f5f3ff;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
        }

        .ai-box-title {
            font-size: 15px;
            font-weight: 700;
        }

        .prompt-bar {
            margin-top: 14px;
            height: 52px;
            border-radius: 999px;
            background: rgba(8,12,22,0.88);
            border: 1px solid rgba(168,85,247,0.25);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 10px 0 16px;
            color: var(--muted);
        }

        .send-btn {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7c3aed, #a855f7);
            box-shadow: 0 0 18px rgba(168,85,247,0.35);
        }

        .table-wrap table {
            width: 100%;
            border-collapse: collapse;
        }

        .table-wrap th {
            text-align: left;
            color: var(--muted);
            font-size: 12px;
            font-weight: 600;
            padding: 10px 8px 10px 0;
            border-bottom: 1px solid rgba(255,255,255,0.06);
        }

        .table-wrap td {
            font-size: 13px;
            color: #edf1ff;
            padding: 12px 8px 12px 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            vertical-align: top;
        }

        .name-main {
            font-weight: 700;
            margin-bottom: 2px;
        }

        .name-sub {
            color: var(--muted);
            font-size: 12px;
        }

        .status-chip {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 700;
            border: 1px solid rgba(255,255,255,0.06);
        }

        .status-running {
            background: rgba(34,197,94,0.12);
            color: #86efac;
        }

        .status-pending {
            background: rgba(245,158,11,0.12);
            color: #fcd34d;
        }

        .status-failed {
            background: rgba(251,113,133,0.12);
            color: #fda4af;
        }

        .status-completed {
            background: rgba(139,92,246,0.14);
            color: #d8b4fe;
        }

        .section-tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }

        .tab-chip {
            padding: 7px 12px;
            border-radius: 999px;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            color: var(--muted);
            font-size: 12px;
        }

        .tab-chip.active {
            color: white;
            border: 1px solid rgba(168,85,247,0.22);
            background: rgba(124,58,237,0.22);
            box-shadow: 0 0 18px rgba(124,58,237,0.18);
        }

        div[data-testid="stPlotlyChart"] {
            background: transparent !important;
        }

        .footer-note {
            color: var(--muted-2);
            font-size: 11px;
            margin-top: 10px;
        }

        @media (max-width: 1280px) {
            .main-grid {
                grid-template-columns: 72px minmax(0, 1fr);
            }
            .right-col {
                grid-column: 1 / -1;
            }
        }

        @media (max-width: 980px) {
            .metrics-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
            .two-col {
                grid-template-columns: 1fr;
            }
            .main-grid {
                grid-template-columns: 1fr;
            }
            .side-nav {
                min-height: auto;
                flex-direction: row;
                align-items: center;
                padding: 10px;
            }
            .nav-stack {
                flex-direction: row;
                margin-top: 0;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )