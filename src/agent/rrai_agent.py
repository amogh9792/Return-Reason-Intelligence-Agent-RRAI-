# ==========================
# RRAI Agentic AI Module
# ==========================

import json

# --------------------------
# 1. Input Data
# --------------------------

# Trend scores from Google Trends or scraped data
trend_data = {
    "Yoga Mat": 64,
    "Dumbbell": 37,
    "Skipping Rope": 50,
    "Shaker Bottle": 50
}

# Boldfit current inventory
boldfit_inventory = ["Yoga Mat", "Dumbbell", "Shaker Bottle"]

# Complementary mapping (helps rank suggestions)
complementary_map = {
    "Yoga Mat": 1.0,
    "Dumbbell": 0.8,
    "Skipping Rope": 0.9,
    "Shaker Bottle": 0.7,
    "Resistance Bands": 0.9,
    "Exercise Ball": 1.0,
    "Jump Rope": 0.95
}

# Suggested new products for recommendation
potential_products = ["Jump Rope", "Resistance Bands", "Exercise Ball"]

# Trend score for new products (can be estimated or scraped)
trend_estimates = {
    "Jump Rope": 50,
    "Resistance Bands": 40,
    "Exercise Ball": 55
}

# --------------------------
# 2. Gap Analysis
# --------------------------

def identify_gaps(trending_products, inventory):
    """Find trending products not yet in inventory"""
    gaps = [p for p in trending_products if p not in inventory]
    return gaps

trending_products = list(trend_data.keys()) + potential_products
product_gaps = identify_gaps(trending_products, boldfit_inventory)

# --------------------------
# 3. Scoring & Prioritization
# --------------------------

def calculate_priority_score(product):
    """Score = trend_score * complementary_factor"""
    score = 0
    if product in trend_data:
        score = trend_data[product] * complementary_map.get(product, 0.8)
    elif product in trend_estimates:
        score = trend_estimates[product] * complementary_map.get(product, 0.8)
    return score

ranked_products = sorted(product_gaps, key=lambda x: calculate_priority_score(x), reverse=True)

# --------------------------
# 4. Strategic Recommendations
# --------------------------

strategy_map = {
    "Yoga Mat": "Launch premium eco-friendly mats with instructional guides; high ROI expected.",
    "Dumbbell": "Introduce adjustable sets or combos for home strength training.",
    "Skipping Rope": "Bundle with beginner cardio guide; portable & affordable.",
    "Shaker Bottle": "Market as part of nutrition & fitness bundle.",
    "Jump Rope": "Focus on cardio trend; lightweight, portable, and easy to bundle.",
    "Resistance Bands": "Promote for home workouts; offer tiered resistance sets.",
    "Exercise Ball": "Supports yoga/core training; launch with instructional videos."
}

agentic_report = []

for rank, product in enumerate(ranked_products, start=1):
    agentic_report.append({
        "Rank": rank,
        "Product": product,
        "Trend Score": trend_data.get(product, trend_estimates.get(product, 0)),
        "Priority Score": round(calculate_priority_score(product), 2),
        "Recommendation": strategy_map.get(product, "Explore product launch opportunities.")
    })

# --------------------------
# 5. Output Report
# --------------------------

print("\n=== RRAI Agentic Recommendations ===\n")
for item in agentic_report:
    print(f"Rank {item['Rank']}: {item['Product']}")
    print(f"  Trend Score: {item['Trend Score']}")
    print(f"  Priority Score: {item['Priority Score']}")
    print(f"  Recommendation: {item['Recommendation']}\n")

# Optional: save to JSON
with open("rrai_agentic_report.json", "w") as f:
    json.dump(agentic_report, f, indent=4)

print("Agentic report saved as 'rrai_agentic_report.json'")
