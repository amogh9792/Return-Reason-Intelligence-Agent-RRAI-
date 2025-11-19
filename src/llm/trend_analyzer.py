import ollama

def analyze_trends(df):
    # Only keyword + trend_score
    items = (
        df[['keyword', 'trend_score']]
        .dropna()
        .to_string(index=False)
    )

    prompt = f"""
You are a fitness market analyst for Boldfit.

Using ONLY this data:
{items}

Create a clean summary with:a
- 3 trend insights (based only on trend_score)
Avoid hallucinations. Do not invent brands or features.
"""

    res = ollama.generate(model="llama3.1", prompt=prompt)
    return res["response"]
