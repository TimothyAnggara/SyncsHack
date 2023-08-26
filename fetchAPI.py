import requests
import json

API_KEY = "GBEXJPOTUHCC9FZC" #Alpha Vantage
symbol = "AAPL"

def fetchDataMonthly(SYMBOL):
    API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={SYMBOL}&apikey={API_KEY}"
    r = requests.get(API_URL).json()
    return r

def fetchDataWeekly(SYMBOL):
    API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={SYMBOL}&apikey={API_KEY}"
    r = requests.get(API_URL).json()
    return r

def fetchDataDaily(SYMBOL):
    API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&apikey={API_KEY}"
    r = requests.get(API_URL).json()
    return r



API_URL_DAILY = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
API_URL_WEEKLY = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&apikey={API_KEY}"
API_URL_MONTHLY = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey={API_KEY}"

daily_data = requests.get(API_URL_DAILY).json()
weekly_data = requests.get(API_URL_WEEKLY).json()
monthly_data = requests.get(API_URL_MONTHLY).json()

combined_data = {
    "daily": daily_data,
    "weekly": weekly_data,
    "monthly": monthly_data
}

with open('data.json', 'w') as json_file:
    json.dump(combined_data, json_file)


