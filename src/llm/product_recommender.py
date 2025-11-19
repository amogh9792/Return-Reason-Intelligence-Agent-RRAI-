# src/llm/product_recommender.py

def recommend_products(merged_df):
    complementary_map = {
        "dumbbells": 1.0,
        "shaker bottles": 0.9,
        "yoga mat": 0.8,
        "skipping rope": 0.7,
        "resistance bands": 0.9,
        "jump rope": 0.95,
        "yoga blocks": 0.85
    }

    strategy_map = {
        "dumbbells": "Launch premium adjustable sets, combo packs, or smart weights.",
        "shaker bottles": "Bundle with protein powders; highlight premium design.",
        "yoga mat": "Eco-friendly, travel-friendly, or alignment-focused mats.",
        "skipping rope": "Innovative ropes (weighted/digital tracking) to differentiate.",
        "resistance bands": "Portable home workout solution; tiered resistance sets.",
        "jump rope": "Cardio trend; lightweight and portable.",
        "yoga blocks": "Support flexibility and yoga poses; useful accessory."
    }

    recos = []

    for product, weight in complementary_map.items():
        product_lower = product.lower()
        product_rows = merged_df[merged_df['keyword'] == product_lower]

        if not product_rows.empty:
            trend_score = int(product_rows['trend_score'].mean())
        else:
            trend_score = 50

        priority_score = trend_score * weight

        if trend_score >= 60:
            demand_level = "High"
        elif trend_score >= 50:
            demand_level = "Moderate"
        else:
            demand_level = "Low"

        recos.append({
            "Product": product.title(),
            "Trend Score": trend_score,
            "Priority Score": round(priority_score, 2),
            "Recommendation": strategy_map[product],
            "Demand Level": demand_level
        })

    # Sort by priority score descending
    recos = sorted(recos, key=lambda x: x["Priority Score"], reverse=True)

    return recos
