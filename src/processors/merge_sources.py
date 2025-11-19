# src/processors/merge_sources.py

import pandas as pd
from datetime import datetime

def merge_sources(flipkart_df, competitors_df, trends_df):
    # Ensure input DataFrames
    flipkart_df = flipkart_df if isinstance(flipkart_df, pd.DataFrame) else pd.DataFrame()
    competitors_df = competitors_df if isinstance(competitors_df, pd.DataFrame) else pd.DataFrame()
    trends_df = trends_df if isinstance(trends_df, pd.DataFrame) else pd.DataFrame()

    # Add source labels
    if not flipkart_df.empty:
        flipkart_df["source"] = "flipkart"
    if not competitors_df.empty:
        competitors_df["source"] = "competitor"
    if not trends_df.empty:
        trends_df["source"] = "trends"

    # Required columns for LLM
    required_cols = ["keyword", "price", "comp_name", "trend_score", "source"]

    # Normalize each dataset
    def normalize(df):
        for col in required_cols:
            if col not in df.columns:
                df[col] = None
        return df[required_cols]

    flipkart_df = normalize(flipkart_df)
    competitors_df = normalize(competitors_df)
    trends_df = normalize(trends_df)

    # Convert trend_score to numeric
    trends_df["trend_score"] = pd.to_numeric(trends_df["trend_score"], errors="coerce").fillna(0)

    # Merge datasets
    merged = pd.concat([flipkart_df, competitors_df, trends_df], ignore_index=True)

    # Normalize keywords to lowercase for consistency
    merged["keyword"] = merged["keyword"].astype(str).str.strip().str.lower()

    # Add timestamp
    merged["merged_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return merged
