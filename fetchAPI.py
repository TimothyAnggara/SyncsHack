import requests
import json

API_KEY = "GBEXJPOTUHCC9FZC" #Alpha Vantage


def fetchDataMonthly(SYMBOL):
    API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={SYMBOL}&apikey={API_KEY}"
    r = requests.get(API_URL).json()
    print(r)
    return r

def fetchDataWeekly(SYMBOL):
    API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={SYMBOL}&apikey={API_KEY}"
    r = requests.get(API_URL).json()
    print(r)
    return r

def fetchDataDaily(SYMBOL):
    API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={SYMBOL}&apikey={API_KEY}"
    r = requests.get(API_URL).json()
    print(r)
    return r


r = fetchData("AAPL")

with open('data.json', 'w') as file:
    json.dump(r, file)

