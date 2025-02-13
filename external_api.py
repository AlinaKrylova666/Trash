import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')

def get_exchange_rate(from_currency, to_currency='RUB'):
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={from_currency}&symbols={to_currency}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['rates'][to_currency]
