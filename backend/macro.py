import requests

def fetch_national_macro():
    url = "https://api.worldbank.org/v2/country/NGA/indicator/FP.CPI.TOTL.ZG?format=json"
    data = requests.get(url).json()[1][0]

    return {
        "inflation": data["value"],
        "year": data["date"]
    }
