import requests
import json

API_KEY = "GBEXJPOTUHCC9FZC" #Alpha Vantage


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

r = fetchDataDaily("AAPL")
with open('data.json', 'w') as json_file:
    json.dump(r, json_file)

