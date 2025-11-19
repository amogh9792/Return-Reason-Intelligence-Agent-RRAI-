import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time


def scrape_flipkart(keyword="yoga mat", pages=1):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    base_url = "https://www.flipkart.com/search?q=" + keyword.replace(" ", "%20")

    products = []

    for page in range(1, pages + 1):
        url = base_url + f"&page={page}"

        time.sleep(random.uniform(1.5, 3.0))

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Flipkart product containers
        items = soup.find_all("div", {"class": "_1AtVbE"})

        for item in items:
            name_tag = item.find("div", {"class": "_4rR01T"})
            if not name_tag:
                continue

            name = name_tag.text.strip()

            price_tag = item.find("div", {"class": "_30jeq3 _1_WHN1"})
            price = price_tag.text.replace("₹", "").replace(",", "").strip() if price_tag else None

            rating_tag = item.find("div", {"class": "_3LWZlK"})
            rating = rating_tag.text.strip() if rating_tag else None

            products.append({
                "name": name,
                "price": price,
                "rating": rating,
                "keyword": keyword,
                "source": "flipkart"
            })

    return pd.DataFrame(products)
