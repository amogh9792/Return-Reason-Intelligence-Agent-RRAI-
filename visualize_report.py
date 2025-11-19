# visualize_report.py
import os
import matplotlib.pyplot as plt
import seaborn as sns

# ===========================
# Example data from your report
# Replace this with actual outputs from main.py
# ===========================
trend_insights = [
    {"Product": "Dumbbells", "Trend Score": 50, "Insight": "Stable interest"},
    {"Product": "Yoga Mat", "Trend Score": 44, "Insight": "Declining interest"},
    {"Product": "Skipping Rope", "Trend Score": 50, "Insight": "Stable interest"},
    {"Product": "Shaker Bottles", "Trend Score": 50, "Insight": "Stable interest"},
]

comp_insights = [
    {"Product": "Dumbbells", "Trend Score": 50, "Gap Description": "Opportunity to improve or differentiate product", "Demand Level": "Moderate"},
    {"Product": "Yoga Mat", "Trend Score": 44, "Gap Description": "Opportunity to improve or differentiate product", "Demand Level": "Low"},
    {"Product": "Skipping Rope", "Trend Score": 50, "Gap Description": "Opportunity to improve or differentiate product", "Demand Level": "Moderate"},
    {"Product": "Shaker Bottles", "Trend Score": 50, "Gap Description": "Opportunity to improve or differentiate product", "Demand Level": "Moderate"},
]

recos = [
    {"Product": "Dumbbells", "Trend Score": 50, "Priority Score": 50.0, "Recommendation": "Launch premium adjustable sets, combo packs, or smart weights.", "Demand Level": "Moderate"},
    {"Product": "Jump Rope", "Trend Score": 50, "Priority Score": 47.5, "Recommendation": "Cardio trend; lightweight and portable.", "Demand Level": "Moderate"},
    {"Product": "Shaker Bottles", "Trend Score": 50, "Priority Score": 45.0, "Recommendation": "Bundle with protein powders; highlight premium design.", "Demand Level": "Moderate"},
    {"Product": "Resistance Bands", "Trend Score": 50, "Priority Score": 45.0, "Recommendation": "Portable home workout solution; tiered resistance sets.", "Demand Level": "Moderate"},
    {"Product": "Yoga Blocks", "Trend Score": 50, "Priority Score": 42.5, "Recommendation": "Support flexibility and yoga poses; useful accessory.", "Demand Level": "Moderate"},
    {"Product": "Yoga Mat", "Trend Score": 44, "Priority Score": 35.2, "Recommendation": "Eco-friendly, travel-friendly, or alignment-focused mats.", "Demand Level": "Low"},
    {"Product": "Skipping Rope", "Trend Score": 50, "Priority Score": 35.0, "Recommendation": "Innovative ropes (weighted/digital tracking) to differentiate.", "Demand Level": "Moderate"},
]

# Create output folder
os.makedirs("outputs", exist_ok=True)

# ===========================
# 1️⃣ Trend Insights Bar Chart
# ===========================
products = [item['Product'] for item in trend_insights]
scores = [item['Trend Score'] for item in trend_insights]
colors = ['green' if s >= 60 else 'orange' if s >= 50 else 'red' for s in scores]

plt.figure(figsize=(8,5))
plt.bar(products, scores, color=colors)
plt.title("Trend Insights - Product Popularity")
plt.ylabel("Trend Score")
plt.ylim(0,100)
for i, score in enumerate(scores):
    plt.text(i, score+1, str(score), ha='center')
plt.savefig("outputs/trend_insights.png", bbox_inches='tight')
plt.close()

# ===========================
# 2️⃣ Competitor Gap - Demand Levels
# ===========================
demand_colors = {'High': 'green', 'Moderate': 'orange', 'Low': 'red'}
products = [item['Product'] for item in comp_insights]
levels = [item['Demand Level'] for item in comp_insights]
colors = [demand_colors[level] for level in levels]

plt.figure(figsize=(8,5))
plt.bar(products, [1]*len(products), color=colors)
plt.title("Competitor Gap - Demand Levels")
plt.xticks(rotation=15)
plt.savefig("outputs/competitor_gaps.png", bbox_inches='tight')
plt.close()

# ===========================
# 3️⃣ Product Recommendations - Priority Scores
# ===========================
products = [item['Product'] for item in recos]
priority = [item['Priority Score'] for item in recos]

plt.figure(figsize=(10,6))
plt.barh(products[::-1], priority[::-1], color='skyblue')
plt.xlabel("Priority Score")
plt.title("Product Recommendations Ranked by Priority Score")
for i, val in enumerate(priority[::-1]):
    plt.text(val+0.5, i, str(val), va='center')
plt.savefig("outputs/product_recommendations.png", bbox_inches='tight')
plt.close()

# ===========================
# 4️⃣ Heatmap - Trend Score + Priority
# ===========================
import pandas as pd
df = pd.DataFrame(recos)
df = df[['Product', 'Trend Score', 'Priority Score']]
df.set_index('Product', inplace=True)

plt.figure(figsize=(8,6))
sns.heatmap(df, annot=True, cmap='YlGnBu', fmt=".1f")
plt.title("Agentic Product Dashboard")
plt.savefig("outputs/product_dashboard_heatmap.png", bbox_inches='tight')
plt.close()

print("✅ Visualizations saved in outputs/ folder!")
