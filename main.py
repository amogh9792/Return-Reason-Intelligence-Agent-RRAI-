import os
import pandas as pd

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

    logger.info("STEP 1 → Scraping Flipkart bestsellers...")
    flipkart = scrape_flipkart()
    logger.info(f"Flipkart rows: {0 if flipkart is None else len(flipkart)}")

    logger.info("STEP 2 → Scraping competitor (Decathlon)...")
    competitors = scrape_decathlon()
    logger.info(f"Competitor rows: {0 if competitors is None else len(competitors)}")

    logger.info("STEP 3 → Fetching Google Trends...")
    keywords = ["yoga mat", "dumbbell", "shaker", "skipping rope"]
    trends = fetch_trends(keywords)
    logger.info(f"Trend rows: {0 if trends is None else len(trends)}")

    logger.info("STEP 4 → Merging datasets...")
    merged = merge_sources(flipkart, competitors, trends)
    os.makedirs("data/processed", exist_ok=True)
    merged.to_csv(output_file, index=False)
    logger.info(f"Merged dataset saved: {output_file}")

    logger.info("STEP 5 → LLM: trend analysis...")
    trend_insights = analyze_trends(merged)

    logger.info("STEP 6 → LLM: competitor gap analysis...")
    comp_insights = competitor_gap(merged)

    logger.info("STEP 7 → LLM: product recommendations...")
    recos = recommend_products(merged)

    logger.info("STEP 8 → Writing final report...")

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/weekly_report.txt", "w", encoding="utf-8") as f:
        f.write("=== TREND INSIGHTS ===\n")
        f.write(trend_insights)
        f.write("\n\n=== COMPETITOR GAPS ===\n")
        f.write(comp_insights)
        f.write("\n\n=== PRODUCT RECOMMENDATIONS ===\n")
        f.write(recos)

    logger.info("AGENT RUN COMPLETE → Report generated: outputs/weekly_report.txt")


if __name__ == "__main__":
    run_agent()
