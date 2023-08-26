from flask import Flask, jsonify #pip install Flask
import requests #pip install requests
from flask_cors import CORS #pip install Flask-Cors
from SMA import SMA
from RSI import calculate_rsi, RSI_monthly, RSI_daily, RSI_weekly
from EMA import daily_ema, weekly_ema, monthly_ema
import json
import math

app = Flask(__name__)
CORS(app)

API_KEY = "6ZP516EDZC9M2JBK"
with open('data.json', 'r') as file:
    fetchedData = json.load(file)
    
def convert_to_json(data_frame):
    json_data = {}
    
    for index, row in data_frame.iterrows():
        date = str(index.date())
        ema_close = row['EMA-close']

        if not np.isnan(ema_close):
            json_data[date] = ema_close
    
    return json_data

def convert_to_json_SMA(data_frame):
    json_data = {}
    
    for index, row in data_frame.iterrows():
        date = str(index.date())
        sma_close = row['SMA']

        if np.isnan(sma_close):
            json_data[date] = "null"
        else:
            json_data[date] = sma_close
    
    return json_data

def convert_to_json_RSI(data_frame):
    json_data = {}
    
    for index, row in data_frame.iterrows():
        date = str(index.date())
        rsi_close = row['rsi']

        if not np.isnan(rsi_close):
            json_data[date] = rsi_close
    
    return json_data

@app.route('/fetchData/<symbol>', methods=['GET'])
def fetchData(symbol):
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
    fetchedData = jsonify(combined_data)
    return fetchedData

@app.route('/sma', methods=['GET'])
def get_sma():
    combined_data = fetchedData
    daily_df = SMA(combined_data, 'daily', 3)
    weekly_df = SMA(combined_data, 'weekly', 3)
    monthly_df = SMA(combined_data, 'monthly', 3)
    daily_json_data = convert_to_json_SMA(daily_df)
    weekly_json_data = convert_to_json_SMA(weekly_df)
    monthly_json_data = convert_to_json_SMA(monthly_df)

    combined_json_data = {
        "Daily": daily_json_data,
        "Weekly": weekly_json_data,
        "Monthly": monthly_json_data
    }

    with open("sma-close.json", 'w') as output_json_file:
        json.dump(combined_json_data, output_json_file, indent=4)

    print("JSON conversion complete.")
@app.route('/rsi', methods=['GET'])
def get_rsi():
    # Collect data as before
    combined_data = fetchedData
    
    daily_df = RSI_daily(combined_data, 14)
    weekly_df = RSI_weekly(combined_data, 14)
    monthly_df = RSI_monthly(combined_data, 14)
    daily_json_data = convert_to_json(daily_df)
    weekly_json_data = convert_to_json(weekly_df)
    monthly_json_data = convert_to_json(monthly_df)

    combined_rsi_data = {
        "Daily": daily_json_data,
        "Weekly": weekly_json_data,
        "Monthly": monthly_json_data
    }
    combined_rsi_data = json.dumps(combined_rsi_data, default=str, indent=4)
    return combined_rsi_data

@app.route('/ema', methods=['GET'])
def get_ema():
    combined_data = fetchedData
    daily_df = daily_ema(combined_data, 20)
    weekly_df = weekly_ema(combined_data, 20)
    monthly_df = monthly_ema(combined_data, 20)
    daily_json_data = convert_to_json(daily_df)
    weekly_json_data = convert_to_json(weekly_df)
    monthly_json_data = convert_to_json(monthly_df)
    
    combined_ema_data = {
    "Daily": daily_json_data,
    "Weekly": weekly_json_data,
    "Monthly": monthly_json_data
    }   
    combined_ema_json = json.dumps(combined_ema_data, default=str, indent=4)
    return combined_ema_json

        
    
if __name__ == '__main__':
    app.run(port=5000)
