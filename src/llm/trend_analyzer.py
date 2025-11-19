# src/llm/trend_analyzer.py

def analyze_trends(merged_df):
    trend_insights = []

    products = ["dumbbells", "yoga mat", "skipping rope", "shaker bottles"]

    for product in products:
        product_lower = product.lower()

        # Filter merged_df by keyword
        product_rows = merged_df[merged_df['keyword'] == product_lower]

        if not product_rows.empty:
            # Take mean trend_score if multiple rows
            trend_score = int(product_rows['trend_score'].mean())
        else:
            trend_score = 50  # default estimate

        # Insight based on trend score
        if trend_score >= 60:
            insight = "Strong and rising interest"
        elif trend_score >= 50:
            insight = "Stable interest"
        else:
            insight = "Declining interest"

        trend_insights.append({
            "Product": product.title(),
            "Trend Score": trend_score,
            "Insight": insight
        })

    return trend_insights
