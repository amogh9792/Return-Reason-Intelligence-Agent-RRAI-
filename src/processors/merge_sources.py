import pandas as pd
from datetime import datetime

def merge_sources(flipkart_df, competitors_df, trends_df):
    # Make sure empty inputs don't break the merge
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

    # These are the only columns your LLM needs
    required_cols = [
        "keyword",       # product keyword (yoga mat, dumbbell…)
        "price",         # flipkart or competitor price
        "comp_name",     # competitor name if available
        "trend_score",   # latest interest/trend data
        "source"         # where the row came from
    ]

    # Standardize each dataset to use the same columns
    def normalize(df):
        for col in required_cols:
            if col not in df.columns:
                df[col] = None
        return df[required_cols]

    flipkart_df = normalize(flipkart_df)
    competitors_df = normalize(competitors_df)
    trends_df = normalize(trends_df)

    # Convert trend score into a proper number
    trends_df["trend_score"] = pd.to_numeric(
        trends_df["trend_score"], errors="coerce"
    ).fillna(0)

    # Merge all rows together
    merged = pd.concat(
        [flipkart_df, competitors_df, trends_df],
        ignore_index=True
    )

    # Add timestamp
    merged["merged_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return merged
