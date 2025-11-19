import re

def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]", "", text)
    return text