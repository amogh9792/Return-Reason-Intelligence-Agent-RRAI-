# src/llm/competitor_insight.py

def competitor_gap(merged_df):
    comp_insights = []

    products = ["dumbbells", "yoga mat", "skipping rope", "shaker bottles"]

    for product in products:
        product_lower = product.lower()
        product_rows = merged_df[merged_df['keyword'] == product_lower]

        if not product_rows.empty:
            trend_score = int(product_rows['trend_score'].mean())
        else:
            trend_score = 50

        if trend_score >= 60:
            demand_level = "High"
        elif trend_score >= 50:
            demand_level = "Moderate"
        else:
            demand_level = "Low"

        gap_description = (
            "Opportunity to improve or differentiate product"
            if demand_level != "High"
            else "Strong demand, maintain market share"
        )

        comp_insights.append({
            "Product": product.title(),
            "Trend Score": trend_score,
            "Gap Description": gap_description,
            "Demand Level": demand_level
        })

    return comp_insights
