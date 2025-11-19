import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_decathlon():
    url = "https://www.decathlon.in/sports/fitness"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.select(".product-card")
    names, prices = [], []

    for c in cards[:15]:
        name = c.select_one(".product-card-name")
        price = c.select_one(".product-card-price")

        names.append(name.text.strip() if name else "Unknown")
        prices.append(price.text.strip() if price else "N/A")

    return pd.DataFrame({"comp_name": names, "comp_price": prices})