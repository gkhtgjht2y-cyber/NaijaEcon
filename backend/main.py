from fastapi import FastAPI

from exchange import fetch_exchange_rate
from macro import fetch_national_macro
from state_inflation import get_state_inflation
from state_gdp_news import fetch_state_gdp
from outlook import generate_outlook

app = FastAPI()

@app.get("/api/dashboard")
def dashboard():
    exchange = fetch_exchange_rate()
    macro = fetch_national_macro()

    return {
        "exchange_rate": exchange,
        "national_macro": macro,
        "state_inflation": get_state_inflation(),
        "state_gdp": fetch_state_gdp(),
        "outlook": generate_outlook(
            exchange["rate"],
            macro["inflation"]
        )
    }
