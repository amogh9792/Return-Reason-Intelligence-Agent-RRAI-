from pytrends.request import TrendReq
import pandas as pd

def fetch_trends(keywords):
    pytrends = TrendReq(hl='en-IN', tz=330)
    pytrends.build_payload(keywords, timeframe = 'today 3-m')

    data = pytrends.interest_over_time()
    data = data.reset_index()

    latest = data.iloc[-1].to_dict()
    return pd.DataFrame([latest])