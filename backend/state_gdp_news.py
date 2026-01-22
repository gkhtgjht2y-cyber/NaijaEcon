import requests
import re
import os

STATES = [
    "Lagos", "Rivers", "Ogun", "Oyo",
    "Kano", "Kaduna", "Delta", "Edo"
]

def extract_gdp(text):
    match = re.search(r'GDP[^0-9]{0,15}([\$₦]?[0-9,.]+)', text)
    return match.group(1) if match else None

def fetch_state_gdp():
    api_key = os.environ.get("GNEWS_KEY")
    results = []

    for state in STATES:
        query = f"{state} State GDP"
        url = f"https://gnews.io/api/v4/search?q={query}&lang=en&max=1&token={api_key}"

        data = requests.get(url).json()
        articles = data.get("articles", [])

        if articles:
            article = articles[0]
            gdp = extract_gdp(article.get("content", ""))
            source = article["source"]["name"]
        else:
            gdp = "Updating"
            source = "Pending"

        results.append({
            "state": state,
            "gdp": gdp,
            "source": source
        })

    return results
