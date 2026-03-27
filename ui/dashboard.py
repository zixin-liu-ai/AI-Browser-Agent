import requests
import pandas as pd
import streamlit as st


API_BASE = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Browser Agent Dashboard",
    page_icon="🤖",
    layout="wide"
)


def fetch_data(endpoint: str):
    try:
        response = requests.get(f"{API_BASE}{endpoint}", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Failed to fetch data from {endpoint}: {e}")
        return None


def get_top_author(report: dict) -> str:
    authors = report.get("top_10_authors", [])
    if not authors:
        return "N/A"
    return f"{authors[0][0]} ({authors[0][1]})"


def get_top_tag(report: dict) -> str:
    tags = report.get("top_10_tags", [])
    if not tags:
        return "N/A"
    return f"{tags[0][0]} ({tags[0][1]})"


def get_top_ai_theme(report: dict) -> str:
    themes = report.get("top_10_ai_themes", [])
    if not themes:
        return "N/A"
    return f"{themes[0][0]} ({themes[0][1]})"


def build_quotes_dataframe(quotes_data: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(quotes_data)

    if "tags" in df.columns:
        df["tags_display"] = df["tags"].apply(
            lambda x: ", ".join(x) if isinstance(x, list) else ""
        )
    else:
        df["tags_display"] = ""

    for col in ["ai_theme", "ai_sentiment", "ai_tone", "ai_summary"]:
        if col not in df.columns:
            df[col] = ""

    return df


def main():
    st.title("🤖 AI Browser Agent Dashboard")
    st.caption("Browser automation + structured crawling + AI-enhanced analysis")

    quotes_data = fetch_data("/quotes")
    report_data = fetch_data("/analysis")

    if quotes_data is None or report_data is None:
        st.warning("⚠️ Please make sure FastAPI is running at http://127.0.0.1:8000")
        return

    df = build_quotes_dataframe(quotes_data)

    total_quotes = report_data.get("total_quotes", 0)
    total_pages = len(report_data.get("quotes_per_page", {}))
    top_author = get_top_author(report_data)
    top_tag = get_top_tag(report_data)
    top_ai_theme = get_top_ai_theme(report_data)

    st.subheader("📊 Overview")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Quotes", total_quotes)
    c2.metric("Total Pages", total_pages)
    c3.metric("Top Author", top_author)
    c4.metric("Top Tag", top_tag)
    c5.metric("Top AI Theme", top_ai_theme)

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("🏆 Top Authors")
        author_data = report_data.get("top_10_authors", [])
        if author_data:
            author_df = pd.DataFrame(author_data, columns=["Author", "Count"])
            st.bar_chart(author_df.set_index("Author"))
            st.dataframe(author_df, use_container_width=True)
        else:
            st.info("No author statistics found.")

    with right:
        st.subheader("🏷️ Top Tags")
        tag_data = report_data.get("top_10_tags", [])
        if tag_data:
            tag_df = pd.DataFrame(tag_data, columns=["Tag", "Count"])
            st.bar_chart(tag_df.set_index("Tag"))
            st.dataframe(tag_df, use_container_width=True)
        else:
            st.info("No tag statistics found.")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("🧠 Top AI Themes")
        theme_data = report_data.get("top_10_ai_themes", [])
        if theme_data:
            theme_df = pd.DataFrame(theme_data, columns=["AI Theme", "Count"])
            st.bar_chart(theme_df.set_index("AI Theme"))
            st.dataframe(theme_df, use_container_width=True)
        else:
            st.info("No AI theme statistics found.")

    with right:
        st.subheader("😊 Sentiment Distribution")
        sentiment_data = report_data.get("sentiment_distribution", {})
        if sentiment_data:
            sentiment_df = pd.DataFrame(
                [{"Sentiment": k, "Count": v} for k, v in sentiment_data.items()]
            )
            st.bar_chart(sentiment_df.set_index("Sentiment"))
            st.dataframe(sentiment_df, use_container_width=True)
        else:
            st.info("No sentiment statistics found.")

    st.divider()

    st.subheader("📑 Quotes Per Page")
    page_data = report_data.get("quotes_per_page", {})
    if page_data:
        page_df = pd.DataFrame(
            [{"Page": int(k), "Count": v} for k, v in page_data.items()]
        ).sort_values("Page")
        st.line_chart(page_df.set_index("Page"))
        st.dataframe(page_df, use_container_width=True)
    else:
        st.info("No page distribution found.")

    st.divider()

    st.subheader("🔎 Search & Filter Quotes")

    authors = sorted(df["author"].dropna().unique().tolist()) if "author" in df.columns else []
    sentiments = sorted(df["ai_sentiment"].dropna().unique().tolist()) if "ai_sentiment" in df.columns else []

    col1, col2 = st.columns(2)
    with col1:
        selected_author = st.selectbox("Filter by Author", ["All"] + authors)
    with col2:
        selected_sentiment = st.selectbox("Filter by AI Sentiment", ["All"] + sentiments)

    search_text = st.text_input("Search in Quote Text")
    search_tag = st.text_input("Search in Tags / AI Theme")

    filtered_df = df.copy()

    if selected_author != "All":
        filtered_df = filtered_df[filtered_df["author"] == selected_author]

    if selected_sentiment != "All":
        filtered_df = filtered_df[filtered_df["ai_sentiment"] == selected_sentiment]

    if search_text.strip():
        filtered_df = filtered_df[
            filtered_df["text"].str.contains(search_text, case=False, na=False)
        ]

    if search_tag.strip():
        filtered_df = filtered_df[
            filtered_df["tags_display"].str.contains(search_tag, case=False, na=False)
            | filtered_df["ai_theme"].str.contains(search_tag, case=False, na=False)
        ]

    display_df = filtered_df[
        ["page", "author", "text", "tags_display", "ai_theme", "ai_sentiment", "ai_tone", "ai_summary"]
    ].rename(
        columns={
            "page": "Page",
            "author": "Author",
            "text": "Quote",
            "tags_display": "Tags",
            "ai_theme": "AI Theme",
            "ai_sentiment": "AI Sentiment",
            "ai_tone": "AI Tone",
            "ai_summary": "AI Summary",
        }
    )

    st.dataframe(display_df, use_container_width=True, height=500)

    st.divider()

    st.subheader("📡 API Status")
    st.success("✅ Connected to FastAPI backend")
    st.write(f"Quotes endpoint: {API_BASE}/quotes")
    st.write(f"Analysis endpoint: {API_BASE}/analysis")


if __name__ == "__main__":
    main()