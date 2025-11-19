import ollama

def recommend_products(df):
    items = (
        df[['keyword', 'trend_score']]
        .dropna()
        .to_string(index=False)
    )

    prompt = f"""
Using ONLY this trend data:
{items}

Suggest 3 NEW Boldfit products.
Keep them simple and realistic.
Do NOT invent smart gadgets, Bluetooth, LED ropes etc.
Base suggestions ONLY on interest level.
"""

    res = ollama.generate(model="llama3.1", prompt=prompt)
    return res["response"]
