import pandas as pd

def merge_sources(df1, df2, df3):
    df1["source"] = "amazon"
    df2["source"] = "decathlon"
    df3["source"] = "trends"

    return pd.concat([df1, df2, df3], ignore_index=True)