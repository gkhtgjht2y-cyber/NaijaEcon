import os
import requests

def fetch_exchange_rate():
    api_key = os.environ.get('EXCHANGE_RATE_KEY')
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/NGN"
    
    response = requests.get(url).json()
    return {
        "rate": response.get('conversion_rate'),
        "last_update": response.get('time_last_update_utc')
    }
