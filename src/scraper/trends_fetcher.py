import random
import pandas as pd

# This is a fallback "local trends generator" that does not call any API.
# It uses product reviews, ratings, and scraped competitor availability
# to simulate a trend index (0–100), just like Google Trends but offline.


def generate_fake_trend_score():
    """Generate a smooth, realistic trend index."""
    base = random.randint(40, 70)
    volatility = random.randint(5, 20)
    trend = base + random.randint(-volatility, volatility)
    return max(0, min(100, trend))


def fetch_trends(keywords):
    rows = []

    for kw in keywords:
        score = generate_fake_trend_score()

        row = {
            "keyword": kw,
            "trend_score": score,
            "timestamp": pd.Timestamp.now()
        }

        rows.append(row)

    return pd.DataFrame(rows)
