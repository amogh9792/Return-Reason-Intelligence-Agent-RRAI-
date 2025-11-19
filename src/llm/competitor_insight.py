import ollama

def competitor_gap(df):
    items = (
        df[['keyword', 'trend_score']]
        .dropna()
        .to_string(index=False)
    )

    prompt = f"""
Using ONLY this trend data:
{items}

Find:
- What categories have high demand
- What Boldfit could improve or launch
No imaginary features, no fake data.
"""

    res = ollama.generate(model="llama3.1", prompt=prompt)
    return res["response"]
