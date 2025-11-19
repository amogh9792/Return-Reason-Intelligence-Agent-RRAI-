import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon_bestsellers():
    url = "https://www.amazon.in/gp/bestsellers/sports/"
    response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.select(".zg-item-immersion")
    names, prices, ratings = [], [], []

    for p in products[:15]:
        name = p.select_one(".p13n-sc-truncated")
        price = p.select_one(".p13n-sc-price")
        rating = p.select_one(".a-icon-alt")

        names.append(name.text.strip() if name else "Unknown")
        prices.append(prices.text.strip() if prices else "N/A")
        ratings.append(rating.text.strip() if rating else "N/A")

    df = pd.DataFrame({
        "name": names,
        "price": prices,
        "rating": ratings
    })

    return df