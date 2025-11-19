# main.py

import os
import pandas as pd
import json

from src.scraper.flipkart_scraper import scrape_flipkart
from src.scraper.competitor_scraper import scrape_decathlon
from src.scraper.trends_fetcher import fetch_trends
from src.processors.merge_sources import merge_sources
from src.llm.trend_analyzer import analyze_trends
from src.llm.competitor_insight import competitor_gap
from src.llm.product_recommender import recommend_products
from src.utils.logger import get_logger

logger = get_logger()


def run_agent():
    # Clean previous output
    output_file = "data/processed/merged_dataset.csv"
    if os.path.exists(output_file):
        os.remove(output_file)

    # STEP 1 → Scrape Flipkart
    flipkart = scrape_flipkart()
    logger.info(f"Flipkart rows: {0 if flipkart is None else len(flipkart)}")

    # STEP 2 → Scrape competitors
    competitors = scrape_decathlon()
    logger.info(f"Competitor rows: {0 if competitors is None else len(competitors)}")

    # STEP 3 → Fetch trends
    keywords = ["yoga mat", "dumbbell", "shaker", "skipping rope"]
    trends = fetch_trends(keywords)
    logger.info(f"Trend rows: {0 if trends is None else len(trends)}")

    # STEP 4 → Merge datasets
    merged = merge_sources(flipkart, competitors, trends)
    os.makedirs("data/processed", exist_ok=True)
    merged.to_csv(output_file, index=False)
    logger.info(f"Merged dataset saved: {output_file}")

    # STEP 5 → Trend analysis
    trend_insights = analyze_trends(merged)

    # STEP 6 → Competitor gap
    comp_insights = competitor_gap(merged)

    # STEP 7 → Product recommendations
    recos = recommend_products(merged)

    # STEP 8 → Write fully agentic report
    os.makedirs("outputs", exist_ok=True)
    report_txt = "outputs/weekly_report.txt"
    with open(report_txt, "w", encoding="utf-8") as f:
        f.write("=== FULLY AGENTIC TREND INSIGHTS ===\n")
        for item in trend_insights:
            f.write(f"{item['Product']} - Trend Score: {item['Trend Score']} | Insight: {item['Insight']}\n")

        f.write("\n=== FULLY AGENTIC COMPETITOR GAPS ===\n")
        for item in comp_insights:
            f.write(f"{item['Product']} - Gap: {item['Gap Description']} | Demand: {item['Demand Level']}\n")

        f.write("\n=== FULLY AGENTIC PRODUCT RECOMMENDATIONS ===\n")
        for idx, item in enumerate(recos, 1):
            f.write(f"Rank {idx}: {item['Product']}\n")
            f.write(f"  Trend Score: {item['Trend Score']}\n")
            f.write(f"  Priority Score: {item['Priority Score']}\n")
            f.write(f"  Recommendation: {item['Recommendation']}\n")
            f.write(f"  Demand Level: {item['Demand Level']}\n\n")

    # Save JSON for dashboards or future use
    with open("outputs/weekly_report.json", "w", encoding="utf-8") as f:
        json.dump({
            "trend_insights": trend_insights,
            "competitor_gaps": comp_insights,
            "product_recommendations": recos
        }, f, indent=4)

    logger.info(f"AGENT RUN COMPLETE → Reports generated: {report_txt} + JSON")


if __name__ == "__main__":
    run_agent()
