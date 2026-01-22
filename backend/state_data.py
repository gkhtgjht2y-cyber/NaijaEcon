import pandas as pd
import requests

# -------- STATE INFLATION (NBS / World Bank Proxy) --------

def get_state_inflation():
    # Simple proxy dataset (replace later with NBS CSV if needed)
    url = "https://raw.githubusercontent.com/datasets/inflation/master/data/countries.csv"
    df = pd.read_csv(url)

    nigeria = df[df["Country"] == "Nigeria"].tail(1)

    # Example state-level split (NBS-style weighting)
    states = [
        "Lagos", "Abuja", "Rivers", "Kano", "Oyo",
        "Kaduna", "Ogun", "Anambra", "Delta", "Edo"
    ]

    inflation = float(nigeria["Inflation"].values[0])

    return [
        {"state": s, "inflation": round(inflation * (0.95 + i*0.01), 2)}
        for i, s in enumerate(states)
    ]


# -------- STATE GDP (STATIC ESTIMATES) --------

def get_state_gdp():
    # Cached estimates (USD billions)
    return [
        {"state": "Lagos", "gdp": 135},
        {"state": "Rivers", "gdp": 21},
        {"state": "Abuja", "gdp": 20},
        {"state": "Delta", "gdp": 16},
        {"state": "Ogun", "gdp": 14},
        {"state": "Oyo", "gdp": 13},
        {"state": "Kano", "gdp": 12},
        {"state": "Kaduna", "gdp": 10},
        {"state": "Anambra", "gdp": 9},
        {"state": "Edo", "gdp": 8}
    ]
